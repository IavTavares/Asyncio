import asyncio,time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(f"what = {what}, at {time.strftime('%X')}")


background_tasks = set()

async def main():
	for i in range(5):
		task = asyncio.create_task(say_after(delay=i,what=i))
		
		# Add task to the set. This creates a strong reference.
		background_tasks.add(task)
		
	await task
	
	# To prevent keeping references to finished tasks forever,
	# make each task remove its own reference from the set after
	# completion:
	task.add_done_callback(background_tasks.discard) # discard is a set method.
		
if __name__=="__main__":
	asyncio.run(main())

