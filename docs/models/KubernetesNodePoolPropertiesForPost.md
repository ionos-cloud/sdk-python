# KubernetesNodePoolPropertiesForPost

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **annotations** | **dict(str, str)** | The annotations attached to the node pool. | [optional]  |
| **auto_scaling** | [**KubernetesAutoScaling**](KubernetesAutoScaling.md) |  | [optional]  |
| **availability_zone** | **str** | The availability zone in which the target VM should be provisioned. |  |
| **cores_count** | **int** | The total number of cores for the nodes. |  |
| **cpu_family** | **str** | The CPU type for the nodes. |  |
| **datacenter_id** | **str** | The unique identifier of the VDC where the worker nodes of the node pool are provisioned.Note that the data center is located in the exact place where the parent cluster of the node pool is located. |  |
| **k8s_version** | **str** | The Kubernetes version running in the node pool. Note that this imposes restrictions on which Kubernetes versions can run in the node pools of a cluster. Also, not all Kubernetes versions are suitable upgrade targets for all earlier versions. | [optional]  |
| **labels** | **dict(str, str)** | The labels attached to the node pool. | [optional]  |
| **lans** | [**list[KubernetesNodePoolLan]**](KubernetesNodePoolLan.md) | The array of existing private LANs to attach to worker nodes. | [optional]  |
| **maintenance_window** | [**KubernetesMaintenanceWindow**](KubernetesMaintenanceWindow.md) |  | [optional]  |
| **name** | **str** | A Kubernetes node pool name. Valid Kubernetes node pool name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |  |
| **node_count** | **int** | The number of worker nodes of the node pool. |  |
| **public_ips** | **list[str]** | Optional array of reserved public IP addresses to be used by the nodes. The IPs must be from the exact location of the node pool&#39;s data center. If autoscaling is used, the array must contain one more IP than the maximum possible number of nodes (nodeCount+1 for a fixed number of nodes or maxNodeCount+1). The extra IP is used when the nodes are rebuilt. | [optional]  |
| **ram_size** | **int** | The RAM size for the nodes. Must be specified in multiples of 1024 MB, with a minimum size of 2048 MB. |  |
| **storage_size** | **int** | The allocated volume size in GB. The allocated volume size in GB. To achieve good performance, we recommend a size greater than 100GB for SSD. |  |
| **storage_type** | **str** | The storage type for the nodes. |  |


