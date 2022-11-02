import asyncio

# Tasks are used to schedule coroutines concurrently.

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is completed:
    print(await task)
if __name__=="__main__":
	asyncio.run(main())
