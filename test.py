from unittest import result
from urllib import request
from wsgiref import headers
import  requests
import json

url = 'http://192.168.2.26/zabbix/api_jsonrpc.php'
username = "Admin"
password = "030699Tbo"

def usertoken():
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": username,
            "password": password
        },
        "id": 0,
        # "auth": None,
    }

    head = {'Content-Type': 'application/json'}
    request =requests.post(url, data=json.dumps(data), headers=head)
    # print(request.text)
    connect = json.loads(request.text)
    return connect['result']


def get_host():
    user_token = usertoken()
    data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": [
                    "hostid",
                    "host"
                ],
                "selectInterfaces":[
                    "interfaceid",
                    "ip"
                ]
            },
            "id": 0,
            "auth": user_token
        }
    head = {'Content-Type': 'application/json'}
    request = requests.post(url, data=json.dumps(data), headers=head)
    print(request.text)
    # dict = json.loads(request.content)
    # print(dict)




if __name__ == '__main__':
    usertoken()
    get_host()
