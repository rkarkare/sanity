import requests
import pytest
import json

# Auth param not required


def test_health_check(get_hiveCore_auth_token, hivecore_url):
    endpoint = hivecore_url+'/healthcheck/hive/status'
    print(endpoint)
    response = requests.get(
        endpoint, headers={'Authorization': get_hiveCore_auth_token})
    assert response.status_code == 200

# Auth param not required


def test_full_server_status(get_hiveCore_auth_token, hivecore_url):
    endpoint = hivecore_url + '/healthcheck/hive/fullServerStatus'
    response = requests.get(
        endpoint, headers={'Authorization': get_hiveCore_auth_token})
    error = json.loads(response.text)['error']
    assert error == None and response.status_code == 200


def test_full_mpos_server_status(get_mpos_auth_token, mpos_url):
    endpoint = mpos_url + '/healthcheck/mpos/fullServerStatus'
    response = requests.get(
        endpoint, headers={'Authorization': get_mpos_auth_token})
    error = json.loads(response.text)['error']
    assert error == None and response.status_code == 200


def test_end_to_end_purchase_scenario_1(mpos_url, get_mpos_auth_token, hivecore_url, get_hiveCore_auth_token):
    mpos_endpoint = mpos_url + '/management/mpos/transactions/details'
    hive_endpoint = hivecore_url+'api/v3/management/hive/transactions/{id}'
    with open('src/resources/purchase.json') as purchase:
        payload = json.load(purchase)
    response = requests.post(
        mpos_endpoint, headers={'Authorization': get_mpos_auth_token}, json=payload)
    assert response.status_code == 200
    # get transaction id from response
    # verifying on Hive Core that transaction is didplayed
    response = requests.get(
        hive_endpoint, headers={'Authorization': get_hiveCore_auth_token}, params="")
    assert response.status_code == 200


def test_end_to_end_void_scenario_2(mpos_url, get_mpos_auth_token, hivecore_url, get_hiveCore_auth_token):
    # should not repeat below lines of code
    mpos_endpoint = mpos_url + '/management/mpos/transactions/details'
    hive_endpoint = hivecore_url+'api/v3/management/hive/transactions/{id}'
    with open('src/resources/void.json') as void:
        payload = json.load(void)
    response = requests.post(
        mpos_endpoint, headers={'Authorization': get_mpos_auth_token}, json=payload)
    assert response.status_code == 200
    # get transaction id from response
    # verifying on Hive Core that transaction is didplayed
    response = requests.get(
        hive_endpoint, headers={'Authorization': get_hiveCore_auth_token}, params="")
    assert response.status_code == 200
