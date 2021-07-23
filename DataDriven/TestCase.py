import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

#data driven testing
#with multple datas in registration page
#multiplestudent from excel
#static data

def test_add_multiple_students():
    API_Url = r'http://thetestingworldapi.com/api/studentsDetails'
    f = open(r'D:\API\Addstudent.json')
    request_json = json.loads(f.read())

    obj = Library.Common(r"D:\API\dataxl.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()


    #Excel code

    for i in range(2,row+1):
        updated_request_json = obj.update_request_with_data(i,request_json,keyList)
        response = requests.post(API_Url,updated_request_json)
        print(response.text)