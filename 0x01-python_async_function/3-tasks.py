#!/usr/bin/env python3
"""
Module that contains a function to create an asyncio task.
"""
import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
