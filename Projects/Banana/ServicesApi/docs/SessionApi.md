# swagger_client.SessionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_session_info**](SessionApi.md#get_session_info) | **GET** /d/session | 获取accesstoken用户信息
[**login_sms**](SessionApi.md#login_sms) | **POST** /d/sms/login | 手机号登录step1-发送短信
[**logout**](SessionApi.md#logout) | **DELETE** /d/session | 登出
[**password_login**](SessionApi.md#password_login) | **POST** /d/session/password | 手机号密码登录
[**phone_login**](SessionApi.md#phone_login) | **POST** /d/session/phone_number | 手机号登录step2-登录
[**session_refresh**](SessionApi.md#session_refresh) | **POST** /d/session/refresh | 使用refresh获取新的token
[**user_login**](SessionApi.md#user_login) | **POST** /d/session/username | 用户名密码登录

# **get_session_info**
> SessionInfoResp get_session_info(x_tenant_type, authorization)

获取accesstoken用户信息

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
authorization = 'authorization_example' # str | 

try:
    # 获取accesstoken用户信息
    api_response = api_instance.get_session_info(x_tenant_type, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_session_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_type** | **str**|  来自哪个平台 | 
 **authorization** | **str**|  | 

### Return type

[**SessionInfoResp**](SessionInfoResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_sms**
> EmptyResp login_sms(body, x_tenant_type)

手机号登录step1-发送短信

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoginSMSReq() # LoginSMSReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # 手机号登录step1-发送短信
    api_response = api_instance.login_sms(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->login_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginSMSReq**](LoginSMSReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 

### Return type

[**EmptyResp**](EmptyResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> LoginResp logout(body, x_tenant_type, authorization)

登出

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.SessionInfoReq() # SessionInfoReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
authorization = 'authorization_example' # str | 

try:
    # 登出
    api_response = api_instance.logout(body, x_tenant_type, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionInfoReq**](SessionInfoReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 
 **authorization** | **str**|  | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_login**
> LoginResp password_login(body, x_tenant_type)

手机号密码登录

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.PasswordLoginReq() # PasswordLoginReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # 手机号密码登录
    api_response = api_instance.password_login(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->password_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordLoginReq**](PasswordLoginReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_login**
> LoginResp phone_login(body, x_tenant_type)

手机号登录step2-登录

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneLoginReq() # PhoneLoginReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # 手机号登录step2-登录
    api_response = api_instance.phone_login(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->phone_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneLoginReq**](PhoneLoginReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_refresh**
> LoginResp session_refresh(body, x_tenant_type)

使用refresh获取新的token

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.SessionRefreshReq() # SessionRefreshReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # 使用refresh获取新的token
    api_response = api_instance.session_refresh(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->session_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionRefreshReq**](SessionRefreshReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_login**
> LoginResp user_login(body, x_tenant_type)

用户名密码登录

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
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserLoginReq() # UserLoginReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # 用户名密码登录
    api_response = api_instance.user_login(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->user_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserLoginReq**](UserLoginReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

