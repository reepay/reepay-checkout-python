# Charge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **str** | Per account unique reference to charge/invoice. E.g. order id from own system. Multiple payments can be attempted for the same handle but only one succeeded charge can exist per handle. Max length 255 with allowable characters [a-zA-Z0-9_.-@]. | 
**state** | **str** | The charge state one of the following: &#x60;authorized&#x60;, &#x60;settled&#x60;, &#x60;failed&#x60;, &#x60;cancelled&#x60; | 
**customer** | **str** | Customer handle | 
**amount** | **int** | The invoice amount including VAT | 
**currency** | **str** | Currency for the account in [ISO 4217](http://da.wikipedia.org/wiki/ISO_4217) three letter alpha code | 
**authorized** | **datetime** | When the charge was authorized, if the charge went through an authorize and settle flow, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format. | [optional] 
**settled** | **datetime** | When the charge was settled, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format. | [optional] 
**cancelled** | **datetime** | When the charge was cancelled, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format. | [optional] 
**created** | **datetime** | When the invoice was created, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format. | 
**transaction** | **str** | Transaction id assigned by Reepay. Assigned when transaction is performed. | [optional] 
**error** | **str** | Reepay error code if failed. See [transaction errors](https://reference.reepay.com/api/#transaction-errors). | [optional] 
**source** | [**ChargeSource**](ChargeSource.md) | Object describing the source for the charge. E.g. credit card. | 
**order_lines** | [**list[OrderLine]**](OrderLine.md) | Order lines for charge | 
**refunded_amount** | **int** | Refunded amount | 
**authorized_amount** | **int** | Authorized amount if authorization was performed. The maximum amount that can be settled. | 
**error_state** | **str** | Reepay error state if failed: &#x60;soft_declined&#x60;, &#x60;hard_declined&#x60; or &#x60;processing_error&#x60;. Soft and hard declines indicate a card decline. A soft decline is possibly recoverable and a subsequent request with the same card may succeed. E.g. insufficient funds. A processing error indicates an error processing the card either at Reepay, the acquirer, or between Reepay amd the acquirer. | [optional] 
**recurring_payment_method** | **str** | Optional reference to recurring payment method created in conjunction with charging | [optional] 
**billing_address** | [**InvoiceBillingAddress**](InvoiceBillingAddress.md) | Optional billing address | [optional] 
**shipping_address** | [**InvoiceShippingAddress**](InvoiceShippingAddress.md) | Optional shipping address | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


