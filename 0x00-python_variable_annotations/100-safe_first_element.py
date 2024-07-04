#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""
from typing import Sequence, Any, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Duck typing - first element of a sequence

    Args:
        lst (Sequence[Any]): The sequence from which the first element is returned.

    Returns:
        Optional[Any]: The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
