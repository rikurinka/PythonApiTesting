import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

#parse request to json format

json_response = json.loads(response.text)

#Fetch the value using jsonpath
#list
first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(first_name[0])

fone_name= jsonpath.jsonpath(json_response, 'data[3].first_name')
print(fone_name[0])
print("--------------")

#convert str[i] and concatenate
for i in range(0,4):
    first_nm = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_nm[0])

#assert first_nm ==
