import asyncio

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
loop2 = asyncio.get_event_loop()
loop4 = asyncio.get_event_loop()



print(loop2 is loop4)
