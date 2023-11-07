# KubernetesClusterPropertiesForPost

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **api_subnet_allow_list** | **list[str]** | Access to the K8s API server is restricted to these CIDRs. Intra-cluster traffic is not affected by this restriction. If no AllowList is specified, access is not limited. If an IP is specified without a subnet mask, the default value is 32 for IPv4 and 128 for IPv6. | [optional]  |
| **k8s_version** | **str** | The Kubernetes version that the cluster is running. This limits which Kubernetes versions can run in a cluster&#39;s node pools. Also, not all Kubernetes versions are suitable upgrade targets for all earlier versions. | [optional]  |
| **location** | **str** | This attribute is mandatory if the cluster is private. The location must be enabled for your contract, or you must have a data center at that location. This property is not adjustable. | [optional]  |
| **maintenance_window** | [**KubernetesMaintenanceWindow**](KubernetesMaintenanceWindow.md) |  | [optional]  |
| **name** | **str** | A Kubernetes cluster name. Valid Kubernetes cluster name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. |  |
| **nat_gateway_ip** | **str** | The nat gateway IP of the cluster if the cluster is private. This property is immutable. Must be a reserved IP in the same location as the cluster&#39;s location. This attribute is mandatory if the cluster is private. | [optional]  |
| **node_subnet** | **str** | The node subnet of the cluster, if the cluster is private. This property is optional and immutable. Must be a valid CIDR notation for an IPv4 network prefix of 16 bits length. | [optional]  |
| **public** | **bool** | The indicator whether the cluster is public or private. Note that the status FALSE is still in the beta phase. | [optional] [default to True] |
| **s3_buckets** | [**list[S3Bucket]**](S3Bucket.md) | List of S3 buckets configured for K8s usage. At the moment, it contains only one S3 bucket that is used to store K8s API audit logs. | [optional]  |


