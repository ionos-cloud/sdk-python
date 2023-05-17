# NetworkLoadBalancerForwardingRuleProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the Network Load Balancer forwarding rule. |  |
| **algorithm** | **str** | Balancing algorithm |  |
| **protocol** | **str** | Balancing protocol |  |
| **listener_ip** | **str** | Listening (inbound) IP. |  |
| **listener_port** | **int** | Listening (inbound) port number; valid range is 1 to 65535. |  |
| **health_check** | [**NetworkLoadBalancerForwardingRuleHealthCheck**](NetworkLoadBalancerForwardingRuleHealthCheck.md) |  | [optional]  |
| **targets** | [**list[NetworkLoadBalancerForwardingRuleTarget]**](NetworkLoadBalancerForwardingRuleTarget.md) | Array of items in the collection. |  |


