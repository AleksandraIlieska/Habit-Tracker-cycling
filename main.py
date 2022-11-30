import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "fGdkjskJsmskdjJdjhdueAh3hdj89shdja2jahdj"
USERNAME = "aleksandra"
GRAPH_ID = "graph1"

# Creating user account on pixela
user_params = {
    "token": TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)


# Creating graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"     # or "https://pixe.la/v1/users/aleksandra/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# We can see the graph at the following url: "https://pixe.la/v1/users/aleksandra/graphs/graph1.html"


# Creating pixel on the graph (ex.Adding 23 km cycling on current day)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# or "https://pixe.la/v1/users/aleksandra/graphs/graph1"

today = datetime.now()
# today = datetime(year=2022, month=11, day=30)

pixel_data_1 = {
    "date": "20221123",
    "quantity": "100",
}

pixel_data_2 = {
    "date": "20221128",
    "quantity": "56",
}

pixel_data_3 = {
    "date": today.strftime("%Y%m%d"),    # Formatting today date as accepted in pixela
    "quantity": "23",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data_1, headers=headers)
response = requests.post(url=pixel_creation_endpoint, json=pixel_data_2, headers=headers)
response = requests.post(url=pixel_creation_endpoint, json=pixel_data_3, headers=headers)


# Using put method
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "101"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

# Using delete method
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)


