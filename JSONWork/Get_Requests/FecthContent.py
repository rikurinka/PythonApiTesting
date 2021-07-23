import requests
import json
import jsonpath

#API URL

url = "https://reqres.in/api/users?page=2"

#send get requests in objects
response = requests.get(url)
#print(response.content)

#specific value in response (content in response)
#Jsonpath can be used
#parsing json in json response
json_response = json.loads(response.text)
print(json_response)

#fetch specify value
#response will be list in pages
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])

assert pages[0] == 3