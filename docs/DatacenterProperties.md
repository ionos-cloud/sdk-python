# DatacenterProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A name of that resource | [optional]  |
| **description** | **str** | A description for the datacenter, e.g. staging, production | [optional]  |
| **location** | **str** | The physical location where the datacenter will be created. This will be where all of your servers live. Property cannot be modified after datacenter creation (disallowed in update requests) |  |
| **version** | **int** | The version of that Data Center. Gets incremented with every change | [optional] [readonly]  |
| **features** | **list[str]** | List of features supported by the location this data center is part of | [optional] [readonly]  |
| **sec_auth_protection** | **bool** | Boolean value representing if the data center requires extra protection e.g. two factor protection | [optional]  |
| **cpu_architecture** | [**list[CpuArchitectureProperties]**](CpuArchitectureProperties.md) | Array of features and CPU families available in a location | [optional] [readonly]  |


