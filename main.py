import asyncio
from time import perf_counter
from agify_client import predict_age
from bored_client import get_activity_for_age


async def predict_and_suggest(name: str):
    age = await predict_age(name)
    activity = await get_activity_for_age(age)
    print(f"For {name}, predicted age: {age}, suggested activity: {activity}")

async def main(names: list):
    # async calls 
    time_before = perf_counter()
    await asyncio.gather(*[predict_and_suggest(name) for name in names])
    print(f"Total time (async): {perf_counter() - time_before}")
    
    # sync calls
    time_before = perf_counter()
    for name in names:
        await predict_and_suggest(name)
    print(f"Total time (sync): {perf_counter() - time_before}")

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie", "Aiden"]  # Example names
    asyncio.run(main(names))