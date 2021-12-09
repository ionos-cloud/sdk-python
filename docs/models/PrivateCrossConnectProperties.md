# PrivateCrossConnectProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of the  resource. | [optional]  |
| **description** | **str** | Human-readable description. | [optional]  |
| **peers** | [**list[Peer]**](Peer.md) | Read-Only attribute. Lists LAN&#39;s joined to this private Cross-Connect. | [optional] [readonly]  |
| **connectable_datacenters** | [**list[ConnectableDatacenter]**](ConnectableDatacenter.md) | Read-Only attribute. Lists data centers that can be joined to this private Cross-Connect. | [optional] [readonly]  |


