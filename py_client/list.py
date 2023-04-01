import requests

endpoint = "http://127.0.0.1:3000/incomes/" 

get_response = requests.get(endpoint)
print(get_response.json())
