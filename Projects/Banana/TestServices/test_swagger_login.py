from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models import PasswordLoginReq

from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.host = "https://gateway-banana-dev.chunsutech.com/auth"

api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
x_tenant_type = "client" # str |  来自哪个平台

def test_swagger():
    password = "qwer`123" # str |  密码
    phone_number = "8615195927818" # str | 手机号
    body = PasswordLoginReq(phone_number, password)
    api_response = api_instance.password_login(x_tenant_type=x_tenant_type, body=body)

    pprint(api_response)
