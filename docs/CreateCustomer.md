# CreateCustomer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Customer email | [optional] 
**address** | **str** | Customer address | [optional] 
**address2** | **str** | Customer address2 | [optional] 
**city** | **str** | Customer city | [optional] 
**country** | **str** | Customer country in ISO 3166-1 alpha-2 | [optional] 
**phone** | **str** | Customer phone number | [optional] 
**company** | **str** | Customer company | [optional] 
**vat** | **str** | Customer vat number | [optional] 
**handle** | **str** | Per account unique handle for the customer. Max length 255 with allowable characters [a-zA-Z0-9_.-@]. Must be provided if generate_handle is not defined. | [optional] 
**test** | **bool** | Test flag. If given it will be verified that the account state matches the intended create state. | [optional] 
**metadata** | **dict(str, object)** | Custom metadata. | [optional] 
**first_name** | **str** | Customer first name | [optional] 
**last_name** | **str** | Customer last name | [optional] 
**postal_code** | **str** | Customer postal code | [optional] 
**generate_handle** | **bool** | Auto generate handle on the form cust-[sequence_number] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


