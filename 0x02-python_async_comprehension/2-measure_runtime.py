#!/usr/bin/env python3
"""
Module to measure runtime of four parallel async comprehensions.
"""
import asyncio
import time
from importlib import import_module

# Import async_comprehension module first
async_comprehension_module = import_module("1-async_comprehension")
# Now import the async_comprehension from the imported module
async_comprehension = async_comprehension_module.async_comprehension


async def measure_runtime() -> float:
    """
    Measure runtime of executing async_comprehension four times in parallel.
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
