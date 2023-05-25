# KubernetesNodeProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **k8s_version** | **str** | The Kubernetes version running in the node pool. Note that this imposes restrictions on which Kubernetes versions can run in the node pools of a cluster. Also, not all Kubernetes versions are suitable upgrade targets for all earlier versions. |  |
| **name** | **str** | The Kubernetes node name. |  |
| **private_ip** | **str** | The private IP associated with the node. | [optional]  |
| **public_ip** | **str** | The public IP associated with the node. | [optional]  |


