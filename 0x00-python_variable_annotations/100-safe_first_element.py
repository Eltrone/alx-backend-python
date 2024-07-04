#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Duck typing - first element of a sequence

    Args:
        lst (Sequence[Any]):sequence from which first element is returned.

    Returns:
        Optional[Any]: first element of sequence or None if sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
