# NATGatewaysApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_natgateways_delete**](NATGatewaysApi.md#datacenters_natgateways_delete) | **DELETE** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Remove a NAT gateway |
| [**datacenters_natgateways_find_by_nat_gateway_id**](NATGatewaysApi.md#datacenters_natgateways_find_by_nat_gateway_id) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Retrieve a NAT gateway |
| [**datacenters_natgateways_flowlogs_delete**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Remove Flow Log from NAT Gateway |
| [**datacenters_natgateways_flowlogs_find_by_flow_log_id**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_find_by_flow_log_id) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Retrieve a Flow Log of the NAT Gateway |
| [**datacenters_natgateways_flowlogs_get**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_get) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs | List NAT Gateway Flow Logs |
| [**datacenters_natgateways_flowlogs_patch**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Partially modify a Flow Log of the NAT Gateway |
| [**datacenters_natgateways_flowlogs_post**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_post) | **POST** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs | Add a NAT Gateways Flow Log |
| [**datacenters_natgateways_flowlogs_put**](NATGatewaysApi.md#datacenters_natgateways_flowlogs_put) | **PUT** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Modify a Flow Log of the NAT Gateway |
| [**datacenters_natgateways_get**](NATGatewaysApi.md#datacenters_natgateways_get) | **GET** /datacenters/{datacenterId}/natgateways | List NAT Gateways |
| [**datacenters_natgateways_patch**](NATGatewaysApi.md#datacenters_natgateways_patch) | **PATCH** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Partially update a NAT gateway |
| [**datacenters_natgateways_post**](NATGatewaysApi.md#datacenters_natgateways_post) | **POST** /datacenters/{datacenterId}/natgateways | Create a NAT Gateway |
| [**datacenters_natgateways_put**](NATGatewaysApi.md#datacenters_natgateways_put) | **PUT** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Update a NAT gateway |
| [**datacenters_natgateways_rules_delete**](NATGatewaysApi.md#datacenters_natgateways_rules_delete) | **DELETE** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Remove rule from NAT Gateway |
| [**datacenters_natgateways_rules_find_by_nat_gateway_rule_id**](NATGatewaysApi.md#datacenters_natgateways_rules_find_by_nat_gateway_rule_id) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Retrieve a NAT Gateway Rule |
| [**datacenters_natgateways_rules_get**](NATGatewaysApi.md#datacenters_natgateways_rules_get) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules | List NAT Gateways Rules |
| [**datacenters_natgateways_rules_patch**](NATGatewaysApi.md#datacenters_natgateways_rules_patch) | **PATCH** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Partially modify a rule of the NAT gateway |
| [**datacenters_natgateways_rules_post**](NATGatewaysApi.md#datacenters_natgateways_rules_post) | **POST** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules | Create a NAT Gateway Rule |
| [**datacenters_natgateways_rules_put**](NATGatewaysApi.md#datacenters_natgateways_rules_put) | **PUT** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Modify a rule of the NAT gateway |


# **datacenters_natgateways_delete**
> object datacenters_natgateways_delete(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Remove a NAT gateway

Removes the specified NAT gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Remove a NAT gateway
        api_response = api_instance.datacenters_natgateways_delete(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_delete: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Remove a NAT gateway
        api_response = api_instance.datacenters_natgateways_delete(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
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

# **datacenters_natgateways_find_by_nat_gateway_id**
> NatGateway datacenters_natgateways_find_by_nat_gateway_id(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a NAT gateway

Retrieves the attributes of a given NAT gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a NAT gateway
        api_response = api_instance.datacenters_natgateways_find_by_nat_gateway_id(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_find_by_nat_gateway_id: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a NAT gateway
        api_response = api_instance.datacenters_natgateways_find_by_nat_gateway_id(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_find_by_nat_gateway_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NatGateway**](NatGateway.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_delete**
> object datacenters_natgateways_flowlogs_delete(datacenter_id, nat_gateway_id, flow_log_id, pretty=pretty, depth=depth)

Remove Flow Log from NAT Gateway

This will remove a flow log from the NAT gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Remove Flow Log from NAT Gateway
        api_response = api_instance.datacenters_natgateways_flowlogs_delete(datacenter_id, nat_gateway_id, flow_log_id, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_delete: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Remove Flow Log from NAT Gateway
        api_response = api_instance.datacenters_natgateways_flowlogs_delete(datacenter_id, nat_gateway_id, flow_log_id, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **flow_log_id** | **str**| The unique ID of the flow log |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_find_by_flow_log_id**
> FlowLog datacenters_natgateways_flowlogs_find_by_flow_log_id(datacenter_id, nat_gateway_id, flow_log_id, pretty=pretty, depth=depth)

Retrieve a Flow Log of the NAT Gateway

This will return a Flow Log of the NAT Gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Retrieve a Flow Log of the NAT Gateway
        api_response = api_instance.datacenters_natgateways_flowlogs_find_by_flow_log_id(datacenter_id, nat_gateway_id, flow_log_id, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_find_by_flow_log_id: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Retrieve a Flow Log of the NAT Gateway
        api_response = api_instance.datacenters_natgateways_flowlogs_find_by_flow_log_id(datacenter_id, nat_gateway_id, flow_log_id, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_find_by_flow_log_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **flow_log_id** | **str**| The unique ID of the flow log |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_get**
> FlowLogs datacenters_natgateways_flowlogs_get(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, offset=offset, limit=limit)

List NAT Gateway Flow Logs

You can retrieve a list of Flow Logs of the NAT Gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # List NAT Gateway Flow Logs
        api_response = api_instance.datacenters_natgateways_flowlogs_get(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_get: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # List NAT Gateway Flow Logs
        api_response = api_instance.datacenters_natgateways_flowlogs_get(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with limit for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with offset for pagination) | [optional] [default to 1000] |

### Return type

[**FlowLogs**](FlowLogs.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_patch**
> FlowLog datacenters_natgateways_flowlogs_patch(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log_properties, pretty=pretty, depth=depth)

Partially modify a Flow Log of the NAT Gateway

You can use to partially update a Flow Log of a NAT Gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log
    nat_gateway_flow_log_properties = ionoscloud.FlowLogProperties() # FlowLogProperties | Properties of a Flow Log to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Partially modify a Flow Log of the NAT Gateway
        api_response = api_instance.datacenters_natgateways_flowlogs_patch(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log_properties, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_patch: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log
    nat_gateway_flow_log_properties = ionoscloud.FlowLogProperties() # FlowLogProperties | Properties of a Flow Log to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Partially modify a Flow Log of the NAT Gateway
        api_response = api_instance.datacenters_natgateways_flowlogs_patch(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log_properties, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **flow_log_id** | **str**| The unique ID of the flow log |  |
| **nat_gateway_flow_log_properties** | [**FlowLogProperties**](FlowLogProperties.md)| Properties of a Flow Log to be updated |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_post**
> FlowLog datacenters_natgateways_flowlogs_post(datacenter_id, nat_gateway_id, nat_gateway_flow_log, pretty=pretty, depth=depth)

Add a NAT Gateways Flow Log

This will add a new Flow Log to the NAT Gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_flow_log = ionoscloud.FlowLog() # FlowLog | Flow Log to add on NAT Gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Add a NAT Gateways Flow Log
        api_response = api_instance.datacenters_natgateways_flowlogs_post(datacenter_id, nat_gateway_id, nat_gateway_flow_log, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_post: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_flow_log = ionoscloud.FlowLog() # FlowLog | Flow Log to add on NAT Gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Add a NAT Gateways Flow Log
        api_response = api_instance.datacenters_natgateways_flowlogs_post(datacenter_id, nat_gateway_id, nat_gateway_flow_log, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **nat_gateway_flow_log** | [**FlowLog**](FlowLog.md)| Flow Log to add on NAT Gateway |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_natgateways_flowlogs_put**
> FlowLog datacenters_natgateways_flowlogs_put(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log, pretty=pretty, depth=depth)

Modify a Flow Log of the NAT Gateway

You can use to update a Flow Log of the NAT Gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log
    nat_gateway_flow_log = ionoscloud.FlowLogPut() # FlowLogPut | Modified NAT Gateway Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Modify a Flow Log of the NAT Gateway
        api_response = api_instance.datacenters_natgateways_flowlogs_put(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_put: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log
    nat_gateway_flow_log = ionoscloud.FlowLogPut() # FlowLogPut | Modified NAT Gateway Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Modify a Flow Log of the NAT Gateway
        api_response = api_instance.datacenters_natgateways_flowlogs_put(datacenter_id, nat_gateway_id, flow_log_id, nat_gateway_flow_log, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_flowlogs_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **flow_log_id** | **str**| The unique ID of the flow log |  |
| **nat_gateway_flow_log** | [**FlowLogPut**](FlowLogPut.md)| Modified NAT Gateway Flow Log |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_natgateways_get**
> NatGateways datacenters_natgateways_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List NAT Gateways

Retrieve a list of NAT Gateways within the datacenter.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List NAT Gateways
        api_response = api_instance.datacenters_natgateways_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_get: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List NAT Gateways
        api_response = api_instance.datacenters_natgateways_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NatGateways**](NatGateways.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_patch**
> NatGateway datacenters_natgateways_patch(datacenter_id, nat_gateway_id, nat_gateway_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially update a NAT gateway

Partially update the attributes of a given NAT gateway

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_properties = ionoscloud.NatGatewayProperties() # NatGatewayProperties | NAT gateway properties to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially update a NAT gateway
        api_response = api_instance.datacenters_natgateways_patch(datacenter_id, nat_gateway_id, nat_gateway_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_patch: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_properties = ionoscloud.NatGatewayProperties() # NatGatewayProperties | NAT gateway properties to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially update a NAT gateway
        api_response = api_instance.datacenters_natgateways_patch(datacenter_id, nat_gateway_id, nat_gateway_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **nat_gateway_properties** | [**NatGatewayProperties**](NatGatewayProperties.md)| NAT gateway properties to be updated |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NatGateway**](NatGateway.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_post**
> NatGateway datacenters_natgateways_post(datacenter_id, nat_gateway, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a NAT Gateway

Creates a NAT Gateway within the datacenter. User should be the contract owner or a admin or a user with createInternetAccess privilege

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway = ionoscloud.NatGateway() # NatGateway | NAT gateway to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a NAT Gateway
        api_response = api_instance.datacenters_natgateways_post(datacenter_id, nat_gateway, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_post: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway = ionoscloud.NatGateway() # NatGateway | NAT gateway to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a NAT Gateway
        api_response = api_instance.datacenters_natgateways_post(datacenter_id, nat_gateway, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway** | [**NatGateway**](NatGateway.md)| NAT gateway to be created |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NatGateway**](NatGateway.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_natgateways_put**
> NatGateway datacenters_natgateways_put(datacenter_id, nat_gateway_id, nat_gateway, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

Update a NAT gateway

Update the attributes of a given NAT gateway

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway = ionoscloud.NatGatewayPut() # NatGatewayPut | Modified NAT Gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # Update a NAT gateway
        api_response = api_instance.datacenters_natgateways_put(datacenter_id, nat_gateway_id, nat_gateway, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_put: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway = ionoscloud.NatGatewayPut() # NatGatewayPut | Modified NAT Gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # Update a NAT gateway
        api_response = api_instance.datacenters_natgateways_put(datacenter_id, nat_gateway_id, nat_gateway, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **nat_gateway** | [**NatGatewayPut**](NatGatewayPut.md)| Modified NAT Gateway |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with limit for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with offset for pagination) | [optional] [default to 1000] |

### Return type

[**NatGateway**](NatGateway.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_natgateways_rules_delete**
> object datacenters_natgateways_rules_delete(datacenter_id, nat_gateway_id, nat_gateway_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Remove rule from NAT Gateway

This will remove a rule from the NAT gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT gateway rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Remove rule from NAT Gateway
        api_response = api_instance.datacenters_natgateways_rules_delete(datacenter_id, nat_gateway_id, nat_gateway_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_delete: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT gateway rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Remove rule from NAT Gateway
        api_response = api_instance.datacenters_natgateways_rules_delete(datacenter_id, nat_gateway_id, nat_gateway_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **nat_gateway_rule_id** | **str**| The unique ID of the NAT gateway rule |  |
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

# **datacenters_natgateways_rules_find_by_nat_gateway_rule_id**
> NatGatewayRule datacenters_natgateways_rules_find_by_nat_gateway_rule_id(datacenter_id, nat_gateway_id, nat_gateway_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a NAT Gateway Rule

Retrieves the attributes of a given NAT gateway rule.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT gateway rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a NAT Gateway Rule
        api_response = api_instance.datacenters_natgateways_rules_find_by_nat_gateway_rule_id(datacenter_id, nat_gateway_id, nat_gateway_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_find_by_nat_gateway_rule_id: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT gateway rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a NAT Gateway Rule
        api_response = api_instance.datacenters_natgateways_rules_find_by_nat_gateway_rule_id(datacenter_id, nat_gateway_id, nat_gateway_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_find_by_nat_gateway_rule_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **nat_gateway_rule_id** | **str**| The unique ID of the NAT gateway rule |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NatGatewayRule**](NatGatewayRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_rules_get**
> NatGatewayRules datacenters_natgateways_rules_get(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List NAT Gateways Rules

Retrieve a list of rules of a NAT Gateway within the datacenter.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List NAT Gateways Rules
        api_response = api_instance.datacenters_natgateways_rules_get(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_get: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List NAT Gateways Rules
        api_response = api_instance.datacenters_natgateways_rules_get(datacenter_id, nat_gateway_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NatGatewayRules**](NatGatewayRules.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_rules_patch**
> NatGatewayRule datacenters_natgateways_rules_patch(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a rule of the NAT gateway

You can use to partially update a rule of a NAT gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT gateway rule
    nat_gateway_rule_properties = ionoscloud.NatGatewayRuleProperties() # NatGatewayRuleProperties | Properties of a NAT gateway rule to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify a rule of the NAT gateway
        api_response = api_instance.datacenters_natgateways_rules_patch(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_patch: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT gateway rule
    nat_gateway_rule_properties = ionoscloud.NatGatewayRuleProperties() # NatGatewayRuleProperties | Properties of a NAT gateway rule to be updated
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify a rule of the NAT gateway
        api_response = api_instance.datacenters_natgateways_rules_patch(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **nat_gateway_rule_id** | **str**| The unique ID of the NAT gateway rule |  |
| **nat_gateway_rule_properties** | [**NatGatewayRuleProperties**](NatGatewayRuleProperties.md)| Properties of a NAT gateway rule to be updated |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NatGatewayRule**](NatGatewayRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_natgateways_rules_post**
> NatGatewayRule datacenters_natgateways_rules_post(datacenter_id, nat_gateway_id, nat_gateway_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a NAT Gateway Rule

Creates a rule within the NAT Gateway of a datacenter.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_rule = ionoscloud.NatGatewayRule() # NatGatewayRule | NAT gateway rule to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a NAT Gateway Rule
        api_response = api_instance.datacenters_natgateways_rules_post(datacenter_id, nat_gateway_id, nat_gateway_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_post: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_rule = ionoscloud.NatGatewayRule() # NatGatewayRule | NAT gateway rule to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a NAT Gateway Rule
        api_response = api_instance.datacenters_natgateways_rules_post(datacenter_id, nat_gateway_id, nat_gateway_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **nat_gateway_rule** | [**NatGatewayRule**](NatGatewayRule.md)| NAT gateway rule to be created |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NatGatewayRule**](NatGatewayRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_natgateways_rules_put**
> NatGatewayRule datacenters_natgateways_rules_put(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a rule of the NAT gateway

You can use to update a rule of the NAT gateway.

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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT gateway rule
    nat_gateway_rule = ionoscloud.NatGatewayRulePut() # NatGatewayRulePut | Modified NAT Gateway Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a rule of the NAT gateway
        api_response = api_instance.datacenters_natgateways_rules_put(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_put: %s\n' % e)
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
    api_instance = ionoscloud.NATGatewaysApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    nat_gateway_id = 'nat_gateway_id_example' # str | The unique ID of the NAT gateway
    nat_gateway_rule_id = 'nat_gateway_rule_id_example' # str | The unique ID of the NAT gateway rule
    nat_gateway_rule = ionoscloud.NatGatewayRulePut() # NatGatewayRulePut | Modified NAT Gateway Rule
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a rule of the NAT gateway
        api_response = api_instance.datacenters_natgateways_rules_put(datacenter_id, nat_gateway_id, nat_gateway_rule_id, nat_gateway_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NATGatewaysApi.datacenters_natgateways_rules_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **nat_gateway_id** | **str**| The unique ID of the NAT gateway |  |
| **nat_gateway_rule_id** | **str**| The unique ID of the NAT gateway rule |  |
| **nat_gateway_rule** | [**NatGatewayRulePut**](NatGatewayRulePut.md)| Modified NAT Gateway Rule |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**NatGatewayRule**](NatGatewayRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

