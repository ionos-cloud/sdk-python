# VolumeProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the  resource. | [optional]  |
| **type** | **str** | Hardware type of the volume. DAS (Direct Attached Storage) could be used only in a composite call with a Cube server. | [optional]  |
| **size** | **float** | The size of the volume in GB. |  |
| **availability_zone** | **str** | The availability zone in which the volume should be provisioned. The storage volume will be provisioned on as few physical storage devices as possible, but this cannot be guaranteed upfront. This is uavailable for DAS (Direct Attached Storage), and subject to availability for SSD. | [optional]  |
| **image** | **str** | Image or snapshot ID to be used as template for this volume. | [optional]  |
| **image_password** | **str** | Initial password to be set for installed OS. Works with public images only. Not modifiable, forbidden in update requests. Password rules allows all characters from a-z, A-Z, 0-9. | [optional]  |
| **image_alias** | **str** |  | [optional]  |
| **ssh_keys** | **list[str]** | Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. | [optional]  |
| **bus** | **str** | The bus type for this volume; default is VIRTIO. | [optional]  |
| **licence_type** | **str** | OS type for this volume. | [optional] [readonly]  |
| **cpu_hot_plug** | **bool** | Hot-plug capable CPU (no reboot required). | [optional]  |
| **ram_hot_plug** | **bool** | Hot-plug capable RAM (no reboot required). | [optional]  |
| **nic_hot_plug** | **bool** | Hot-plug capable NIC (no reboot required). | [optional]  |
| **nic_hot_unplug** | **bool** | Hot-unplug capable NIC (no reboot required). | [optional]  |
| **disc_virtio_hot_plug** | **bool** | Hot-plug capable Virt-IO drive (no reboot required). | [optional]  |
| **disc_virtio_hot_unplug** | **bool** | Hot-unplug capable Virt-IO drive (no reboot required). Not supported with Windows VMs. | [optional]  |
| **device_number** | **int** | The Logical Unit Number of the storage volume. Null for volumes, not mounted to a VM. | [optional] [readonly]  |
| **pci_slot** | **int** | The PCI slot number of the storage volume. Null for volumes, not mounted to a VM. | [optional] [readonly]  |
| **backupunit_id** | **str** | The ID of the backup unit that the user has access to. The property is immutable and is only allowed to be set on creation of a new a volume. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; in conjunction with this property. | [optional]  |
| **user_data** | **str** | The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on creation of a new a volume. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; that has cloud-init compatibility in conjunction with this property. | [optional]  |
| **boot_server** | **str** | The UUID of the attached server. | [optional] [readonly]  |


