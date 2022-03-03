# swagger_client.RegisterApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_google**](RegisterApi.md#register_google) | **POST** /d/register/google | google登录
[**register_phone_number**](RegisterApi.md#register_phone_number) | **POST** /d/register/phone_number | 手机号注册step2-注册
[**register_sms**](RegisterApi.md#register_sms) | **POST** /d/sms/register | 手机号注册step1-发送短信

# **register_google**
> LoginResp register_google(body, x_tenant_type)

google登录

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
api_instance = swagger_client.RegisterApi(swagger_client.ApiClient(configuration))
body = swagger_client.RegisterGoogleReq() # RegisterGoogleReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # google登录
    api_response = api_instance.register_google(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisterApi->register_google: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterGoogleReq**](RegisterGoogleReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_phone_number**
> LoginResp register_phone_number(body, x_tenant_type)

手机号注册step2-注册

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
api_instance = swagger_client.RegisterApi(swagger_client.ApiClient(configuration))
body = swagger_client.PhoneRegisterReq() # PhoneRegisterReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # 手机号注册step2-注册
    api_response = api_instance.register_phone_number(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisterApi->register_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhoneRegisterReq**](PhoneRegisterReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 

### Return type

[**LoginResp**](LoginResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_sms**
> EmptyResp register_sms(body, x_tenant_type)

手机号注册step1-发送短信

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
api_instance = swagger_client.RegisterApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoginSMSReq() # LoginSMSReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台

try:
    # 手机号注册step1-发送短信
    api_response = api_instance.register_sms(body, x_tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisterApi->register_sms: %s\n" % e)
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

