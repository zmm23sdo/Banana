# swagger_client.ProfileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_phone_number_new_sms**](ProfileApi.md#update_phone_number_new_sms) | **POST** /sms/new_phone_number | 个人中心修改手机号step3-新手机号发送短信
[**update_phone_number_old_sms**](ProfileApi.md#update_phone_number_old_sms) | **POST** /sms/old_phone_number | 个人中心修改手机号step1-旧手机号发送短信
[**update_profile**](ProfileApi.md#update_profile) | **POST** /account/profile | 设置用户名/姓名
[**verify_new_phone_number**](ProfileApi.md#verify_new_phone_number) | **POST** /sms/verify_new_phone_number | 个人中心修改手机号step4-验证新手机号
[**verify_old_phone_number**](ProfileApi.md#verify_old_phone_number) | **POST** /account/verify_old_phone_number | 个人中心修改手机号step2-验证旧手机号

# **update_phone_number_new_sms**
> EmptyResp update_phone_number_new_sms(body, x_tenant_type, x_uuid)

个人中心修改手机号step3-新手机号发送短信

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePhoneNumberNewSmsReq() # UpdatePhoneNumberNewSmsReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
x_uuid = 'x_uuid_example' # str | 

try:
    # 个人中心修改手机号step3-新手机号发送短信
    api_response = api_instance.update_phone_number_new_sms(body, x_tenant_type, x_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->update_phone_number_new_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePhoneNumberNewSmsReq**](UpdatePhoneNumberNewSmsReq.md)|  | 
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

# **update_phone_number_old_sms**
> EmptyResp update_phone_number_old_sms(body, x_tenant_type, x_uuid)

个人中心修改手机号step1-旧手机号发送短信

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePhoneNumberOldSmsReq() # UpdatePhoneNumberOldSmsReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
x_uuid = 'x_uuid_example' # str | 

try:
    # 个人中心修改手机号step1-旧手机号发送短信
    api_response = api_instance.update_phone_number_old_sms(body, x_tenant_type, x_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->update_phone_number_old_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePhoneNumberOldSmsReq**](UpdatePhoneNumberOldSmsReq.md)|  | 
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

# **update_profile**
> EmptyResp update_profile(body, x_tenant_type, x_uuid)

设置用户名/姓名

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateProfileReq() # UpdateProfileReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
x_uuid = 'x_uuid_example' # str | 

try:
    # 设置用户名/姓名
    api_response = api_instance.update_profile(body, x_tenant_type, x_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProfileReq**](UpdateProfileReq.md)|  | 
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

# **verify_new_phone_number**
> EmptyResp verify_new_phone_number(body, x_tenant_type, x_uuid)

个人中心修改手机号step4-验证新手机号

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerifyNewPhoneNumberReq() # VerifyNewPhoneNumberReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
x_uuid = 'x_uuid_example' # str | 

try:
    # 个人中心修改手机号step4-验证新手机号
    api_response = api_instance.verify_new_phone_number(body, x_tenant_type, x_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->verify_new_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyNewPhoneNumberReq**](VerifyNewPhoneNumberReq.md)|  | 
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

# **verify_old_phone_number**
> VerifyOldPhoneNumberResp verify_old_phone_number(body, x_tenant_type, x_uuid)

个人中心修改手机号step2-验证旧手机号

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
body = swagger_client.VerifyOldPhoneNumberReq() # VerifyOldPhoneNumberReq | 
x_tenant_type = 'x_tenant_type_example' # str |  来自哪个平台
x_uuid = 'x_uuid_example' # str | 

try:
    # 个人中心修改手机号step2-验证旧手机号
    api_response = api_instance.verify_old_phone_number(body, x_tenant_type, x_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->verify_old_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyOldPhoneNumberReq**](VerifyOldPhoneNumberReq.md)|  | 
 **x_tenant_type** | **str**|  来自哪个平台 | 
 **x_uuid** | **str**|  | 

### Return type

[**VerifyOldPhoneNumberResp**](VerifyOldPhoneNumberResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

