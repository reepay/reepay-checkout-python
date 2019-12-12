# swagger_client.ConfigurationApi

All URIs are relative to *https://checkout-api.reepay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration**](ConfigurationApi.md#create_configuration) | **POST** /v1/configuration | Create configuration
[**delete_configuration**](ConfigurationApi.md#delete_configuration) | **DELETE** /v1/configuration/{handle} | Delete configuration
[**get_configuration**](ConfigurationApi.md#get_configuration) | **GET** /v1/configuration/{handle} | Get configuration
[**get_configurations**](ConfigurationApi.md#get_configurations) | **GET** /v1/configuration | Get configurations
[**update_configuration**](ConfigurationApi.md#update_configuration) | **PUT** /v1/configuration/{handle} | Update configuration


# **create_configuration**
> Configuration create_configuration(body=body)

Create configuration



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
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateConfiguration() # CreateConfiguration |  (optional)

try:
    # Create configuration
    api_response = api_instance.create_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->create_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateConfiguration**](CreateConfiguration.md)|  | [optional] 

### Return type

[**Configuration**](Configuration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_configuration**
> delete_configuration(handle)

Delete configuration



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
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
handle = 'handle_example' # str | Configuration handle

try:
    # Delete configuration
    api_instance.delete_configuration(handle)
except ApiException as e:
    print("Exception when calling ConfigurationApi->delete_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**| Configuration handle | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration**
> Configuration get_configuration(handle)

Get configuration



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
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
handle = 'handle_example' # str | Configuration handle

try:
    # Get configuration
    api_response = api_instance.get_configuration(handle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**| Configuration handle | 

### Return type

[**Configuration**](Configuration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configurations**
> list[Configuration] get_configurations()

Get configurations



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
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Get configurations
    api_response = api_instance.get_configurations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configurations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Configuration]**](Configuration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration**
> Configuration update_configuration(handle, body=body)

Update configuration



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
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
handle = 'handle_example' # str | Configuration handle
body = swagger_client.UpdateConfiguration() # UpdateConfiguration |  (optional)

try:
    # Update configuration
    api_response = api_instance.update_configuration(handle, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->update_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**| Configuration handle | 
 **body** | [**UpdateConfiguration**](UpdateConfiguration.md)|  | [optional] 

### Return type

[**Configuration**](Configuration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

