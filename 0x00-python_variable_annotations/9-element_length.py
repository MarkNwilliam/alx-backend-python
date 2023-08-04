#!/usr/bin/env python3
"""
Module for task 9 - Let's duck type an iterable object
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable object and returns a list of tuples 
    """
    return [(i, len(i)) for i in lst]
