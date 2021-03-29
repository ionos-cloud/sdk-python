# NetworkLoadBalancerForwardingRuleTargetHealthCheck

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **check** | **bool** | Check specifies whether the target VM&#39;s health is checked. If turned off, a target VM is always considered available. If turned on, the target VM is available when accepting periodic TCP connections, to ensure that it is really able to serve requests. The address and port to send the tests to are those of the target VM. The health check only consists of a connection attempt. | [optional]  |
| **check_interval** | **int** | CheckInterval determines the duration (in milliseconds) between consecutive health checks. If unspecified a default of 2000 ms is used. | [optional]  |
| **maintenance** | **bool** | Maintenance specifies if a target VM should be marked as down, even if it is not. | [optional]  |


