# Requests

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **str** | The resource&#39;s unique identifier. | [optional] [readonly]  |
| **type** | [**Type**](Type.md) | The type of object that has been created. | [optional]  |
| **href** | **str** | URL to the object representation (absolute path). | [optional] [readonly]  |
| **items** | [**list[Request]**](Request.md) | Array of items in the collection. | [optional] [readonly]  |
| **offset** | **float** | The offset, specified in the request (if not is specified, 0 is used by default). |  |
| **limit** | **float** | The limit, specified in the request (if not specified, the endpoint&#39;s default pagination limit is used). |  |
| **links** | [**PaginationLinks**](PaginationLinks.md) |  |  |


