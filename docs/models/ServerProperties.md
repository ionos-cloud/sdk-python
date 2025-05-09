# ServerProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **template_uuid** | **str** | The ID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource. | [optional]  |
| **name** | **str** | The name of the  resource. | [optional]  |
| **hostname** | **str** | The hostname of the  resource. Allowed characters are a-z, 0-9 and - (minus). Hostname should not start with minus and should not be longer than 63 characters. | [optional]  |
| **cores** | **int** | The total number of cores for the enterprise server. | [optional]  |
| **ram** | **int** | The memory size for the enterprise server in MB, such as 2048. Size must be specified in multiples of 256 MB with a minimum of 256 MB; however, if you set ramHotPlug to TRUE then you must use a minimum of 1024 MB. If you set the RAM size more than 240GB, then ramHotPlug will be set to FALSE and can not be set to TRUE unless RAM size not set to less than 240GB. | [optional]  |
| **availability_zone** | **str** | The availability zone in which the server should be provisioned. | [optional]  |
| **vm_state** | **str** | Status of the virtual machine. | [optional] [readonly]  |
| **boot_cdrom** | [**ResourceReference**](ResourceReference.md) |  | [optional]  |
| **boot_volume** | [**ResourceReference**](ResourceReference.md) |  | [optional]  |
| **cpu_family** | **str** | CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource; must not be provided for CUBE and VCPU servers. | [optional]  |
| **type** | **str** | Server type: CUBE, ENTERPRISE or VCPU. | [optional]  |
| **nic_multi_queue** | **bool** | Activate or deactivate the Multi Queue feature on all NICs of this server. This feature is beneficial to  enable when the NICs are experiencing performance issues (e.g. low throughput). Toggling this feature will also initiate a restart of the server. If the specified value is &#x60;true&#x60;, the feature will  be activated; if it is not specified or set to &#x60;false&#x60;, the feature will be deactivated. It is not allowed for servers of type Cube. | [optional] [default to False] |


