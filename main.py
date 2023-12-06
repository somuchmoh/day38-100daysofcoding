import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
GENDER = "female"
WEIGHT_KG = 70
HEIGHT_CM = 154
AGE = 27

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
body = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=body, headers=headers)
response.raise_for_status()
exercise_data = response.json()
exercise = exercise_data['exercises'][0]['name'].title()
duration = exercise_data['exercises'][0]['duration_min']
calories = exercise_data['exercises'][0]['nf_calories']
ex_id = exercise_data['exercises'][0]['tag_id']


USERNAME = os.getenv("USERNAME")
PROJECT_NAME = os.getenv("PROJECT_NAME")
SHEET_NAME = os.getenv("SHEET_NAME")
AUTHORIZATION = f"Bearer {os.getenv("AUTHORIZATION")}"
excel_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
today = datetime.now()

ex_body = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
        "id": ex_id
    },
}

bearer_headers = {
    "Authorization": AUTHORIZATION,
}

excel_response = requests.post(url=excel_endpoint, json=ex_body, headers=bearer_headers)
print(excel_response.text)
