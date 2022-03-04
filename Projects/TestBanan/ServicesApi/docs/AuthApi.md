# swagger_client.AuthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**init_password**](AuthApi.md#init_password) | **POST** /account/password | 注册初次设置密码
[**unique_email**](AuthApi.md#unique_email) | **GET** /d/unique/email | 验证邮箱唯一性
[**unique_phone_number**](AuthApi.md#unique_phone_number) | **GET** /d/unique/phone_number | 验证手机号唯一性

# **init_password**
> EmptyResp init_password(body, x_tenant_type, x_uuid)

注册初次设置密码

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetPasswordReq() # SetPasswordReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
x_uuid = 'x_uuid_example' # str | 

try:
    # 注册初次设置密码
    api_response = api_instance.init_password(body, x_tenant_type, x_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->init_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetPasswordReq**](SetPasswordReq.md)|  | 
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

# **unique_email**
> UniqueResp unique_email(x_tenant_type, email)

验证邮箱唯一性

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
email = 'email_example' # str | 

try:
    # 验证邮箱唯一性
    api_response = api_instance.unique_email(x_tenant_type, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->unique_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_type** | **str**|  来自哪个平台 | 
 **email** | **str**|  | 

### Return type

[**UniqueResp**](UniqueResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unique_phone_number**
> UniqueResp unique_phone_number(x_tenant_type, phone_number)

验证手机号唯一性

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
phone_number = 'phone_number_example' # str | 

try:
    # 验证手机号唯一性
    api_response = api_instance.unique_phone_number(x_tenant_type, phone_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->unique_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_type** | **str**|  来自哪个平台 | 
 **phone_number** | **str**|  | 

### Return type

[**UniqueResp**](UniqueResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

