import requests
import pytest
import json

# Auth param not required


def test_health_check(get_hiveCore_auth_token, url):
    endpoint = url+'/healthcheck/hive/status'
    print(endpoint)
    response = requests.get(
        endpoint, headers={'Authorization': get_hiveCore_auth_token})
    assert response.status_code == 200

# Auth param not required


def test_full_server_status(get_hiveCore_auth_token, url):
    endpoint = url+'/healthcheck/hive/fullServerStatus'
    response = requests.get(
        endpoint, headers={'Authorization': get_hiveCore_auth_token})
    error = json.loads(response.text)['error']
    assert error == 'None' and response.status_code == 200


def test_end_to_end_scenario_1(mpos_url, get_mpos_auth_token):
    endpoint = mpos_url+''
    response = requests.get(
        endpoint, headers={'Authorization': get_mpos_auth_token})


# assert error == None
