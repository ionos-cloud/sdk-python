# NatGatewayRuleProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the NAT Gateway rule. |  |
| **type** | [**NatGatewayRuleType**](NatGatewayRuleType.md) | Type of the NAT Gateway rule. | [optional]  |
| **protocol** | [**NatGatewayRuleProtocol**](NatGatewayRuleProtocol.md) | Protocol of the NAT Gateway rule. Defaults to ALL. If protocol is &#39;ICMP&#39; then targetPortRange start and end cannot be set. | [optional]  |
| **source_subnet** | **str** | Source subnet of the NAT Gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address. |  |
| **public_ip** | **str** | Public IP address of the NAT Gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT Gateway resource |  |
| **target_subnet** | **str** | Target or destination subnet of the NAT Gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address. | [optional]  |
| **target_port_range** | [**TargetPortRange**](TargetPortRange.md) |  | [optional]  |


