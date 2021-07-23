import json

import jsonpath
import requests

url = "https://reqres.in/api/users"

#post or put - send request body

#
file = open("D:\\API\\createuserjson.json", 'r')
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)

#make post request

response= requests.post(url,request_json)
print(response.text)

assert response.status_code == 201

#fetch header from response
print(response.headers)
print(response.headers.get('Content-Length'))

#Parse response in json format

response_json = json.loads(response.text)

id = jsonpath.jsonpath(response_json, 'id')
print(id[0])

'''
headers = {'content-type': 'text/xml'}
url = r'https://xxxxxxxxxxxxxxxx/Services/LoansIntegrationService.svc?singleWsdl'
client = Client(url ,wsse=UsernameToken(‘Demo’, ‘test123’))
body = client.transport.load(r'.\wsdl\LoanRequest.wsdl') #to fetch the updated wsdl file and pass it to request
result = client.transport.post(message=body, address=url, headers=headers)
print(result.content) #An error occurred when verifying security for the message.

'''