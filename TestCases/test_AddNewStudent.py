import requests
import json
import jsonpath

#To run the test
#right click on empty area and select run on terminal
#type pytest test_AddNewStudent.py
#if u want to see details
#type pytest test_AddNewStudent.py -s

def test_add_student_data():
    API_URL = r"http://thetestingworldapi.com/api/studentsDetails"
    f = open(r'D:\API\RequestJson.json', 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL,json_request)
    print(response.text)


def test_update_student_data():
    API_URL = r"http://thetestingworldapi.com/api/studentsDetails/334965"
    f = open(r'D:\API\RequestJson.json', 'r')
    json_request = json.loads(f.read())
    response = requests.put(API_URL,json_request)
    print(response.text)

def test_get_student_data():
    API_URL=r"http://thetestingworldapi.com/api/studentsDetails/334952"
    response= requests.get(API_URL)
    print(response.text)
    json_response= json.loads(response.text)
    id = jsonpath.jsonpath(json_response,'data.id')
    print(id)
    assert id[0] == 334952

def test_get_second_student_data():
    API_URL = r"http://thetestingworldapi.com/api/studentsDetails/334965"
    response = requests.get(API_URL)
    print(response.text)
    #typecasting the value
    json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(id)
    assert id[0] == 334965

def test_delete_student():
    API_URL= r"http://thetestingworldapi.com/api/studentsDetails/334971"
    response = requests.delete(API_URL)
    print(response.text)

def test_get_second_student_data():
    API_URL = r"http://thetestingworldapi.com/api/studentsDetails/334971"
    response = requests.get(API_URL)
    print(response.text)
    #typecasting the value
    json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(id)
    assert id[0] == 334971