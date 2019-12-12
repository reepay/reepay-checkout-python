# CheckoutSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Session id | 
**type** | **str** | Session type | 
**result** | **str** |  | [optional] 
**error_code** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**configuration** | **str** |  | [optional] 
**locale** | **str** | Session locale | 
**cancel_url** | **str** |  | [optional] 
**accept_url** | **str** |  | [optional] 
**payment_methods** | [**SessionPaymentMethods**](SessionPaymentMethods.md) |  | [optional] 
**subscription_invoice** | [**Invoice**](Invoice.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 
**charge** | [**Charge**](Charge.md) |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**subscription** | [**Subscription**](Subscription.md) |  | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**add_ons** | [**list[SubscriptionAddOn]**](SubscriptionAddOn.md) |  | [optional] 
**discounts** | [**list[SubscriptionDiscount]**](SubscriptionDiscount.md) |  | [optional] 
**subscription_payment_methods** | [**PaymentMethods**](PaymentMethods.md) |  | [optional] 
**recurring** | **bool** |  | [optional] 
**settle** | **bool** |  | [optional] 
**pkey** | **str** |  | [optional] 
**strong_auth** | [**StrongAuth**](StrongAuth.md) |  | [optional] 
**payment_method** | **str** |  | [optional] 
**pgw_url** | **str** |  | [optional] 
**mpo_url** | **str** |  | [optional] 
**mpo_session_token** | **str** |  | [optional] 
**mpo_version** | **str** |  | [optional] 
**viabill_url** | **str** |  | [optional] 
**resurs_url** | **str** |  | [optional] 
**applepay_payment_request** | [**ApplepayPaymentRequestDto**](ApplepayPaymentRequestDto.md) |  | [optional] 
**googlepay_payment_request** | [**GooglepayPaymentRequestDto**](GooglepayPaymentRequestDto.md) |  | [optional] 
**paypal_client_id** | **str** |  | [optional] 
**paypal_payment_request** | **dict(str, object)** |  | [optional] 
**paypal_auth_url** | **str** |  | [optional] 
**button_text** | **str** |  | [optional] 
**show_subscription_details** | **bool** |  | [optional] 
**show_terms** | **bool** |  | [optional] 
**card_on_file** | [**CardOnFile**](CardOnFile.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


