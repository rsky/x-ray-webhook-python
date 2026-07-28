# x_ray_webhook.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_data_post**](DefaultApi.md#api_data_post) | **POST** /api_data | 
[**member_info_post**](DefaultApi.md#member_info_post) | **POST** /member_info | 
[**resource_update_post**](DefaultApi.md#resource_update_post) | **POST** /resource_update | 


# **api_data_post**
> ApiDataPost200Response api_data_post(api_data_post_request=api_data_post_request)

Receives KanColle API request and response data

### Example


```python
import x_ray_webhook
from x_ray_webhook.models.api_data_post200_response import ApiDataPost200Response
from x_ray_webhook.models.api_data_post_request import ApiDataPostRequest
from x_ray_webhook.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = x_ray_webhook.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with x_ray_webhook.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = x_ray_webhook.DefaultApi(api_client)
    api_data_post_request = x_ray_webhook.ApiDataPostRequest() # ApiDataPostRequest |  (optional)

    try:
        api_response = await api_instance.api_data_post(api_data_post_request=api_data_post_request)
        print("The response of DefaultApi->api_data_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_data_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_data_post_request** | [**ApiDataPostRequest**](ApiDataPostRequest.md)|  | [optional] 

### Return type

[**ApiDataPost200Response**](ApiDataPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_info_post**
> ApiDataPost200Response member_info_post(member_info_post_request=member_info_post_request)

Updates member information

### Example


```python
import x_ray_webhook
from x_ray_webhook.models.api_data_post200_response import ApiDataPost200Response
from x_ray_webhook.models.member_info_post_request import MemberInfoPostRequest
from x_ray_webhook.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = x_ray_webhook.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with x_ray_webhook.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = x_ray_webhook.DefaultApi(api_client)
    member_info_post_request = x_ray_webhook.MemberInfoPostRequest() # MemberInfoPostRequest |  (optional)

    try:
        api_response = await api_instance.member_info_post(member_info_post_request=member_info_post_request)
        print("The response of DefaultApi->member_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->member_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_info_post_request** | [**MemberInfoPostRequest**](MemberInfoPostRequest.md)|  | [optional] 

### Return type

[**ApiDataPost200Response**](ApiDataPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_update_post**
> ApiDataPost200Response resource_update_post(resource_update_post_request=resource_update_post_request)

Notifies that the resource has been updated

### Example


```python
import x_ray_webhook
from x_ray_webhook.models.api_data_post200_response import ApiDataPost200Response
from x_ray_webhook.models.resource_update_post_request import ResourceUpdatePostRequest
from x_ray_webhook.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = x_ray_webhook.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with x_ray_webhook.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = x_ray_webhook.DefaultApi(api_client)
    resource_update_post_request = x_ray_webhook.ResourceUpdatePostRequest() # ResourceUpdatePostRequest |  (optional)

    try:
        api_response = await api_instance.resource_update_post(resource_update_post_request=resource_update_post_request)
        print("The response of DefaultApi->resource_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->resource_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_update_post_request** | [**ResourceUpdatePostRequest**](ResourceUpdatePostRequest.md)|  | [optional] 

### Return type

[**ApiDataPost200Response**](ApiDataPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

