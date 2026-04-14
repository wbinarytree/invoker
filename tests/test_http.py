import time

from invoker.http.ratelimit import TokenBucket


async def test_bucket_paces_calls():
    bucket = TokenBucket(rate=10, capacity=2)
    start = time.monotonic()
    for _ in range(5):
        await bucket.acquire()
    elapsed = time.monotonic() - start
    assert elapsed >= 0.25
