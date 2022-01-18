print("----------------------------------------------")
print("COOKIE SET")

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

url = 'https://postman-echo.com/cookies/set'
cookie1 = "bar1"
cookie2 = "bar2"

response = requests.get(url, cookies=cookies_function(cookie1, cookie2))
json_response = response.json()

for element in json_response['cookies']:
    if element == "cookie_1":
        print(json_response['cookies'][element])
        assert json_response['cookies'][element] == cookie1
        assert response.status_code == 200, "Cookie couldn't be set properly"
        print(response.status_code)

    if element == "cookie_2":
        print(json_response['cookies'][element])
        assert json_response['cookies'][element] == cookie2
        assert response.status_code == 200, "Cookie couldn't be set properly"
        print(response.status_code)
