import pytest
import requests
import json

version = "V3"


@pytest.fixture(scope="session")
def hivecore_url():
    return 'https://virginia-integration-hivecore.mobeewave-hive.com/api/' + version


@pytest.fixture(scope="session")
def mpos_url():
    return 'https://virginia-integration-mposcore.mobeewave-hive.com/api/' + version


@pytest.fixture(scope="session")
def get_mpos_auth_token():
    mpos_endpoint = 'https://virginia-integration-mposcore.mobeewave-hive.com/api/v3/authentication/mpos/login'
    payload = {
        "merchantAccountNumber": "0018175",
        "email": "shivakumar.mobeewave@gmail.com",
        "password": "Mobeewave2015"
    }
    return get_auth_token(mpos_endpoint, payload)


@pytest.fixture(scope="session")
def get_hiveCore_auth_token():

    hive_endpoint = 'https://virginia-integration-hivecore.mobeewave-hive.com/api/V3/authentication/hive/login'
    payload = {
        "username": "convergeadmin",
        "password": "Mobeewave2015"
    }
    return get_auth_token(hive_endpoint, payload)


def get_auth_token(endpoint, payload):
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 200
    auth_token = json.loads(response.text)['payload']['tokens']['accessToken']
    print(auth_token)
    return auth_token
