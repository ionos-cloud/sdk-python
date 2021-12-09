# LabelResources

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **str** | A unique representation of the label as a resource collection. | [optional] [readonly]  |
| **type** | **str** | The type of resource within a collection. | [optional] [readonly]  |
| **href** | **str** | URL to the collection representation (absolute path). | [optional] [readonly]  |
| **items** | [**list[LabelResource]**](LabelResource.md) | Array of items in that collection. | [optional] [readonly]  |
| **offset** | **float** | The offset (if specified in the request). | [optional]  |
| **limit** | **float** | The limit (if specified in the request). | [optional]  |
| **links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional]  |


