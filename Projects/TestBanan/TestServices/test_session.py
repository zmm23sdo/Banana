from __future__ import print_function
import config
from email import header
import time
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models import PasswordLoginReq

from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.host = "https://gateway-banana-dev.chunsutech.com/auth"
access_token = config.phone_login()
configuration.api_key['Authorization'] = access_token
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
x_tenant_type = "client" # str |  来自哪个平台


def test_get_session_info():
    try:
        api_response = api_instance.get_session_info(x_tenant_type=x_tenant_type,authorization=access_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->init_password: %s\n" % e)
        
        
        
        
        
        
        
        
        
        
        
        
        
def test_phone_login():
    password = "qwer`123" # str |  密码
    phone_number = "8615195927818" # str | 手机号
    body = PasswordLoginReq(phone_number, password)
    
    try:
    # 手机号密码登录
        api_response = api_instance.password_login(x_tenant_type=x_tenant_type, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->init_password: %s\n" % e)

# def test_
