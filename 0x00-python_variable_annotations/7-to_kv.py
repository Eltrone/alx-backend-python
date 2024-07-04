#!/usr/bin/env python3
"""
Module to return a tuple from a string and the square of an int/float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple consisting of a string and the square of a number.

    Args:
    k (str): The string.
    v (Union[int, float]): The number to be squared.

    Returns:
    Tuple[str, float]: A tuple containing the string and the square of the number.
    """
    return (k, float(v ** 2))
