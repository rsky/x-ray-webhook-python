# ApiDataPostRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Request URL | 
**parameters** | **Dict[str, str]** | Request parameters | 

## Example

```python
from x_ray_webhook.models.api_data_post_request_request import ApiDataPostRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDataPostRequestRequest from a JSON string
api_data_post_request_request_instance = ApiDataPostRequestRequest.from_json(json)
# print the JSON string representation of the object
print(ApiDataPostRequestRequest.to_json())

# convert the object into a dict
api_data_post_request_request_dict = api_data_post_request_request_instance.to_dict()
# create an instance of ApiDataPostRequestRequest from a dict
api_data_post_request_request_from_dict = ApiDataPostRequestRequest.from_dict(api_data_post_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


