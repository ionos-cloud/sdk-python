# ServerProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **availability_zone** | **str** | The availability zone in which the server should be provisioned. | [optional]  |
| **boot_cdrom** | [**ResourceReference**](ResourceReference.md) |  | [optional]  |
| **boot_volume** | [**ResourceReference**](ResourceReference.md) |  | [optional]  |
| **cores** | **int** | The total number of cores for the enterprise server. | [optional]  |
| **cpu_family** | **str** | CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource; must not be provided for CUBE servers. | [optional]  |
| **name** | **str** | The name of the  resource. | [optional]  |
| **ram** | **int** | The memory size for the enterprise server in MB, such as 2048. Size must be specified in multiples of 256 MB with a minimum of 256 MB; however, if you set ramHotPlug to TRUE then you must use a minimum of 1024 MB. If you set the RAM size more than 240GB, then ramHotPlug will be set to FALSE and can not be set to TRUE unless RAM size not set to less than 240GB. | [optional]  |
| **template_uuid** | **str** | The ID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource. | [optional]  |
| **type** | **str** | Server type: CUBE or ENTERPRISE. | [optional]  |
| **vm_state** | **str** | Status of the virtual machine. | [optional] [readonly]  |


