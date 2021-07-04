import requests

parameters = {
    "amount": 20,
    "type": "boolean",
    "category": 15
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data["results"]
