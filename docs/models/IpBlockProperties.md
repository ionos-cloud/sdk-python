# IpBlockProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **ips** | **list[str]** | Collection of IPs, associated with the IP Block. | [optional] [readonly]  |
| **location** | **str** | Location of that IP block. Property cannot be modified after it is created (disallowed in update requests). |  |
| **size** | **int** | The size of the IP block. |  |
| **name** | **str** | The name of the  resource. | [optional]  |
| **ip_consumers** | [**list[IpConsumer]**](IpConsumer.md) | Read-Only attribute. Lists consumption detail for an individual IP | [optional] [readonly]  |


