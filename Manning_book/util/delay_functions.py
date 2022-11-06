import asyncio
import time


async def delay(delay_seconds: int) -> int:
    print(f"sleeping for {delay_seconds} second(s), at {time.strftime('%X')}")
    await asyncio.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds} second(s) at {time.strftime('%X')}")
    return delay_seconds