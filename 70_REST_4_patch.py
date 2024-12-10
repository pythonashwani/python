import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
print(response.json()) # {'userId': 1, 'id': 10, 'title': 'Mow lawn', 'completed': True}

print(response.status_code) #200