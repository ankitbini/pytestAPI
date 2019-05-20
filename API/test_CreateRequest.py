import requests
import json
import jsonpath
import pytest
url = 'https://reqres.in/api/users'

@pytest.fixture
def beforeConfig():
    global file
    # Read body from json file
    file = open('D:\\Ankit\\bodyfile.json', 'r')


def test_createNewUser(beforeConfig):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    result = json.loads(response.text)
    id = jsonpath.jsonpath(result, 'id')
    print("created account id = {}".format(id[0]))


def test_createanotherNewUser(beforeConfig):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    result = json.loads(response.text)
    id = jsonpath.jsonpath(result, 'id')
    print("created account id = {}".format(id[0]))