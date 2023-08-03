#!/usr/bin/env python3
"""
Module for task 12 - Type Checking
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

# This would cause a type error because 3.0 is a float. Commenting it out for now.
# zoom_3x = zoom_array(array, 3.0)
