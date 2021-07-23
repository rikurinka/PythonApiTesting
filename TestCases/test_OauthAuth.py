import requests
import json
import jsonpath


def test_oauth_api():
    token_url= r'https://thetestingworldapi.com/Token'
    #dictonary - granttype(key)
    data = {'grant_type':'password', 'username':'admin','password':'password'}
    response = requests.post(token_url,data)
    print(response.text)
    token_value = jsonpath.jsonpath(response.json(),'access_token')

    auth={'Authentication':'Bearer'+token_value[0]}
    API_uRL = r'https://thetestingworldapi.com/api/StDetails/334974'
    response = requests.get(API_uRL, headers=auth)
    print(response.text)