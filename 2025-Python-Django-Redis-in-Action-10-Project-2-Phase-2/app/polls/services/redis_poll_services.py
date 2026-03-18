import json

from django.conf import settings

r = settings.REDIS_CLIENT

RATE_LIMIT_SECONDS = 5


async def is_rate_limited(ip: str) -> bool:
    key = f"rate_limit:{ip}"
    added = await r.set(key, 1, ex=RATE_LIMIT_SECONDS, nx=True)
    return added is None  # If key already exists, rate limited


def get_poll_key(poll_id: int, suffix: str) -> str:
    return f"poll:{poll_id}:{suffix}"


async def increment_vote(poll_id: int, option_id: str) -> None:
    """Increment the vote counter for a specific poll option."""
    key = get_poll_key(poll_id, "votes")
    await r.hincrby(key, option_id, 1)


async def try_register_vote(poll_id: int, voter_id: str, suffix: str) -> bool:
    """
    Attempts to register a user vote.
    Returns True (1) if successful, False (0) if user has already voted.
    """
    key = get_poll_key(poll_id, suffix)
    added = await r.sadd(key, voter_id)
    return added == 1  # 1 = added, 0 = already existed


async def track_recent_vote(poll_id: int, user_id: str, ip: str, option_id: str):
    key = get_poll_key(poll_id, "recent_votes")
    vote_data = {
        "user_id": user_id,
        "ip": ip,
        "option_id": option_id,
    }
    await r.lpush(key, json.dumps(vote_data))
    await r.ltrim(key, 0, 99)  # Keep only last 100 entries


async def get_recent_votes(poll_id: int) -> list:
    key = get_poll_key(poll_id, "recent_votes")
    votes = await r.lrange(key, 0, 99)
    return [json.loads(v) for v in votes]
