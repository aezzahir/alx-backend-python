#!/usr/bin/env python3
"""
4
"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    tasks 4
    """
    listOfDelays: List[float] = []
    for i in range(n):
        taskRandom: float = await task_wait_random(max_delay)
        listOfDelays.append(taskRandom)
    return sorted(listOfDelays)