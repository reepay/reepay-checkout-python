# Plan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the plan | 
**description** | **str** | Description of the plan | [optional] 
**vat** | **float** | Optional vat for this plan. Account default is used if none given. | [optional] 
**amount** | **int** | Amount for the plan in the smallest unit for the account currency | 
**quantity** | **int** | Optional default quantity of the subscription plan product for new subscriptions. Default is 1. | [optional] 
**prepaid** | **bool** | Subscriptions can either be prepaid where an amount is paid in advance, or the opposite. This setting only relates to handling of pause scenarios. | [optional] 
**handle** | **str** | Per account unique handle for the subscription plan. Max length 255 with allowable characters [a-zA-Z0-9_.-@]. | 
**version** | **int** | Plan version | 
**state** | **str** | State of the subscription plan one of the following: &#x60;active&#x60;, &#x60;superseded&#x60;, &#x60;deleted&#x60; | 
**currency** | **str** | Currency for the subscription plan in [ISO 4217](http://da.wikipedia.org/wiki/ISO_4217) three letter alpha code | 
**created** | **datetime** | Date when the subscripton plan was created. In ISO-8601 extended offset date-time format. | 
**dunning_plan** | **str** | Dunning plan handle | [optional] 
**renewal_reminder_email_days** | **int** | Optional renewal reminder email settings. Number of days before next billing to send a reminder email. | [optional] 
**trial_reminder_email_days** | **int** | Optional end of trial reminder email settings. Number of days before end of trial to send a reminder email. | [optional] 
**partial_period_handling** | **str** | How to handle a potential initial partial billing period for fixed day scheduling. The options are to bill for a full period, bill prorated for the partial period, bill a zero amoumt, or not to consider the period before first fixed day a billing period. The default is to bill prorated. Options: &#x60;bill_full&#x60;, &#x60;bill_prorated&#x60;, &#x60;bill_zero_amount&#x60;, &#x60;no_bill&#x60;. | [optional] 
**include_zero_amount** | **bool** | Whether to add a zero amount order line to subscription invoices if plan amount is zero or the subscription overrides to zero amount. The default is to not include the line. If no other order lines are present the plan order line will be added. | [optional] 
**setup_fee** | **int** | Optional one-time setup fee billed with the first invoice or as a separate invoice depending on the setting &#x60;setup_fee_handling&#x60;. | [optional] 
**setup_fee_text** | **str** | Optional invoice order text for the setup fee that | [optional] 
**setup_fee_handling** | **str** | How the billing of the setup fee should be done. The options are: &#x60;first&#x60; - include setup fee as order line on the first scheduled invoice. &#x60;separate&#x60; - create a separate invoice for the setup fee, is appropriate if first invoice is not in conjunction with creation. &#x60;separate_conditional&#x60; - create a separate invoice for setup fee if the first invoice is not created in conjunction with the creation. Default is &#x60;first&#x60;. | [optional] 
**amount_incl_vat** | **bool** | Whether the amount is including VAT. Default true. | [optional] 
**fixed_count** | **int** | Fixed number of renewals for subscriptions using this plan. Equals the number of scheduled invoices. | [optional] 
**fixed_life_time_unit** | **str** | Time unit use for fixed life time | [optional] 
**fixed_life_time_length** | **int** | Fixed life time length for subscriptions using this plan. E.g. 12 months. Subscriptions will cancel after the fixed life time and expire when the active billing cycle ends. | [optional] 
**trial_interval_unit** | **str** | Time unit for free trial period | [optional] 
**trial_interval_length** | **int** | Free trial interval length. E.g. 1 month. | [optional] 
**interval_length** | **int** | The length of intervals. E.g. every second month or every 14 days. | 
**schedule_type** | **str** | Scheduling type, one of the following: &#x60;manual&#x60;, &#x60;daily&#x60;, &#x60;weekly_fixedday&#x60;, &#x60;month_startdate&#x60;, &#x60;month_fixedday&#x60;, &#x60;month_lastday&#x60;. See documentation for descriptions of the different types. | 
**schedule_fixed_day** | **int** | If a fixed day scheduling type is used a fixed day must be provided. For months the allowed value is 1-28 for weeks it is 1-7 | [optional] 
**base_month** | **int** | For fixed month schedule types the base month can be used to control which months are eligible for start of first billing period. The eligible months are calculated as &#x60;base_month + k * interval_length&#x60; up to 12. E.g. to use quaterly billing in the months jan-apr-jul-oct, &#x60;base_month&#x60; 1 and &#x60;interval_length&#x60; 3 can be used. If not defined the first fixed day will be used as start of first billing period. | [optional] 
**notice_periods** | **int** | Optional number of notice periods for a cancel. The subscription will be cancelled for this number of full periods before expiring. Either from the cancellation date, or from the end of the the current period. See &#x60;notice_periods_after_current&#x60;. The default is to expire at the end of current period (0). A value of 1 (and &#x60;notice_periods_after_current&#x60; set to true) will for example result in a scenario where the subscription is cancelled until the end of current period, and then for the full subsequent period before expiring. | [optional] 
**notice_periods_after_current** | **bool** | If notice periods is set, this option controls whether the number of full notice periods should start at the end of the current period, or run from cancellation date and result in a partial period with partial amount for the last period. The default is true. E.g. if set to false and &#x60;notice_periods &#x3D; 1&#x60; then the subscription will be cancelled for exactly for one period from the cancellation time and a partial amount will be billed at the start of the next billing period. | [optional] 
**fixation_periods** | **int** | Optional number of fixation periods. Fixation periods will guarantee that a subscription will have this number of paid full periods before expiring after a cancel. Default is to have no requirement (0). | [optional] 
**fixation_periods_full** | **bool** | If fixation periods are defined, and the subscription can have a partial prorated first period, this parameter controls if the the last period should be full, or partial to give exactly &#x60;fixation_periods&#x60; paid periods. Default is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


