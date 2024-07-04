#!/usr/bin/env python3
"""
Module to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by the specified multiplier.

    Args:
    multiplier (float): The multiplier.

    Returns:
    Callable[[float], float]: A function that multiplies a given float by the multiplier.
    """
    return lambda x: x * multiplier
