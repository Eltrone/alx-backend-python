#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Mapping, Any, TypeVar, Optional

T = TypeVar("T")


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Optional[T] = None) -> Optional[T]:
    """safely_get_value function

    Retrieve a value from a mapping with a default if the key is not found.

    Args:
        dct (Mapping[Any, T]): Dictionary from which to retrieve the value.
        key (Any): Key to search for in the dictionary.
        default (Optional[T], optional): Default value if key not found.

    Returns:
        Optional[T]: The value from the dictionary or the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
