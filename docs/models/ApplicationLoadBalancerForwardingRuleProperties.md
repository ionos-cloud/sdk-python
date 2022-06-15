# ApplicationLoadBalancerForwardingRuleProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the Application Load Balancer forwarding rule. |  |
| **protocol** | **str** | Balancing protocol |  |
| **listener_ip** | **str** | Listening (inbound) IP |  |
| **listener_port** | **int** | Listening (inbound) port number; valid range is 1 to 65535. |  |
| **client_timeout** | **int** | The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds). | [optional]  |
| **server_certificates** | **list[str]** | Array of items in the collection. | [optional]  |
| **http_rules** | [**list[ApplicationLoadBalancerHttpRule]**](ApplicationLoadBalancerHttpRule.md) | An array of items in the collection. The original order of rules is perserved during processing, except for Forward-type rules are processed after the rules with other action defined. The relative order of Forward-type rules is also preserved during the processing. | [optional]  |


