# NATGatewaysApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_natgateways_delete**](NATGatewaysApi.md#datacenters_natgateways_delete) | **DELETE** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Delete NAT Gateways |
| [**datacenters_natgateways_find_by_nat_gateway_id**](NATGatewaysApi.md#datacenters_natgateways_find_by_nat_gateway_id) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Retrieve NAT Gateways |
| [**datacenters_natgateways_flowlogs_delete**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Delete NAT Gateway Flow Logs |
| [**datacenters_natgateways_flowlogs_find_by_flow_log_id**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_find_by_flow_log_id) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Retrieve NAT Gateway Flow Logs |
| [**datacenters_natgateways_flowlogs_get**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_get) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs | List NAT Gateway Flow Logs |
| [**datacenters_natgateways_flowlogs_patch**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Partially modify NAT Gateway Flow Logs |
| [**datacenters_natgateways_flowlogs_post**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_post) | **POST** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs | Create NAT Gateway Flow Logs |
| [**datacenters_natgateways_flowlogs_put**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_put) | **PUT** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Modify NAT Gateway Flow Logs |
| [**datacenters_natgateways_get**](NATGatewaysApi.md#datacenters_natgateways_get) | **GET** /datacenters/{datacenterId}/natgateways | List NAT Gateways |
| [**datacenters_natgateways_patch**](NATGatewaysApi.md#datacenters_natgateways_patch) | **PATCH** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Partially modify NAT Gateways |
| [**datacenters_natgateways_post**](NATGatewaysApi.md#datacenters_natgateways_post) | **POST** /datacenters/{datacenterId}/natgateways | Create NAT Gateways |
| [**datacenters_natgateways_put**](NATGatewaysApi.md#datacenters_natgateways_put) | **PUT** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Modify NAT Gateways |
| [**datacenters_natgateways_rules_delete**](NATGatewaysApi.md#datacenters_natgateways_rules_delete) | **DELETE** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Delete NAT Gateway rules |
| [**datacenters_natgateways_rules_find_by_nat_gateway_rule_id**](NATGatewaysApi.md#datacenters_natgateways_rules_find_by_nat_gateway_rule_id) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Retrieve NAT Gateway rules |
| [**datacenters_natgateways_rules_get**](NATGatewaysApi.md#datacenters_natgateways_rules_get) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules | List NAT Gateway rules |
| [**datacenters_natgateways_rules_patch**](NATGatewaysApi.md#datacenters_natgateways_rules_patch) | **PATCH** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Partially modify NAT Gateway rules |
| [**datacenters_natgateways_rules_post**](NATGatewaysApi.md#datacenters_natgateways_rules_post) | **POST** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules | Create NAT Gateway rules |
| [**datacenters_natgateways_rules_put**](NATGatewaysApi.md#datacenters_natgateways_rules_put) | **PUT** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Modify NAT Gateway rules |


# **datacenters_natgateways_delete**
> datacenters_natgateways_delete(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete NAT Gateways

Remove the specified NAT Gateway from the data center.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    try:
        # Delete NAT Gateways
        api_instance.datacenters_natgateways_delete(datacenter_id, nat_gateway_id)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
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

# **datacenters_natgateways_find_by_nat_gateway_id**
> NatGateway datacenters_natgateways_find_by_nat_gateway_id(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve NAT Gateways

Retrieve the properties of the specified NAT Gateway within the data center.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    try:
        # Retrieve NAT Gateways
        api_response = api_instance.datacenters_natgateways_find_by_nat_gateway_id(datacenter_id, nat_gateway_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_find_by_nat_gateway_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NatGateway**](../models/NatGateway.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_delete**
> datacenters_natgateways_flowlogs_delete(datacenter_id, nat_gateway_id, flow_log_id, pretty=pretty, depth=depth)

Delete NAT Gateway Flow Logs

Delete the specified NAT Gateway Flow Log.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log.
    try:
        # Delete NAT Gateway Flow Logs
        api_instance.datacenters_natgateways_flowlogs_delete(datacenter_id, nat_gateway_id, flow_log_id)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

void (empty response body)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_find_by_flow_log_id**
> FlowLog datacenters_natgateways_flowlogs_find_by_flow_log_id(datacenter_id, nat_gateway_id, flow_log_id, pretty=pretty, depth=depth)

Retrieve NAT Gateway Flow Logs

Retrieve the specified NAT Gateway Flow Log.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log.
    try:
        # Retrieve NAT Gateway Flow Logs
        api_response = api_instance.datacenters_natgateways_flowlogs_find_by_flow_log_id(datacenter_id, nat_gateway_id, flow_log_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_find_by_flow_log_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](../models/FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_get**
> FlowLogs datacenters_natgateways_flowlogs_get(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, offset=offset, limit=limit)

List NAT Gateway Flow Logs

List all the Flow Logs for the specified NAT Gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    try:
        # List NAT Gateway Flow Logs
        api_response = api_instance.datacenters_natgateways_flowlogs_get(datacenter_id, nat_gateway_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000] |

### Return type

[**FlowLogs**](../models/FlowLogs.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_patch**
> FlowLog datacenters_natgateways_flowlogs_patch(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log_properties, pretty=pretty, depth=depth)

Partially modify NAT Gateway Flow Logs

Update the properties of the specified NAT Gateway Flow Log.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log.
    nat_gateway_flow_log_properties = ionoscloud.FlowLogProperties() # FlowLogProperties | The properties of the Flow Log to be updated.
    try:
        # Partially modify NAT Gateway Flow Logs
        api_response = api_instance.datacenters_natgateways_flowlogs_patch(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log_properties)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log. |  |
| **nat_gateway_flow_log_properties** | [**FlowLogProperties**](FlowLogProperties.md)| The properties of the Flow Log to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](../models/FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_post**
> FlowLog datacenters_natgateways_flowlogs_post(datacenter_id, nat_gateway_id, nat_gateway_flow_log, pretty=pretty, depth=depth)

Create NAT Gateway Flow Logs

Add a new Flow Log for the specified NAT Gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    nat_gateway_flow_log = ionoscloud.FlowLog() # FlowLog | The Flow Log to create.
    try:
        # Create NAT Gateway Flow Logs
        api_response = api_instance.datacenters_natgateways_flowlogs_post(datacenter_id, nat_gateway_id, nat_gateway_flow_log)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **nat_gateway_flow_log** | [**FlowLog**](FlowLog.md)| The Flow Log to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](../models/FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_put**
> FlowLog datacenters_natgateways_flowlogs_put(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log, pretty=pretty, depth=depth)

Modify NAT Gateway Flow Logs

Modify the specified NAT Gateway Flow Log.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the Flow Log.
    nat_gateway_flow_log = ionoscloud.FlowLogPut() # FlowLogPut | The modified NAT Gateway Flow Log.
    try:
        # Modify NAT Gateway Flow Logs
        api_response = api_instance.datacenters_natgateways_flowlogs_put(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **flow_log_id** | **str**| The unique ID of the Flow Log. |  |
| **nat_gateway_flow_log** | [**FlowLogPut**](FlowLogPut.md)| The modified NAT Gateway Flow Log. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](../models/FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_natgateways_get**
> NatGateways datacenters_natgateways_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List NAT Gateways

List all NAT Gateways within the data center.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    try:
        # List NAT Gateways
        api_response = api_instance.datacenters_natgateways_get(datacenter_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NatGateways**](../models/NatGateways.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_patch**
> NatGateway datacenters_natgateways_patch(datacenter_id, nat_gateway_id, nat_gateway_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify NAT Gateways

Update the properties of the specified NAT Gateway within the data center.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    nat_gateway_properties = ionoscloud.NatGatewayProperties() # NatGatewayProperties | The properties of the NAT Gateway to be updated.
    try:
        # Partially modify NAT Gateways
        api_response = api_instance.datacenters_natgateways_patch(datacenter_id, nat_gateway_id, nat_gateway_properties)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **nat_gateway_properties** | [**NatGatewayProperties**](NatGatewayProperties.md)| The properties of the NAT Gateway to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NatGateway**](../models/NatGateway.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_post**
> NatGateway datacenters_natgateways_post(datacenter_id, nat_gateway, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create NAT Gateways

Create a NAT Gateway within the data center.  This operation is restricted to contract owner, admin, and users with 'createInternetAccess' privileges.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway = ionoscloud.NatGateway() # NatGateway | The NAT Gateway to create.
    try:
        # Create NAT Gateways
        api_response = api_instance.datacenters_natgateways_post(datacenter_id, nat_gateway)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway** | [**NatGateway**](NatGateway.md)| The NAT Gateway to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NatGateway**](../models/NatGateway.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_natgateways_put**
> NatGateway datacenters_natgateways_put(datacenter_id, nat_gateway_id, nat_gateway, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify NAT Gateways

Modify the properties of the specified NAT Gateway within the data center.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    nat_gateway = ionoscloud.NatGatewayPut() # NatGatewayPut | The modified NAT Gateway.
    try:
        # Modify NAT Gateways
        api_response = api_instance.datacenters_natgateways_put(datacenter_id, nat_gateway_id, nat_gateway)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **nat_gateway** | [**NatGatewayPut**](NatGatewayPut.md)| The modified NAT Gateway. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NatGateway**](../models/NatGateway.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_natgateways_rules_delete**
> datacenters_natgateways_rules_delete(datacenter_id, nat_gateway_id, nat_gateway_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete NAT Gateway rules

Delete the specified NAT Gateway rule.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT Gateway rule.
    try:
        # Delete NAT Gateway rules
        api_instance.datacenters_natgateways_rules_delete(datacenter_id, nat_gateway_id, nat_gateway_rule_id)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **nat_gateway_rule_id** | **str**| The unique ID of the NAT Gateway rule. |  |
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

# **datacenters_natgateways_rules_find_by_nat_gateway_rule_id**
> NatGatewayRule datacenters_natgateways_rules_find_by_nat_gateway_rule_id(datacenter_id, nat_gateway_id, nat_gateway_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve NAT Gateway rules

Retrieve the properties of the specified NAT Gateway rule.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT Gateway rule.
    try:
        # Retrieve NAT Gateway rules
        api_response = api_instance.datacenters_natgateways_rules_find_by_nat_gateway_rule_id(datacenter_id, nat_gateway_id, nat_gateway_rule_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_find_by_nat_gateway_rule_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **nat_gateway_rule_id** | **str**| The unique ID of the NAT Gateway rule. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NatGatewayRule**](../models/NatGatewayRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_rules_get**
> NatGatewayRules datacenters_natgateways_rules_get(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List NAT Gateway rules

List all rules for the specified NAT Gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    try:
        # List NAT Gateway rules
        api_response = api_instance.datacenters_natgateways_rules_get(datacenter_id, nat_gateway_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NatGatewayRules**](../models/NatGatewayRules.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_rules_patch**
> NatGatewayRule datacenters_natgateways_rules_patch(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify NAT Gateway rules

Update the properties of the specified NAT Gateway rule.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT Gateway rule.
    nat_gateway_rule_properties = ionoscloud.NatGatewayRuleProperties() # NatGatewayRuleProperties | The properties of the NAT Gateway rule to be updated.
    try:
        # Partially modify NAT Gateway rules
        api_response = api_instance.datacenters_natgateways_rules_patch(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule_properties)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **nat_gateway_rule_id** | **str**| The unique ID of the NAT Gateway rule. |  |
| **nat_gateway_rule_properties** | [**NatGatewayRuleProperties**](NatGatewayRuleProperties.md)| The properties of the NAT Gateway rule to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NatGatewayRule**](../models/NatGatewayRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_rules_post**
> NatGatewayRule datacenters_natgateways_rules_post(datacenter_id, nat_gateway_id, nat_gateway_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create NAT Gateway rules

Create a rule for the specified NAT Gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    nat_gateway_rule = ionoscloud.NatGatewayRule() # NatGatewayRule | The NAT Gateway rule to create.
    try:
        # Create NAT Gateway rules
        api_response = api_instance.datacenters_natgateways_rules_post(datacenter_id, nat_gateway_id, nat_gateway_rule)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **nat_gateway_rule** | [**NatGatewayRule**](NatGatewayRule.md)| The NAT Gateway rule to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NatGatewayRule**](../models/NatGatewayRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_natgateways_rules_put**
> NatGatewayRule datacenters_natgateways_rules_put(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify NAT Gateway rules

Modify the specified NAT Gateway rule.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT Gateway.
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT Gateway rule.
    nat_gateway_rule = ionoscloud.NatGatewayRulePut() # NatGatewayRulePut | The modified NAT Gateway rule.
    try:
        # Modify NAT Gateway rules
        api_response = api_instance.datacenters_natgateways_rules_put(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT Gateway. |  |
| **nat_gateway_rule_id** | **str**| The unique ID of the NAT Gateway rule. |  |
| **nat_gateway_rule** | [**NatGatewayRulePut**](NatGatewayRulePut.md)| The modified NAT Gateway rule. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**NatGatewayRule**](../models/NatGatewayRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

