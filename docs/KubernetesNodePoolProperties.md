# KubernetesNodePoolProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A Kubernetes Node Pool Name. Valid Kubernetes Node Pool name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |  |
| **datacenter_id** | **str** | A valid uuid of the datacenter on which user has access |  |
| **node_count** | **int** | Number of nodes part of the Node Pool |  |
| **cpu_family** | **str** | A valid cpu family name |  |
| **cores_count** | **int** | Number of cores for node |  |
| **ram_size** | **int** | RAM size for node, minimum size is 2048MB. Ram size must be set to multiple of 1024MB. |  |
| **availability_zone** | **str** | The availability zone in which the target VM should exist |  |
| **storage_type** | **str** | Hardware type of the volume |  |
| **storage_size** | **int** | The size of the volume in GB. The size should be greater than 10GB. |  |
| **k8s_version** | **str** | The kubernetes version in which a nodepool is running. This imposes restrictions on what kubernetes versions can be run in a cluster&#39;s nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions. | [optional]  |
| **maintenance_window** | [**KubernetesMaintenanceWindow**](KubernetesMaintenanceWindow.md) |  | [optional]  |
| **auto_scaling** | [**KubernetesAutoScaling**](KubernetesAutoScaling.md) |  | [optional]  |
| **lans** | [**list[KubernetesNodePoolLan]**](KubernetesNodePoolLan.md) | array of additional LANs attached to worker nodes | [optional]  |
| **labels** | **dict(str, str)** | map of labels attached to node pool | [optional]  |
| **annotations** | **dict(str, str)** | map of annotations attached to node pool | [optional]  |
| **public_ips** | **list[str]** | Optional array of reserved public IP addresses to be used by the nodes. IPs must be from same location as the data center used for the node pool. The array must contain one extra IP than maximum number of nodes could be. (nodeCount+1 if fixed node amount or maxNodeCount+1 if auto scaling is used) The extra provided IP Will be used during rebuilding of nodes. | [optional]  |
| **available_upgrade_versions** | **list[str]** | List of available versions for upgrading the node pool | [optional]  |


