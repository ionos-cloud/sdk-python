# NetworkLoadBalancersApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_networkloadbalancers_delete**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_delete) | **DELETE** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Remove an Network Load Balancer |
| [**datacenters_networkloadbalancers_find_by_network_load_balancer_id**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_find_by_network_load_balancer_id) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Retrieve an Network Load Balancer |
| [**datacenters_networkloadbalancers_flowlogs_delete**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Remove Flow Log from Network Load Balancer |
| [**datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Retrieve a Flow Log of the Network Load Balancer |
| [**datacenters_networkloadbalancers_flowlogs_get**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_get) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs | List Network Load Balancer Flow Logs |
| [**datacenters_networkloadbalancers_flowlogs_patch**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Partially modify a Flow Log of the Network Load Balancer |
| [**datacenters_networkloadbalancers_flowlogs_post**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_post) | **POST** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs | Add a Network Load Balancer Flow Log |
| [**datacenters_networkloadbalancers_flowlogs_put**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_put) | **PUT** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Modify a Flow Log of the Network Load Balancer |
| [**datacenters_networkloadbalancers_forwardingrules_delete**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_delete) | **DELETE** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Remove Forwarding Rule from Network Load Balancer |
| [**datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Retrieve a Forwarding Rule of the Network Load Balancer |
| [**datacenters_networkloadbalancers_forwardingrules_get**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_get) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules | List Network Load Balancer Forwarding Rules |
| [**datacenters_networkloadbalancers_forwardingrules_patch**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_patch) | **PATCH** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Partially modify a forwarding rule of the Network Load Balancer |
| [**datacenters_networkloadbalancers_forwardingrules_post**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_post) | **POST** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules | Add a Network Load Balancer Forwarding Rule |
| [**datacenters_networkloadbalancers_forwardingrules_put**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_put) | **PUT** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Modify a forwarding rule of the Network Load Balancer |
| [**datacenters_networkloadbalancers_get**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_get) | **GET** /datacenters/{datacenterId}/networkloadbalancers | List Network Load Balancers |
| [**datacenters_networkloadbalancers_patch**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_patch) | **PATCH** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Partially update an Network Load Balancer |
| [**datacenters_networkloadbalancers_post**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_post) | **POST** /datacenters/{datacenterId}/networkloadbalancers | Create an Network Load Balancer |
| [**datacenters_networkloadbalancers_put**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_put) | **PUT** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Update an Network Load Balancer |


# **datacenters_networkloadbalancers_delete**
> object datacenters_networkloadbalancers_delete(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Remove an Network Load Balancer

Removes the specified Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Remove an Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_delete(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_delete: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Remove an Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_delete(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
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

# **datacenters_networkloadbalancers_find_by_network_load_balancer_id**
> NetworkLoadBalancer datacenters_networkloadbalancers_find_by_network_load_balancer_id(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve an Network Load Balancer

Retrieves the attributes of a given Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve an Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_find_by_network_load_balancer_id(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_find_by_network_load_balancer_id: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve an Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_find_by_network_load_balancer_id(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_find_by_network_load_balancer_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NetworkLoadBalancer**](NetworkLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_delete**
> object datacenters_networkloadbalancers_flowlogs_delete(datacenter_id, network_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Remove Flow Log from Network Load Balancer

This will remove a flow log from the network load balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Remove Flow Log from Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_delete(datacenter_id, network_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_delete: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Remove Flow Log from Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_delete(datacenter_id, network_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **flow_log_id** | **str**| The unique ID of the flow log |  |
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

# **datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id**
> FlowLog datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, network_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Flow Log of the Network Load Balancer

This will return a Flow Log of the Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Flow Log of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, network_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Flow Log of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, network_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_get**
> FlowLogs datacenters_networkloadbalancers_flowlogs_get(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Network Load Balancer Flow Logs

You can retrieve a list of Flow Logs of the Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List Network Load Balancer Flow Logs
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_get(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_get: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List Network Load Balancer Flow Logs
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_get(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**FlowLogs**](FlowLogs.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_patch**
> FlowLog datacenters_networkloadbalancers_flowlogs_patch(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a Flow Log of the Network Load Balancer

You can use to partially update a Flow Log of a Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log
    network_load_balancer_flow_log_properties = ionoscloud.FlowLogProperties() # FlowLogProperties | Properties of a Flow Log to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify a Flow Log of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_patch(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_patch: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log
    network_load_balancer_flow_log_properties = ionoscloud.FlowLogProperties() # FlowLogProperties | Properties of a Flow Log to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify a Flow Log of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_patch(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log |  |
| **network_load_balancer_flow_log_properties** | [**FlowLogProperties**](FlowLogProperties.md)| Properties of a Flow Log to be updated |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_post**
> FlowLog datacenters_networkloadbalancers_flowlogs_post(datacenter_id, network_load_balancer_id, network_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Add a Network Load Balancer Flow Log

This will add a new Flow Log to the Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    network_load_balancer_flow_log = ionoscloud.FlowLog() # FlowLog | Flow Log to add
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Network Load Balancer Flow Log
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_post(datacenter_id, network_load_balancer_id, network_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_post: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    network_load_balancer_flow_log = ionoscloud.FlowLog() # FlowLog | Flow Log to add
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Network Load Balancer Flow Log
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_post(datacenter_id, network_load_balancer_id, network_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **network_load_balancer_flow_log** | [**FlowLog**](FlowLog.md)| Flow Log to add |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_put**
> FlowLog datacenters_networkloadbalancers_flowlogs_put(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Flow Log of the Network Load Balancer

You can use to update a Flow Log of the Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log
    network_load_balancer_flow_log = ionoscloud.FlowLogPut() # FlowLogPut | Modified Network Load Balancer Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Flow Log of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_put(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_put: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log
    network_load_balancer_flow_log = ionoscloud.FlowLogPut() # FlowLogPut | Modified Network Load Balancer Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Flow Log of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_put(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log |  |
| **network_load_balancer_flow_log** | [**FlowLogPut**](FlowLogPut.md)| Modified Network Load Balancer Flow Log |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_delete**
> object datacenters_networkloadbalancers_forwardingrules_delete(datacenter_id, network_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Remove Forwarding Rule from Network Load Balancer

This will remove a forwarding rule from the Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Remove Forwarding Rule from Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_delete(datacenter_id, network_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_delete: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Remove Forwarding Rule from Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_delete(datacenter_id, network_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule |  |
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

# **datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id**
> NetworkLoadBalancerForwardingRule datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, network_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Forwarding Rule of the Network Load Balancer

This will a forwarding rule of the Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Forwarding Rule of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, network_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Forwarding Rule of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, network_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NetworkLoadBalancerForwardingRule**](NetworkLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_get**
> NetworkLoadBalancerForwardingRules datacenters_networkloadbalancers_forwardingrules_get(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Network Load Balancer Forwarding Rules

You can retrieve a list of forwarding rules of the Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List Network Load Balancer Forwarding Rules
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_get(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_get: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List Network Load Balancer Forwarding Rules
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_get(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NetworkLoadBalancerForwardingRules**](NetworkLoadBalancerForwardingRules.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_patch**
> NetworkLoadBalancerForwardingRule datacenters_networkloadbalancers_forwardingrules_patch(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a forwarding rule of the Network Load Balancer

You can use to partially update a forwarding rule of a Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule
    network_load_balancer_forwarding_rule_properties = ionoscloud.NetworkLoadBalancerForwardingRuleProperties() # NetworkLoadBalancerForwardingRuleProperties | Properties of a forwarding rule to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify a forwarding rule of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_patch(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_patch: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule
    network_load_balancer_forwarding_rule_properties = ionoscloud.NetworkLoadBalancerForwardingRuleProperties() # NetworkLoadBalancerForwardingRuleProperties | Properties of a forwarding rule to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify a forwarding rule of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_patch(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule |  |
| **network_load_balancer_forwarding_rule_properties** | [**NetworkLoadBalancerForwardingRuleProperties**](NetworkLoadBalancerForwardingRuleProperties.md)| Properties of a forwarding rule to be updated |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NetworkLoadBalancerForwardingRule**](NetworkLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_post**
> NetworkLoadBalancerForwardingRule datacenters_networkloadbalancers_forwardingrules_post(datacenter_id, network_load_balancer_id, network_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Add a Network Load Balancer Forwarding Rule

This will add a new forwarding rule to the Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    network_load_balancer_forwarding_rule = ionoscloud.NetworkLoadBalancerForwardingRule() # NetworkLoadBalancerForwardingRule | forwarding rule to add
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Network Load Balancer Forwarding Rule
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_post(datacenter_id, network_load_balancer_id, network_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_post: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    network_load_balancer_forwarding_rule = ionoscloud.NetworkLoadBalancerForwardingRule() # NetworkLoadBalancerForwardingRule | forwarding rule to add
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Network Load Balancer Forwarding Rule
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_post(datacenter_id, network_load_balancer_id, network_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **network_load_balancer_forwarding_rule** | [**NetworkLoadBalancerForwardingRule**](NetworkLoadBalancerForwardingRule.md)| forwarding rule to add |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NetworkLoadBalancerForwardingRule**](NetworkLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_put**
> NetworkLoadBalancerForwardingRule datacenters_networkloadbalancers_forwardingrules_put(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a forwarding rule of the Network Load Balancer

You can use to update a forwarding rule of the Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule
    network_load_balancer_forwarding_rule = ionoscloud.NetworkLoadBalancerForwardingRulePut() # NetworkLoadBalancerForwardingRulePut | Modified Network Load Balancer Forwarding Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a forwarding rule of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_put(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_put: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule
    network_load_balancer_forwarding_rule = ionoscloud.NetworkLoadBalancerForwardingRulePut() # NetworkLoadBalancerForwardingRulePut | Modified Network Load Balancer Forwarding Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a forwarding rule of the Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_put(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule |  |
| **network_load_balancer_forwarding_rule** | [**NetworkLoadBalancerForwardingRulePut**](NetworkLoadBalancerForwardingRulePut.md)| Modified Network Load Balancer Forwarding Rule |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NetworkLoadBalancerForwardingRule**](NetworkLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_networkloadbalancers_get**
> NetworkLoadBalancers datacenters_networkloadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List Network Load Balancers

Retrieve a list of Network Load Balancers within the datacenter.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # List Network Load Balancers
        api_response = api_instance.datacenters_networkloadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_get: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # List Network Load Balancers
        api_response = api_instance.datacenters_networkloadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with limit for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with offset for pagination) | [optional] [default to 1000] |

### Return type

[**NetworkLoadBalancers**](NetworkLoadBalancers.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_patch**
> NetworkLoadBalancer datacenters_networkloadbalancers_patch(datacenter_id, network_load_balancer_id, network_load_balancer_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially update an Network Load Balancer

Partially update the attributes of a given Network Load Balancer

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    network_load_balancer_properties = ionoscloud.NetworkLoadBalancerProperties() # NetworkLoadBalancerProperties | Network Load Balancer properties to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially update an Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_patch(datacenter_id, network_load_balancer_id, network_load_balancer_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_patch: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    network_load_balancer_properties = ionoscloud.NetworkLoadBalancerProperties() # NetworkLoadBalancerProperties | Network Load Balancer properties to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially update an Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_patch(datacenter_id, network_load_balancer_id, network_load_balancer_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **network_load_balancer_properties** | [**NetworkLoadBalancerProperties**](NetworkLoadBalancerProperties.md)| Network Load Balancer properties to be updated |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NetworkLoadBalancer**](NetworkLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_post**
> NetworkLoadBalancer datacenters_networkloadbalancers_post(datacenter_id, network_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create an Network Load Balancer

Creates an Network Load Balancer within the datacenter.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer = ionoscloud.NetworkLoadBalancer() # NetworkLoadBalancer | Network Load Balancer to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create an Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_post(datacenter_id, network_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_post: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer = ionoscloud.NetworkLoadBalancer() # NetworkLoadBalancer | Network Load Balancer to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create an Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_post(datacenter_id, network_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer** | [**NetworkLoadBalancer**](NetworkLoadBalancer.md)| Network Load Balancer to be created |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NetworkLoadBalancer**](NetworkLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_networkloadbalancers_put**
> NetworkLoadBalancer datacenters_networkloadbalancers_put(datacenter_id, network_load_balancer_id, network_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

Update an Network Load Balancer

Update the attributes of a given Network Load Balancer

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    network_load_balancer = ionoscloud.NetworkLoadBalancerPut() # NetworkLoadBalancerPut | Modified Network Load Balancer
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # Update an Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_put(datacenter_id, network_load_balancer_id, network_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_put: %s\n' % e)
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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer
    network_load_balancer = ionoscloud.NetworkLoadBalancerPut() # NetworkLoadBalancerPut | Modified Network Load Balancer
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # Update an Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_put(datacenter_id, network_load_balancer_id, network_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer |  |
| **network_load_balancer** | [**NetworkLoadBalancerPut**](NetworkLoadBalancerPut.md)| Modified Network Load Balancer |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with limit for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with offset for pagination) | [optional] [default to 1000] |

### Return type

[**NetworkLoadBalancer**](NetworkLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

