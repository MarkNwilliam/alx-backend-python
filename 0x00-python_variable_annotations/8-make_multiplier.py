#!/usr/bin/env python3

"""
Module for task 8 - Complex types - functions
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that returns another function that multiplies a given float by multiplier.
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier
    
    return multiplier_func