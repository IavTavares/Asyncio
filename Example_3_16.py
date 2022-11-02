import asyncio

async def main(f: asyncio.Future):
    await asyncio.sleep(2)
    f.set_result('I have finished.')

# i=0 -> this assignment creates a different loop? loop = asyncio.new_event_loop()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop) # we need to set loop as the event loop
fut = asyncio.Future()
print(fut.done())
loop.create_task(main(fut))
print(loop.run_until_complete(fut)) # -> I have finished
print(fut.done()) # -> True
print(fut.result()) # -> I have finished
