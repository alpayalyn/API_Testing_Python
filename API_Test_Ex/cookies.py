print("----------------------------------------------")
print("COOKIE SET")

import requests
import json

response = requests.get('https://postman-echo.com/cookies/set', cookies={"foo1":"bar1", "foo2":"bar2"})
json_response = response.json()
print(json_response)

for element in json_response['cookies']:
    if element == "foo1":
        print(json_response['cookies'][element])
        assert json_response['cookies'][element] == "bar1"
    if element == "foo2":
        print(json_response['cookies'][element])
        assert json_response['cookies'][element] == "bar2"

print(response.status_code)

print("----------------------------------------------")
print("DELETE METHOD")

response = requests.get('https://postman-echo.com/cookies/delete', data="foo2") # Silme işlemini çözmem gerekiyor.
json_response = response.json()
print(json_response)

for element in json_response['cookies']:
    if element == "foo1":
        print(json_response['cookies'][element])
        assert json_response['cookies'][element] == "bar1"
    if element == "foo2":
        print(json_response['cookies'][element])
        assert json_response['cookies'][element] == "bar2"
print("----------------------------------------------")
