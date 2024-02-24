import asyncio
from time import perf_counter
from agify_client import predict_age
from bored_client import get_activity_for_age


"""
Predict a person's age using the agify API.
Get an activity suggestion using the bored API, and print the results.
Parameters: name (str): The person's name to predict age for.
"""
async def predict_and_suggest(name: str):
    age = await predict_age(name)
    activity = await get_activity_for_age(age)
    print(f"For {name}, predicted age: {age}, suggested activity: {activity}")


"""
Execute the function asynchronously for each name in the list and print the total time. 
Then execute synchronously for each name in sequence and print the total time. 
Used to demonstrate performance difference between async and sync.
"""
async def main(names: list[str]):
    # async calls 
    time_before = perf_counter()
    await asyncio.gather(*[predict_and_suggest(name) for name in names])
    print(f"Total time (async): {perf_counter() - time_before}")
    
    # sync calls
    time_before = perf_counter()
    for name in names:
        await predict_and_suggest(name)
    print(f"Total time (sync): {perf_counter() - time_before}")

# If this script is run directly, call the main() coroutine
if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie", "Aiden"]  # Example names
    asyncio.run(main(names))