#!/usr/bin/env python3
"""
Module for task 11 - More involved type annotations
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, NoneType] = None) -> Union[Any, T]:
    """
    Get the value of a key in a dictionary safely.
    """
    if key in dct:
        return dct[key]
    else:
        return default
