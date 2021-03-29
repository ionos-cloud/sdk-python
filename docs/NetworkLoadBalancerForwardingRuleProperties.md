# NetworkLoadBalancerForwardingRuleProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A name of that Network Load Balancer forwarding rule |  |
| **algorithm** | **str** | Algorithm for the balancing. |  |
| **protocol** | **str** | Protocol of the balancing. |  |
| **listener_ip** | **str** | Listening IP. (inbound) |  |
| **listener_port** | **int** | Listening port number. (inbound) (range: 1 to 65535) |  |
| **health_check** | [**NetworkLoadBalancerForwardingRuleHealthCheck**](NetworkLoadBalancerForwardingRuleHealthCheck.md) |  | [optional]  |
| **targets** | [**list[NetworkLoadBalancerForwardingRuleTarget]**](NetworkLoadBalancerForwardingRuleTarget.md) | Array of items in that collection |  |


