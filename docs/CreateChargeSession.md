# CreateChargeSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **str** | Optional handle for a configuration to use for this session | [optional] 
**locale** | **str** | Optional locale for session. E.g. &#x60;en_GB&#x60;, &#x60;da_DK&#x60;, &#x60;es_ES&#x60;. Defaults to configuration locale or account locale.  | [optional] 
**ttl** | **str** | Optional time-to-live duration. The session will expire after the duration from creation. The duration must be given as an ISO-8601 duration. See https://en.wikipedia.org/wiki/ISO_8601#Durations. E.g. PT3H (three hours). | [optional] 
**invoice** | **str** | Handle for existing invoice to charge. Either this argument must be provided or &#x60;order&#x60;. | [optional] 
**settle** | **bool** | Whether or not to immediately settle (capture). Default is false. If not settled immediately an authorization will be performed which can be settled later. Normally this have to be done within 7 days. | [optional] 
**order** | [**Order**](Order.md) | Order object. Either this argument must be provided or &#x60;invoice&#x60;.  | [optional] 
**recurring** | **bool** | If set a recurring payment method is stored for the customer and a reference returned. This parameter if set to true will limit payment methods to those that are reusable. | [optional] 
**accept_url** | **str** | If checkout is opened in separate window the customer will be directed to this page after success | [optional] 
**cancel_url** | **str** | If checkout is opened in separate window the customer will be directed to this page if the customer cancels | [optional] 
**payment_methods** | **list[str]** | Optional list of payment methods to use for the checkout session. Format: &#x60;&lt;payment_methods&gt; &#x3D; list of &lt;payment_method&gt;&#x60; &#x60;&lt;payment_method&gt;  &#x3D; [sca-|scafallback-|nosca-|]&lt;payment_name&gt;&#x60; &#x60;&lt;payment_name&gt;    &#x3D; The id of payment method, e.g. dankort&#x60; See https://docs.reepay.com/docs/checkout-payment-methods for full documentation | [optional] 
**button_text** | **str** | Optional alternative button text. Maximum length 32 characters. | [optional] 
**card_on_file** | **str** | Reference to existing card payment method (&#x60;ca_xxx&#x60;) to perform card-on-file payment for. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


