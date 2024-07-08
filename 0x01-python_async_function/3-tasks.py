#!/usr/bin/env python3
"""
Module that contains a function to create an asyncio task.
"""
import asyncio
import importlib

bas = importlib.import_module('0-basic_async_syntax')


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that waits for a random delay.
    """
    return asyncio.create_task(bas.wait_random(max_delay))
