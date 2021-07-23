#create dictonary of parameter

import requests
#just returning whatever we send
param={'name': 'testing', 'email': 'test@gmail.com', 'number': '34343433'}
response = requests.get("https://httpbin.org/get", params=param)
print(response.text)

#pytest unit test framework
#why need?
#many adva (i) in which condition what all test case can be executed
#(ii) prerequisite (before) and post script in unit test framework (after execution)
#(iii) assertions - actual and expected result
#(iv) generate report