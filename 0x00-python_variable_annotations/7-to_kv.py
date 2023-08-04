#!/usr/bin/env python3
"""
Module for task 7 - Complex types - string and int/float to tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that takes a string and an int or float.
    Returns a tuple where the first element is the string
    and the second is the square of the int/float.
    """
    return (k, float(v**2))
