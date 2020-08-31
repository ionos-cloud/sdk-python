# NicProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name of that resource | [optional] 
**mac** | **str** | The MAC address of the NIC | [optional] [readonly] 
**ips** | **list[str]** | Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically. | [optional] 
**dhcp** | **bool** | Indicates if the nic will reserve an IP using DHCP | [optional] 
**lan** | **int** | The LAN ID the NIC will sit on. If the LAN ID does not exist it will be implicitly created | 
**firewall_active** | **bool** | Activate or deactivate the firewall. By default an active firewall without any defined rules will block all incoming network traffic except for the firewall rules that explicitly allows certain protocols, ip addresses and ports. | [optional] 
**nat** | **bool** | Indicates if NAT is enabled on this NIC | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


