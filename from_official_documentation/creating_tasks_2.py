import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(f"what = {what}, at {time.strftime('%X')}")


async def main():
    await asyncio.gather(*[
        say_after(delay=i, what=i) for i in range(5)
    ])


if __name__ == "__main__":
    asyncio.run(main())