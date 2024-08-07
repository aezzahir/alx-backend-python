#!/usr/bin/env python3
"""
async_comprehension module
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    using an async comprehensing over async_generator
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers
