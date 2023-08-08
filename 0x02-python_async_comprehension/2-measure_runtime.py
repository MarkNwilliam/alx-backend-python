#!/usr/bin/env python3
"""Measure Runtime module"""

import asyncio
from time import time
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """A coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather. It will measure the total runtime
    and return it."""
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time()
    return end_time - start_time
