# TargetGroupHttpHealthCheck

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **path** | **str** | The destination URL for HTTP the health check; the default is &#39;/&#39;. | [optional]  |
| **method** | **str** | The method used for the health check request. | [optional]  |
| **match_type** | **str** | Specify the target&#39;s response type to match ALB&#39;s request. |  |
| **response** | **str** | The response returned by the request. It can be a status code or a response body depending on the definition of &#39;matchType&#39;. |  |
| **regex** | **bool** | Specifies whether to use a regular expression to parse the response body; the default value is &#39;FALSE&#39;.  By using regular expressions, you can flexibly customize the expected response from a healthy server. | [optional]  |
| **negate** | **bool** | Specifies whether to negate an individual entry; the default value is &#39;FALSE&#39;. | [optional]  |


