# swagger_client.CheckoutApi

All URIs are relative to *https://checkout-api.reepay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**charge_checkout_session**](CheckoutApi.md#charge_checkout_session) | **POST** /v1/checkout/{id}/charge | Finish charge using source
[**create_applepay_session**](CheckoutApi.md#create_applepay_session) | **POST** /v1/checkout/{id}/applepay | Create Apple Pay session
[**create_googlepay_session**](CheckoutApi.md#create_googlepay_session) | **POST** /v1/checkout/{id}/googlepay | Create Google Pay session
[**create_mpo_session**](CheckoutApi.md#create_mpo_session) | **POST** /v1/checkout/{id}/mpo | Create MobilePay Online session
[**create_paypal_session**](CheckoutApi.md#create_paypal_session) | **POST** /v1/checkout/{id}/paypal | Create PayPal session
[**create_pgw_session**](CheckoutApi.md#create_pgw_session) | **POST** /v1/checkout/{id}/pgw | Create pgw session
[**create_resurs_session**](CheckoutApi.md#create_resurs_session) | **POST** /v1/checkout/{id}/resurs | Create Resurs session
[**create_viabill_session**](CheckoutApi.md#create_viabill_session) | **POST** /v1/checkout/{id}/viabill | Create ViaBill session
[**get_checkout_session**](CheckoutApi.md#get_checkout_session) | **GET** /v1/checkout/{id} | Get checkout session data
[**get_resurs_payment_method_cost**](CheckoutApi.md#get_resurs_payment_method_cost) | **POST** /v1/checkout/{id}/resurs/payment_method_cost | Get HTML with cost of Resurs payment method
[**get_resurs_payment_methods**](CheckoutApi.md#get_resurs_payment_methods) | **GET** /v1/checkout/{id}/resurs/payment_methods | Get Resurs payment methods
[**get_terms**](CheckoutApi.md#get_terms) | **GET** /v1/checkout/{id}/terms | Get account terms template
[**recurring_checkout_session**](CheckoutApi.md#recurring_checkout_session) | **POST** /v1/checkout/{id}/recurring | Save recurring customer payment method
[**subscription_checkout_session**](CheckoutApi.md#subscription_checkout_session) | **POST** /v1/checkout/{id}/subscription | Set payment method on subscription


# **charge_checkout_session**
> CheckoutSession charge_checkout_session(id, body=body)

Finish charge using source



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id
body = swagger_client.SessionChargeDto() # SessionChargeDto |  (optional)

try:
    # Finish charge using source
    api_response = api_instance.charge_checkout_session(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->charge_checkout_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 
 **body** | [**SessionChargeDto**](SessionChargeDto.md)|  | [optional] 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_applepay_session**
> CheckoutSession create_applepay_session(id)

Create Apple Pay session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id

try:
    # Create Apple Pay session
    api_response = api_instance.create_applepay_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->create_applepay_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_googlepay_session**
> CheckoutSession create_googlepay_session(id)

Create Google Pay session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id

try:
    # Create Google Pay session
    api_response = api_instance.create_googlepay_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->create_googlepay_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mpo_session**
> CheckoutSession create_mpo_session(id, body=body)

Create MobilePay Online session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id
body = swagger_client.CreateMpoSession() # CreateMpoSession |  (optional)

try:
    # Create MobilePay Online session
    api_response = api_instance.create_mpo_session(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->create_mpo_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 
 **body** | [**CreateMpoSession**](CreateMpoSession.md)|  | [optional] 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_paypal_session**
> CheckoutSession create_paypal_session(id)

Create PayPal session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id

try:
    # Create PayPal session
    api_response = api_instance.create_paypal_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->create_paypal_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pgw_session**
> CheckoutSession create_pgw_session(id, body=body)

Create pgw session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id
body = swagger_client.CreatePGWSession() # CreatePGWSession |  (optional)

try:
    # Create pgw session
    api_response = api_instance.create_pgw_session(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->create_pgw_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 
 **body** | [**CreatePGWSession**](CreatePGWSession.md)|  | [optional] 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_resurs_session**
> CheckoutSession create_resurs_session(id, body=body)

Create Resurs session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id
body = swagger_client.CreateResursSession() # CreateResursSession |  (optional)

try:
    # Create Resurs session
    api_response = api_instance.create_resurs_session(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->create_resurs_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 
 **body** | [**CreateResursSession**](CreateResursSession.md)|  | [optional] 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_viabill_session**
> CheckoutSession create_viabill_session(id, body=body)

Create ViaBill session



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id
body = swagger_client.CreateViabillSession() # CreateViabillSession |  (optional)

try:
    # Create ViaBill session
    api_response = api_instance.create_viabill_session(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->create_viabill_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 
 **body** | [**CreateViabillSession**](CreateViabillSession.md)|  | [optional] 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkout_session**
> CheckoutSession get_checkout_session(id)

Get checkout session data



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id

try:
    # Get checkout session data
    api_response = api_instance.get_checkout_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->get_checkout_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resurs_payment_method_cost**
> str get_resurs_payment_method_cost(id, body=body)

Get HTML with cost of Resurs payment method



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id
body = swagger_client.ResursPaymentMethodDto() # ResursPaymentMethodDto |  (optional)

try:
    # Get HTML with cost of Resurs payment method
    api_response = api_instance.get_resurs_payment_method_cost(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->get_resurs_payment_method_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 
 **body** | [**ResursPaymentMethodDto**](ResursPaymentMethodDto.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resurs_payment_methods**
> list[ResursPaymentMethodDto] get_resurs_payment_methods(id)

Get Resurs payment methods



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id

try:
    # Get Resurs payment methods
    api_response = api_instance.get_resurs_payment_methods(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->get_resurs_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 

### Return type

[**list[ResursPaymentMethodDto]**](ResursPaymentMethodDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_terms**
> str get_terms(id)

Get account terms template



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id

try:
    # Get account terms template
    api_response = api_instance.get_terms(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->get_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recurring_checkout_session**
> CheckoutSession recurring_checkout_session(id, body=body)

Save recurring customer payment method



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id
body = swagger_client.SessionRecurring() # SessionRecurring |  (optional)

try:
    # Save recurring customer payment method
    api_response = api_instance.recurring_checkout_session(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->recurring_checkout_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 
 **body** | [**SessionRecurring**](SessionRecurring.md)|  | [optional] 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_checkout_session**
> CheckoutSession subscription_checkout_session(id, body=body)

Set payment method on subscription



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutApi()
id = 'id_example' # str | Session id
body = swagger_client.SessionRecurring() # SessionRecurring |  (optional)

try:
    # Set payment method on subscription
    api_response = api_instance.subscription_checkout_session(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->subscription_checkout_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 
 **body** | [**SessionRecurring**](SessionRecurring.md)|  | [optional] 

### Return type

[**CheckoutSession**](CheckoutSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

