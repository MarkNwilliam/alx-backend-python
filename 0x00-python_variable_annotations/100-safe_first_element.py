#!/usr/bin/env python3

"""
Module for task 10 - Duck typing - first element of a sequence
"""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, Optional]:
    """
    Get the value of a key in a dictionary safely.
    """
    if lst:
        return lst[0]
    else:
        return None

