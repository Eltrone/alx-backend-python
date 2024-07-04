#!/usr/bin/env python3
"""
Module to sum a mixed list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum all elements in a mixed list of integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): The mixed list of integers and floats.

    Returns:
    float: The sum of the list elements.
    """
    return float(sum(mxd_lst))
