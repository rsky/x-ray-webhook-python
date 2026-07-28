# MemberInfoPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **int** | Member ID | 
**nickname** | **str** | Member nickname | 
**host** | **str** | Naval district host name | 

## Example

```python
from x_ray_webhook.models.member_info_post_request import MemberInfoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemberInfoPostRequest from a JSON string
member_info_post_request_instance = MemberInfoPostRequest.from_json(json)
# print the JSON string representation of the object
print(MemberInfoPostRequest.to_json())

# convert the object into a dict
member_info_post_request_dict = member_info_post_request_instance.to_dict()
# create an instance of MemberInfoPostRequest from a dict
member_info_post_request_from_dict = MemberInfoPostRequest.from_dict(member_info_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


