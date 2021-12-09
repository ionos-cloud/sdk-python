# KubernetesNodeProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A Kubernetes node name. |  |
| **public_ip** | **str** | A valid public IP. | [optional]  |
| **private_ip** | **str** | A valid private IP. | [optional]  |
| **k8s_version** | **str** | The Kubernetes version the nodepool is running. This imposes restrictions on what Kubernetes versions can be run in a cluster&#39;s nodepools. Additionally, not all Kubernetes versions are viable upgrade targets for all prior versions. |  |


