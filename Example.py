import asyncio

i = 0

async def inner_func():
    # the code below will never get run, if we don't do await on inner_func
    global i
    i=i+10
    print(f" i value in inner_func -> {i}")
    

async def f():
    global i
    inner_func() # without await, print(i) -> 1
    i = i+1
    print(f" i value in f -> {i}")
    # await asyncio.sleep(0)
    return 123

loop = asyncio.new_event_loop()
coro = f()
print(loop.run_until_complete(coro))
