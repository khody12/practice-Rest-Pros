import requests

endpoint = "http://localhost:8000/api/products/"
headers = {
    'Authorization': 'Bearer ecebdad7ddc542c094af887f65838df4d52c05a3'
}
data = {
    "title": "This field is done",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())

