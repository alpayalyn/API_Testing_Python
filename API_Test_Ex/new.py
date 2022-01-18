import json
import configparser
from payLoad import *
from utilities.resources import *
from utilities.configurations import *

import requests

url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {
        "x-forwarded-proto": "https",
        "x-forwarded-port": "443",
        "host": "postman-echo.com",
        "x-amzn-trace-id": "Root=1-61e58d54-496b170446fed91a6ceca1c0",
        "content-length": "475",
        "content-type": "application/json",
        "user-agent": "PostmanRuntime/7.28.0",
        "accept": "*/*",
        "postman-token": "c4033666-b67f-4e60-9e8d-f47ab18319ff",
        "accept-encoding": "gzip, deflate, br",
        "cookie": "sails.sid=s%3Ah0yLtjnSBjfACW8LrPBj5-o-1qNc392x.9I4Gso8kjnZb%2BRkU%2FY5EKDy4KJAlNZ9I3Lt1FaMt4Ak"
    }
addBook_response = requests.post(url,json=addBookPayload("feasrewe", "123"),headers=headers, )
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(bookId)
# Delete Book -
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

    "ID": bookId
}, headers={"Content-Type": "application/json"},
                                    )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

# Authentication AND SESSION MANAGER ADJUSTMENTS
# session has a capability, to reach request and authentitacion information. by just defined like below. So you can observe difference between two.

sessionn = requests.session()
sessionn.auth = auth=('rahulshettcademy',getPassword())

# FIRST EXAMPLE #########################

url = "https://api.github.com/user"
github_response = requests.get(url,verify=False,auth=('rahulshettcademy',getPassword()))

print(github_response.status_code)

# SECOND EXAMPLE ######################## WITH SESSION

url2 = "https://api.github.com/user/repos"
response = sessionn.get(url2)
print(github_response.status_code)

