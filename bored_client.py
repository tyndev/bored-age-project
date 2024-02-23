import requests

def get_activity_for_age(age: int) -> str:
    # Simple logic to categorize age groups; adjust as needed
    if age < 18:
        type = "recreational"
    elif age <= 65:
        type = "diy"
    else:
        type = "relaxation"
    response = requests.get(f"http://www.boredapi.com/api/activity?type={type}")
    activity = response.json().get('activity', "Just relax!")
    return activity