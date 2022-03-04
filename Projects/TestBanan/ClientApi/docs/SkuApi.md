# swagger_client.SkuApi

All URIs are relative to *http://127.0.0.1:9060/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_info**](SkuApi.md#get_item_info) | **GET** /d/itemInfo/{id} | 获取商品详情

# **get_item_info**
> SkuInfoRes get_item_info(id)

获取商品详情

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
api_instance = swagger_client.SkuApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # 获取商品详情
    api_response = api_instance.get_item_info(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkuApi->get_item_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SkuInfoRes**](SkuInfoRes.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

