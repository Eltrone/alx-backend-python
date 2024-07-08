#!/usr/bin/env python3
"""
Module that contains an async function to execute multiple tasks.
"""
import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawnstask_wait_random n times with the specified max_delay and
    returns a list of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
