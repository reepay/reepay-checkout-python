# CreatePreparedSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | **str** | Customer handle of existing customer. Customer can also be provided in same operation by supplying the parameter &#x60;create_customer&#x60;. | [optional] 
**plan** | **str** | Plan handle | 
**amount** | **int** | Optional custom per quantity plan price. If provided the plan price billed for each billing period will be overridden by this price. | [optional] 
**quantity** | **int** | Optional quantity of the plan product for this subscription. If not provided the default is the default plan quantity defined for the plan. | [optional] 
**test** | **bool** | Test flag. If given it will be verified that the account state matches the intended create state. | [optional] 
**handle** | **str** | Per account unique handle for the subscription. Max length 255 with allowable characters [a-zA-Z0-9_.-@]. Must be provided if generate_handle not defined. | [optional] 
**metadata** | **dict(str, object)** | Custom metadata. | [optional] 
**create_customer** | [**CreateCustomer**](CreateCustomer.md) | Create customer and subscription in an atomic operation | [optional] 
**plan_version** | **int** | Optional plan version, default is to use newest version of plan | [optional] 
**amount_incl_vat** | **bool** | Whether the optional amount is including VAT. Defaults to true. | [optional] 
**generate_handle** | **bool** | Auto generate handle on the form sub-[sequence_number] | [optional] 
**start_date** | **str** | Date and time on the form &#x60;yyyy-MM-dd&#x60;, &#x60;yyyyMMdd&#x60;, &#x60;yyyy-MM-ddTHH:mm&#x60; and &#x60;yyyy-MM-ddTHH:mm:ss&#x60; from which the subscription is eligible to schedule first invoice. If no time part is given start of day will be used. A start date in the past can be used, but no more than one period length in the past. A start date in the past can result in an instant invoice for a past billing period start. Default value is current date and time. | [optional] 
**end_date** | **str** | Fixed date and time on the form &#x60;yyyy-MM-dd&#x60;, &#x60;yyyyMMdd&#x60;, &#x60;yyyy-MM-ddTHH:mm&#x60; and &#x60;yyyy-MM-ddTHH:mm:ss&#x60; where the subscription will automatically cancel. The subscription will expire at the end of the billing period containing the end date. Default is no fixed end date. | [optional] 
**grace_duration** | **int** | A grace duration in seconds from the creation of a subscription where no dunning process is started for a failing invoice. This allows a certain amount of time for the customer to sign up with a payment method. | [optional] 
**no_trial** | **bool** | Override plan trial settings and disable trial | [optional] 
**no_setup_fee** | **bool** | Override plan setup fee settings and disable fee | [optional] 
**subscription_discounts** | [**list[CreateSubscriptionDiscount]**](CreateSubscriptionDiscount.md) | Discounts to attach to subscription | [optional] 
**coupon_codes** | **list[str]** | Coupon codes to redeem for subscription | [optional] 
**add_ons** | [**list[CreateSubscriptionAddOn]**](CreateSubscriptionAddOn.md) | Add-ons to attach to subscription. The same add-on can only be attached to subscription once unless unique handles are supplied for the subscription add-on. | [optional] 
**additional_costs** | [**list[CreateSubscriptionAdditionalCost]**](CreateSubscriptionAdditionalCost.md) | Additional costs to add to subscription at creation time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


