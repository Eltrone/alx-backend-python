#!/usr/bin/env python3
# Module for safely getting a value from a mapping.
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')  # Declare Type Variable


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """Get value from mapping safely with default if the key is not found.

    Args:
    dct (Mapping[Any, T]): The mapping.
    key (Any): The key.
    default (Union[T, None], optional): The default.

    Returns:
    Union[T, None]: The value or the default.
    """
    return dct.get(key, default)
