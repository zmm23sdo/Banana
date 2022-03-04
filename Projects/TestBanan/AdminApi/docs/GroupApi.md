# swagger_client.GroupApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupApi.md#create_group) | **POST** /groups | 创建分组/子分组
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /groups/{id} | 删除分组
[**list_group**](GroupApi.md#list_group) | **GET** /groups | 分组列表
[**update_group**](GroupApi.md#update_group) | **PUT** /groups/{id} | 更新分组

# **create_group**
> EmptyGroup create_group(body)

创建分组/子分组

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateGroupReq() # CreateGroupReq | 

try:
    # 创建分组/子分组
    api_response = api_instance.create_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGroupReq**](CreateGroupReq.md)|  | 

### Return type

[**EmptyGroup**](EmptyGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> EmptyGroup delete_group(body, id)

删除分组

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeleteGroupReq() # DeleteGroupReq | 
id = 'id_example' # str | 

try:
    # 删除分组
    api_response = api_instance.delete_group(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteGroupReq**](DeleteGroupReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**EmptyGroup**](EmptyGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group**
> ListGroupResp list_group(page, page_size=page_size, name=name)

分组列表

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
page = 789 # int |  当前页码
page_size = 15 # int |  展示数量 默认15 (optional) (default to 15)
name = 'name_example' # str |  分组名称 模糊搜 (optional)

try:
    # 分组列表
    api_response = api_instance.list_group(page, page_size=page_size, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  当前页码 | 
 **page_size** | **int**|  展示数量 默认15 | [optional] [default to 15]
 **name** | **str**|  分组名称 模糊搜 | [optional] 

### Return type

[**ListGroupResp**](ListGroupResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> EmptyGroup update_group(body, id)

更新分组

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
api_instance = swagger_client.GroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateGroupReq() # UpdateGroupReq | 
id = 'id_example' # str | 

try:
    # 更新分组
    api_response = api_instance.update_group(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateGroupReq**](UpdateGroupReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**EmptyGroup**](EmptyGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

