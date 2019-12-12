# ChargeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of charge source: &#x60;card&#x60; - existing customer card, &#x60;card_token&#x60; - card token, &#x60;mpo&#x60; - MobilePay Online or &#x60;viabill&#x60; | 
**card** | **str** | Reference to customer card if source type &#x60;card&#x60; | [optional] 
**fingerprint** | **str** | Uniquely identifies this particular card number if credit card source | [optional] 
**provider** | **str** | Card acquirer or card payment gateway used if card source: &#x60;reepay&#x60;, &#x60;clearhaus&#x60;, &#x60;nets&#x60;, &#x60;dibs&#x60;, &#x60;stripe&#x60;, &#x60;quickpay&#x60;, &#x60;epay&#x60;, &#x60;test&#x60; | [optional] 
**auth_transaction** | **str** | Reference to authorization transaction if charge is settled after authorization | [optional] 
**card_type** | **str** | Card type if credit card source: &#x60;unknown&#x60;, &#x60;visa&#x60;, &#x60;mc&#x60;, &#x60;dankort&#x60;, &#x60;visa_dk&#x60;, &#x60;ffk&#x60;, &#x60;visa_elec&#x60;, &#x60;maestro&#x60;, &#x60;laser&#x60;, &#x60;amex&#x60;, &#x60;diners&#x60;, &#x60;discover&#x60; or &#x60;jcb&#x60; | [optional] 
**exp_date** | **str** | Card expire date on form MM-YY if credit card source | [optional] 
**masked_card** | **str** | Masked card number if credit card source | [optional] 
**strong_authentication_status** | **str** | Status for strong customer authentication: &#x60;threed_secure&#x60;, &#x60;threed_secure_not_enrolled, &#x60;threed_secure_local_only&#x60;, &#x60;secured_by_nets&#x60; | [optional] 
**acquirer_code** | **str** | Card acquirer error code in case of card error | [optional] 
**acquirer_message** | **str** | Card acquirer message in case of card error | [optional] 
**acquirer_reference** | **str** | Card acquirer reference to transaction in case of card source. E.g. Nets order id or Clearhaus reference. | [optional] 
**text_on_statement** | **str** | Resulting text on bank statement if known | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


