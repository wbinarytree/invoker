from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field


@dataclass
class TokenBucket:
    """Simple token bucket. Refills continuously at `rate` tokens per second."""

    rate: float
    capacity: float
    _tokens: float = field(init=False)
    _last: float = field(init=False)

    def __post_init__(self) -> None:
        self._tokens = self.capacity
        self._last = time.monotonic()

    async def acquire(self, amount: float = 1.0) -> None:
        while True:
            now = time.monotonic()
            elapsed = now - self._last
            self._tokens = min(self.capacity, self._tokens + elapsed * self.rate)
            self._last = now
            if self._tokens >= amount:
                self._tokens -= amount
                return
            deficit = amount - self._tokens
            await asyncio.sleep(deficit / self.rate)
