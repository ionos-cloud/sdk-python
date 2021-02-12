# ServerProperties

## Properties
| Name | Type | Description | Notes |
------------ | ------------- | ------------- | -------------
| **name** | **str** | A name of that resource | [optional] 
**cores** | **int** | The total number of cores for the server | 
**ram** | **int** | The amount of memory for the server in MB, e.g. 2048. Size must be specified in multiples of 256 MB with a minimum of 256 MB; however, if you set ramHotPlug to TRUE then you must use a minimum of 1024 MB. If you set the RAM size more than 240GB, then ramHotPlug will be set to FALSE and can not be set to TRUE unless RAM size not set to less than 240GB. | 
**availability_zone** | **str** | The availability zone in which the server should exist | [optional] 
**vm_state** | **str** | Status of the virtual Machine | [optional] [readonly] 
**boot_cdrom** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**boot_volume** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**cpu_family** | **str** | Cpu family of pserver | [optional] 
 |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


