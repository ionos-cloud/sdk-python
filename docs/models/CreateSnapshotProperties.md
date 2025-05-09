# CreateSnapshotProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the snapshot | [optional]  |
| **description** | **str** | The description of the snapshot | [optional]  |
| **sec_auth_protection** | **bool** | Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc. | [optional]  |
| **licence_type** | **str** | OS type of this Snapshot | [optional]  |
| **application_type** | **str** | The type of application that is hosted on this resource.  Only public images can have an Application type different than UNKNOWN. | [optional] [default to 'UNKNOWN'] |


