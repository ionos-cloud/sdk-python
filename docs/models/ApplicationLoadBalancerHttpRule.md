# ApplicationLoadBalancerHttpRule

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The unique name of the Application Load Balancer HTTP rule. |  |
| **type** | **str** | Type of the HTTP rule. |  |
| **target_group** | **str** | The ID of the target group; mandatory and only valid for FORWARD actions. | [optional]  |
| **drop_query** | **bool** | Default is false; valid only for REDIRECT actions. | [optional]  |
| **location** | **str** | The location for redirecting; mandatory and valid only for REDIRECT actions. | [optional]  |
| **status_code** | **int** | Valid only for REDIRECT and STATIC actions. For REDIRECT actions, default is 301 and possible values are 301, 302, 303, 307, and 308. For STATIC actions, default is 503 and valid range is 200 to 599. | [optional]  |
| **response_message** | **str** | The response message of the request; mandatory for STATIC actions. | [optional]  |
| **content_type** | **str** | Valid only for STATIC actions. | [optional]  |
| **conditions** | [**list[ApplicationLoadBalancerHttpRuleCondition]**](ApplicationLoadBalancerHttpRuleCondition.md) | An array of items in the collection.The action is only performed if each and every condition is met; if no conditions are set, the rule will always be performed. | [optional]  |


