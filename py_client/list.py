import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
username = input("what is ur username\n")
password = getpass()
auth_response = requests.post(endpoint, json={'username':'cfe', 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}" # standard is token {token}, but within api we make an authentications.py and change the keyword.
    }
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())

