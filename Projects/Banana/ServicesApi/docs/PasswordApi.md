# swagger_client.PasswordApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_forget_pwd**](PasswordApi.md#email_forget_pwd) | **POST** /d/email/forget_pwd | 忘记密码step1-发送邮件
[**reset_password**](PasswordApi.md#reset_password) | **PUT** /d/password | 忘记密码step3-修改密码
[**sms_forget_pwd**](PasswordApi.md#sms_forget_pwd) | **POST** /d/sms/forget_pwd | 忘记密码step1-发送手机短信
[**update_password**](PasswordApi.md#update_password) | **PUT** /account/password | 个人中心修改密码
[**verify_email_code**](PasswordApi.md#verify_email_code) | **GET** /d/password/email | 忘记密码step2-验证邮件验证码
[**verify_phone_code**](PasswordApi.md#verify_phone_code) | **GET** /d/password/phone_code | 忘记密码step2-验证手机验证码

# **email_forget_pwd**
> EmptyResp email_forget_pwd(body, x_tenant_type)

忘记密码step1-发送邮件

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PasswordApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmailForgetPwdReq() # EmailForgetPwdReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # 忘记密码step1-发送邮件
    api_response = api_instance.email_forget_pwd(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->email_forget_pwd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailForgetPwdReq**](EmailForgetPwdReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> EmptyResp reset_password(body, x_tenant_type)

忘记密码step3-修改密码

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PasswordApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResetPasswordReq() # ResetPasswordReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # 忘记密码step3-修改密码
    api_response = api_instance.reset_password(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordReq**](ResetPasswordReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sms_forget_pwd**
> EmptyResp sms_forget_pwd(body, x_tenant_type)

忘记密码step1-发送手机短信

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PasswordApi(swagger_client.ApiClient(configuration))
body = swagger_client.SmsForgetPwdReq() # SmsForgetPwdReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # 忘记密码step1-发送手机短信
    api_response = api_instance.sms_forget_pwd(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->sms_forget_pwd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmsForgetPwdReq**](SmsForgetPwdReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> EmptyResp update_password(body, x_tenant_type, x_uuid)

个人中心修改密码

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PasswordApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePassword() # UpdatePassword | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
x_uuid = 'x_uuid_example' # str | 

try:
    # 个人中心修改密码
    api_response = api_instance.update_password(body, x_tenant_type, x_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePassword**](UpdatePassword.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 
 **x_uuid** | **str**|  | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email_code**
> VerifyPhoneCodeResp verify_email_code(x_tenant_type, email, code)

忘记密码step2-验证邮件验证码

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PasswordApi(swagger_client.ApiClient(configuration))
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
email = 'email_example' # str | 
code = 'code_example' # str |  邮件验证码

try:
    # 忘记密码step2-验证邮件验证码
    api_response = api_instance.verify_email_code(x_tenant_type, email, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->verify_email_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_type** | **str**|  来自哪个平台 | 
 **email** | **str**|  | 
 **code** | **str**|  邮件验证码 | 

### Return type

[**VerifyPhoneCodeResp**](VerifyPhoneCodeResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_phone_code**
> VerifyPhoneCodeResp verify_phone_code(x_tenant_type, phone_number, code)

忘记密码step2-验证手机验证码

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PasswordApi(swagger_client.ApiClient(configuration))
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
phone_number = 'phone_number_example' # str | 
code = 'code_example' # str |  短信验证码

try:
    # 忘记密码step2-验证手机验证码
    api_response = api_instance.verify_phone_code(x_tenant_type, phone_number, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordApi->verify_phone_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_type** | **str**|  来自哪个平台 | 
 **phone_number** | **str**|  | 
 **code** | **str**|  短信验证码 | 

### Return type

[**VerifyPhoneCodeResp**](VerifyPhoneCodeResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

