# ImageProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **cloud_init** | **str** | Cloud init compatibility. | [optional]  |
| **cpu_hot_plug** | **bool** | Hot-plug capable CPU (no reboot required). | [optional]  |
| **cpu_hot_unplug** | **bool** | Hot-unplug capable CPU (no reboot required). | [optional]  |
| **description** | **str** | Human-readable description. | [optional]  |
| **disc_scsi_hot_plug** | **bool** | Hot-plug capable SCSI drive (no reboot required). | [optional]  |
| **disc_scsi_hot_unplug** | **bool** | Hot-unplug capable SCSI drive (no reboot required). Not supported with Windows VMs. | [optional]  |
| **disc_virtio_hot_plug** | **bool** | Hot-plug capable Virt-IO drive (no reboot required). | [optional]  |
| **disc_virtio_hot_unplug** | **bool** | Hot-unplug capable Virt-IO drive (no reboot required). Not supported with Windows VMs. | [optional]  |
| **image_aliases** | **list[str]** | List of image aliases mapped for this image | [optional] [readonly]  |
| **image_type** | **str** | The image type. | [optional] [readonly]  |
| **licence_type** | **str** | The OS type of this image. |  |
| **location** | **str** | The location of this image/snapshot. | [optional] [readonly]  |
| **name** | **str** | The resource name. | [optional]  |
| **nic_hot_plug** | **bool** | Hot-plug capable NIC (no reboot required). | [optional]  |
| **nic_hot_unplug** | **bool** | Hot-unplug capable NIC (no reboot required). | [optional]  |
| **public** | **bool** | Indicates whether the image is part of a public repository. | [optional] [readonly]  |
| **ram_hot_plug** | **bool** | Hot-plug capable RAM (no reboot required). | [optional]  |
| **ram_hot_unplug** | **bool** | Hot-unplug capable RAM (no reboot required). | [optional]  |
| **size** | **float** | The image size in GB. | [optional] [readonly]  |


