# KubernetesNodePoolPropertiesForPost

## Properties

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **name** | **str** | A Kubernetes Node Pool Name. Valid Kubernetes Node Pool name must be 63 characters or less and must be empty or begin and end with an alphanumeric character \(\[a-z0-9A-Z\]\) with dashes \(-\), underscores \(\_\), dots \(.\), and alphanumerics between. |  |
| **datacenter\_id** | **str** | A valid uuid of the datacenter on which user has access |  |
| **node\_count** | **int** | Number of nodes part of the Node Pool |  |
| **cpu\_family** | **str** | A valid cpu family name |  |
| **cores\_count** | **int** | Number of cores for node |  |
| **ram\_size** | **int** | RAM size for node, minimum size 2048MB is recommended. Ram size must be set to multiple of 1024MB. |  |
| **availability\_zone** | **str** | The availability zone in which the target VM should exist |  |
| **storage\_type** | **str** | Hardware type of the volume |  |
| **storage\_size** | **int** | The size of the volume in GB. The size should be greater than 10GB. |  |
| **k8s\_version** | **str** | The kubernetes version in which a nodepool is running. This imposes restrictions on what kubernetes versions can be run in a cluster's nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions. | \[optional\] |
| **maintenance\_window** | [**KubernetesMaintenanceWindow**](kubernetesmaintenancewindow.md) |  | \[optional\] |
| **auto\_scaling** | [**KubernetesAutoScaling**](kubernetesautoscaling.md) |  | \[optional\] |
| **lans** | [**list\[KubernetesNodePoolLan\]**](kubernetesnodepoollan.md) | array of additional LANs attached to worker nodes | \[optional\] |
| **labels** | **dict\(str, str\)** | map of labels attached to node pool | \[optional\] |
| **annotations** | **dict\(str, str\)** | map of annotations attached to node pool | \[optional\] |
| **public\_ips** | **list\[str\]** | Optional array of reserved public IP addresses to be used by the nodes. IPs must be from same location as the data center used for the node pool. The array must contain one extra IP than maximum number of nodes could be. \(nodeCount+1 if fixed node amount or maxNodeCount+1 if auto scaling is used\) The extra provided IP Will be used during rebuilding of nodes. | \[optional\] |

