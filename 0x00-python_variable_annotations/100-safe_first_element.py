#!/usr/bin/env python3
"""
Module for task 10 - Duck typing - first element of a sequence
"""

from typing import Sequence, Any, Union, NoneType

def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """
    Returns the first element of a sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
