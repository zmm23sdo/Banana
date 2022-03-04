# swagger_client.CartsApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_change_cart_selected**](CartsApi.md#batch_change_cart_selected) | **POST** /carts/selected | 批量设置购物车商品选中状态
[**change_cart_selected**](CartsApi.md#change_cart_selected) | **POST** /cart/{id} | 设置购物车商品选中状态
[**create_carts**](CartsApi.md#create_carts) | **POST** /carts | 添加到商品购物车
[**get_cart**](CartsApi.md#get_cart) | **GET** /cart/{id} | 获取购物车商品详情
[**list_carts**](CartsApi.md#list_carts) | **GET** /carts | 购物车商品列表
[**merge_carts**](CartsApi.md#merge_carts) | **POST** /carts/merge | 合并本地购物车商品
[**remove_cart**](CartsApi.md#remove_cart) | **POST** /carts/del | 删除购物车商品
[**update_cart**](CartsApi.md#update_cart) | **PUT** /cart/{id} | 修改购物车商品

# **batch_change_cart_selected**
> BatchChangeCartSelectedResp batch_change_cart_selected(body)

批量设置购物车商品选中状态

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
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BatchChangeCartSelectedReq() # BatchChangeCartSelectedReq | 

try:
    # 批量设置购物车商品选中状态
    api_response = api_instance.batch_change_cart_selected(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->batch_change_cart_selected: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchChangeCartSelectedReq**](BatchChangeCartSelectedReq.md)|  | 

### Return type

[**BatchChangeCartSelectedResp**](BatchChangeCartSelectedResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_cart_selected**
> CartInfo change_cart_selected(body, id)

设置购物车商品选中状态

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
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChangeCartSelectedReq() # ChangeCartSelectedReq | 
id = 'id_example' # str | 

try:
    # 设置购物车商品选中状态
    api_response = api_instance.change_cart_selected(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->change_cart_selected: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeCartSelectedReq**](ChangeCartSelectedReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**CartInfo**](CartInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_carts**
> CartInfo create_carts(body)

添加到商品购物车

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
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateCartsReq() # CreateCartsReq | 

try:
    # 添加到商品购物车
    api_response = api_instance.create_carts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->create_carts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCartsReq**](CreateCartsReq.md)|  | 

### Return type

[**CartInfo**](CartInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart**
> CartInfo get_cart(id)

获取购物车商品详情

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
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # 获取购物车商品详情
    api_response = api_instance.get_cart(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->get_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CartInfo**](CartInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_carts**
> ListCartsResp list_carts(page, page_size=page_size, orderby=orderby, sort=sort)

购物车商品列表

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
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
page = 789 # int |  当前页码
page_size = 15 # int |  展示数量 (optional) (default to 15)
orderby = 'cart_id' # str |  排序字段,默认 cart_id (optional) (default to cart_id)
sort = 'desc' # str |  排序方式(asc,desc), 默认 desc (optional) (default to desc)

try:
    # 购物车商品列表
    api_response = api_instance.list_carts(page, page_size=page_size, orderby=orderby, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->list_carts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  当前页码 | 
 **page_size** | **int**|  展示数量 | [optional] [default to 15]
 **orderby** | **str**|  排序字段,默认 cart_id | [optional] [default to cart_id]
 **sort** | **str**|  排序方式(asc,desc), 默认 desc | [optional] [default to desc]

### Return type

[**ListCartsResp**](ListCartsResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_carts**
> MergeCartsResp merge_carts(body)

合并本地购物车商品

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
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.MergeCartsReq() # MergeCartsReq | 

try:
    # 合并本地购物车商品
    api_response = api_instance.merge_carts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->merge_carts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MergeCartsReq**](MergeCartsReq.md)|  | 

### Return type

[**MergeCartsResp**](MergeCartsResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_cart**
> RemoveCartResp remove_cart(body)

删除购物车商品

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
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.RemoveCartReq() # RemoveCartReq | 

try:
    # 删除购物车商品
    api_response = api_instance.remove_cart(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->remove_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoveCartReq**](RemoveCartReq.md)|  | 

### Return type

[**RemoveCartResp**](RemoveCartResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cart**
> CartInfo update_cart(body, id)

修改购物车商品

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
api_instance = swagger_client.CartsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateCartReq() # UpdateCartReq | 
id = 'id_example' # str | 

try:
    # 修改购物车商品
    api_response = api_instance.update_cart(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartsApi->update_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCartReq**](UpdateCartReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**CartInfo**](CartInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

