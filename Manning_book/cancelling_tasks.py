import asyncio
from asyncio import CancelledError
from util.delay_functions import delay

async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    while not long_task.done():
        print('Task not finished, checking again in a second.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        await long_task #asyncio.sleep(0) 
        # -> in this case task is still cancelled, but since we're not calling long_task, 
        # no exception is raised.
    except CancelledError:
        print('Our task was cancelled')
    except BaseException as be:
        print(f"Exception -> {type(be)}")

asyncio.run(main())