#!/usr/bin/env python3
"""
2. Measure the runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
     2. Measure the runtime
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    timeframe: float = (end_time - start_time) / n
    return timeframe