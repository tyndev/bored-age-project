import asyncio
from async_req import http_get

"""
Predict the age of a person given their name.
Args: name (str): The person's name.
Returns: int: The predicted age.
"""
async def predict_age(name: str) -> int:
    response = await http_get(f"https://api.agify.io?name={name}")
    age = response['age']
    return age


# MAIN
async def main() -> None:
    name = "Tyler"
    age = await predict_age(name)
    print(f"Predicted age for {name}: {age}")

# If this script is run directly, call the main() coroutine
if __name__ == "__main__":
    asyncio.run(main())


