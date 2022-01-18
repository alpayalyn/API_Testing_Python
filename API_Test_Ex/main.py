"""
# -------------
print("----------------------------------------------")

import requests
import json

headers = {
    "headers": {
        "host": "echo.getpostman.com",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, sdch",
        "accept-language": "en-US,en;q=0.8",
        "cache-control": "no-cache",
        "my-sample-header": "Lorem ipsum dolor sit amet",
        "postman-token": "3c8ea80b-f599-fba6-e0b4-a0910440e7b6",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
        "x-forwarded-port": "443",
        "x-forwarded-proto": "https"
    }
}

response = requests.get('https://postman-echo.com/headers',
                        json=headers, headers={"my-sample-header": "Lorem ipsum dolor sit amet"})

json_response = response.json()
print(json_response)
print(type(json_response))

assert response.status_code == 200

print(response.status_code)
print(response.headers)
"""
# -------------
"""
import requests
import json

headers = {
  "headers": {
    "host": "echo.getpostman.com",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, sdch",
    "accept-language": "en-US,en;q=0.8",
    "cache-control": "no-cache",
    "my-sample-header": "Lorem ipsum dolor sit amet",
    "postman-token": "3c8ea80b-f599-fba6-e0b4-a0910440e7b6",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
    "x-forwarded-port": "443",
    "x-forwarded-proto": "https"
  }
}

response = requests.get('https://postman-echo.com/cookies/set',params={"foo1":"bar1", "foo2":"bar2"})

json_response = response.json()
print(json_response)
print(type(json_response))
data = json_response['cookies']['foo1']

assert data == "bar1", "Wrong cookies chosen"
assert response.status_code == 200
print(response.status_code)

deleted_response = requests.get('https://postman-echo.com/cookies/delete',params={"foo1"})
json_deleted_response = deleted_response.json()
print(json_deleted_response)
"""
# ---------








