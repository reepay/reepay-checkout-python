# swagger_client.SessionInfoApi

All URIs are relative to *https://checkout-api.reepay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_session**](SessionInfoApi.md#get_session) | **GET** /v1/session_info/{id} | Get session info
[**get_sessions**](SessionInfoApi.md#get_sessions) | **GET** /v1/session_info/{relation_type}/{handle} | Get sessions by relation type and handle


# **get_session**
> SessionInfo get_session(id)

Get session info



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
api_instance = swagger_client.SessionInfoApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Session id

try:
    # Get session info
    api_response = api_instance.get_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionInfoApi->get_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Session id | 

### Return type

[**SessionInfo**](SessionInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions**
> list[SessionInfo] get_sessions(relation_type, handle)

Get sessions by relation type and handle



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
api_instance = swagger_client.SessionInfoApi(swagger_client.ApiClient(configuration))
relation_type = 'relation_type_example' # str | Relation type
handle = 'handle_example' # str | Relation handle

try:
    # Get sessions by relation type and handle
    api_response = api_instance.get_sessions(relation_type, handle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionInfoApi->get_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_type** | **str**| Relation type | 
 **handle** | **str**| Relation handle | 

### Return type

[**list[SessionInfo]**](SessionInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

