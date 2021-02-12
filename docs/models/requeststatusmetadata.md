# RequestStatusMetadata

## Properties

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **status** | **str** |  | \[optional\] |
| **message** | **str** |  | \[optional\] |
| **etag** | **str** | Resource's Entity Tag as defined in [http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html\#sec3.11](http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11) . Entity Tag is also added as an 'ETag response header to requests which don't use 'depth' parameter. | \[optional\] \[readonly\] |
| **targets** | [**list\[RequestTarget\]**](requesttarget.md) |  | \[optional\] |

