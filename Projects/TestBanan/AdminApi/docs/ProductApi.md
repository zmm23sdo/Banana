# swagger_client.ProductApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_group_products**](ProductApi.md#change_group_products) | **POST** /products/groups | 批量设置商品分组
[**change_publish_status_products**](ProductApi.md#change_publish_status_products) | **POST** /products/status | 批量上架/下架商品
[**create_product**](ProductApi.md#create_product) | **POST** /products | 发布商品
[**delete_products**](ProductApi.md#delete_products) | **DELETE** /products | 批量删除商品
[**get_product**](ProductApi.md#get_product) | **GET** /products/{id} | 商品详情
[**list_products**](ProductApi.md#list_products) | **GET** /products | 商品列表
[**update_price_product**](ProductApi.md#update_price_product) | **PUT** /products/{id}/price | 编辑价格
[**update_stock_product**](ProductApi.md#update_stock_product) | **PUT** /products/{id}/stock | 编辑库存

# **change_group_products**
> EmptyProduct change_group_products(body)

批量设置商品分组

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChangeGroupProductsReq() # ChangeGroupProductsReq | 

try:
    # 批量设置商品分组
    api_response = api_instance.change_group_products(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->change_group_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeGroupProductsReq**](ChangeGroupProductsReq.md)|  | 

### Return type

[**EmptyProduct**](EmptyProduct.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_publish_status_products**
> EmptyProduct change_publish_status_products(body)

批量上架/下架商品

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChangePublishStatusProductsReq() # ChangePublishStatusProductsReq | 

try:
    # 批量上架/下架商品
    api_response = api_instance.change_publish_status_products(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->change_publish_status_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangePublishStatusProductsReq**](ChangePublishStatusProductsReq.md)|  | 

### Return type

[**EmptyProduct**](EmptyProduct.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_product**
> Product create_product(body)

发布商品

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateProductReq() # CreateProductReq | 

try:
    # 发布商品
    api_response = api_instance.create_product(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->create_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProductReq**](CreateProductReq.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_products**
> EmptyProduct delete_products(body)

批量删除商品

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeleteProductsReq() # DeleteProductsReq | 

try:
    # 批量删除商品
    api_response = api_instance.delete_products(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->delete_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteProductsReq**](DeleteProductsReq.md)|  | 

### Return type

[**EmptyProduct**](EmptyProduct.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> Product get_product(id)

商品详情

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # 商品详情
    api_response = api_instance.get_product(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Product**](Product.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> ListProductsResp list_products(page, page_size=page_size, orderby=orderby, sort=sort, type=type, search=search, group_id=group_id, category_id=category_id, sold_out=sold_out, price=price)

商品列表

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
page = 789 # int |  当前页码
page_size = 15 # int |  展示数量 默认15 (optional) (default to 15)
orderby = 'created_at' # str |  排序字段(支持:created_at|price|stock|sold_out),默认 created_at (optional) (default to created_at)
sort = 'desc' # str |  排序方式(asc,desc), 默认 desc (optional) (default to desc)
type = 'all' # str |  列表数据类型支持: all|live|sold_out|delisted 默认 all (optional) (default to all)
search = 'search_example' # str |  用户名模糊搜索 (optional)
group_id = 'group_id_example' # str |  商品分组ID搜索 (optional)
category_id = 'category_id_example' # str |  商品分类ID搜索 (optional)
sold_out = 'sold_out_example' # str |  商品起始销量搜索 (optional)
price = 'price_example' # str |  商品起始价格搜索 (optional)

try:
    # 商品列表
    api_response = api_instance.list_products(page, page_size=page_size, orderby=orderby, sort=sort, type=type, search=search, group_id=group_id, category_id=category_id, sold_out=sold_out, price=price)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->list_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  当前页码 | 
 **page_size** | **int**|  展示数量 默认15 | [optional] [default to 15]
 **orderby** | **str**|  排序字段(支持:created_at|price|stock|sold_out),默认 created_at | [optional] [default to created_at]
 **sort** | **str**|  排序方式(asc,desc), 默认 desc | [optional] [default to desc]
 **type** | **str**|  列表数据类型支持: all|live|sold_out|delisted 默认 all | [optional] [default to all]
 **search** | **str**|  用户名模糊搜索 | [optional] 
 **group_id** | **str**|  商品分组ID搜索 | [optional] 
 **category_id** | **str**|  商品分类ID搜索 | [optional] 
 **sold_out** | **str**|  商品起始销量搜索 | [optional] 
 **price** | **str**|  商品起始价格搜索 | [optional] 

### Return type

[**ListProductsResp**](ListProductsResp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_price_product**
> EmptyProduct update_price_product(body, id)

编辑价格

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePriceProductReq() # UpdatePriceProductReq | 
id = 'id_example' # str | 

try:
    # 编辑价格
    api_response = api_instance.update_price_product(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->update_price_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePriceProductReq**](UpdatePriceProductReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**EmptyProduct**](EmptyProduct.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stock_product**
> EmptyProduct update_stock_product(body, id)

编辑库存

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
api_instance = swagger_client.ProductApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateStockProductReq() # UpdateStockProductReq | 
id = 'id_example' # str | 

try:
    # 编辑库存
    api_response = api_instance.update_stock_product(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->update_stock_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateStockProductReq**](UpdateStockProductReq.md)|  | 
 **id** | **str**|  | 

### Return type

[**EmptyProduct**](EmptyProduct.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

