import requests
import datetime

current_date = datetime.date.today()
format_date_time = current_date.strftime("%Y%m%d")

API_ENDPOINT = "https://pixe.la/v1/users"
USER_TOKEN = ".........."
USER_NAME = ".........."

# ---Create pixe.la account---
USER_DATA = {
    "token": USER_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=API_ENDPOINT, json=USER_DATA)
# print(response.text)

# ---Create Graphs---
USER_GRAPH_API = f"https://pixe.la/v1/users/{USER_NAME}/graphs"

REQ_HEADER = {
    "X-USER-TOKEN": USER_TOKEN
}

GRAPH_PAR = {
    "id": "daysofcode",
    "name": "Coding Challenge",
    "unit": "comit",
    "type": "int",
    "color": "ajisai",
}

# response = requests.post(url=USER_GRAPH_API, json=GRAPH_PAR, headers=REQ_HEADER)
# print(response.text)

# ---Adding a Pixel Habit---
USER_GRAPH_EP = f"{USER_GRAPH_API}/daysofcode"
quantity = input("How many code project you commit today ")

ADDING_PIXEL = {
    "date": format_date_time,
    "quantity": quantity
}

response = requests.post(url=USER_GRAPH_EP, json=ADDING_PIXEL, headers=REQ_HEADER)
print(response.text)

# ---Update a Pixel Habit---
UPDATE_GRAPH_EP = f"{USER_GRAPH_EP}/{format_date_time}"

UPDATE_PIXEL = {
    "quantity": quantity
}

# response = requests.put(url=UPDATE_GRAPH_EP, json=UPDATE_PIXEL, headers=REQ_HEADER)
# print(response.text)

# ---Delete a Pixel Habit---
DELETE_GRAPH_EP = UPDATE_GRAPH_EP

# response = requests.delete(url=DELETE_GRAPH_EP, headers=REQ_HEADER)
# print(response.text)
