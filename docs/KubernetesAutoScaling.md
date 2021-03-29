# KubernetesAutoScaling

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **min_node_count** | **int** | The minimum number of worker nodes that the managed node group can scale in. Should be set together with &#39;maxNodeCount&#39;. Value for this attribute must be greater than equal to 1 and less than equal to maxNodeCount. |  |
| **max_node_count** | **int** | The maximum number of worker nodes that the managed node pool can scale-out. Should be set together with &#39;minNodeCount&#39;. Value for this attribute must be greater than equal to 1 and minNodeCount. |  |


