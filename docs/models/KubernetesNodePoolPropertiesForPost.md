# KubernetesNodePoolPropertiesForPost

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A Kubernetes node pool name. Valid Kubernetes node pool name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |  |
| **datacenter_id** | **str** | A valid ID of the data center, to which the user has access. |  |
| **node_count** | **int** | The number of nodes that make up the node pool. |  |
| **cpu_family** | **str** | A valid CPU family name. |  |
| **cores_count** | **int** | The number of cores for the node. |  |
| **ram_size** | **int** | The RAM size for the node. Must be set in multiples of 1024 MB, with minimum size is of 2048 MB. |  |
| **availability_zone** | **str** | The availability zone in which the target VM should be provisioned. |  |
| **storage_type** | **str** | The type of hardware for the volume. |  |
| **storage_size** | **int** | The size of the volume in GB. The size should be greater than 10GB. |  |
| **k8s_version** | **str** | The Kubernetes version the nodepool is running. This imposes restrictions on what Kubernetes versions can be run in a cluster&#39;s nodepools. Additionally, not all Kubernetes versions are viable upgrade targets for all prior versions. | [optional]  |
| **maintenance_window** | [**KubernetesMaintenanceWindow**](KubernetesMaintenanceWindow.md) |  | [optional]  |
| **auto_scaling** | [**KubernetesAutoScaling**](KubernetesAutoScaling.md) |  | [optional]  |
| **lans** | [**list[KubernetesNodePoolLan]**](KubernetesNodePoolLan.md) | array of additional LANs attached to worker nodes | [optional]  |
| **labels** | **dict(str, str)** | map of labels attached to node pool. | [optional]  |
| **annotations** | **dict(str, str)** | map of annotations attached to node pool. | [optional]  |
| **public_ips** | **list[str]** | Optional array of reserved public IP addresses to be used by the nodes. IPs must be from same location as the data center used for the node pool. The array must contain one more IP than the maximum possible number of nodes (nodeCount+1 for fixed number of nodes or maxNodeCount+1 when auto scaling is used). The extra IP is used when the nodes are rebuilt. | [optional]  |


