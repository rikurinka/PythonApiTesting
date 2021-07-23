#Post
import json
import pytest
import jsonpath
import requests

#Run in terminal
#pytest -v TestCases - details can be seen

url = "https://reqres.in/api/users"


@pytest.fixture(scope="module")
def start_exe():
    global file
    file = open("D:\\API\\createuserjson.json", 'r')

#post or put - send request body
@pytest.mark.Smoke
def test_create_other_user(start_exe):

    json_input = file.read()
    request_json = json.loads(json_input)

    print(request_json)

    # make post request

    response = requests.post(url, request_json)
    print(response.text)

    assert response.status_code == 201


def test_create_new_user(start_exe):
    #user input json file
    #file = open("D:\\API\\createuserjson.json", 'r')
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