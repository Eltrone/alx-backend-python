#!/usr/bin/env python3
"""
Module for generating random numbers asynchronously.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator yields 10random numbers, each after waiting for 1 s.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
