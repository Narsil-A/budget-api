import requests

endpoint = "http://127.0.0.1:3000/budgets/" 

get_response = requests.get(endpoint)
print(get_response.json())
