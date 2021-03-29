# NetworkLoadBalancerProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A name of that Network Load Balancer |  |
| **listener_lan** | **int** | Id of the listening LAN. (inbound) |  |
| **ips** | **list[str]** | Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer. | [optional]  |
| **target_lan** | **int** | Id of the balanced private target LAN. (outbound) |  |
| **lb_private_ips** | **list[str]** | Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet. | [optional]  |


