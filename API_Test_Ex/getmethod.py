print("----------------------------------------------")
print("GET METHOD")

import requests
import json
from fynctions import *

print(""" Test case:
    - Endpoint is: https://postman-echo.com/get
    - Request will be sent by GET method.
    - id1=1 parameter will be sent to the Endpoint.
    - Response is expected as, "id1" : "1" under the "args" dict.
    - Returned value will be " 1 "
    - Status Code expected to be = 200
""")

url = "https://postman-echo.com/get"

response = requests.get(url,params=params_function("id1"))
json_response = response.json()
print(json_response["args"]["id1"])

assert response.status_code == 200
print(response.status_code)