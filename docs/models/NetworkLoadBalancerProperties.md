# NetworkLoadBalancerProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the Network Load Balancer. |  |
| **listener_lan** | **int** | ID of the listening LAN (inbound). |  |
| **ips** | **list[str]** | Collection of the Network Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan must be customer-reserved IPs for public Load Balancers, and private IPs for private Load Balancers. | [optional]  |
| **target_lan** | **int** | ID of the balanced private target LAN (outbound). |  |
| **lb_private_ips** | **list[str]** | Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain a valid subnet mask. If no IP is provided, the system will generate an IP with /24 subnet. | [optional]  |


