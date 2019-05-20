import requests
import json
import jsonpath

def test_oAuth():
    token_url = "http://thetestingworldapi.com/token"
    data = {'grant_type': 'password', 'username': 'admin', 'password': 'yourPassword'}
    response = requests.post(token_url, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')
    auth = {'Authorization': 'Bearer '+token_value[0]}
    API_URL = "http://thetestingworldapi.com/api/StDetails/5357"
    response = requests.get(API_URL, headers = auth)
    print(response.text)