# swagger_client.SignupApi

All URIs are relative to *https://checkout-api.reepay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_signup_page**](SignupApi.md#create_signup_page) | **POST** /v1/signup_page | Create signup page
[**delete_signup_page**](SignupApi.md#delete_signup_page) | **DELETE** /v1/signup_page/{id} | Delete signup page
[**get_signup_page**](SignupApi.md#get_signup_page) | **GET** /v1/signup_page/{id} | Get signup page
[**get_signup_page_signup**](SignupApi.md#get_signup_page_signup) | **GET** /v1/signup_page/{id}/signup | Get signup page signup data
[**get_signup_pages**](SignupApi.md#get_signup_pages) | **GET** /v1/signup_page | Get signup pages
[**update_signup_page**](SignupApi.md#update_signup_page) | **PUT** /v1/signup_page/{id} | Update signup page


# **create_signup_page**
> SignupPage create_signup_page(body=body)

Create signup page



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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSignupPage() # CreateSignupPage |  (optional)

try:
    # Create signup page
    api_response = api_instance.create_signup_page(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignupApi->create_signup_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSignupPage**](CreateSignupPage.md)|  | [optional] 

### Return type

[**SignupPage**](SignupPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_signup_page**
> delete_signup_page(id)

Delete signup page



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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Signup page id

try:
    # Delete signup page
    api_instance.delete_signup_page(id)
except ApiException as e:
    print("Exception when calling SignupApi->delete_signup_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Signup page id | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signup_page**
> SignupPage get_signup_page(id)

Get signup page



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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Signup page id

try:
    # Get signup page
    api_response = api_instance.get_signup_page(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignupApi->get_signup_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Signup page id | 

### Return type

[**SignupPage**](SignupPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signup_page_signup**
> SignupPageSignup get_signup_page_signup(id, coupon=coupon)

Get signup page signup data



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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Signup page id
coupon = 'coupon_example' # str |  (optional)

try:
    # Get signup page signup data
    api_response = api_instance.get_signup_page_signup(id, coupon=coupon)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignupApi->get_signup_page_signup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Signup page id | 
 **coupon** | **str**|  | [optional] 

### Return type

[**SignupPageSignup**](SignupPageSignup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signup_pages**
> list[SignupPage] get_signup_pages(size=size, plan=plan, created_before=created_before)

Get signup pages



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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
size = 100 # int | Page size. A maximum of 100 is allowed. (optional) (default to 100)
plan = 'plan_example' # str | Optional plan handle to filter on (optional)
created_before = 'created_before_example' # str | Get signup pages created before this date, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format. Use last created date as filter for next page. Default far far future. (optional)

try:
    # Get signup pages
    api_response = api_instance.get_signup_pages(size=size, plan=plan, created_before=created_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignupApi->get_signup_pages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Page size. A maximum of 100 is allowed. | [optional] [default to 100]
 **plan** | **str**| Optional plan handle to filter on | [optional] 
 **created_before** | **str**| Get signup pages created before this date, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format. Use last created date as filter for next page. Default far far future. | [optional] 

### Return type

[**list[SignupPage]**](SignupPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signup_page**
> SignupPage update_signup_page(id, body=body)

Update signup page



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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Signup page id
body = swagger_client.CreateSignupPage() # CreateSignupPage |  (optional)

try:
    # Update signup page
    api_response = api_instance.update_signup_page(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignupApi->update_signup_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Signup page id | 
 **body** | [**CreateSignupPage**](CreateSignupPage.md)|  | [optional] 

### Return type

[**SignupPage**](SignupPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

