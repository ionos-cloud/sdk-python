# ApplicationLoadBalancerHttpRuleCondition

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **type** | **str** | Type of the HTTP rule condition. |  |
| **condition** | **str** | Matching rule for the HTTP rule condition attribute; mandatory for HEADER, PATH, QUERY, METHOD, HOST, and COOKIE types; must be null when type is SOURCE_IP. |  |
| **negate** | **bool** | Specifies whether the condition is negated or not; the default is False. | [optional]  |
| **key** | **str** | Must be null when type is PATH, METHOD, HOST, or SOURCE_IP. Key can only be set when type is COOKIES, HEADER, or QUERY. | [optional]  |
| **value** | **str** | Mandatory for conditions CONTAINS, EQUALS, MATCHES, STARTS_WITH, ENDS_WITH; must be null when condition is EXISTS; should be a valid CIDR if provided and if type is SOURCE_IP. | [optional]  |


