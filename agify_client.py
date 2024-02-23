import requests

def predict_age(name: str) -> int:
    response = requests.get(f"https://api.agify.io?name={name}")
    age = response.json().get('age', 0)  # Default to 0 if age not found
    return age