#!/usr/bin/env python3
"""
Write a type-annotated function 
from typing import Tuple, Union
"""

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string k and an int OR float v as arguments and returns a tuple
    the square of the int/float v and should be annotated as a float
    """
    return k, float(v ** 2)
