# LoadbalancerProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A name of that resource | [optional]  |
| **ip** | **str** | IPv4 address of the loadbalancer. All attached NICs will inherit this IP. Leaving value null will assign IP automatically | [optional]  |
| **dhcp** | **bool** | Indicates if the loadbalancer will reserve an IP using DHCP | [optional]  |


