import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything" # echo back what i send to it

endpoint = "http://localhost:8000/api/"


get_response = requests.get(endpoint, json={"query":"Hello world"}) # Application programming interface

print(get_response.text) # printing out the source code / raw text response that we got from our request
print(get_response.status_code)

# the difference between rest and regular requests

# Http request -> html
#rest api request (http) -> JSON

# javascript object notation (json) ~ python dict

print(get_response.json())

#print(get_response.status_code)