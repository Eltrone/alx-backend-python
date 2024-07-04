#!/usr/bin/env python3
# Module to zoom in on elements of a tuple by repeating them.
from typing import Tuple, List, Union


def zoom_array(lst: Union[Tuple[int, ...], List[int]], factor: int = 2) -> List[int]:
    """Increase the size of a tuple or list by repeating each element.

    Args:
    lst (Union[Tuple[int, ...], List[int]]): The tuple or list to zoom.
    factor (int): The factor to repeat each element.

    Returns:
    List[int]: A list with each element repeated.
    """
    zoomed_in: List[int] = [
        item for item in lst for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(array)  # Valid as it is a list
zoom_3x = zoom_array(array, 3)  # Must be integer
