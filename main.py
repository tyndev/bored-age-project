import asyncio
import aiohttp
from agify_client import predict_age
from bored_client import get_activity_for_age

async def predict_and_suggest(name: str, session):
    age = predict_age(name)  # This is synchronous; consider making it async for real concurrency
    activity = get_activity_for_age(age)
    print(f"For {name}, predicted age: {age}, suggested activity: {activity}")

async def main(names: list):
    async with aiohttp.ClientSession() as session:
        tasks = [predict_and_suggest(name, session) for name in names]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]  # Example names
    asyncio.run(main(names))