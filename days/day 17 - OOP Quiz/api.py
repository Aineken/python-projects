import requests

url = "https://opentdb.com/api.php?amount=10&category=11&type=boolean"

# Make a GET request to the API endpoint
response = requests.get(url)
response_data = response.json()



datas = response_data["results"]