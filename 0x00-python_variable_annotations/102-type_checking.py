#!/usr/bin/env python3
"""Type Checking"""
"""Defines a function that expands an array by repeating its elements."""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    return [item for item in lst for _ in range(factor)]



array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
