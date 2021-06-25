# ImageProperties

## Properties

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **name** | **str** | A name of that resource | \[optional\] |
| **description** | **str** | Human readable description | \[optional\] |
| **location** | **str** | Location of that image/snapshot. | \[optional\] \[readonly\] |
| **size** | **float** | The size of the image in GB | \[optional\] \[readonly\] |
| **cpu\_hot\_plug** | **bool** | Is capable of CPU hot plug \(no reboot required\) | \[optional\] |
| **cpu\_hot\_unplug** | **bool** | Is capable of CPU hot unplug \(no reboot required\) | \[optional\] |
| **ram\_hot\_plug** | **bool** | Is capable of memory hot plug \(no reboot required\) | \[optional\] |
| **ram\_hot\_unplug** | **bool** | Is capable of memory hot unplug \(no reboot required\) | \[optional\] |
| **nic\_hot\_plug** | **bool** | Is capable of nic hot plug \(no reboot required\) | \[optional\] |
| **nic\_hot\_unplug** | **bool** | Is capable of nic hot unplug \(no reboot required\) | \[optional\] |
| **disc\_virtio\_hot\_plug** | **bool** | Is capable of Virt-IO drive hot plug \(no reboot required\) | \[optional\] |
| **disc\_virtio\_hot\_unplug** | **bool** | Is capable of Virt-IO drive hot unplug \(no reboot required\). This works only for non-Windows virtual Machines. | \[optional\] |
| **disc\_scsi\_hot\_plug** | **bool** | Is capable of SCSI drive hot plug \(no reboot required\) | \[optional\] |
| **disc\_scsi\_hot\_unplug** | **bool** | Is capable of SCSI drive hot unplug \(no reboot required\). This works only for non-Windows virtual Machines. | \[optional\] |
| **licence\_type** | **str** | OS type of this Image |  |
| **image\_type** | **str** | This indicates the type of image | \[optional\] \[readonly\] |
| **public** | **bool** | Indicates if the image is part of the public repository or not | \[optional\] \[readonly\] |
| **image\_aliases** | **list\[str\]** | List of image aliases mapped for this Image | \[optional\] \[readonly\] |
| **cloud\_init** | **str** | Cloud init compatibility | \[optional\] |

