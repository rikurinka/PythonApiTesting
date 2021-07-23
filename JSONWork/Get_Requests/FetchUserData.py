import requests

#API URL

url = "https://reqres.in/api/users?page=2"

#send get requests
response = requests.get(url)
print(response)

#display response content
print(response.content)
print("-------------")
#print(response.headers)

#Validate status code
print(response.status_code)

#compare the result (for fail change code to 201)
assert response.status_code == 200

#fetch response header
print(response.headers)
print(response.headers.get(('Date')))
print(response.headers.get(('Server')))

#fetch cookies
print(response.cookies)

#fetch encoding
print(response.encoding)

#fetch elapsed time -time taken request sent and response received
print(response.elapsed)
