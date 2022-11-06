import asyncio
import time

# this version of say_after is blocking... 
def say_after(delay, what):
    time.sleep(delay)
    print(f"what = {what}, at {time.strftime('%X')}")


async def main():
    print(f"started main at {time.strftime('%X')}")
    await asyncio.gather(*[
        asyncio.to_thread(say_after,delay=i, what=i) for i in range(5)
    ])
    print(f"finished main at {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main()) # it will take only 4s to run. 