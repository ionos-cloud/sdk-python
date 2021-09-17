# PrivateCrossConnectProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A name of that resource | [optional]  |
| **description** | **str** | Human readable description | [optional]  |
| **peers** | [**list[Peer]**](Peer.md) | Read-Only attribute. Lists LAN&#39;s joined to this private cross connect | [optional] [readonly]  |
| **connectable_datacenters** | [**list[ConnectableDatacenter]**](ConnectableDatacenter.md) | Read-Only attribute. Lists datacenters that can be joined to this private cross connect | [optional] [readonly]  |


