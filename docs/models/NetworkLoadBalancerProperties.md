# NetworkLoadBalancerProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **ips** | **list[str]** | Collection of the Network Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan must be customer-reserved IPs for public Load Balancers, and private IPs for private Load Balancers. | [optional]  |
| **lb_private_ips** | **list[str]** | Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain a valid subnet mask. If no IP is provided, the system will generate an IP with /24 subnet. | [optional]  |
| **listener_lan** | **int** | ID of the listening LAN (inbound). |  |
| **name** | **str** | The name of the Network Load Balancer. |  |
| **target_lan** | **int** | ID of the balanced private target LAN (outbound). |  |


