# SnapshotProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **cpu_hot_plug** | **bool** | Hot-plug capable CPU (no reboot required). | [optional]  |
| **cpu_hot_unplug** | **bool** | Hot-unplug capable CPU (no reboot required). | [optional]  |
| **description** | **str** | Human-readable description. | [optional]  |
| **disc_scsi_hot_plug** | **bool** | Hot-plug capable SCSI drive (no reboot required). | [optional]  |
| **disc_scsi_hot_unplug** | **bool** | Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines. | [optional]  |
| **disc_virtio_hot_plug** | **bool** | Hot-plug capable Virt-IO drive (no reboot required). | [optional]  |
| **disc_virtio_hot_unplug** | **bool** | Hot-unplug capable Virt-IO drive (no reboot required). Not supported with Windows VMs. | [optional]  |
| **licence_type** | **str** | OS type of this snapshot | [optional]  |
| **location** | **str** | Location of that image/snapshot.  | [optional] [readonly]  |
| **name** | **str** | The name of the  resource. | [optional]  |
| **nic_hot_plug** | **bool** | Hot-plug capable NIC (no reboot required). | [optional]  |
| **nic_hot_unplug** | **bool** | Hot-unplug capable NIC (no reboot required). | [optional]  |
| **ram_hot_plug** | **bool** | Hot-plug capable RAM (no reboot required). | [optional]  |
| **ram_hot_unplug** | **bool** | Hot-unplug capable RAM (no reboot required). | [optional]  |
| **sec_auth_protection** | **bool** | Boolean value representing if the snapshot requires extra protection, such as two-step verification. | [optional]  |
| **size** | **float** | The size of the image in GB. | [optional] [readonly]  |


