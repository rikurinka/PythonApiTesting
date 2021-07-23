import requests
import json
import jsonpath

#fecthing data from one request and adding as input for other request is chaining
#since id is local variable it cannot be accessed in 'get' method, hence need to declare id as global
def test_add_new_student():
    global id
    API_URL = r'http://thetestingworldapi.com/api/studentsDetails'
    f = open(r'D:\API\Addstudent.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(API_URL, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

#if we want to concatenate the url and value we need to typecast as string
def test_get_details():
    API_URL =r'https://thetestingworldapi.com/api/studentsDetails/'+str(id[0])
    response = requests.get(API_URL)
    print(response.text)
