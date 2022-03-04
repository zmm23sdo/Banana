from __future__ import print_function
from unicodedata import name
import config
from email import header
import time
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models import PasswordLoginReq
from pprint import pprint
import random

configuration = swagger_client.Configuration()
configuration.host = config.URL

access_token = config.phone_login()
configuration.api_key['Authorization'] = access_token
x_tenant_type = "client"
x_uuid = config.get_session_info()
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))


def test_update_profile():
    user_name = "mingvtest"+ random.randint(0,99)
    name = "Edison" + config.now()
    body = swagger_client.UpdateProfileReq(user_name, name)
    try:
        api_response = api_instance.update_profile(body=body,x_tenant_type=x_tenant_type,x_uuid=x_uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->init_password: %s\n" % e)