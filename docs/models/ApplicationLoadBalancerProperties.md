# ApplicationLoadBalancerProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The Application Load Balancer name. |  |
| **listener_lan** | **int** | The ID of the listening (inbound) LAN. |  |
| **ips** | **list[str]** | Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the &#39;listenerLan&#39; are customer-reserved public IPs for the public load balancers, and private IPs for the private load balancers. | [optional]  |
| **target_lan** | **int** | The ID of the balanced private target LAN (outbound). |  |
| **lb_private_ips** | **list[str]** | Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet. | [optional]  |
| **central_logging** | **bool** | Turn logging on and off for this product. Default value is &#39;false&#39;. | [optional]  |
| **logging_format** | **str** | Specifies the format of the logs. | [optional]  |


