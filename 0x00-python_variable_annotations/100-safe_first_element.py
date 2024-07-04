#!/usr/bin/env python3
# Module to safely get the first element of a sequence.
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element ofsequence, or None ifsequence is empty.

    Args:
    lst (Sequence[Any]): The sequence.

    Returns:
    Union[Any, None]: The first element of the sequence or None.
    """
    if lst:
        return lst[0]
    else:
        return None
