# FirewallRulesApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_servers_nics_firewallrules_delete**](FirewallRulesApi.md#datacenters_servers_nics_firewallrules_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Delete a Firewall Rule |
| [**datacenters_servers_nics_firewallrules_find_by_id**](FirewallRulesApi.md#datacenters_servers_nics_firewallrules_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Retrieve a Firewall Rule |
| [**datacenters_servers_nics_firewallrules_get**](FirewallRulesApi.md#datacenters_servers_nics_firewallrules_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules | List Firewall Rules |
| [**datacenters_servers_nics_firewallrules_patch**](FirewallRulesApi.md#datacenters_servers_nics_firewallrules_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Partially Modify a Firewall Rule |
| [**datacenters_servers_nics_firewallrules_post**](FirewallRulesApi.md#datacenters_servers_nics_firewallrules_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules | Create a Firewall Rule |
| [**datacenters_servers_nics_firewallrules_put**](FirewallRulesApi.md#datacenters_servers_nics_firewallrules_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Modify a Firewall Rule |


# **datacenters_servers_nics_firewallrules_delete**
> object datacenters_servers_nics_firewallrules_delete(datacenter_id, server_id, nic_id, firewallrule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Firewall Rule

Removes the specified firewall rule.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_delete(datacenter_id, server_id, nic_id, firewallrule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_delete: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_delete(datacenter_id, server_id, nic_id, firewallrule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **firewallrule_id** | **str**| The unique ID of the Firewall Rule |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_firewallrules_find_by_id**
> FirewallRule datacenters_servers_nics_firewallrules_find_by_id(datacenter_id, server_id, nic_id, firewallrule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Firewall Rule

Retrieves the attributes of a given firewall rule.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_find_by_id(datacenter_id, server_id, nic_id, firewallrule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_find_by_id: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_find_by_id(datacenter_id, server_id, nic_id, firewallrule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **firewallrule_id** | **str**| The unique ID of the Firewall Rule |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_firewallrules_get**
> FirewallRules datacenters_servers_nics_firewallrules_get(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List Firewall Rules

Retrieves a list of firewall rules associated with a particular network interface.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # List Firewall Rules
        api_response = api_instance.datacenters_servers_nics_firewallrules_get(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_get: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # List Firewall Rules
        api_response = api_instance.datacenters_servers_nics_firewallrules_get(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with limit for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with offset for pagination) | [optional] [default to 1000] |

### Return type

[**FirewallRules**](FirewallRules.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_firewallrules_patch**
> FirewallRule datacenters_servers_nics_firewallrules_patch(datacenter_id, server_id, nic_id, firewallrule_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially Modify a Firewall Rule

You can use update attributes of a resource.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
    firewallrule = ionoscloud.FirewallruleProperties() # FirewallruleProperties | Modified Firewall Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially Modify a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_patch(datacenter_id, server_id, nic_id, firewallrule_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_patch: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
    firewallrule = ionoscloud.FirewallruleProperties() # FirewallruleProperties | Modified Firewall Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially Modify a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_patch(datacenter_id, server_id, nic_id, firewallrule_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **firewallrule_id** | **str**| The unique ID of the Firewall Rule |  |
| **firewallrule** | [**FirewallruleProperties**](FirewallruleProperties.md)| Modified Firewall Rule |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_nics_firewallrules_post**
> FirewallRule datacenters_servers_nics_firewallrules_post(datacenter_id, server_id, nic_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Firewall Rule

This will add a Firewall Rule to the network interface.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    firewallrule = ionoscloud.FirewallRule() # FirewallRule | Firewall Rule to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_post(datacenter_id, server_id, nic_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_post: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    firewallrule = ionoscloud.FirewallRule() # FirewallRule | Firewall Rule to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_post(datacenter_id, server_id, nic_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **firewallrule** | [**FirewallRule**](FirewallRule.md)| Firewall Rule to be created |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_nics_firewallrules_put**
> FirewallRule datacenters_servers_nics_firewallrules_put(datacenter_id, server_id, nic_id, firewallrule_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Firewall Rule

You can use update attributes of a resource.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
    firewallrule = ionoscloud.FirewallRule() # FirewallRule | Modified Firewall Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_put(datacenter_id, server_id, nic_id, firewallrule_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_put: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.FirewallRulesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
    firewallrule = ionoscloud.FirewallRule() # FirewallRule | Modified Firewall Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_put(datacenter_id, server_id, nic_id, firewallrule_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FirewallRulesApi.datacenters_servers_nics_firewallrules_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **firewallrule_id** | **str**| The unique ID of the Firewall Rule |  |
| **firewallrule** | [**FirewallRule**](FirewallRule.md)| Modified Firewall Rule |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

