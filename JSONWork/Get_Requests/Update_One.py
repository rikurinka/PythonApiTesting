import requests
import json
import jsonpath

#Put request -response code 200

url ="https://reqres.in/api/users/2"

#input in file

input_file = open('D:\\API\\createuserjson.json', 'r')
json_input = input_file.read()
request_json = json.loads(json_input)

#Put

response = requests.put(url,request_json)

assert response.status_code == 200

#parse response content
response_json = json.loads(response.text)
updated_list = jsonpath.jsonpath(response_json, 'updatedAt')

print(updated_list[0])