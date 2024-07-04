#!/usr/bin/env python3
"""
Module to compute the length of elements in an iterable.
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples each containing a sequence and its length.

    Args:
    lst (Iterable[Sequence]): Iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: List of tuples with sequence and length.
    """
    return [(i, len(i)) for i in lst]
