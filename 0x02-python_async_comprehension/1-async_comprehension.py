#!/usr/bin/env python3
"""
Module for comprehending values from an async generator.
"""
from typing import List
import asyncio

async_comprehension = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random numbers from an async generator
    """
    return [i async for i in async_generator()]
