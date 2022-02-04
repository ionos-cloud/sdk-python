# NetworkLoadBalancerForwardingRuleTargetHealthCheck

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **check** | **bool** | Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. | [optional]  |
| **check_interval** | **int** | The interval in milliseconds between consecutive health checks; default is 2000. | [optional]  |
| **maintenance** | **bool** | Maintenance mode prevents the target from receiving balanced traffic. | [optional]  |


