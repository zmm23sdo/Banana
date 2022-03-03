# ListUsersReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  当前页码 | 
**page_size** | **int** |  展示数量,默认 15 | [optional] [default to 15]
**orderby** | **str** |  排序字段,默认 created_at | [optional] [default to 'created_at']
**sort** | **str** |  排序方式(asc,desc), 默认 desc | [optional] [default to 'desc']
**username** | **str** |  用户名模糊搜索 | [optional] 
**name** | **str** |  用户昵称搜索 | [optional] 
**email** | **str** |  用户邮箱搜索 | [optional] 
**is_deleted_at** | **str** |  用户状态 , \&quot;true\&quot;:已注销, \&quot;false\&quot;:正常 | [optional] 
**created_at_start** | **str** |  创建时间起始时间 | [optional] 
**created_at_end** | **str** |  创建时间结束时间 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

