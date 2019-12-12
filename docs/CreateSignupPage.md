# CreateSignupPage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** | Subscription plan | 
**locale** | **str** | Optional locale. E.g. &#x60;en_GB&#x60;, &#x60;da_DK&#x60;, &#x60;es_ES&#x60;. Defaults to configuration locale or account locale.  | [optional] 
**email** | **str** | Field configuration | [optional] 
**phone** | **str** | Field configuration | [optional] 
**address** | **str** | Field configuration | [optional] 
**company** | **str** | Field configuration | [optional] 
**city** | **str** | Field configuration | [optional] 
**coupon** | **str** | Field configuration | [optional] 
**accept_url** | **str** | Redirect to this url after successful signup | [optional] 
**cancel_url** | **str** | Redirect to this url if the customer cancels sign-up | [optional] 
**payment_methods** | **list[str]** | Optional list of payment methods to present to customer. Format: &lt;payment_methods&gt; &#x3D; list of &lt;payment_method&gt; &lt;payment_method&gt;  &#x3D; [sca-|nosca-]&lt;payment_name&gt; &lt;payment_name&gt;    &#x3D; The id of payment method, e.g. dankort See https://docs.reepay.com/docs/checkout-payment-methods for full documentation | [optional] 
**subscription_configuration** | [**CreateSubscription**](CreateSubscription.md) | Configuration configuration | [optional] 
**first_name** | **str** | Field configuration | [optional] 
**last_name** | **str** | Field configuration | [optional] 
**postal_code** | **str** | Field configuration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


