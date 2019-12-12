# PaypalTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error code if failed. See [transaction errors](https://reference.reepay.com/api/#transaction-errors). | [optional] 
**ref_transaction** | **str** | Id of a possible referenced transaction | [optional] 
**paypal_id** | **str** | PayPal id | [optional] 
**error_state** | **str** | Error state if failed: &#x60;pending&#x60;, &#x60;soft_declined&#x60;, &#x60;hard_declined&#x60; or &#x60;processing_error&#x60; | [optional] 
**acquirer_message** | **str** | Acquirer message in case of error | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


