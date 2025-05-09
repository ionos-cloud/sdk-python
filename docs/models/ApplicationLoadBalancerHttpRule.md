# ApplicationLoadBalancerHttpRule

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The unique name of the Application Load Balancer HTTP rule. |  |
| **type** | **str** | The HTTP rule type. |  |
| **target_group** | **str** | The ID of the target group; this parameter is mandatory and is valid only for &#39;FORWARD&#39; actions. | [optional]  |
| **drop_query** | **bool** | Indicates whether the query part of the URI should be dropped and is valid only for &#39;REDIRECT&#39; actions. Default value is &#39;FALSE&#39;, the redirect URI does not contain any query parameters. | [optional]  |
| **location** | **str** | The location for the redirection; this parameter is mandatory and valid only for &#39;REDIRECT&#39; actions. | [optional]  |
| **status_code** | **int** | The status code is for &#39;REDIRECT&#39; and &#39;STATIC&#39; actions only.   If the HTTP rule is &#39;REDIRECT&#39; the valid values are: 301, 302, 303, 307, 308; default value is &#39;301&#39;.  If the HTTP rule is &#39;STATIC&#39; the valid values are from the range 200-599; default value is &#39;503&#39;. | [optional]  |
| **response_message** | **str** | The response message of the request; this parameter is mandatory for &#39;STATIC&#39; actions. | [optional]  |
| **content_type** | **str** | Specifies the content type and is valid only for &#39;STATIC&#39; actions. | [optional]  |
| **conditions** | [**list[ApplicationLoadBalancerHttpRuleCondition]**](ApplicationLoadBalancerHttpRuleCondition.md) | An array of items in the collection. The action will be executed only if each condition is met; the rule will always be applied if no conditions are set. | [optional]  |


