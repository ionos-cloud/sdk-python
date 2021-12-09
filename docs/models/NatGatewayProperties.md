# NatGatewayProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | Name of the NAT Gateway. |  |
| **public_ips** | **list[str]** | Collection of public IP addresses of the NAT Gateway. Should be customer reserved IP addresses in that location. |  |
| **lans** | [**list[NatGatewayLanProperties]**](NatGatewayLanProperties.md) | Collection of LANs connected to the NAT Gateway. IPs must contain valid subnet mask. If user will not provide any IP then system will generate an IP with /24 subnet. | [optional]  |


