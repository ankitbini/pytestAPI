import requests
from requests.auth import HTTPBasicAuth

def test_basic_auth():
    response = requests.get('https://api.github.com/user', auth = HTTPBasicAuth('ankitbini', 'GHAR!wsXm2s'))
    print(response.text)