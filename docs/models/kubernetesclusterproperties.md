# KubernetesClusterProperties

## Properties

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **name** | **str** | A Kubernetes Cluster Name. Valid Kubernetes Cluster name must be 63 characters or less and must be empty or begin and end with an alphanumeric character \(\[a-z0-9A-Z\]\) with dashes \(-\), underscores \(\_\), dots \(.\), and alphanumerics between. |  |
| **k8s\_version** | **str** | The kubernetes version in which a cluster is running. This imposes restrictions on what kubernetes versions can be run in a cluster's nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions. | \[optional\] |
| **maintenance\_window** | [**KubernetesMaintenanceWindow**](kubernetesmaintenancewindow.md) |  | \[optional\] |
| **available\_upgrade\_versions** | **list\[str\]** | List of available versions for upgrading the cluster | \[optional\] |
| **viable\_node\_pool\_versions** | **list\[str\]** | List of versions that may be used for node pools under this cluster | \[optional\] |
| **public** | **bool** | The indicator if the cluster is public or private. Be aware that setting it to false is currently in beta phase. | \[optional\] \[default to True\] |
| **gateway\_ip** | **str** | The IP address of the gateway used by the cluster. This is mandatory when \`public\` is set to \`false\` and should not be provided otherwise. | \[optional\] |

