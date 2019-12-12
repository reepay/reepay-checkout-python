# Card

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id for payment method | 
**state** | **str** | State of the payment method: &#x60;active&#x60;, &#x60;inactivated&#x60;, &#x60;failed&#x60; or &#x60;deleted&#x60; | 
**customer** | **str** | Customer by handle | 
**failed** | **datetime** | Date when the payment method failed. In ISO-8601 extended offset date-time format. | [optional] 
**created** | **datetime** | Date when the payment method was created. In ISO-8601 extended offset date-time format. | 
**fingerprint** | **str** | Uniquely identifies this particular card number | [optional] 
**reactivated** | **datetime** | Date and time of reactivation if the card has been reactivated from failed state. In ISO-8601 extended offset date-time format. | [optional] 
**gw_ref** | **str** | Card gateway reference id | 
**card_type** | **str** | Card type: &#x60;unknown&#x60;, &#x60;visa&#x60;, &#x60;mc&#x60;, &#x60;dankort&#x60;, &#x60;visa_dk&#x60;, &#x60;ffk&#x60;, &#x60;visa_elec&#x60;, &#x60;maestro&#x60;, &#x60;laser&#x60;, &#x60;amex&#x60;, &#x60;diners&#x60;, &#x60;discover&#x60; or &#x60;jcb&#x60; | 
**exp_date** | **str** | Card expire date on form MM-YY  | [optional] 
**masked_card** | **str** | Masked card number | [optional] 
**last_success** | **datetime** | Date and time of last succesfull use of the card. In ISO-8601 extended offset date-time format. | [optional] 
**last_failed** | **datetime** | Date and time of last failed use of the card. In ISO-8601 extended offset date-time format. | [optional] 
**first_fail** | **datetime** | Date and time of first succesfull use of the card. In ISO-8601 extended offset date-time format. | [optional] 
**error_code** | **str** | An error code from the last failed use of the card. See [transaction errors](https://reference.reepay.com/api/#transaction-errors). | [optional] 
**error_state** | **str** | Error state from last failed use of the card: &#x60;pending&#x60;, &#x60;soft_declined&#x60;, &#x60;hard_declined&#x60; or &#x60;processing_error&#x60; | [optional] 
**strong_authentication_status** | **str** | Status for strong customer authentication | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


