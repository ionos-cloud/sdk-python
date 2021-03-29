# NetworkLoadBalancerForwardingRuleHealthCheck

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **client_timeout** | **int** | ClientTimeout is expressed in milliseconds. This inactivity timeout applies when the client is expected to acknowledge or send data. If unset the default of 50 seconds will be used. | [optional]  |
| **check_timeout** | **int** | It specifies the time (in milliseconds) for a target VM in this pool to answer the check. If a target VM has CheckInterval set and CheckTimeout is set too, then the smaller value of the two is used after the TCP connection is established. | [optional]  |
| **connect_timeout** | **int** | It specifies the maximum time (in milliseconds) to wait for a connection attempt to a target VM to succeed. If unset, the default of 5 seconds will be used. | [optional]  |
| **target_timeout** | **int** | TargetTimeout specifies the maximum inactivity time (in milliseconds) on the target VM side. If unset, the default of 50 seconds will be used. | [optional]  |
| **retries** | **int** | Retries specifies the number of retries to perform on a target VM after a connection failure. If unset, the default value of 3 will be used. (valid range: [0, 65535]) | [optional]  |


