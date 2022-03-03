# swagger_client.CategoryApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories**](CategoryApi.md#categories) | **GET** /d/categories | 获取类别树形列表
[**create_category**](CategoryApi.md#create_category) | **POST** /d/categories | 创建类别
[**get_category**](CategoryApi.md#get_category) | **GET** /d/categories/{id} | 获取单个类别信息
[**get_popular_categories**](CategoryApi.md#get_popular_categories) | **GET** /d/categories/popular | 获取热门类别列表
[**update_popular_categories**](CategoryApi.md#update_popular_categories) | **PATCH** /d/categories/popular | 更新热门类别列表

# **categories**
> Categories categories()

获取类别树形列表

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))

try:
    # 获取类别树形列表
    api_response = api_instance.categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Categories**](Categories.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_category**
> CreateCategory create_category(body)

创建类别

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateCategory() # CreateCategory | 

try:
    # 创建类别
    api_response = api_instance.create_category(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->create_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCategory**](CreateCategory.md)|  | 

### Return type

[**CreateCategory**](CreateCategory.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> Category get_category(id)

获取单个类别信息

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # 获取单个类别信息
    api_response = api_instance.get_category(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->get_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Category**](Category.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_popular_categories**
> PopularCategories get_popular_categories()

获取热门类别列表

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))

try:
    # 获取热门类别列表
    api_response = api_instance.get_popular_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->get_popular_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PopularCategories**](PopularCategories.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_popular_categories**
> CategoryOrder update_popular_categories(body)

更新热门类别列表

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
api_instance = swagger_client.CategoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.CategoryOrder() # CategoryOrder | 

try:
    # 更新热门类别列表
    api_response = api_instance.update_popular_categories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->update_popular_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategoryOrder**](CategoryOrder.md)|  | 

### Return type

[**CategoryOrder**](CategoryOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

