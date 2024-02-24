import asyncio
import requests

"""
Gets JSON data from a URL synchronously using requests.
Args: url (str): The URL to send the GET request to.
Returns: dict: The JSON response data.
"""
def http_get_sync(url: str):
    response = requests.get(url)
    return response.json()


"""
Gets JSON data from a URL asynchronously using asyncio.
Args: url (str): The URL to send the GET request to.
Returns: dict: The JSON response data.
"""
async def http_get(url: str):
    return await asyncio.to_thread(http_get_sync, url)

