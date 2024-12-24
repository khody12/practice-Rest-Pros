import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything" # echo back what i send to it

endpoint = "http://localhost:8000/api/"

# we have our end point which is a certain url, we pass into requests.get, 
# django will now take this url, and try to map a certain view to it, if there is a view
# it will go inside that view and then do what the view says. right now, we have a view within api that imports data
# from products, and it then returns the information to get_response. 

get_response = requests.get(endpoint, params={"abc":123}, json={"query":"Hello world"}) # Application programming interface

#print(get_response.text) # printing out the source code / raw text response that we got from our request
#print(get_response.status_code)

# the difference between rest and regular requests

# Http request -> html
#rest api request (http) -> JSON

# javascript object notation (json) ~ python dict

print(get_response.json())

#print(get_response.status_code)