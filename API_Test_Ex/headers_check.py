print("----------------------------------------------")
print("HEADERS SET")

import requests
import json
from fynctions import *

print(""" Test case:
    - Endpoint is: https://postman-echo.com/headers
    - Request will be sent by GET method.
    - Headers content will be sent in the json parameter to the Endpoint.
    - First and Second texts will be written inside the dictionary which will be assigned to Variable1 & Variable2, respectively.
    - Response is expected as, Variable1 = "first" & Variable2 = "second"
    - Returned value will be related headers' variable if the process works successfully.
    - Status Code expected to be = 200
""")

url = 'https://postman-echo.com/headers'

response = requests.get(url, json=headers_content(), headers=headers_function("first", "second"))
json_response = response.json()

assert response.status_code == 200

for element in json_response['headers']:
    if element == "variable1":
        print(json_response['headers'][element])
        assert json_response['headers'][element] == "first"
    if element == "variable2":
        print(json_response['headers'][element])
        assert json_response['headers'][element] == "second"

print(response.status_code)
