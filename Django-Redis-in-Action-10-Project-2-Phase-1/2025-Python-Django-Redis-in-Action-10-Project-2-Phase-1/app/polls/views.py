from typing import List

from asgiref.sync import sync_to_async
from ninja import Header, Router

from polls.services.redis_poll_services import increment_vote, try_register_user_vote

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

    try:
        poll = await Poll.objects.aget(pk=poll_id)
    except Poll.DoesNotExist:
        return 404, {"error": "Poll not found"}

    if option_id not in poll.text:
        return 400, {"error": "Invalid option ID"}

    user_id = request.headers.get("X-USER-ID")

    if user_id:
        success = await try_register_user_vote(poll_id, user_id)
        if not success:
            return 400, {"error": "User has already voted"}

    # if user_id:
    #     if await has_user_voted(poll_id, user_id):
    #         return 400, {"error": "User has already voted"}
    #     await register_user_vote(poll_id, user_id)

    await increment_vote(poll_id, option_id)

    return {"message": f"Vote for option {option_id} counted"}
