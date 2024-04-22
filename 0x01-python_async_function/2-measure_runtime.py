#!/usr/bin/env python3
"""
Module for the measure_time function.
"""
import asyncio
import time
from . import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n by running it asynchronously.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    execution_time = (end_time - start_time) / n
    return execution_time
