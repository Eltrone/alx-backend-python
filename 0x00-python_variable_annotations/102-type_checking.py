#!/usr/bin/env python3
"""Type Checking"""
from typing import Tuple, List, Union

def zoom_array(lst: Union[Tuple[int, ...], List[int]], factor: int = 2) -> List[int]:
    """zoom_array function

    Increase the size of a sequence by repeating its elements.

    Args:
        lst (Union[Tuple[int, ...], List[int]]): Sequence to zoom.
        factor (int): How many times to repeat each element.

    Returns:
        List[int]: List where each element is repeated 'factor' times.
    """
    zoomed_in: List[int] = [item for item in lst for _ in range(factor)]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
