# InvoiceCreditNote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Credit note id | 
**invoice** | **str** | Invoice credited by this note | 
**transaction** | **str** | Refund transaction id if credit note has an associated refund | [optional] 
**credit** | **str** | Credit reference if the credit note relates to a subscription credit | [optional] 
**amount** | **int** | Credit note amount | 
**created** | **datetime** | Creation date for note, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format. | 
**credit_note_lines** | [**list[CreditNoteLine]**](CreditNoteLine.md) | Credit note lines | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


