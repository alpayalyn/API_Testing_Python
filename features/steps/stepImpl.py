import requests
from behave import *
from payLoad import *
from utilities.resources import *
from utilities.configurations import *
import json

@given('the Book details which needs to be added to Library') # to be able to use the local variables in other modules below, you can you context. to use the VARIABLE.
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload("asdasd")

@when('we execute the AddBook PostAPI method'):
def step_impl(context):
    context.response = requests.post(context.url, json=context.response, headers=context.headers, ) # You sent POST and wait for repsonse.

@then('book is successfully added'): # You want to retrieve the Book ID
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    print(type(response_json))

    context.bookId = response_json['ID']
    print(bookId)
    assert response_json["Msg"] == "successfully added"

@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload(isbn, aisle)

@when('we execute the AddBook PostAPI method'):
def step_impl(context):
    context.response = requests.post(context.url, json=context.response, headers=context.headers, ) # You sent POST and wait for repsonse.

@then('book is successfully added'): # You want to retrieve the Book ID
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    print(type(response_json))

    context.bookId = response_json['ID']
    print(bookId)
    assert response_json["Msg"] == "successfully added"

@given('I have github auth credentials')
# To be able to login to github account
# -requests.session assigned to sessionn object. Auth branch of the session, was assigned with correct auth info.
# Then we get to the github repo by the sessionn object which already has the authentication
# A response is being received, and you can check its status.
# Status code can be entered via github.feature but It also can be used by BookAPI.feature as well.
# You just need to add AND after THEN; ie. Then AND Then .....<statuscode> below there |    | version of the info entrance.
# but if you want you can directly, copy the exact text which is written then(here) and copy it to the feature file.
# and write the statuscode -> {statuscode:d} if you do this you can directly type in the feature what you want to be as a variable.
# INFO --- ACTION --- RESULTS
def step_impl(context):
    context.sessionn = requests.session()
    context.sessionn.auth = auth = ('rahulshettcademy', getPassword())

@when('I hit getRepo API of Github'):
def step_impl(context):
    context.response = context.sessionn.get(ApiResources.githubRepo)

@then('status code of response should be {statuscode:d}'): # You want to retrieve the Book ID
def step_impl(context, statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode

