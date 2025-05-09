# VolumeProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the  resource. | [optional]  |
| **type** | **str** | Hardware type of the volume. DAS (Direct Attached Storage) could be used only in a composite call with a Cube server. | [optional]  |
| **size** | **float** | The size of the volume in GB. | [optional]  |
| **availability_zone** | **str** | The availability zone in which the volume should be provisioned. The storage volume will be provisioned on as few physical storage devices as possible, but this cannot be guaranteed upfront. This is uavailable for DAS (Direct Attached Storage), and subject to availability for SSD. | [optional]  |
| **image** | **str** | Image or snapshot ID to be used as template for this volume. MSSQL Enterprise Images can be used only if the feature toggle for MSSQL Enterprise is enabled on the contract. | [optional]  |
| **image_password** | **str** | Initial password to be set for installed OS. Works with public images only. Not modifiable, forbidden in update requests. Password rules allows all characters from a-z, A-Z, 0-9. | [optional]  |
| **image_alias** | **str** | Image alias of an image to be used as template for this volume. MSSQL Enterprise Images can be used only if the feature toggle for MSSQL Enterprise is enabled on the contract. | [optional]  |
| **ssh_keys** | **list[str]** | Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. | [optional]  |
| **bus** | **str** | The bus type for this volume; default is VIRTIO. | [optional]  |
| **licence_type** | **str** | OS type for this volume. | [optional]  |
| **application_type** | **str** | The type of application that is hosted on this resource.  Only public images can have an Application type different than UNKNOWN. | [optional] [default to 'UNKNOWN'] |
| **cpu_hot_plug** | **bool** | Hot-plug capable CPU (no reboot required). | [optional]  |
| **ram_hot_plug** | **bool** | Hot-plug capable RAM (no reboot required). | [optional]  |
| **nic_hot_plug** | **bool** | Hot-plug capable NIC (no reboot required). | [optional]  |
| **nic_hot_unplug** | **bool** | Hot-unplug capable NIC (no reboot required). | [optional]  |
| **disc_virtio_hot_plug** | **bool** | Hot-plug capable Virt-IO drive (no reboot required). | [optional]  |
| **disc_virtio_hot_unplug** | **bool** | Hot-unplug capable Virt-IO drive (no reboot required). Not supported with Windows VMs. | [optional]  |
| **expose_serial** | **bool** | If set to &#x60;true&#x60; will expose the serial id of the disk attached to the server. If set to &#x60;false&#x60; will not expose the serial id. Some operating systems or software solutions require the serial id to be exposed to work properly. Exposing the serial  can influence licensed software (e.g. Windows) behavior | [optional] [default to False] |
| **require_legacy_bios** | **bool** | Indicates if the image requires the legacy BIOS for compatibility or specific needs. | [optional] [default to True] |
| **device_number** | **int** | The Logical Unit Number of the storage volume. Null for volumes, not mounted to a VM. | [optional] [readonly]  |
| **pci_slot** | **int** | The PCI slot number of the storage volume. Null for volumes, not mounted to a VM. | [optional] [readonly]  |
| **backupunit_id** | **str** | The ID of the backup unit that the user has access to. The property is immutable and is only allowed to be set on creation of a new a volume. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; in conjunction with this property. | [optional]  |
| **user_data** | **str** | The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on creation of a new a volume. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; that has cloud-init compatibility in conjunction with this property. | [optional]  |
| **boot_server** | **str** | The UUID of the attached server. | [optional] [readonly]  |
| **boot_order** | **str** | Determines whether the volume will be used as a boot volume. Set to &#x60;NONE&#x60;, the volume will not be used as boot volume. Set to &#x60;PRIMARY&#x60;, the volume will be used as boot volume and all other volumes must be set to &#x60;NONE&#x60;. Set to &#x60;AUTO&#x60; or &#x60;null&#x60; requires all volumes to be set to &#x60;AUTO&#x60; or &#x60;null&#x60;; this will use the legacy behavior, which is to use the volume as a boot volume only if there are no other volumes or cdrom devices. | [optional] [default to 'AUTO'] |


