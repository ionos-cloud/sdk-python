# SnapshotProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the  resource. | [optional]  |
| **description** | **str** | Human-readable description. | [optional]  |
| **location** | **str** | Location of that image/snapshot.  | [optional] [readonly]  |
| **size** | **float** | The size of the image in GB. | [optional] [readonly]  |
| **sec_auth_protection** | **bool** | Boolean value representing if the snapshot requires extra protection, such as two-step verification. | [optional]  |
| **cpu_hot_plug** | **bool** | Hot-plug capable CPU (no reboot required). | [optional]  |
| **cpu_hot_unplug** | **bool** | Hot-unplug capable CPU (no reboot required). | [optional]  |
| **ram_hot_plug** | **bool** | Hot-plug capable RAM (no reboot required). | [optional]  |
| **ram_hot_unplug** | **bool** | Hot-unplug capable RAM (no reboot required). | [optional]  |
| **nic_hot_plug** | **bool** | Hot-plug capable NIC (no reboot required). | [optional]  |
| **nic_hot_unplug** | **bool** | Hot-unplug capable NIC (no reboot required). | [optional]  |
| **disc_virtio_hot_plug** | **bool** | Hot-plug capable Virt-IO drive (no reboot required). | [optional]  |
| **disc_virtio_hot_unplug** | **bool** | Hot-unplug capable Virt-IO drive (no reboot required). Not supported with Windows VMs. | [optional]  |
| **disc_scsi_hot_plug** | **bool** | Hot-plug capable SCSI drive (no reboot required). | [optional]  |
| **expose_serial** | **bool** | If set to &#x60;true&#x60; will expose the serial id of the disk attached to the server. If set to &#x60;false&#x60; will not expose the serial id. Some operating systems or software solutions require the serial id to be exposed to work properly. Exposing the serial  can influence licensed software (e.g. Windows) behavior | [optional] [default to False] |
| **require_legacy_bios** | **bool** | Indicates if the image requires the legacy BIOS for compatibility or specific needs. | [optional] [default to True] |
| **disc_scsi_hot_unplug** | **bool** | Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines. | [optional]  |
| **licence_type** | **str** | OS type of this snapshot | [optional]  |
| **application_type** | **str** | The type of application that is hosted on this resource.  Only public images can have an Application type different than UNKNOWN. | [optional] [default to 'UNKNOWN'] |


