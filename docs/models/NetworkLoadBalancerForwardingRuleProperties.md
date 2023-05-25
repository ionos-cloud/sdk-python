# NetworkLoadBalancerForwardingRuleProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **algorithm** | **str** | Balancing algorithm |  |
| **health_check** | [**NetworkLoadBalancerForwardingRuleHealthCheck**](NetworkLoadBalancerForwardingRuleHealthCheck.md) |  | [optional]  |
| **listener_ip** | **str** | Listening (inbound) IP. |  |
| **listener_port** | **int** | Listening (inbound) port number; valid range is 1 to 65535. |  |
| **name** | **str** | The name of the Network Load Balancer forwarding rule. |  |
| **protocol** | **str** | Balancing protocol |  |
| **targets** | [**list[NetworkLoadBalancerForwardingRuleTarget]**](NetworkLoadBalancerForwardingRuleTarget.md) | Array of items in the collection. |  |


