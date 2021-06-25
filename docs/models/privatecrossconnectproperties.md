# PrivateCrossConnectProperties

## Properties

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **name** | **str** | A name of that resource | \[optional\] |
| **description** | **str** | Human readable description | \[optional\] |
| **peers** | [**list\[Peer\]**](peer.md) | Read-Only attribute. Lists LAN's joined to this private cross connect | \[optional\] \[readonly\] |
| **connectable\_datacenters** | [**list\[ConnectableDatacenter\]**](connectabledatacenter.md) | Read-Only attribute. Lists datacenters that can be joined to this private cross connect | \[optional\] \[readonly\] |

