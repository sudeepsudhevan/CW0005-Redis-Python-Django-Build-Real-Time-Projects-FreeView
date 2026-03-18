from typing import List

from asgiref.sync import sync_to_async
from django.http import JsonResponse
from ninja import Header, Router

from polls.services.cookie_services import has_cookie_voted, set_vote_cookie
from polls.services.ip_services import get_client_ip
from polls.services.redis_poll_reporting import (
    cache_poll_results,
    get_cached_poll_results,
    get_poll_vote_counts,
)
from polls.services.redis_poll_services import (
    is_rate_limited,
    record_vote,
    try_register_vote,
)

from .models import Poll
from .schema import (
    CreatePollSchema,
    ErrorSchema,
    PollOutListSchema,
    PollOutSchema,
    VoteSchema,
)

router = Router()


@router.get("/polls/list", response=List[PollOutListSchema])
async def poll_list(request):
    polls = await sync_to_async(list)(Poll.objects.all())
    return polls


@router.post("/polls/add", response={201: PollOutSchema, 400: ErrorSchema})
async def create_poll(request, data: CreatePollSchema):
    if not data.text or len(data.text) < 2:
        return 400, {"error": "At least two poll options are required."}

    poll = Poll(question=data.question, text=data.text)
    await poll.asave()

    return 201, PollOutSchema(id=poll.id, question=poll.question, text=poll.text)


@router.post(
    "/polls/{poll_id}/vote", response={200: dict, 400: ErrorSchema, 404: ErrorSchema}
)
async def vote(request, poll_id: int, data: VoteSchema, x_user_id: str = Header(None)):
    option_id = data.option

    # 1. Validate poll and option
    try:
        poll = await Poll.objects.aget(pk=poll_id)
    except Poll.DoesNotExist:
        return 404, {"error": "Poll not found"}

    # 1.1 Enforce status and expiry
    if not poll.is_active:
        return 400, {"error": "This poll is not active."}

    if poll.expires_at and poll.is_expired():
        return 400, {"error": "This poll has expired."}

    if option_id not in poll.text:
        return 400, {"error": "Invalid option ID"}

    # 2. Get identity
    ip = get_client_ip(request)
    user_id = request.headers.get("X-USER-ID")

    # ⏳ 2.1 Rate limit check (before anything else)
    if await is_rate_limited(ip):
        return 400, {"error": "You're voting too quickly. Please wait a few seconds."}

    # 3. Check for existing votes
    if user_id:
        user_already_voted = await try_register_vote(poll_id, user_id, "voted_users")
        if not user_already_voted:
            return 400, {"error": "User has already voted"}

    ip_already_voted = not await try_register_vote(poll_id, ip, "voted_ips")
    if ip_already_voted or has_cookie_voted(request, poll_id):
        return 400, {"error": "This IP/Browser has already voted"}

    # 4. Record Vote
    await record_vote(poll_id, option_id, user_id or "anonymous", ip)

    # 5. Return success + set cookie
    response = JsonResponse({"message": f"Vote for option {option_id} counted"})
    set_vote_cookie(response, request, poll_id)
    return response


@router.get(
    "/polls/{poll_id}/results", response={200: dict, 400: ErrorSchema, 404: ErrorSchema}
)
async def poll_results(request, poll_id: int):
    # Try cache first
    cached = await get_cached_poll_results(poll_id)
    if cached:
        return cached

    # Fallback to rebuild
    try:
        poll = await Poll.objects.aget(pk=poll_id)
    except Poll.DoesNotExist:
        return 404, {"error": "Poll not found"}

    results = await get_poll_vote_counts(poll_id)

    for option_id in poll.text.keys():
        if option_id not in results:
            results[option_id] = 0

    total_votes = sum(results.values())
    response = {
        "poll_id": poll.id,
        "question": poll.question,
        "options": [{"id": k, "text": v} for k, v in poll.text.items()],
        "results": results,
        "total_votes": total_votes,
    }

    await cache_poll_results(poll_id, response)  # Cache it for next time
    return response
