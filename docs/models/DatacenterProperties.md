# DatacenterProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **cpu_architecture** | [**list[CpuArchitectureProperties]**](CpuArchitectureProperties.md) | Array of features and CPU families available in a location | [optional] [readonly]  |
| **description** | **str** | A description for the datacenter, such as staging, production. | [optional]  |
| **features** | **list[str]** | List of features supported by the location where this data center is provisioned. | [optional] [readonly]  |
| **location** | **str** | The physical location where the datacenter will be created. This will be where all of your servers live. Property cannot be modified after datacenter creation (disallowed in update requests). |  |
| **name** | **str** | The name of the  resource. | [optional]  |
| **sec_auth_protection** | **bool** | Boolean value representing if the data center requires extra protection, such as two-step verification. | [optional]  |
| **version** | **int** | The version of the data center; incremented with every change. | [optional] [readonly]  |


