# ResourceUpdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the updated resource | 
**timestamp** | **int** | The UNIX timestamp (in milliseconds) when the new resource was received | 

## Example

```python
from x_ray_webhook.models.resource_update_post_request import ResourceUpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceUpdatePostRequest from a JSON string
resource_update_post_request_instance = ResourceUpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceUpdatePostRequest.to_json())

# convert the object into a dict
resource_update_post_request_dict = resource_update_post_request_instance.to_dict()
# create an instance of ResourceUpdatePostRequest from a dict
resource_update_post_request_from_dict = ResourceUpdatePostRequest.from_dict(resource_update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


