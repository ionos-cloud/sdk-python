# KubernetesClusterPropertiesForPostAndPut

## Properties

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **name** | **str** | A Kubernetes Cluster Name |  |
| **k8s\_version** | **str** | The kubernetes version in which a cluster is running. This imposes restrictions on what kubernetes versions can be run in a cluster's nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions. | \[optional\] |
| **maintenance\_window** | [**KubernetesMaintenanceWindow**](kubernetesmaintenancewindow.md) |  | \[optional\] |

