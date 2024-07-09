#!/usr/bin/env python3
"""
Module for comprehending values from an async generator.
"""
import asyncio
from importlib import import_module
from typing import List

async_generator = import_module("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random numbers from async generator.
    """
    return [i async for i in async_generator()]
