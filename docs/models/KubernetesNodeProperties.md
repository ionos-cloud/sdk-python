# KubernetesNodeProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A Kubernetes Node Name. |  |
| **public_ip** | **str** | A valid public IP. | [optional]  |
| **private_ip** | **str** | A valid private IP. | [optional]  |
| **k8s_version** | **str** | The kubernetes version in which a nodepool is running. This imposes restrictions on what kubernetes versions can be run in a cluster&#39;s nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions. |  |


