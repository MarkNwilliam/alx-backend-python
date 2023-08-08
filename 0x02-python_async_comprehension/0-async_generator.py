#!/usr/bin/env python3
"""Async Generator module"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """An asynchronous generator that will loop 10 times, each time
    asynchronously waiting 1 second, then yielding a random number
    between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
