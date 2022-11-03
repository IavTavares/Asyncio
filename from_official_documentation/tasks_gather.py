import asyncio

async def factorial(name, number):
    f = 1
    if number <= 10:
        for i in range(2, number + 1):
            print(f"Task {name}: Compute factorial({number}), currently i={i}...")
            await asyncio.sleep(1)
            f *= i
        print(f"Task {name}: factorial({number}) = {f}")
        return f
    else:
        raise Exception("Raising an exception")

async def main():
    # Schedule three calls *concurrently*:
    L_1 = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(f"\nL_1 -> {L_1}\n")

    L_2 = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 11),
        return_exceptions = True # the exception will be passed, but not thrown.
    )
    print(f"\nL_2 -> {L_2}\n")

    L_3 = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 11)
    ) # this gather will throw the exception.
    print("\nL_3 -> ",L_3)
asyncio.run(main())