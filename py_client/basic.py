import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything" # echo back what i send to it


get_response = requests.get(endpoint) # Application programming interface

print(get_response.text) # printing out the source code / raw text response that we got from our request

