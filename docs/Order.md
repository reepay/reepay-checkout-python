# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **str** | Per account unique reference to charge/invoice. E.g. order id from own system. Multiple payments can be attempted for the same handle but only one authorized or settled charge can exist per handle. Max length 255 with allowable characters [a-zA-Z0-9_.-@]. It is recommended to use a maximum of 20 characters as this will allow for the use of handle as reference on bank statements without truncation. | 
**key** | **str** | Optional idempotency key. Only one authorization or settle can be performed for the same handle. If two create attempts are attempted and the first succeeds the second will fail because charge is already settled or authorized. An idempotency key identifies uniquely the request and multiple requests with the same key and handle will yield the same result. In case of networking errors the same request with same key can safely be retried. | [optional] 
**amount** | **int** | Amount in the smallest unit for the account currency. Either &#x60;amount&#x60; or &#x60;order_lines&#x60; must be provided if charge/invoice does not already exists. | [optional] 
**currency** | **str** | Optional currency in [ISO 4217](http://da.wikipedia.org/wiki/ISO_4217) three letter alpha code. If not provided the account default currency will be used. The currency of an existing charge or invoice cannot be changed. | [optional] 
**customer** | [**CreateCustomer**](CreateCustomer.md) | Optional create customer object. An alternative to using a reference to an already created customer either by the &#x60;customer_handle&#x60; parameter or implicitly given if using a saved payment method as source. If this object is provided and the customer already exists, the existing customer will be used. Notice that customer cannot be changed for existing charge/invoice so if handle is provided it must match the customer handle for existing customer. | [optional] 
**metadata** | **dict(str, object)** | Custom metadata. | [optional] 
**ordertext** | **str** | Optional order text. Used in conjunction with &#x60;amount&#x60;. Ignored if &#x60;order_lines&#x60; is provided. | [optional] 
**order_lines** | [**list[CreateOrderLine]**](CreateOrderLine.md) | Order lines for the charge. The order lines controls the amount. Only required if charge/invoice does not already exist. If given for existing charge the order lines and amount are adjusted. | [optional] 
**customer_handle** | **str** | Customer reference. If charge does not already exist either this reference must be provided, a create customer object must be provided or the source must be a payment method reference (e.g. &#x60;ca_..&#x60;) identifying customer. Notice that customer cannot be changed for existing charge/invoice so if handle is provided it must match the customer handle for existing customer. | [optional] 
**billing_address** | [**InvoiceBillingAddress**](InvoiceBillingAddress.md) | Optional billing address | [optional] 
**shipping_address** | [**InvoiceShippingAddress**](InvoiceShippingAddress.md) | Optional shipping address | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


