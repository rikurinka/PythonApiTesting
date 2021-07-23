import requests
import json
import jsonpath

def test_Add_new_data():
    API_URL = r"http://thetestingworldapi.com/api/studentsDetails"
    f = open(r'D:\API\RequestPostJson.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(API_URL,request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tec_api_url=r"http://thetestingworldapi.com/api/technicalskills"
    f = open(r'D:\API\TecDetJson.json', 'r')
    request_json = json.loads(f.read())
    request_json['id'] = int(id[0])
    request_json['stId'] = id[0]
    response = requests.post(tec_api_url,request_json)
    print(response.text)

    address_api_url=r"http://thetestingworldapi.com/api/addresses"
    f = open(r'D:\API\AddressJson.json', 'r')
    request_json = json.loads(f.read())
    request_json['stId'] = id[0]
    response = requests.post(address_api_url,request_json)
    print(response.text)

    #final_api_url=r'http://thetestingworldapi.com/api/FinalStudentDetails/334975'
    final_api_url = r'http://thetestingworldapi.com/api/FinalStudentDetails/'+str(id[0])
    response= requests.get(final_api_url)
    print(response.text)


