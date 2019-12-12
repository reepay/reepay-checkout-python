# swagger_client.SessionApi

All URIs are relative to *https://checkout-api.reepay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_charge_session**](SessionApi.md#create_charge_session) | **POST** /v1/session/charge | Create charge session
[**create_recurring_session**](SessionApi.md#create_recurring_session) | **POST** /v1/session/recurring | Create recurring session
[**create_subscription_session**](SessionApi.md#create_subscription_session) | **POST** /v1/session/subscription | Create subscription session
[**delete_session**](SessionApi.md#delete_session) | **DELETE** /v1/session/{id} | Delete session


# **create_charge_session**
> Session create_charge_session(body=body)

Create charge session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateChargeSession() # CreateChargeSession |  (optional)

try:
    # Create charge session
    api_response = api_instance.create_charge_session(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_charge_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateChargeSession**](CreateChargeSession.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recurring_session**
> Session create_recurring_session(body=body)

Create recurring session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRecurringSession() # CreateRecurringSession |  (optional)

try:
    # Create recurring session
    api_response = api_instance.create_recurring_session(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_recurring_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRecurringSession**](CreateRecurringSession.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_session**
> Session create_subscription_session(body=body)

Create subscription session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSubscriptionSession() # CreateSubscriptionSession |  (optional)

try:
    # Create subscription session
    api_response = api_instance.create_subscription_session(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_subscription_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSubscriptionSession**](CreateSubscriptionSession.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_session**
> delete_session(id)

Delete session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SessionApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Session id

try:
    # Delete session
    api_instance.delete_session(id)
except ApiException as e:
    print("Exception when calling SessionApi->delete_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

