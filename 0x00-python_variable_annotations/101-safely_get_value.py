#!/usr/bin/env python3
# Module for safely getting a value from a mapping.
from typing import TypeVar, Mapping, Any, Union, Optional

T = TypeVar('T')  # Declare Type Variable


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Optional[T] = None) -> Optional[T]:
    """Get a value from a mapping safely with a default if the key is not found.

    Args:
    dct (Mapping[Any, T]): The mapping.
    key (Any): The key.
    default (Optional[T], optional): The default.

    Returns:
    Optional[T]: The value or the default.
    """
    return dct.get(key, default)
