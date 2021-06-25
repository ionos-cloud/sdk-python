# LabelResources

## Properties

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **id** | **str** | Unique representation for Label as a collection on a resource. | \[optional\] \[readonly\] |
| **type** | **str** | The type of resource within a collection | \[optional\] \[readonly\] |
| **href** | **str** | URL to the collection representation \(absolute path\) | \[optional\] \[readonly\] |
| **items** | [**list\[LabelResource\]**](labelresource.md) | Array of items in that collection | \[optional\] \[readonly\] |
| **offset** | **float** | the offset \(if specified in the request\) | \[optional\] |
| **limit** | **float** | the limit \(if specified in the request\) | \[optional\] |
| **links** | [**PaginationLinks**](paginationlinks.md) |  | \[optional\] |

