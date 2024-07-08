#!/usr/bin/env python3
"""
Module that contains an async function to execute multiple tasks.
"""
import asyncio
from typing import List
import importlib

tasks = importlib.import_module('3-tasks')


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawnstask_wait_random n times with the specified max_delay and
    returns a list of all the delays in ascending order.
    """
    task_list = [tasks.task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*task_list)
    return sorted(delays)
