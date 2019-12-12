# AddOn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of add-on. Will be used as order line text. | 
**description** | **str** | Optional description of add-on | [optional] 
**amount** | **int** | Add-on amount | 
**vat** | **float** | Optional vat for add-on. Account default is used if none given. | [optional] 
**handle** | **str** | Per account unique handle for the add-on | 
**type** | **str** | Add-on type &#x60;on_off&#x60; or &#x60;quantity&#x60;. An &#x60;on_off&#x60; type cannot be given a quantity when attached to subscription. For &#x60;quantity&#x60; type it is possible. | 
**state** | **str** | Add-on state &#x60;active&#x60; or &#x60;deleted&#x60;. | 
**deleted** | **datetime** | Date when the add-on was deleted if deleted. In ISO-8601 extended offset date-time format. | [optional] 
**created** | **datetime** | Date when the add-on was created. In ISO-8601 extended offset date-time format. | 
**amount_incl_vat** | **bool** | Whether the amount is including VAT. Default true. | [optional] 
**all_plans** | **bool** | Whether all plans are eligible for this add-on. Defaults to false. | [optional] 
**eligible_plans** | **list[str]** | If not &#x60;all_plans&#x60; are set to true, then the set of eligible plan handles must be defined. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


