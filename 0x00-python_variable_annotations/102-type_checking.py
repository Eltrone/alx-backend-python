i#!/usr/bin/env python3
"""Type Checking"""
# Import Tuple and List types for type annotations.
from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into an array by repeating each element.

    Args:
        lst (Tuple): Tuple containing elements to repeat.
        factor (int, optional)

    Returns:
        List: Contains repeated elements.
    """
    # Create a list with each element of lst repeated 'factor' times.
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in

# Define a tuple 'array' with three integers.
array = (12, 72, 91)

# Call function with the array and default factor.
zoom_2x = zoom_array(array)

# Call function with the array and a factor of 3.
zoom_3x = zoom_array(array, 3)
