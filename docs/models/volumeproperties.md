# VolumeProperties

## Properties

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **name** | **str** | A name of that resource | \[optional\] |
| **type** | **str** | Hardware type of the volume. | \[optional\] |
| **size** | **float** | The size of the volume in GB |  |
| **availability\_zone** | **str** | The availability zone in which the volume should exist. The storage volume will be provisioned on as less physical storages as possible but cannot guarantee upfront | \[optional\] |
| **image** | **str** | Image or snapshot ID to be used as template for this volume | \[optional\] |
| **image\_password** | **str** | Initial password to be set for installed OS. Works with public images only. Not modifiable, forbidden in update requests. Password rules allows all characters from a-z, A-Z, 0-9 | \[optional\] |
| **image\_alias** | **str** |  | \[optional\] |
| **ssh\_keys** | **list\[str\]** | Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. | \[optional\] |
| **bus** | **str** | The bus type of the volume. Default is VIRTIO | \[optional\] |
| **licence\_type** | **str** | OS type of this volume | \[optional\] \[readonly\] |
| **cpu\_hot\_plug** | **bool** | Is capable of CPU hot plug \(no reboot required\) | \[optional\] |
| **ram\_hot\_plug** | **bool** | Is capable of memory hot plug \(no reboot required\) | \[optional\] |
| **nic\_hot\_plug** | **bool** | Is capable of nic hot plug \(no reboot required\) | \[optional\] |
| **nic\_hot\_unplug** | **bool** | Is capable of nic hot unplug \(no reboot required\) | \[optional\] |
| **disc\_virtio\_hot\_plug** | **bool** | Is capable of Virt-IO drive hot plug \(no reboot required\) | \[optional\] |
| **disc\_virtio\_hot\_unplug** | **bool** | Is capable of Virt-IO drive hot unplug \(no reboot required\). This works only for non-Windows virtual Machines. | \[optional\] |
| **device\_number** | **int** | The LUN ID of the storage volume. Null for volumes not mounted to any VM | \[optional\] \[readonly\] |
| **backupunit\_id** | **str** | The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property. | \[optional\] |
| **user\_data** | **str** | The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' that has cloud-init compatibility in conjunction with this property. | \[optional\] |

