#!/usr/bin/env python3
"""
Module that contains an async function to execute multiple coroutines.
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawnswait_random n times with the specified max_delay and
    returns a list of all the delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
