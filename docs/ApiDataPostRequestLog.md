# ApiDataPostRequestLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | Bucket name | 
**key** | **str** | S3 object key | 

## Example

```python
from x_ray_webhook.models.api_data_post_request_log import ApiDataPostRequestLog

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDataPostRequestLog from a JSON string
api_data_post_request_log_instance = ApiDataPostRequestLog.from_json(json)
# print the JSON string representation of the object
print(ApiDataPostRequestLog.to_json())

# convert the object into a dict
api_data_post_request_log_dict = api_data_post_request_log_instance.to_dict()
# create an instance of ApiDataPostRequestLog from a dict
api_data_post_request_log_from_dict = ApiDataPostRequestLog.from_dict(api_data_post_request_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


