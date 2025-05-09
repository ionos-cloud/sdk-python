# KubernetesNodePoolLan

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **int** | The LAN ID of an existing LAN at the related data center |  |
| **dhcp** | **bool** | Specifies whether the Kubernetes node pool LAN reserves an IP with DHCP. | [optional]  |
| **routes** | [**list[KubernetesNodePoolLanRoutes]**](KubernetesNodePoolLanRoutes.md) | The array of additional LANs attached to worker nodes. | [optional]  |


