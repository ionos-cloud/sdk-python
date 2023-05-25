# KubernetesNodePoolLan

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **datacenter_id** | **str** | The datacenter ID, requires system privileges, for internal usage only | [optional]  |
| **dhcp** | **bool** | Specifies whether the Kubernetes node pool LAN reserves an IP with DHCP. | [optional]  |
| **id** | **int** | The LAN ID of an existing LAN at the related data center |  |
| **routes** | [**list[KubernetesNodePoolLanRoutes]**](KubernetesNodePoolLanRoutes.md) | The array of additional LANs attached to worker nodes. | [optional]  |


