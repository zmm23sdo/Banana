from __future__ import print_function
import swagger_client
from swagger_client.models import PasswordLoginReq
import datetime
from pprint import pprint

URL =  "https://gateway-banana-dev.chunsutech.com/auth"
# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.host = URL


x_tenant_type = "client" # str |  来自哪个平台


def now():
    now = datetime.datetime.now().isoformat() + "Z"
    print(now)
    return now

def phone_login():
    password = "qwer`123" # str |  密码
    phone_number = "8615195927818" # str | 手机号
    body = PasswordLoginReq(phone_number, password)
    api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
    api_response = api_instance.password_login(x_tenant_type=x_tenant_type, body=body)
    # pprint(api_response)
    access_token = str(api_response.access)
    # pprint(access_token)
    return access_token


def get_session_info():#    get uuid
    
    access_token = phone_login()
    configuration.api_key['Authorization'] = access_token
    api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
    api_response = api_instance.get_session_info(x_tenant_type=x_tenant_type,authorization=access_token)
    pprint(api_response)
    uuid = str(api_response.uuid)
    pprint(uuid)
    return uuid