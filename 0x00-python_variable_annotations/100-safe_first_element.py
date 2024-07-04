#!/usr/bin/env python3
# Module to safely get the first element of a sequence.
from typing import Any, Sequence, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence, or None if the sequence is empty.

    Args:
    lst (Sequence[Any]): The sequence.

    Returns:
    Optional[Any]: The first element of the sequence or None.
    """
    if lst:
        return lst[0]
    else:
        return None
