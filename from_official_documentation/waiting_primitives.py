import asyncio, time

async def factorial(name, number):
    f = 1
    if number <= 10:
        for i in range(2, number + 1):
            print(f"{time.strftime('%X')}: inside for loop for factorial({number})")
            await asyncio.sleep(1)
            f *= i
        print(f"{time.strftime('%X')}: factorial({number}) = {f}")
        return f
    else:
        raise Exception("Raising an exception")

async def main():
    # Schedule three calls *concurrently*:
    done_1, pending_1 = await asyncio.wait(
        [factorial("A", 1),
        factorial("B", 2),
        factorial("C", 3)],
    )
    print(f"\n\ndone_1 -> {done_1}, \t pending_1 -> {pending_1}\n\n")

    done_2, pending_2 = await asyncio.wait(
        [factorial("A", 4),
        factorial("B", 5),
        factorial("C", 6)],
        timeout=5 # the exception will be passed, but not thrown.
    )
    print(f"\n\ndone_2 -> {done_2}, \t pending_2 -> {pending_2}\n\n")
    task_pending_2 = pending_2.pop()
    print(f"task_pending_2.done() -> {task_pending_2.done()}")# -> False
    task_pending_2.cancel()
    print(f"task_pending_2.cancelled() -> {task_pending_2.cancelled()}")# -> False
    try:
        # without running again the task, it won't get cancelled.
        await task_pending_2
    except asyncio.CancelledError as e:
        pass
    print(f"task_pending_2.cancelled() -> {task_pending_2.cancelled()}")# -> True
    print(f"task_pending_2.done() -> {task_pending_2.done()}")# -> True



asyncio.run(main())