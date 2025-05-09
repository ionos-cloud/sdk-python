# SecurityGroupsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_securitygroups_delete**](SecurityGroupsApi.md#datacenters_securitygroups_delete) | **DELETE** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Delete a Security Group |
| [**datacenters_securitygroups_find_by_id**](SecurityGroupsApi.md#datacenters_securitygroups_find_by_id) | **GET** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Retrieve a Security Group |
| [**datacenters_securitygroups_firewallrules_delete**](SecurityGroupsApi.md#datacenters_securitygroups_firewallrules_delete) | **DELETE** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Remove a Firewall Rule from a Security Group |
| [**datacenters_securitygroups_firewallrules_post**](SecurityGroupsApi.md#datacenters_securitygroups_firewallrules_post) | **POST** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules | Create Firewall rule to a Security Group |
| [**datacenters_securitygroups_get**](SecurityGroupsApi.md#datacenters_securitygroups_get) | **GET** /datacenters/{datacenterId}/securitygroups | List Security Groups |
| [**datacenters_securitygroups_patch**](SecurityGroupsApi.md#datacenters_securitygroups_patch) | **PATCH** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Partially modify Security Group |
| [**datacenters_securitygroups_post**](SecurityGroupsApi.md#datacenters_securitygroups_post) | **POST** /datacenters/{datacenterId}/securitygroups | Create a Security Group |
| [**datacenters_securitygroups_put**](SecurityGroupsApi.md#datacenters_securitygroups_put) | **PUT** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Modify Security Group |
| [**datacenters_securitygroups_rules_find_by_id**](SecurityGroupsApi.md#datacenters_securitygroups_rules_find_by_id) | **GET** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Retrieve security group rule by id |
| [**datacenters_securitygroups_rules_get**](SecurityGroupsApi.md#datacenters_securitygroups_rules_get) | **GET** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules | List Security Group rules |
| [**datacenters_securitygroups_rules_patch**](SecurityGroupsApi.md#datacenters_securitygroups_rules_patch) | **PATCH** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Partially modify Security Group Rules |
| [**datacenters_securitygroups_rules_put**](SecurityGroupsApi.md#datacenters_securitygroups_rules_put) | **PUT** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Modify a Security Group Rule |
| [**datacenters_servers_nics_securitygroups_put**](SecurityGroupsApi.md#datacenters_servers_nics_securitygroups_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/securitygroups | Attach a list of Security Groups to a NIC |
| [**datacenters_servers_securitygroups_put**](SecurityGroupsApi.md#datacenters_servers_securitygroups_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/securitygroups | Attach a list of Security Groups to a Server |


# **datacenters_securitygroups_delete**
> datacenters_securitygroups_delete(datacenter_id, security_group_id, pretty=pretty)

Delete a Security Group

Deletes the specified Security Group.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the Security Group.
    try:
        # Delete a Security Group
        api_instance.datacenters_securitygroups_delete(datacenter_id, security_group_id)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **security_group_id** | **str**| The unique ID of the Security Group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |

### Return type

void (empty response body)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_securitygroups_find_by_id**
> SecurityGroup datacenters_securitygroups_find_by_id(datacenter_id, security_group_id, pretty=pretty, depth=depth)

Retrieve a Security Group

Retrieves the attributes of a given Security Group.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    try:
        # Retrieve a Security Group
        api_response = api_instance.datacenters_securitygroups_find_by_id(datacenter_id, security_group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center |  |
| **security_group_id** | **str**| The unique ID of the security group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**SecurityGroup**](../models/SecurityGroup.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_securitygroups_firewallrules_delete**
> datacenters_securitygroups_firewallrules_delete(datacenter_id, security_group_id, rule_id)

Remove a Firewall Rule from a Security Group

Removes the specific Firewall Rule from the Security Group and delete the Firewall rule

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    rule_id = 'rule_id_example' # str | The unique ID of the firewall rule.
    try:
        # Remove a Firewall Rule from a Security Group
        api_instance.datacenters_securitygroups_firewallrules_delete(datacenter_id, security_group_id, rule_id)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_firewallrules_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center |  |
| **security_group_id** | **str**| The unique ID of the security group. |  |
| **rule_id** | **str**| The unique ID of the firewall rule. |  |

### Return type

void (empty response body)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_securitygroups_firewallrules_post**
> FirewallRule datacenters_securitygroups_firewallrules_post(datacenter_id, security_group_id, firewall_rule)

Create Firewall rule to a Security Group

Create one firewall rule and attach it to the existing security group

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    firewall_rule = ionoscloud.FirewallRule() # FirewallRule | The firewall to be attached (or created and attached).
    try:
        # Create Firewall rule to a Security Group
        api_response = api_instance.datacenters_securitygroups_firewallrules_post(datacenter_id, security_group_id, firewall_rule)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_firewallrules_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center |  |
| **security_group_id** | **str**| The unique ID of the security group. |  |
| **firewall_rule** | [**FirewallRule**](../models/FirewallRule.md)| The firewall to be attached (or created and attached). |  |

### Return type

[**FirewallRule**](../models/FirewallRule.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_securitygroups_get**
> SecurityGroups datacenters_securitygroups_get(datacenter_id, pretty=pretty, depth=depth, offset=offset, limit=limit)

List Security Groups

Retrieve a list of available security groups.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    try:
        # List Security Groups
        api_response = api_instance.datacenters_securitygroups_get(datacenter_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000] |

### Return type

[**SecurityGroups**](../models/SecurityGroups.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_securitygroups_patch**
> SecurityGroup datacenters_securitygroups_patch(datacenter_id, security_group_id, security_group, pretty=pretty, depth=depth)

Partially modify Security Group

Modify the properties of the specified Security Group within the data center.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the Security Group.
    security_group = ionoscloud.SecurityGroupProperties() # SecurityGroupProperties | The modified Security Group
    try:
        # Partially modify Security Group
        api_response = api_instance.datacenters_securitygroups_patch(datacenter_id, security_group_id, security_group)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **security_group_id** | **str**| The unique ID of the Security Group. |  |
| **security_group** | [**SecurityGroupProperties**](../models/SecurityGroupProperties.md)| The modified Security Group |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**SecurityGroup**](../models/SecurityGroup.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_securitygroups_post**
> SecurityGroup datacenters_securitygroups_post(datacenter_id, security_group, pretty=pretty, depth=depth)

Create a Security Group

Creates a security group within the data center. This will allow you to define which IP addresses and networks have access to your servers.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group = ionoscloud.SecurityGroupRequest() # SecurityGroupRequest | The security group to be created
    try:
        # Create a Security Group
        api_response = api_instance.datacenters_securitygroups_post(datacenter_id, security_group)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **security_group** | [**SecurityGroupRequest**](../models/SecurityGroupRequest.md)| The security group to be created |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**SecurityGroup**](../models/SecurityGroup.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_securitygroups_put**
> SecurityGroup datacenters_securitygroups_put(datacenter_id, security_group_id, security_group, pretty=pretty, depth=depth)

Modify Security Group

Modify the properties of the specified Security Group within the data center.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the Security Group.
    security_group = ionoscloud.SecurityGroupRequest() # SecurityGroupRequest | The modified Security Group
    try:
        # Modify Security Group
        api_response = api_instance.datacenters_securitygroups_put(datacenter_id, security_group_id, security_group)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **security_group_id** | **str**| The unique ID of the Security Group. |  |
| **security_group** | [**SecurityGroupRequest**](../models/SecurityGroupRequest.md)| The modified Security Group |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**SecurityGroup**](../models/SecurityGroup.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_securitygroups_rules_find_by_id**
> FirewallRule datacenters_securitygroups_rules_find_by_id(datacenter_id, security_group_id, rule_id, pretty=pretty, depth=depth)

Retrieve security group rule by id

Retrieve the properties of the specified Security Group rule.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the Security Group.
    rule_id = 'rule_id_example' # str | The unique ID of the Security Group rule.
    try:
        # Retrieve security group rule by id
        api_response = api_instance.datacenters_securitygroups_rules_find_by_id(datacenter_id, security_group_id, rule_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_rules_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **security_group_id** | **str**| The unique ID of the Security Group. |  |
| **rule_id** | **str**| The unique ID of the Security Group rule. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FirewallRule**](../models/FirewallRule.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_securitygroups_rules_get**
> FirewallRules datacenters_securitygroups_rules_get(datacenter_id, security_group_id, pretty=pretty, depth=depth, offset=offset, limit=limit)

List Security Group rules

List all rules for the specified Security Group.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    try:
        # List Security Group rules
        api_response = api_instance.datacenters_securitygroups_rules_get(datacenter_id, security_group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_rules_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **security_group_id** | **str**| The unique ID of the security group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000] |

### Return type

[**FirewallRules**](../models/FirewallRules.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_securitygroups_rules_patch**
> FirewallRule datacenters_securitygroups_rules_patch(datacenter_id, security_group_id, rule_id, rule, pretty=pretty, depth=depth)

Partially modify Security Group Rules

Update the properties of the specified Security Group rule.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    rule_id = 'rule_id_example' # str | The unique ID of the Security Group Rule.
    rule = ionoscloud.FirewallruleProperties() # FirewallruleProperties | The properties of the Security Group Rule to be updated.
    try:
        # Partially modify Security Group Rules
        api_response = api_instance.datacenters_securitygroups_rules_patch(datacenter_id, security_group_id, rule_id, rule)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_rules_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **security_group_id** | **str**| The unique ID of the security group. |  |
| **rule_id** | **str**| The unique ID of the Security Group Rule. |  |
| **rule** | [**FirewallruleProperties**](../models/FirewallruleProperties.md)| The properties of the Security Group Rule to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FirewallRule**](../models/FirewallRule.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_securitygroups_rules_put**
> FirewallRule datacenters_securitygroups_rules_put(datacenter_id, security_group_id, rule_id, rule, pretty=pretty, depth=depth)

Modify a Security Group Rule

Modifies the properties of the specified Security Group Rule.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    security_group_id = 'security_group_id_example' # str | The unique ID of the security group.
    rule_id = 'rule_id_example' # str | The unique ID of the Security Group Rule.
    rule = ionoscloud.FirewallRule() # FirewallRule | The modified Security Group Rule.
    try:
        # Modify a Security Group Rule
        api_response = api_instance.datacenters_securitygroups_rules_put(datacenter_id, security_group_id, rule_id, rule)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_securitygroups_rules_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **security_group_id** | **str**| The unique ID of the security group. |  |
| **rule_id** | **str**| The unique ID of the Security Group Rule. |  |
| **rule** | [**FirewallRule**](../models/FirewallRule.md)| The modified Security Group Rule. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FirewallRule**](../models/FirewallRule.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_nics_securitygroups_put**
> SecurityGroups datacenters_servers_nics_securitygroups_put(datacenter_id, server_id, nic_id, securitygroups, pretty=pretty, depth=depth)

Attach a list of Security Groups to a NIC

Updating the list of Security Groups attached to an existing NIC specified by its ID.  Security Groups should already exist as part of the datacenter.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    nic_id = 'nic_id_example' # str | The unique ID of the server.
    securitygroups = ionoscloud.ListOfIds() # ListOfIds | The list of NIC attached Security Groups IDs.
    try:
        # Attach a list of Security Groups to a NIC
        api_response = api_instance.datacenters_servers_nics_securitygroups_put(datacenter_id, server_id, nic_id, securitygroups)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_servers_nics_securitygroups_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **nic_id** | **str**| The unique ID of the server. |  |
| **securitygroups** | [**ListOfIds**](../models/ListOfIds.md)| The list of NIC attached Security Groups IDs. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**SecurityGroups**](../models/SecurityGroups.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_securitygroups_put**
> SecurityGroups datacenters_servers_securitygroups_put(datacenter_id, server_id, securitygroups, pretty=pretty, depth=depth)

Attach a list of Security Groups to a Server

Updating the list of Security Groups attached to an existing server specified by its ID.  Security Groups should already exist as part of the datacenter.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SecurityGroupsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    securitygroups = ionoscloud.ListOfIds() # ListOfIds | The list of server attached Security Groups IDs.
    try:
        # Attach a list of Security Groups to a Server
        api_response = api_instance.datacenters_servers_securitygroups_put(datacenter_id, server_id, securitygroups)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SecurityGroupsApi.datacenters_servers_securitygroups_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **securitygroups** | [**ListOfIds**](../models/ListOfIds.md)| The list of server attached Security Groups IDs. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth&#x3D;0: Only direct properties are included;              children (servers and other elements) are not included.   - depth&#x3D;1: Direct properties and children references are included.   - depth&#x3D;2: Direct properties and children properties are included.   - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.   - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**SecurityGroups**](../models/SecurityGroups.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

