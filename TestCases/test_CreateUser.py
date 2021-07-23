#Post
import json

import jsonpath
import requests

url = "https://reqres.in/api/users"

#post or put - send request body
def test_create_other_user():
    file = open("D:\\API\\createuserjson.json", 'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    print(request_json)

    # make post request

    response = requests.post(url, request_json)
    print(response.text)

    assert response.status_code == 201


def test_create_new_user():
    #user input json file
    file = open("D:\\API\\createuserjson.json", 'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    print(request_json)

    #make post request

    response= requests.post(url,request_json)
    print(response.text)

    #fetch header from response
    print(response.headers)
    print(response.headers.get('Content-Length'))

    #Parse response in json format

    response_json = json.loads(response.text)

    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])