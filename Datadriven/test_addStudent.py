import json
import jsonpath
import requests
from Datadriven import Library

def test_addMultipleStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('D:\\Ankit\\apiwork\\addstudent.json', 'r')
    body = json.loads(file.read())
    obj = Library.Common("D:\\Ankit\\apiwork\\testdata.xlsx", "Sheet1")
    col = obj.fetchColumnCount()
    keyList = obj.fetchKeyName()
    row = obj.fetchRowCount()

    for i in range(2,row+1):
        updated_json_request = obj.updateRequestWithData(i, body, keyList)
        response = requests.post(API_URL, updated_json_request)
        print(response)