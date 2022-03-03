# swagger_client.UserApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_address**](UserApi.md#add_address) | **POST** /address | 添加地址
[**address_detail**](UserApi.md#address_detail) | **GET** /address/{id} | 根据id获取地址信息
[**address_list**](UserApi.md#address_list) | **GET** /address | 获取地址簿列表
[**get_user_info**](UserApi.md#get_user_info) | **GET** /user/info | 获取用户基本信息
[**remove_address**](UserApi.md#remove_address) | **DELETE** /address/{id} | 删除地址
[**update_address**](UserApi.md#update_address) | **PUT** /address/{id} | 编辑地址
[**update_avatar**](UserApi.md#update_avatar) | **PUT** /user/avatar | 更新用户头像地址

# **add_address**
> AddAddressRsep add_address(body)

添加地址

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddAddressReq() # AddAddressReq | 

try:
    # 添加地址
    api_response = api_instance.add_address(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddAddressReq**](AddAddressReq.md)|  | 

### Return type

[**AddAddressRsep**](AddAddressRsep.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_detail**
> AddAddressRsep address_detail(id)

根据id获取地址信息

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # 根据id获取地址信息
    api_response = api_instance.address_detail(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->address_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AddAddressRsep**](AddAddressRsep.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_list**
> AddressListResp address_list(cursor, per_page)

获取地址簿列表

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
cursor = 789 # int |  游标
per_page = 789 # int |  每页多少

try:
    # 获取地址簿列表
    api_response = api_instance.address_list(cursor, per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->address_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **int**|  游标 | 
 **per_page** | **int**|  每页多少 | 

### Return type

[**AddressListResp**](AddressListResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_info**
> User get_user_info()

获取用户基本信息

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

try:
    # 获取用户基本信息
    api_response = api_instance.get_user_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_address**
> RemoveWishListResp remove_address(body, id)

删除地址

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeleteAddressReq() # DeleteAddressReq | 
id = 'id_example' # str | 

try:
    # 删除地址
    api_response = api_instance.remove_address(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->remove_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteAddressReq**](DeleteAddressReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**RemoveWishListResp**](RemoveWishListResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> AddAddressRsep update_address(body, id)

编辑地址

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateAddressReq() # UpdateAddressReq | 
id = 'id_example' # str | 

try:
    # 编辑地址
    api_response = api_instance.update_address(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAddressReq**](UpdateAddressReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**AddAddressRsep**](AddAddressRsep.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avatar**
> EmptyUser update_avatar(body)

更新用户头像地址

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
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateAvatarReq() # UpdateAvatarReq | 

try:
    # 更新用户头像地址
    api_response = api_instance.update_avatar(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAvatarReq**](UpdateAvatarReq.md)|  | 

### Return type

[**EmptyUser**](EmptyUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

