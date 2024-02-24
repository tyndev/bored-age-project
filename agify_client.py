import asyncio
from async_req import http_get, http_get_sync

async def predict_age(name: str) -> int:
    response = await http_get(f"https://api.agify.io?name={name}")
    age = response['age']
    return int(age)


# MAIN
async def main() -> None:
    name = "Tyler"
    age = await predict_age(name)
    print(f"Predicted age for {name}: {age}")
    
if __name__ == "__main__":
    asyncio.run(main())


