#!/usr/bin/env python3
"""
    Asynchronous coroutine that takes in an integer argument
    `max_delay` (default 10).
    It waits for a random delay between 0 and `max_delay`
    seconds (inclusive) and returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    `max_delay` (default 10).
    It waits for a random delay between 0 and `max_delay`
    seconds (inclusive) and returns it.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
