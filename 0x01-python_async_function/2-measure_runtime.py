#!/usr/bin/env python3
"""
Module that measures the runtime of wait_n function.
"""
import time
import asyncio
import importlib

cc = importlib.import_module('1-concurrent_coroutines')


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and
    returns the average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(cc.wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
