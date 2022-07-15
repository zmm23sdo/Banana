import requests
URL = "https://gateway-banana-dev.chunsutech.com/auth"
headers = {'Authorization': '', 'X-Tenant-Type':'admin'}


username = "mvtest1"
password = "qwer`123"
def AdminLogin(username, password, headers):
    path = URL + "/d/session/username"
    res = requests.post(path, json = {
        "username":username,
        "password":password
    },headers=headers)
    return res
