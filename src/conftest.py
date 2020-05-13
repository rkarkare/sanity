import pytest
import requests

@pytest.fixture(scope="session")
def url():
    version='V3'
    return 'https://virginia-integration-hivecore.mobeewave-hive.com/api/'+version

@pytest.fixture(scope="session")
def get_auth_token():

    endpoint = 'https://virginia-integration-hivecore.mobeewave-hive.com/api/V3/authentication/hive/login'
    payload = {
        "username": "convergeadmin",
        "password": "Mobeewave2015"
    }
    response = requests.post(endpoint, json=payload)
    status = response.status_code
    body=response.json()
    new=body.items()
    keys =list(new)
    auth_token = keys[1][1]['tokens']['accessToken']
    #print(auth_token)
    return auth_token