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
    context.addBook_response = requests.post(context.url, json=context.addBook_response, headers=context.headers, ) # You sent POST and wait for repsonse.

@then('book is successfully added'): # You want to retrieve the Book ID
def step_impl(context):
    print(context.addBook_response.json())
    response_json = context.addBook_response.json()
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
    context.addBook_response = requests.post(context.url, json=context.addBook_response, headers=context.headers, ) # You sent POST and wait for repsonse.

@then('book is successfully added'): # You want to retrieve the Book ID
def step_impl(context):
    print(context.addBook_response.json())
    response_json = context.addBook_response.json()
    print(type(response_json))

    context.bookId = response_json['ID']
    print(bookId)
    assert response_json["Msg"] == "successfully added"