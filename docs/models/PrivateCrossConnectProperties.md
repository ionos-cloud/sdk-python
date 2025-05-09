# PrivateCrossConnectProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the Cross Connect. | [optional]  |
| **description** | **str** | Human-readable description of the Cross Connect. | [optional]  |
| **peers** | [**list[Peer]**](Peer.md) | Read-Only attribute. Lists LAN&#39;s connected to this Cross Connect. | [optional] [readonly]  |
| **connectable_datacenters** | [**list[ConnectableDatacenter]**](ConnectableDatacenter.md) | Read-Only attribute. Lists data centers that can be connected to this Cross Connect. If the Cross Connect is not connected to any LANs it lists all VDCs the user has access to. If the Cross Connect is connected to at least 1 LAN it lists all VDCs the user has access to in the location of the connected LAN. | [optional] [readonly]  |


