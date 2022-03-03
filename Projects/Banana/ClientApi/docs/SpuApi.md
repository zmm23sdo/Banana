# swagger_client.SpuApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_spu_items**](SpuApi.md#get_spu_items) | **GET** /d/items | 获取商品列表

# **get_spu_items**
> SpuListRes get_spu_items(category_id, sorter, brand_id=brand_id, cursor=cursor, page=page)

获取商品列表

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
api_instance = swagger_client.SpuApi(swagger_client.ApiClient(configuration))
category_id = 'category_id_example' # str |  类别 id
sorter = 'price' # str |  排序关键字，当前只支持 price (default to price)
brand_id = 'brand_id_example' # str |  品牌 id (optional)
cursor = -1 # int |  滑动分页 id (optional) (default to -1)
page = 10 # int |  每页数量 (optional) (default to 10)

try:
    # 获取商品列表
    api_response = api_instance.get_spu_items(category_id, sorter, brand_id=brand_id, cursor=cursor, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpuApi->get_spu_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  类别 id | 
 **sorter** | **str**|  排序关键字，当前只支持 price | [default to price]
 **brand_id** | **str**|  品牌 id | [optional] 
 **cursor** | **int**|  滑动分页 id | [optional] [default to -1]
 **page** | **int**|  每页数量 | [optional] [default to 10]

### Return type

[**SpuListRes**](SpuListRes.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

