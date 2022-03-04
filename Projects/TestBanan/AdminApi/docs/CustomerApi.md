# swagger_client.CustomerApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer**](CustomerApi.md#delete_customer) | **DELETE** /customers/{id} | 注销客户
[**edit_desc_customer**](CustomerApi.md#edit_desc_customer) | **PUT** /customers/{id} | 修改客户备注
[**get_customer**](CustomerApi.md#get_customer) | **GET** /customers/{id} | 客户详情
[**list_customer**](CustomerApi.md#list_customer) | **GET** /customers | 客户列表

# **delete_customer**
> EmptyCustomer delete_customer(body, id)

注销客户

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeleteCustomerReq() # DeleteCustomerReq | 
id = 'id_example' # str | 

try:
    # 注销客户
    api_response = api_instance.delete_customer(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->delete_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteCustomerReq**](DeleteCustomerReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**EmptyCustomer**](EmptyCustomer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_desc_customer**
> EmptyCustomer edit_desc_customer(body, id)

修改客户备注

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
body = swagger_client.EditDescCustomerReq() # EditDescCustomerReq | 
id = 'id_example' # str | 

try:
    # 修改客户备注
    api_response = api_instance.edit_desc_customer(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->edit_desc_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditDescCustomerReq**](EditDescCustomerReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**EmptyCustomer**](EmptyCustomer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer**
> Customer get_customer(id)

客户详情

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # 客户详情
    api_response = api_instance.get_customer(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer**
> ListCustomerResp list_customer(page, page_size=page_size, orderby=orderby, sort=sort, name=name, is_deleted_at=is_deleted_at, created_at_start=created_at_start, created_at_end=created_at_end, last_at_start=last_at_start, last_at_end=last_at_end)

客户列表

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
api_instance = swagger_client.CustomerApi(swagger_client.ApiClient(configuration))
page = 789 # int |  当前页码
page_size = 15 # int |  展示数量 默认15 (optional) (default to 15)
orderby = 'created_at' # str |  排序字段,默认 created_at (optional) (default to created_at)
sort = 'desc' # str |  排序方式(asc,desc), 默认 desc (optional) (default to desc)
name = 'name_example' # str |  用户昵称搜索 (optional)
is_deleted_at = 'is_deleted_at_example' # str |  用户状态 , \"true\":已注销, \"false\":正常 (optional)
created_at_start = 'created_at_start_example' # str |  创建时间起始时间 (optional)
created_at_end = 'created_at_end_example' # str |  创建时间结束时间 (optional)
last_at_start = 'last_at_start_example' # str |  最后购买时间起始时间 (optional)
last_at_end = 'last_at_end_example' # str |  最后购买时间结束时间 (optional)

try:
    # 客户列表
    api_response = api_instance.list_customer(page, page_size=page_size, orderby=orderby, sort=sort, name=name, is_deleted_at=is_deleted_at, created_at_start=created_at_start, created_at_end=created_at_end, last_at_start=last_at_start, last_at_end=last_at_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->list_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  当前页码 | 
 **page_size** | **int**|  展示数量 默认15 | [optional] [default to 15]
 **orderby** | **str**|  排序字段,默认 created_at | [optional] [default to created_at]
 **sort** | **str**|  排序方式(asc,desc), 默认 desc | [optional] [default to desc]
 **name** | **str**|  用户昵称搜索 | [optional] 
 **is_deleted_at** | **str**|  用户状态 , \&quot;true\&quot;:已注销, \&quot;false\&quot;:正常 | [optional] 
 **created_at_start** | **str**|  创建时间起始时间 | [optional] 
 **created_at_end** | **str**|  创建时间结束时间 | [optional] 
 **last_at_start** | **str**|  最后购买时间起始时间 | [optional] 
 **last_at_end** | **str**|  最后购买时间结束时间 | [optional] 

### Return type

[**ListCustomerResp**](ListCustomerResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

