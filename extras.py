# How to parse JSON Strings in Python..
import requests
import json
# Language is a key which is a list.

courses = ' {"name": "Alpay", "languages": ["Java", "Python"]} ' # This variable holds JSON String

# We will convert JSON to Dictionary type so that we will be able to read it.
# ****** Convert JSON.STRING -> to DICTIONARY thats the point at first. ******

dict_courses = json.loads(courses) # by print(type(dict_courses)) adding this you can see the type.
print(dict_courses)

print(dict_courses['name']) # We reached the name KEY!

# print(dict_courses['languages']) # What we will get out of this row is, a LIST!

# list_language = dict_courses['languages'] # so We assigned that list to a new LIST VARIABLE we created so that we can get he first ITEM.

# print(list_language[0])

print(dict_courses['languages'][0])

# ****** Parse content present in JSON FILE ******

with open('C:\Users\alpay\Downloads\course.json') as f:

    data = json.load(f) # Now it is dictionary again.
    # you can minimize when it is KEY in the JSON. If it is normal string under that key, you can [0] choose it by
    # indexing. but if there is another key after key you have to call it the way you called the first key.
    print(data)
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(type(data['courses'])) # There will be more KEYs under the 'courses'

    for course in data['courses']:
        if course == "TRY":
            assert course['price'] == 45
            print(course['price'])

            print(type(data['courses']))


# ******* COMPARE TO JSON files ******

# We defined second dictionary to compared with course1.json
with open('C:\Users\alpay\Downloads\course1.json') as fi:
    data2 = json.load(fi)
    assert data == data2



# What type of HTTP method API is having? Method = GET
# PYTHON ACCEPTS get method parameters as dictionary.
# when you call it you will get a response back.


response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty2'})

print(response.text)

dict_response = json.loads(response.text) # we get list or dict
print(dict_response[0]['isbn'])


# ******* #
json_response = response.json() # this way will provide you the LIST or DICT right away. 




