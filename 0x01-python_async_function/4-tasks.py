#!/usr/bin/env python3
"""
Module for the task_wait_n function.
"""
import asyncio
from typing import List
from . import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that takes in two integer arguments,
    `n` and `max_delay`.
    It returns a list of all the delays (float values)
    sorted in ascending order.
    """
    delays: List[float] = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
