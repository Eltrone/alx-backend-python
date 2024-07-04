#!/usr/bin/env python3
"""
Module to compute the length of elements in an iterable.
"""
from typing import Iterable, List, Tuple, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with each sequence and its length.

    Args:
    lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
