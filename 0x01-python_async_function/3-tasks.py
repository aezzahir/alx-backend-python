#!/usr/bin/env python3
"""
Module for the task_wait_random function.
"""
import asyncio
from . import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task object for the wait_random coroutine with
    the given max_delay.
    """
    coroutine = wait_random(max_delay)
    return asyncio.create_task(coroutine)
