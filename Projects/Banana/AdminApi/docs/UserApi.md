# swagger_client.UserApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_users**](UserApi.md#create_users) | **POST** /users | 创建用户
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{id} | 删除用户
[**list_users**](UserApi.md#list_users) | **GET** /users | 用户列表
[**reset_password_user**](UserApi.md#reset_password_user) | **POST** /users/{id} | 重置用户密码
[**update_user**](UserApi.md#update_user) | **PUT** /users/{id} | 修改用户信息

# **create_users**
> User create_users(body)

创建用户

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
body = swagger_client.CreateUserReq() # CreateUserReq | 

try:
    # 创建用户
    api_response = api_instance.create_users(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserReq**](CreateUserReq.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> Empty delete_user(body, id)

删除用户

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
body = swagger_client.DeleteUserReq() # DeleteUserReq | 
id = 'id_example' # str | 

try:
    # 删除用户
    api_response = api_instance.delete_user(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteUserReq**](DeleteUserReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsersResp list_users(page, page_size=page_size, orderby=orderby, sort=sort, username=username, name=name, email=email, is_deleted_at=is_deleted_at, created_at_start=created_at_start, created_at_end=created_at_end)

用户列表

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
page = 789 # int |  当前页码
page_size = 15 # int |  展示数量,默认 15 (optional) (default to 15)
orderby = 'created_at' # str |  排序字段,默认 created_at (optional) (default to created_at)
sort = 'desc' # str |  排序方式(asc,desc), 默认 desc (optional) (default to desc)
username = 'username_example' # str |  用户名模糊搜索 (optional)
name = 'name_example' # str |  用户昵称搜索 (optional)
email = 'email_example' # str |  用户邮箱搜索 (optional)
is_deleted_at = 'is_deleted_at_example' # str |  用户状态 , \"true\":已注销, \"false\":正常 (optional)
created_at_start = 'created_at_start_example' # str |  创建时间起始时间 (optional)
created_at_end = 'created_at_end_example' # str |  创建时间结束时间 (optional)

try:
    # 用户列表
    api_response = api_instance.list_users(page, page_size=page_size, orderby=orderby, sort=sort, username=username, name=name, email=email, is_deleted_at=is_deleted_at, created_at_start=created_at_start, created_at_end=created_at_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  当前页码 | 
 **page_size** | **int**|  展示数量,默认 15 | [optional] [default to 15]
 **orderby** | **str**|  排序字段,默认 created_at | [optional] [default to created_at]
 **sort** | **str**|  排序方式(asc,desc), 默认 desc | [optional] [default to desc]
 **username** | **str**|  用户名模糊搜索 | [optional] 
 **name** | **str**|  用户昵称搜索 | [optional] 
 **email** | **str**|  用户邮箱搜索 | [optional] 
 **is_deleted_at** | **str**|  用户状态 , \&quot;true\&quot;:已注销, \&quot;false\&quot;:正常 | [optional] 
 **created_at_start** | **str**|  创建时间起始时间 | [optional] 
 **created_at_end** | **str**|  创建时间结束时间 | [optional] 

### Return type

[**ListUsersResp**](ListUsersResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_user**
> Empty reset_password_user(body, id)

重置用户密码

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
body = swagger_client.ResetPasswordUserReq() # ResetPasswordUserReq | 
id = 'id_example' # str | 

try:
    # 重置用户密码
    api_response = api_instance.reset_password_user(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->reset_password_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordUserReq**](ResetPasswordUserReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(body, id)

修改用户信息

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
body = swagger_client.UpdateUserReq() # UpdateUserReq | 
id = 'id_example' # str | 

try:
    # 修改用户信息
    api_response = api_instance.update_user(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserReq**](UpdateUserReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

