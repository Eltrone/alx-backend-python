#!/usr/bin/env python3
"""
Module to sum a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum all elements in a list of floats.

    Args:
    input_list (List[float]): The list of floats.

    Returns:
    float: The sum of the list elements.
    """
    return sum(input_list)
