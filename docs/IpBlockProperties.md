# IpBlockProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **ips** | **list[str]** | A collection of IPs associated with the IP Block | [optional] [readonly]  |
| **location** | **str** | Location of that IP Block. Property cannot be modified after creation (disallowed in update requests) |  |
| **size** | **int** | The size of the IP block |  |
| **name** | **str** | A name of that resource | [optional]  |
| **ip_consumers** | [**list[IpConsumer]**](IpConsumer.md) | Read-Only attribute. Lists consumption detail of an individual ip | [optional] [readonly]  |


