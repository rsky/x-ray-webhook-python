# ApiDataPostRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The UNIX timestamp (in milliseconds) when the response was received | 
**data** | [**ApiDataPostRequestResponseData**](ApiDataPostRequestResponseData.md) |  | 

## Example

```python
from x_ray_webhook.models.api_data_post_request_response import ApiDataPostRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDataPostRequestResponse from a JSON string
api_data_post_request_response_instance = ApiDataPostRequestResponse.from_json(json)
# print the JSON string representation of the object
print(ApiDataPostRequestResponse.to_json())

# convert the object into a dict
api_data_post_request_response_dict = api_data_post_request_response_instance.to_dict()
# create an instance of ApiDataPostRequestResponse from a dict
api_data_post_request_response_from_dict = ApiDataPostRequestResponse.from_dict(api_data_post_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


