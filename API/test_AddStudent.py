import requests
import json
import jsonpath


def test_addNewStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('D:\\Ankit\\apiwork\\addstudent.json', 'r')
    body = json.loads(file.read())
    response = requests.post(API_URL, body)
    # print(response.text)


def test_getStudentDetails():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/5340"
    response = requests.get(API_URL)
    # result = json.loads(response.text)
    result = response.json()
    id = jsonpath.jsonpath(result, 'data.id')
    assert id[0] == 5340

def test_updateStudent():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/5340"
    file = open('D:\\Ankit\\apiwork\\addstudent.json', 'r')
    body = json.loads(file.read())
    response = requests.put(API_URL,body)
    print(response.text)


def test_deleteUser():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/5340"
    response = requests.delete(API_URL)
    print(response.text)
