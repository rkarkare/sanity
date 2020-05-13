import requests
import pytest
import json



def test_health_check(get_auth_token,url):
   a = url+'/healthcheck/hive/status'
   print(a)
   response = requests.get(a, headers={'Authorization': get_auth_token})
   assert response.status_code == 200


def test_full_server_status(get_auth_token,url):
   #b = url('/healthcheck/hive/fullServerStatus')
   b= url+'/healthcheck/hive/fullServerStatus'
   print(b)
   response = requests.get(b, headers={'Authorization': get_auth_token})
   payload =response.json()
   new = payload.items()
   keys = list(new)
   error = keys[2]
   assert error == ('error', None)