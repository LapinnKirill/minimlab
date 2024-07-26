import asyncio

async def worker(name, duration):
    print(f"{name} starting.")
    await asyncio.sleep(duration)
    print(f"{name} done after {duration} seconds.")

async def main():
    await asyncio.gather(
        worker("Worker 1", 2),
        worker("Worker 2", 4)
    )

# Run the main coroutine
asyncio.run(main())
