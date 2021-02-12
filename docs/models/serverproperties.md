# ServerProperties

## Properties

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **name** | **str** | A name of that resource | \[optional\] |
| **cores** | **int** | The total number of cores for the server |  |
| **ram** | **int** | The amount of memory for the server in MB, e.g. 2048. Size must be specified in multiples of 256 MB with a minimum of 256 MB; however, if you set ramHotPlug to TRUE then you must use a minimum of 1024 MB. If you set the RAM size more than 240GB, then ramHotPlug will be set to FALSE and can not be set to TRUE unless RAM size not set to less than 240GB. |  |
| **availability\_zone** | **str** | The availability zone in which the server should exist | \[optional\] |
| **vm\_state** | **str** | Status of the virtual Machine | \[optional\] \[readonly\] |
| **boot\_cdrom** | [**ResourceReference**](resourcereference.md) |  | \[optional\] |
| **boot\_volume** | [**ResourceReference**](resourcereference.md) |  | \[optional\] |
| **cpu\_family** | **str** | Cpu family of pserver | \[optional\] |

