# ApplicationLoadBalancerProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the Application Load Balancer. |  |
| **listener_lan** | **int** | ID of the listening (inbound) LAN. |  |
| **ips** | **list[str]** | Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers. | [optional]  |
| **target_lan** | **int** | ID of the balanced private target LAN (outbound). |  |
| **lb_private_ips** | **list[str]** | Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet. | [optional]  |


