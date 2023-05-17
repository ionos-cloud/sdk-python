# NetworkLoadBalancersApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_networkloadbalancers_delete**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_delete) | **DELETE** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Delete Network Load Balancers |
| [**datacenters_networkloadbalancers_find_by_network_load_balancer_id**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_find_by_network_load_balancer_id) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Retrieve Network Load Balancers |
| [**datacenters_networkloadbalancers_flowlogs_delete**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Delete NLB Flow Logs |
| [**datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Retrieve NLB Flow Logs |
| [**datacenters_networkloadbalancers_flowlogs_get**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_get) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs | List NLB Flow Logs |
| [**datacenters_networkloadbalancers_flowlogs_patch**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Partially modify NLB Flow Logs |
| [**datacenters_networkloadbalancers_flowlogs_post**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_post) | **POST** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs | Create a NLB Flow Log |
| [**datacenters_networkloadbalancers_flowlogs_put**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_put) | **PUT** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Modify NLB Flow Logs |
| [**datacenters_networkloadbalancers_forwardingrules_delete**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_delete) | **DELETE** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Delete NLB forwarding rules |
| [**datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Retrieve NLB forwarding rules |
| [**datacenters_networkloadbalancers_forwardingrules_get**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_get) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules | List NLB forwarding rules |
| [**datacenters_networkloadbalancers_forwardingrules_patch**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_patch) | **PATCH** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Partially modify NLB forwarding rules |
| [**datacenters_networkloadbalancers_forwardingrules_post**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_post) | **POST** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules | Create a NLB Forwarding Rule |
| [**datacenters_networkloadbalancers_forwardingrules_put**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_put) | **PUT** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Modify NLB forwarding rules |
| [**datacenters_networkloadbalancers_get**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_get) | **GET** /datacenters/{datacenterId}/networkloadbalancers | List Network Load Balancers |
| [**datacenters_networkloadbalancers_patch**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_patch) | **PATCH** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Partially modify Network Load Balancers |
| [**datacenters_networkloadbalancers_post**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_post) | **POST** /datacenters/{datacenterId}/networkloadbalancers | Create a Network Load Balancer |
| [**datacenters_networkloadbalancers_put**](NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_put) | **PUT** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Modify Network Load Balancers |


# **datacenters_networkloadbalancers_delete**
> datacenters_networkloadbalancers_delete(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete Network Load Balancers

Remove the specified Network Load Balancer from the data center.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    try:
        # Delete Network Load Balancers
        api_instance.datacenters_networkloadbalancers_delete(datacenter_id, network_load_balancer_id)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

void (empty response body)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_find_by_network_load_balancer_id**
> NetworkLoadBalancer datacenters_networkloadbalancers_find_by_network_load_balancer_id(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve Network Load Balancers

Retrieve the properties of the specified Network Load Balancer within the data center.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    try:
        # Retrieve Network Load Balancers
        api_response = api_instance.datacenters_networkloadbalancers_find_by_network_load_balancer_id(datacenter_id, network_load_balancer_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_find_by_network_load_balancer_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NetworkLoadBalancer**](../models/NetworkLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_delete**
> datacenters_networkloadbalancers_flowlogs_delete(datacenter_id, network_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete NLB Flow Logs

Delete the specified Network Load Balancer Flow Log.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log.
    try:
        # Delete NLB Flow Logs
        api_instance.datacenters_networkloadbalancers_flowlogs_delete(datacenter_id, network_load_balancer_id, flow_log_id)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

void (empty response body)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id**
> FlowLog datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, network_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve NLB Flow Logs

Retrieve the specified Network Load Balancer Flow Log.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log.
    try:
        # Retrieve NLB Flow Logs
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, network_load_balancer_id, flow_log_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**FlowLog**](../models/FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_get**
> FlowLogs datacenters_networkloadbalancers_flowlogs_get(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List NLB Flow Logs

List all the Flow Logs for the specified Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    try:
        # List NLB Flow Logs
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_get(datacenter_id, network_load_balancer_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**FlowLogs**](../models/FlowLogs.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_patch**
> FlowLog datacenters_networkloadbalancers_flowlogs_patch(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify NLB Flow Logs

Update the properties of the specified Network Load Balancer Flow Log.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log.
    network_load_balancer_flow_log_properties = ionoscloud.FlowLogProperties() # FlowLogProperties | The properties of the Flow Log to be updated.
    try:
        # Partially modify NLB Flow Logs
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_patch(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log_properties)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log. |  |
| **network_load_balancer_flow_log_properties** | [**FlowLogProperties**](../models/FlowLogProperties.md)| The properties of the Flow Log to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**FlowLog**](../models/FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_post**
> FlowLog datacenters_networkloadbalancers_flowlogs_post(datacenter_id, network_load_balancer_id, network_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a NLB Flow Log

Adds a new Flow Log for the Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    network_load_balancer_flow_log = ionoscloud.FlowLog() # FlowLog | The Flow Log to create.
    try:
        # Create a NLB Flow Log
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_post(datacenter_id, network_load_balancer_id, network_load_balancer_flow_log)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **network_load_balancer_flow_log** | [**FlowLog**](../models/FlowLog.md)| The Flow Log to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**FlowLog**](../models/FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_networkloadbalancers_flowlogs_put**
> FlowLog datacenters_networkloadbalancers_flowlogs_put(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify NLB Flow Logs

Modify the specified Network Load Balancer Flow Log.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log.
    network_load_balancer_flow_log = ionoscloud.FlowLogPut() # FlowLogPut | The modified NLB Flow Log.
    try:
        # Modify NLB Flow Logs
        api_response = api_instance.datacenters_networkloadbalancers_flowlogs_put(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_flowlogs_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log. |  |
| **network_load_balancer_flow_log** | [**FlowLogPut**](../models/FlowLogPut.md)| The modified NLB Flow Log. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**FlowLog**](../models/FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_delete**
> datacenters_networkloadbalancers_forwardingrules_delete(datacenter_id, network_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete NLB forwarding rules

Delete the specified Network Load Balancer forwarding rule.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    try:
        # Delete NLB forwarding rules
        api_instance.datacenters_networkloadbalancers_forwardingrules_delete(datacenter_id, network_load_balancer_id, forwarding_rule_id)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

void (empty response body)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id**
> NetworkLoadBalancerForwardingRule datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, network_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve NLB forwarding rules

Retrieve the specified Network Load Balance forwarding rule.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    try:
        # Retrieve NLB forwarding rules
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, network_load_balancer_id, forwarding_rule_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NetworkLoadBalancerForwardingRule**](../models/NetworkLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_get**
> NetworkLoadBalancerForwardingRules datacenters_networkloadbalancers_forwardingrules_get(datacenter_id, network_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List NLB forwarding rules

List the forwarding rules for the specified Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    try:
        # List NLB forwarding rules
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_get(datacenter_id, network_load_balancer_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NetworkLoadBalancerForwardingRules**](../models/NetworkLoadBalancerForwardingRules.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_patch**
> NetworkLoadBalancerForwardingRule datacenters_networkloadbalancers_forwardingrules_patch(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify NLB forwarding rules

Update the properties of the specified Network Load Balancer forwarding rule.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    network_load_balancer_forwarding_rule_properties = ionoscloud.NetworkLoadBalancerForwardingRuleProperties() # NetworkLoadBalancerForwardingRuleProperties | The properties of the forwarding rule to be updated.
    try:
        # Partially modify NLB forwarding rules
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_patch(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule_properties)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. |  |
| **network_load_balancer_forwarding_rule_properties** | [**NetworkLoadBalancerForwardingRuleProperties**](../models/NetworkLoadBalancerForwardingRuleProperties.md)| The properties of the forwarding rule to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NetworkLoadBalancerForwardingRule**](../models/NetworkLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_post**
> NetworkLoadBalancerForwardingRule datacenters_networkloadbalancers_forwardingrules_post(datacenter_id, network_load_balancer_id, network_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a NLB Forwarding Rule

Creates a forwarding rule for the specified Network Load Balancer.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    network_load_balancer_forwarding_rule = ionoscloud.NetworkLoadBalancerForwardingRule() # NetworkLoadBalancerForwardingRule | The forwarding rule to create.
    try:
        # Create a NLB Forwarding Rule
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_post(datacenter_id, network_load_balancer_id, network_load_balancer_forwarding_rule)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **network_load_balancer_forwarding_rule** | [**NetworkLoadBalancerForwardingRule**](../models/NetworkLoadBalancerForwardingRule.md)| The forwarding rule to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NetworkLoadBalancerForwardingRule**](../models/NetworkLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_networkloadbalancers_forwardingrules_put**
> NetworkLoadBalancerForwardingRule datacenters_networkloadbalancers_forwardingrules_put(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify NLB forwarding rules

Modify the specified Network Load Balancer forwarding rule.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    network_load_balancer_forwarding_rule = ionoscloud.NetworkLoadBalancerForwardingRulePut() # NetworkLoadBalancerForwardingRulePut | The modified NLB forwarding rule.
    try:
        # Modify NLB forwarding rules
        api_response = api_instance.datacenters_networkloadbalancers_forwardingrules_put(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_forwardingrules_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. |  |
| **network_load_balancer_forwarding_rule** | [**NetworkLoadBalancerForwardingRulePut**](../models/NetworkLoadBalancerForwardingRulePut.md)| The modified NLB forwarding rule. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NetworkLoadBalancerForwardingRule**](../models/NetworkLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_networkloadbalancers_get**
> NetworkLoadBalancers datacenters_networkloadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List Network Load Balancers

List all the Network Load Balancers within the data center.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    try:
        # List Network Load Balancers
        api_response = api_instance.datacenters_networkloadbalancers_get(datacenter_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000] |

### Return type

[**NetworkLoadBalancers**](../models/NetworkLoadBalancers.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_patch**
> NetworkLoadBalancer datacenters_networkloadbalancers_patch(datacenter_id, network_load_balancer_id, network_load_balancer_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify Network Load Balancers

Update the properties of the specified Network Load Balancer within the data center.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    network_load_balancer_properties = ionoscloud.NetworkLoadBalancerProperties() # NetworkLoadBalancerProperties | The properties of the Network Load Balancer to be updated.
    try:
        # Partially modify Network Load Balancers
        api_response = api_instance.datacenters_networkloadbalancers_patch(datacenter_id, network_load_balancer_id, network_load_balancer_properties)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **network_load_balancer_properties** | [**NetworkLoadBalancerProperties**](../models/NetworkLoadBalancerProperties.md)| The properties of the Network Load Balancer to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NetworkLoadBalancer**](../models/NetworkLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_networkloadbalancers_post**
> NetworkLoadBalancer datacenters_networkloadbalancers_post(datacenter_id, network_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Network Load Balancer

Creates a Network Load Balancer within the data center.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer = ionoscloud.NetworkLoadBalancer() # NetworkLoadBalancer | The Network Load Balancer to create.
    try:
        # Create a Network Load Balancer
        api_response = api_instance.datacenters_networkloadbalancers_post(datacenter_id, network_load_balancer)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer** | [**NetworkLoadBalancer**](../models/NetworkLoadBalancer.md)| The Network Load Balancer to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NetworkLoadBalancer**](../models/NetworkLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_networkloadbalancers_put**
> NetworkLoadBalancer datacenters_networkloadbalancers_put(datacenter_id, network_load_balancer_id, network_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify Network Load Balancers

Modify the properties of the specified Network Load Balancer within the data center.

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
    api_instance = ionoscloud.NetworkLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    network_load_balancer_id = 'network_load_balancer_id_example' # str | The unique ID of the Network Load Balancer.
    network_load_balancer = ionoscloud.NetworkLoadBalancerPut() # NetworkLoadBalancerPut | The modified Network Load Balancer.
    try:
        # Modify Network Load Balancers
        api_response = api_instance.datacenters_networkloadbalancers_put(datacenter_id, network_load_balancer_id, network_load_balancer)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkLoadBalancersApi.datacenters_networkloadbalancers_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **network_load_balancer_id** | **str**| The unique ID of the Network Load Balancer. |  |
| **network_load_balancer** | [**NetworkLoadBalancerPut**](../models/NetworkLoadBalancerPut.md)| The modified Network Load Balancer. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NetworkLoadBalancer**](../models/NetworkLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

