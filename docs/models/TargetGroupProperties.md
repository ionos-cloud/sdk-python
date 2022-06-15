# TargetGroupProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the target group. |  |
| **algorithm** | **str** | Balancing algorithm |  |
| **protocol** | **str** | Balancing protocol |  |
| **targets** | [**list[TargetGroupTarget]**](TargetGroupTarget.md) | Array of items in the collection. | [optional]  |
| **health_check** | [**TargetGroupHealthCheck**](TargetGroupHealthCheck.md) |  | [optional]  |
| **http_health_check** | [**TargetGroupHttpHealthCheck**](TargetGroupHttpHealthCheck.md) |  | [optional]  |


