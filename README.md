# Learning Project: Concurrent API Calls

## Overview: Age Predictor and Activity Suggester
Demonstrates asynchronous concurrent programming, type annotations, and API usage. This Python application uses `agify.io` and `Bored API` to predict ages and suggest activities. 

## Key Features
- **Concurrent API Calls:** Uses `async/await` and `asyncio.gather` for efficient concurrent execution.
- **Performance Insight:** Compares asynchronous vs. synchronous execution times.
- **Type Safety:** Employs type annotations for clearer code.
- **API Integration:** Seamlessly integrates external APIs for dynamic data retrieval.

## Structure
- `async_req.py`: HTTP request handlers.
- `agify_client.py`: Age prediction from `agify.io`.
- `bored_client.py`: Activity suggestions from `Bored API`.
- `main.py`: Orchestrates the application logic.

## My Related Notes
- [tyndev / notes / How to Get Concurrency with Synchronous Requests in Python](https://github.com/tyndev/tyndev/blob/main/notes/How%20to%20Get%20Concurrency%20with%20Synchronous%20Requests%20in%20Python.md)
- [tyndev / notes / Typing in Python](https://github.com/tyndev/tyndev/blob/main/notes/Typing%20in%20Python.md)

## Output
Below is an example output from running `main.py` in the terminal, demonstrating both the asynchronous and synchronous execution times along with the age predictions and suggested activities:

```plaintext
For Bob, predicted age: 70, suggested activity: Go on a long drive with no music
For Alice, predicted age: 56, suggested activity: Make a scrapbook with pictures of your favorite memories
For Charlie, predicted age: 63, suggested activity: Learn woodworking
For Aiden, predicted age: 33, suggested activity: Fix something that's broken in your house
Total time (async): 1.9195028000012826

For Alice, predicted age: 56, suggested activity: Create a compost pile
For Bob, predicted age: 70, suggested activity: Color
For Charlie, predicted age: 63, suggested activity: Make a scrapbook with pictures of your favorite memories
For Aiden, predicted age: 33, suggested activity: Fix something that's broken in your house
Total time (sync): 5.013090200000079
```