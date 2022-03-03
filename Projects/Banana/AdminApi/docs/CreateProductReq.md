# CreateProductReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  商品名称, 规则: 请输入20-120个字符 | 
**category_id** | **str** |  商品类目id | 
**describe** | **str** |  商品描述,暂时仅用于商品管理的作用，非必填项目,0-3000个字符 | 
**pic** | **list[str]** |  商品图 | 
**group_id** | **list[str]** |  商品分组id | 
**brand** | **str** |  品牌 | 
**warranty_duration** | **str** |  保修时间 | 
**warranty_type** | **str** |  保修类型 | 
**sku_items** | [**list[SkuItem]**](SkuItem.md) |  变体集合 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

