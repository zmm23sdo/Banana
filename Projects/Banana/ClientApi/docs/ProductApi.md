# swagger_client.ProductApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brands**](ProductApi.md#brands) | **GET** /d/brands | 获取品牌列表
[**create_brand**](ProductApi.md#create_brand) | **POST** /d/brands | 创建品牌
[**get_brand**](ProductApi.md#get_brand) | **GET** /d/brands/{id} | 获取单个品牌信息
[**get_brand_tree**](ProductApi.md#get_brand_tree) | **GET** /d/tree-brands | 获取品牌列表树形结构
[**get_popular_brands**](ProductApi.md#get_popular_brands) | **GET** /d/popular-brands | 获取热门品牌列表
[**get_product**](ProductApi.md#get_product) | **GET** /d/products/{id} | 
[**update_brand_order**](ProductApi.md#update_brand_order) | **PATCH** /d/popular-brands | 更新热门品牌列表

# **brands**
> Brands brands()

获取品牌列表

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

try:
    # 获取品牌列表
    api_response = api_instance.brands()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->brands: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Brands**](Brands.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_brand**
> CreateBrand create_brand(body)

创建品牌

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
body = swagger_client.CreateBrand() # CreateBrand | 

try:
    # 创建品牌
    api_response = api_instance.create_brand(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->create_brand: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBrand**](CreateBrand.md)|  | 

### Return type

[**CreateBrand**](CreateBrand.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand**
> Brand get_brand(id)

获取单个品牌信息

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
    # 获取单个品牌信息
    api_response = api_instance.get_brand(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_brand: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Brand**](Brand.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand_tree**
> Brands get_brand_tree()

获取品牌列表树形结构

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

try:
    # 获取品牌列表树形结构
    api_response = api_instance.get_brand_tree()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_brand_tree: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Brands**](Brands.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_popular_brands**
> PopularBrands get_popular_brands()

获取热门品牌列表

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

try:
    # 获取热门品牌列表
    api_response = api_instance.get_popular_brands()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_popular_brands: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PopularBrands**](PopularBrands.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> ProductReply get_product(id)



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

[**ProductReply**](ProductReply.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_brand_order**
> BrandOrder update_brand_order(body)

更新热门品牌列表

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
body = swagger_client.BrandOrder() # BrandOrder | 

try:
    # 更新热门品牌列表
    api_response = api_instance.update_brand_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->update_brand_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BrandOrder**](BrandOrder.md)|  | 

### Return type

[**BrandOrder**](BrandOrder.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

