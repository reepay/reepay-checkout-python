# OrderLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Per account unique order line id | 
**ordertext** | **str** | Order line text | 
**amount** | **int** | Order line total amount including vat | 
**vat** | **float** | Order line vat percent | 
**quantity** | **int** | Order line quantity | 
**origin** | **str** | Order line origin, one of the following: &#x60;plan&#x60;, &#x60;add_on&#x60;, &#x60;ondemand&#x60;, &#x60;additional_cost&#x60;, &#x60;credit&#x60;, &#x60;discount&#x60;, &#x60;setup_fee&#x60; | 
**timestamp** | **datetime** | Timestamp from order line origin, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format. | 
**discounted_amount** | **int** | Order line amount after potential discount has been deducted | [optional] 
**amount_vat** | **int** | Order line total vat amount | 
**amount_ex_vat** | **int** | Order line total amount without vat | 
**unit_amount** | **int** | Order line unit amount including vat | 
**unit_amount_vat** | **int** | Order line unit vat amount | 
**unit_amount_ex_vat** | **int** | Order line unit amount without vat | 
**amount_defined_incl_vat** | **bool** | Whether the amount was defined including VAT. E.g. plan amount defined including VAT. | 
**origin_handle** | **str** | Handle for additional cost, credit, plan or subscription discount in the case one of those are the origin | [optional] 
**period_from** | **datetime** | The start of billing period if the order line is a plan order line for a specific billing period, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format. | [optional] 
**period_to** | **datetime** | The end of billing period if the order line is a plan order line for a specific billing period, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format. | [optional] 
**discount_percentage** | **int** | The discount percentage for discount order lines that has a percentage discount | [optional] 
**discounted_order_line** | **str** | For discount order lines a reference to the order line for which the order line is a discount | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


