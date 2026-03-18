from django.conf import settings

r = settings.REDIS_CLIENT


def get_poll_key(poll_id: int, suffix: str) -> str:
    return f"poll:{poll_id}:{suffix}"


async def increment_vote(poll_id: int, option_id: str) -> None:
    """Increment the vote counter for a specific poll option."""
    key = get_poll_key(poll_id, "votes")
    await r.hincrby(key, option_id, 1)


async def try_register_user_vote(poll_id: int, user_id: str) -> bool:
    """
    Attempts to register a user vote.
    Returns True if successful, False if user has already voted.
    """
    key = get_poll_key(poll_id, "voted_users")
    added = await r.sadd(key, user_id)
    return added == 1  # 1 = added, 0 = already existed


# async def register_user_vote(poll_id: int, user_id: str) -> None:
#     """Register a user as having voted."""
#     key = get_poll_key(poll_id, "voted_users")
#     await r.sadd(key, user_id)


# async def has_user_voted(poll_id: int, user_id: str) -> bool:
#     """Check if user has already voted in the poll."""
#     key = get_poll_key(poll_id, "voted_users")
#     return await r.sismember(key, user_id)
