# ImageProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The resource name. | [optional]  |
| **description** | **str** | Human-readable description. | [optional]  |
| **location** | **str** | The location of this image/snapshot. | [optional] [readonly]  |
| **size** | **float** | The image size in GB. | [optional] [readonly]  |
| **cpu_hot_plug** | **bool** | Hot-plug capable CPU (no reboot required). | [optional]  |
| **cpu_hot_unplug** | **bool** | Hot-unplug capable CPU (no reboot required). | [optional]  |
| **ram_hot_plug** | **bool** | Hot-plug capable RAM (no reboot required). | [optional]  |
| **ram_hot_unplug** | **bool** | Hot-unplug capable RAM (no reboot required). | [optional]  |
| **nic_hot_plug** | **bool** | Hot-plug capable NIC (no reboot required). | [optional]  |
| **nic_hot_unplug** | **bool** | Hot-unplug capable NIC (no reboot required). | [optional]  |
| **disc_virtio_hot_plug** | **bool** | Hot-plug capable Virt-IO drive (no reboot required). | [optional]  |
| **disc_virtio_hot_unplug** | **bool** | Hot-unplug capable Virt-IO drive (no reboot required). Not supported with Windows VMs. | [optional]  |
| **disc_scsi_hot_plug** | **bool** | Hot-plug capable SCSI drive (no reboot required). | [optional]  |
| **disc_scsi_hot_unplug** | **bool** | Hot-unplug capable SCSI drive (no reboot required). Not supported with Windows VMs. | [optional]  |
| **expose_serial** | **bool** | If set to &#x60;true&#x60; will expose the serial id of the disk attached to the server. If set to &#x60;false&#x60; will not expose the serial id. Some operating systems or software solutions require the serial id to be exposed to work properly. Exposing the serial  can influence licensed software (e.g. Windows) behavior | [optional] [default to False] |
| **require_legacy_bios** | **bool** | Indicates if the image requires the legacy BIOS for compatibility or specific needs. | [optional] [default to True] |
| **licence_type** | **str** | The OS type of this image. |  |
| **application_type** | **str** | The type of application that is hosted on this resource.  Only public images can have an Application type different than UNKNOWN. | [optional] [default to 'UNKNOWN'] |
| **image_type** | **str** | The image type. | [optional] [readonly]  |
| **public** | **bool** | Indicates whether the image is part of a public repository. | [optional] [readonly]  |
| **image_aliases** | **list[str]** | List of image aliases mapped for this image | [optional] [readonly]  |
| **cloud_init** | **str** | Cloud init compatibility. | [optional]  |


