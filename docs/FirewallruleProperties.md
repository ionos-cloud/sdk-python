# FirewallruleProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A name of that resource | [optional]  |
| **protocol** | **str** | The protocol for the rule. Property cannot be modified after creation (disallowed in update requests) |  |
| **source_mac** | **str** | Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address | [optional]  |
| **source_ip** | **str** | Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs | [optional]  |
| **target_ip** | **str** | In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs | [optional]  |
| **icmp_code** | **int** | Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes | [optional]  |
| **icmp_type** | **int** | Defines the allowed type (from 0 to 254) if the protocol ICMP is chosen. Value null allows all types | [optional]  |
| **port_range_start** | **int** | Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd value null to allow all ports | [optional]  |
| **port_range_end** | **int** | Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports | [optional]  |
| **type** | **str** | The type of firewall rule. If is not specified, it will take the default value INGRESS | [optional]  |


