# ApiDataPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **int** | Member ID | 
**request** | [**ApiDataPostRequestRequest**](ApiDataPostRequestRequest.md) |  | 
**response** | [**ApiDataPostRequestResponse**](ApiDataPostRequestResponse.md) |  | 
**log** | [**ApiDataPostRequestLog**](ApiDataPostRequestLog.md) |  | [optional] 

## Example

```python
from x_ray_webhook.models.api_data_post_request import ApiDataPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDataPostRequest from a JSON string
api_data_post_request_instance = ApiDataPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiDataPostRequest.to_json())

# convert the object into a dict
api_data_post_request_dict = api_data_post_request_instance.to_dict()
# create an instance of ApiDataPostRequest from a dict
api_data_post_request_from_dict = ApiDataPostRequest.from_dict(api_data_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


