import json

from django.conf import settings

r = settings.REDIS_CLIENT


def get_poll_key(poll_id: int, suffix: str) -> str:
    return f"poll:{poll_id}:{suffix}"


async def get_poll_vote_counts(poll_id: int) -> dict:
    """
    Fetch vote counts for each option in a poll from Redis.
    Returns a dict mapping option_id -> vote_count.
    """
    key = get_poll_key(poll_id, "votes")
    raw = await r.hgetall(key)
    return {k: int(v) for k, v in raw.items()}


async def get_cached_poll_results(poll_id: int) -> dict | None:
    key = get_poll_key(poll_id, "results_data")
    cached = await r.get(key)
    if cached:
        return json.loads(cached)
    return None


async def cache_poll_results(
    poll_id: int, data: dict, expire_seconds: int = 3600
) -> None:
    key = get_poll_key(poll_id, "results_data")
    await r.set(key, json.dumps(data), ex=expire_seconds)


async def delete_cached_poll_results(poll_id: int) -> None:
    key = get_poll_key(poll_id, "results_data")
    await r.delete(key)
