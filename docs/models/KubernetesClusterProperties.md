# KubernetesClusterProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A Kubernetes Cluster Name. Valid Kubernetes Cluster name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |  |
| **k8s_version** | **str** | The kubernetes version in which a cluster is running. This imposes restrictions on what kubernetes versions can be run in a cluster&#39;s nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions. | [optional]  |
| **maintenance_window** | [**KubernetesMaintenanceWindow**](KubernetesMaintenanceWindow.md) |  | [optional]  |
| **available_upgrade_versions** | **list[str]** | List of available versions for upgrading the cluster | [optional]  |
| **viable_node_pool_versions** | **list[str]** | List of versions that may be used for node pools under this cluster | [optional]  |
| **api_subnet_allow_list** | **list[str]** | Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6. | [optional]  |
| **s3_buckets** | [**list[S3Bucket]**](S3Bucket.md) | List of S3 bucket configured for K8s usage. For now it contains only one S3 bucket used to store K8s API audit logs | [optional]  |

