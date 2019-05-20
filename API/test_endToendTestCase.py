import requests
import json
import jsonpath

def test_addNewUser():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('D:\\Ankit\\apiwork\\addstudent.json', 'r')
    body = json.loads(file.read())
    response = requests.post(API_URL, body)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_detail_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open('D:\\Ankit\\apiwork\\addtechdetails.json', 'r')
    body = json.loads(file.read())
    body['id'] = int(id[0])
    body['st_id'] = id[0]
    response = requests.post(tech_detail_url, body)
    print(response.text)

    sddress_url = "http://thetestingworldapi.com/api/addresses"
    file = open('D:\\Ankit\\apiwork\\address.json', 'r')
    body = json.loads(file.read())
    body['stId'] = id[0]
    response = requests.post(sddress_url, body)
    print(response.text)

    completedetail_url = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(completedetail_url)
    print(response.text)