# swagger_client.RoleApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RoleApi.md#create_role) | **POST** /roles | 创建角色
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /roles/{id} | 删除角色
[**exist_role_by_name**](RoleApi.md#exist_role_by_name) | **POST** /roles/exist/byname | 角色是否存在
[**get_all_permission**](RoleApi.md#get_all_permission) | **GET** /roles/permissions | 获取所有权限包含分类
[**get_role_detail**](RoleApi.md#get_role_detail) | **GET** /roles/{id} | 角色详情
[**list_role**](RoleApi.md#list_role) | **GET** /roles | 角色列表
[**permission_by_uuid**](RoleApi.md#permission_by_uuid) | **POST** /roles/permissions/byuuid | 获取指定用户的所有权限包含分类
[**update_role**](RoleApi.md#update_role) | **PUT** /roles/{id} | 修改角色

# **create_role**
> Role create_role(body)

创建角色

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
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRoleReq() # CreateRoleReq | 

try:
    # 创建角色
    api_response = api_instance.create_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleReq**](CreateRoleReq.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> EmptyRole delete_role(body, id)

删除角色

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
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeleteRoleReq() # DeleteRoleReq | 
id = 'id_example' # str | 

try:
    # 删除角色
    api_response = api_instance.delete_role(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteRoleReq**](DeleteRoleReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**EmptyRole**](EmptyRole.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exist_role_by_name**
> EmptyRole exist_role_by_name(body)

角色是否存在

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
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExistRoleByNameReq() # ExistRoleByNameReq |  判断角色名称是否存在

try:
    # 角色是否存在
    api_response = api_instance.exist_role_by_name(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->exist_role_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExistRoleByNameReq**](ExistRoleByNameReq.md)|  判断角色名称是否存在 | 

### Return type

[**EmptyRole**](EmptyRole.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_permission**
> AllPermissionResp get_all_permission()

获取所有权限包含分类

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
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))

try:
    # 获取所有权限包含分类
    api_response = api_instance.get_all_permission()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->get_all_permission: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AllPermissionResp**](AllPermissionResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_detail**
> Role get_role_detail(id)

角色详情

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
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # 角色详情
    api_response = api_instance.get_role_detail(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->get_role_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Role**](Role.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role**
> ListRoleResp list_role(page, page_size=page_size, orderby=orderby, sort=sort, name=name)

角色列表

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
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
page = 789 # int |  当前页码
page_size = 15 # int |  展示数量,默认15 (optional) (default to 15)
orderby = 'created_at' # str |  排序字段,默认 created_at (optional) (default to created_at)
sort = 'desc' # str |  排序方式(asc,desc), 默认 desc (optional) (default to desc)
name = 'name_example' # str |  角色名称搜索 (optional)

try:
    # 角色列表
    api_response = api_instance.list_role(page, page_size=page_size, orderby=orderby, sort=sort, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->list_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  当前页码 | 
 **page_size** | **int**|  展示数量,默认15 | [optional] [default to 15]
 **orderby** | **str**|  排序字段,默认 created_at | [optional] [default to created_at]
 **sort** | **str**|  排序方式(asc,desc), 默认 desc | [optional] [default to desc]
 **name** | **str**|  角色名称搜索 | [optional] 

### Return type

[**ListRoleResp**](ListRoleResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permission_by_uuid**
> PermissionByUuidResp permission_by_uuid(body)

获取指定用户的所有权限包含分类

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
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
body = swagger_client.PermissionByUuidReq() # PermissionByUuidReq |  获取用户权限包含分类

try:
    # 获取指定用户的所有权限包含分类
    api_response = api_instance.permission_by_uuid(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->permission_by_uuid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermissionByUuidReq**](PermissionByUuidReq.md)|  获取用户权限包含分类 | 

### Return type

[**PermissionByUuidResp**](PermissionByUuidResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> Role update_role(body, id)

修改角色

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
api_instance = swagger_client.RoleApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateRoleReq() # UpdateRoleReq | 
id = 'id_example' # str | 

try:
    # 修改角色
    api_response = api_instance.update_role(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRoleReq**](UpdateRoleReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**Role**](Role.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

