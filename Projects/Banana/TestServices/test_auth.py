from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import config

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.host = config.URL
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration.api_key['Authorization'] = config.phone_login()
# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

def test_password_account():
    x_tenant_type = 'client' # str |  来自哪个平台
    x_uuid = '56632670083354620' # str | 
    password = 'qwer`123'
    body = swagger_client.SetPasswordReq(password)
    try:
        # 注册初次设置密码
        api_response = api_instance.init_password(body=body, x_tenant_type=x_tenant_type, x_uuid=x_uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->init_password: %s\n" % e)
        # e = eval(e.body)
        # msg = e['msg']
        # pprint(msg)
        