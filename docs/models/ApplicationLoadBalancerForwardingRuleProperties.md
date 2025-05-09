# ApplicationLoadBalancerForwardingRuleProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the Application Load Balancer forwarding rule. |  |
| **protocol** | **str** | The balancing protocol. |  |
| **listener_ip** | **str** | The listening (inbound) IP. |  |
| **listener_port** | **int** | The listening (inbound) port number; the valid range is 1 to 65535. |  |
| **client_timeout** | **int** | The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds). | [optional]  |
| **server_certificates** | **list[str]** | Array of items in the collection. | [optional]  |
| **http_rules** | [**list[ApplicationLoadBalancerHttpRule]**](ApplicationLoadBalancerHttpRule.md) | An array of items in the collection. The original order of rules is preserved during processing, except that rules of the &#39;FORWARD&#39; type are processed after the rules with other defined actions. The relative order of the &#39;FORWARD&#39; type rules is also preserved during the processing. | [optional]  |


