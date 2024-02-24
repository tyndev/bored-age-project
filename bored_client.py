import asyncio
from async_req import http_get

"""
Gets an activity suggestion based on the given age.
Categorizes the age into groups like recreational, diy, or relaxation. 
Then calls the Bored API to get an activity of that type.
Args: age (int): The age to get an activity suggestion for.
Returns: str: The suggested activity name.
"""
async def get_activity_for_age(age: int) -> str:
    # Simple logic to categorize age groups; adjust as needed
    if age < 18:
        type = "recreational"
    elif age <= 65:
        type = "diy"
    else:
        type = "relaxation"
    response = await http_get(f"http://www.boredapi.com/api/activity?type={type}")
    activity = response["activity"]
    return str(activity)


# MAIN
async def main() -> None:
    age = 31
    activity = await get_activity_for_age(age)
    print(f"Activity for age {age}: {activity}")

# If this script is run directly, call the main() coroutine
if __name__ == "__main__":
    asyncio.run(main())
