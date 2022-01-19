print("----------------------------------------------")
print("COOKIE SET")

import requests
import json
from fynctions import *

print(""" Test case:
    - Endpoint is: https://postman-echo.com/cookies/set
    - Request will be sent by GET method.
    - You can change the content of cookies will be sent to the Endpoint.
    - Those 2 Cookies will be added to cookies section of the Endpoint.
    - Returned value will be whatever will be entered.
    - Validation of those 2 Contents were sent successfully or not, is made inside of the for loop below.
    - 2 content will be printed.
    - 2 times Status Code expected to be written as = 200
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

print("----------------------------------------------")
print("COOKIE DELETE")

print(""" Test case:
    - Endpoint is: https://postman-echo.com/cookies/delete
    - Request will be sent by GET method.
    - All the cookies which were stored in the Cookie will be deleted in the end of this section.
    - Status Code expected to be written as = 200
""")

url = 'https://postman-echo.com/cookies/delete'

response = requests.get(url)
json_response = response.json()

print(json_response['cookies'])
assert len(json_response['cookies']) == 0, "Cookies couldn't be deleted, properly."
assert response.status_code == 200, "Cookies are deleted."
print(response.status_code)
