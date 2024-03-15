# ApplicationLoadBalancersApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_applicationloadbalancers_delete**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_delete) | **DELETE** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Delete an Application Load Balancer by ID |
| [**datacenters_applicationloadbalancers_find_by_application_load_balancer_id**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_find_by_application_load_balancer_id) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Get an Application Load Balancer by ID |
| [**datacenters_applicationloadbalancers_flowlogs_delete**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Delete an ALB Flow Log by ID |
| [**datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Get an ALB Flow Log by ID |
| [**datacenters_applicationloadbalancers_flowlogs_get**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_get) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs | Get ALB Flow Logs |
| [**datacenters_applicationloadbalancers_flowlogs_patch**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Partially Modify an ALB Flow Log by ID |
| [**datacenters_applicationloadbalancers_flowlogs_post**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_post) | **POST** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs | Create an ALB Flow Log |
| [**datacenters_applicationloadbalancers_flowlogs_put**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_put) | **PUT** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Modify an ALB Flow Log by ID |
| [**datacenters_applicationloadbalancers_forwardingrules_delete**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_delete) | **DELETE** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Delete an ALB Forwarding Rule by ID |
| [**datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Get an ALB Forwarding Rule by ID |
| [**datacenters_applicationloadbalancers_forwardingrules_get**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_get) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules | Get ALB Forwarding Rules |
| [**datacenters_applicationloadbalancers_forwardingrules_patch**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_patch) | **PATCH** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Partially modify an ALB Forwarding Rule by ID |
| [**datacenters_applicationloadbalancers_forwardingrules_post**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_post) | **POST** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules | Create an ALB Forwarding Rule |
| [**datacenters_applicationloadbalancers_forwardingrules_put**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_put) | **PUT** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Modify an ALB Forwarding Rule by ID |
| [**datacenters_applicationloadbalancers_get**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_get) | **GET** /datacenters/{datacenterId}/applicationloadbalancers | Get Application Load Balancers |
| [**datacenters_applicationloadbalancers_patch**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_patch) | **PATCH** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Partially Modify an Application Load Balancer by ID |
| [**datacenters_applicationloadbalancers_post**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_post) | **POST** /datacenters/{datacenterId}/applicationloadbalancers | Create an Application Load Balancer |
| [**datacenters_applicationloadbalancers_put**](ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_put) | **PUT** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Modify an Application Load Balancer by ID |


# **datacenters_applicationloadbalancers_delete**
> datacenters_applicationloadbalancers_delete(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete an Application Load Balancer by ID

Removes the specified Application Load Balancer from the data center.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    try:
        # Delete an Application Load Balancer by ID
        api_instance.datacenters_applicationloadbalancers_delete(datacenter_id, application_load_balancer_id)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
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

# **datacenters_applicationloadbalancers_find_by_application_load_balancer_id**
> ApplicationLoadBalancer datacenters_applicationloadbalancers_find_by_application_load_balancer_id(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get an Application Load Balancer by ID

Retrieves the properties of the specified Application Load Balancer within the data center.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    try:
        # Get an Application Load Balancer by ID
        api_response = api_instance.datacenters_applicationloadbalancers_find_by_application_load_balancer_id(datacenter_id, application_load_balancer_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_find_by_application_load_balancer_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ApplicationLoadBalancer**](../models/ApplicationLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_applicationloadbalancers_flowlogs_delete**
> datacenters_applicationloadbalancers_flowlogs_delete(datacenter_id, application_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete an ALB Flow Log by ID

Deletes the Application Load Balancer flow log specified by its ID.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log.
    try:
        # Delete an ALB Flow Log by ID
        api_instance.datacenters_applicationloadbalancers_flowlogs_delete(datacenter_id, application_load_balancer_id, flow_log_id)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_flowlogs_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **flow_log_id** | **str**| The unique ID of the flow log. |  |
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

# **datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id**
> FlowLog datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, application_load_balancer_id, flow_log_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get an ALB Flow Log by ID

Retrieves the Application Load Balancer flow log specified by its ID.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log.
    try:
        # Get an ALB Flow Log by ID
        api_response = api_instance.datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, application_load_balancer_id, flow_log_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **flow_log_id** | **str**| The unique ID of the flow log. |  |
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

# **datacenters_applicationloadbalancers_flowlogs_get**
> FlowLogs datacenters_applicationloadbalancers_flowlogs_get(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get ALB Flow Logs

Retrieves the flow logs for the specified Application Load Balancer.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    try:
        # Get ALB Flow Logs
        api_response = api_instance.datacenters_applicationloadbalancers_flowlogs_get(datacenter_id, application_load_balancer_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_flowlogs_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
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

# **datacenters_applicationloadbalancers_flowlogs_patch**
> FlowLog datacenters_applicationloadbalancers_flowlogs_patch(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially Modify an ALB Flow Log by ID

Updates the properties of the Application Load Balancer flow log specified by its ID.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log.
    application_load_balancer_flow_log_properties = ionoscloud.FlowLogProperties() # FlowLogProperties | The properties of the ALB flow log to be updated.
    try:
        # Partially Modify an ALB Flow Log by ID
        api_response = api_instance.datacenters_applicationloadbalancers_flowlogs_patch(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log_properties)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_flowlogs_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **flow_log_id** | **str**| The unique ID of the flow log. |  |
| **application_load_balancer_flow_log_properties** | [**FlowLogProperties**](../models/FlowLogProperties.md)| The properties of the ALB flow log to be updated. |  |
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

# **datacenters_applicationloadbalancers_flowlogs_post**
> FlowLog datacenters_applicationloadbalancers_flowlogs_post(datacenter_id, application_load_balancer_id, application_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create an ALB Flow Log

Creates a flow log for the Application Load Balancer specified by ID.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    application_load_balancer_flow_log = ionoscloud.FlowLog() # FlowLog | The flow log to create.
    try:
        # Create an ALB Flow Log
        api_response = api_instance.datacenters_applicationloadbalancers_flowlogs_post(datacenter_id, application_load_balancer_id, application_load_balancer_flow_log)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_flowlogs_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **application_load_balancer_flow_log** | [**FlowLog**](../models/FlowLog.md)| The flow log to create. |  |
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

# **datacenters_applicationloadbalancers_flowlogs_put**
> FlowLog datacenters_applicationloadbalancers_flowlogs_put(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify an ALB Flow Log by ID

Modifies the Application Load Balancer flow log specified by its ID.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    flow_log_id = 'flow_log_id_example' # str | The unique ID of the flow log.
    application_load_balancer_flow_log = ionoscloud.FlowLogPut() # FlowLogPut | The modified ALB flow log.
    try:
        # Modify an ALB Flow Log by ID
        api_response = api_instance.datacenters_applicationloadbalancers_flowlogs_put(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_flowlogs_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **flow_log_id** | **str**| The unique ID of the flow log. |  |
| **application_load_balancer_flow_log** | [**FlowLogPut**](../models/FlowLogPut.md)| The modified ALB flow log. |  |
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

# **datacenters_applicationloadbalancers_forwardingrules_delete**
> datacenters_applicationloadbalancers_forwardingrules_delete(datacenter_id, application_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete an ALB Forwarding Rule by ID

Deletes the Application Load Balancer forwarding rule specified by its ID.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    try:
        # Delete an ALB Forwarding Rule by ID
        api_instance.datacenters_applicationloadbalancers_forwardingrules_delete(datacenter_id, application_load_balancer_id, forwarding_rule_id)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_forwardingrules_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
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

# **datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id**
> ApplicationLoadBalancerForwardingRule datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, application_load_balancer_id, forwarding_rule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get an ALB Forwarding Rule by ID

Retrieves the Application Load Balancer forwarding rule specified by its ID.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    try:
        # Get an ALB Forwarding Rule by ID
        api_response = api_instance.datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, application_load_balancer_id, forwarding_rule_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ApplicationLoadBalancerForwardingRule**](../models/ApplicationLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_applicationloadbalancers_forwardingrules_get**
> ApplicationLoadBalancerForwardingRules datacenters_applicationloadbalancers_forwardingrules_get(datacenter_id, application_load_balancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get ALB Forwarding Rules

Lists the forwarding rules of the specified Application Load Balancer.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    try:
        # Get ALB Forwarding Rules
        api_response = api_instance.datacenters_applicationloadbalancers_forwardingrules_get(datacenter_id, application_load_balancer_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_forwardingrules_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ApplicationLoadBalancerForwardingRules**](../models/ApplicationLoadBalancerForwardingRules.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_applicationloadbalancers_forwardingrules_patch**
> ApplicationLoadBalancerForwardingRule datacenters_applicationloadbalancers_forwardingrules_patch(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify an ALB Forwarding Rule by ID

Updates the properties of the Application Load Balancer forwarding rule specified by its ID.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    application_load_balancer_forwarding_rule_properties = ionoscloud.ApplicationLoadBalancerForwardingRuleProperties() # ApplicationLoadBalancerForwardingRuleProperties | The properties of the forwarding rule to be updated.
    try:
        # Partially modify an ALB Forwarding Rule by ID
        api_response = api_instance.datacenters_applicationloadbalancers_forwardingrules_patch(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule_properties)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_forwardingrules_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. |  |
| **application_load_balancer_forwarding_rule_properties** | [**ApplicationLoadBalancerForwardingRuleProperties**](../models/ApplicationLoadBalancerForwardingRuleProperties.md)| The properties of the forwarding rule to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ApplicationLoadBalancerForwardingRule**](../models/ApplicationLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_applicationloadbalancers_forwardingrules_post**
> ApplicationLoadBalancerForwardingRule datacenters_applicationloadbalancers_forwardingrules_post(datacenter_id, application_load_balancer_id, application_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create an ALB Forwarding Rule

Creates a forwarding rule for the specified Application Load Balancer.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    application_load_balancer_forwarding_rule = ionoscloud.ApplicationLoadBalancerForwardingRule() # ApplicationLoadBalancerForwardingRule | The forwarding rule to create.
    try:
        # Create an ALB Forwarding Rule
        api_response = api_instance.datacenters_applicationloadbalancers_forwardingrules_post(datacenter_id, application_load_balancer_id, application_load_balancer_forwarding_rule)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_forwardingrules_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **application_load_balancer_forwarding_rule** | [**ApplicationLoadBalancerForwardingRule**](../models/ApplicationLoadBalancerForwardingRule.md)| The forwarding rule to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ApplicationLoadBalancerForwardingRule**](../models/ApplicationLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_applicationloadbalancers_forwardingrules_put**
> ApplicationLoadBalancerForwardingRule datacenters_applicationloadbalancers_forwardingrules_put(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify an ALB Forwarding Rule by ID

Modifies the Application Load Balancer forwarding rule specified by its ID.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    forwarding_rule_id = 'forwarding_rule_id_example' # str | The unique ID of the forwarding rule.
    application_load_balancer_forwarding_rule = ionoscloud.ApplicationLoadBalancerForwardingRulePut() # ApplicationLoadBalancerForwardingRulePut | The modified ALB forwarding rule.
    try:
        # Modify an ALB Forwarding Rule by ID
        api_response = api_instance.datacenters_applicationloadbalancers_forwardingrules_put(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_forwardingrules_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **forwarding_rule_id** | **str**| The unique ID of the forwarding rule. |  |
| **application_load_balancer_forwarding_rule** | [**ApplicationLoadBalancerForwardingRulePut**](../models/ApplicationLoadBalancerForwardingRulePut.md)| The modified ALB forwarding rule. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ApplicationLoadBalancerForwardingRule**](../models/ApplicationLoadBalancerForwardingRule.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_applicationloadbalancers_get**
> ApplicationLoadBalancers datacenters_applicationloadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

Get Application Load Balancers

Lists all Application Load Balancers within a data center.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    try:
        # Get Application Load Balancers
        api_response = api_instance.datacenters_applicationloadbalancers_get(datacenter_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_get: %s\n' % e)
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

[**ApplicationLoadBalancers**](../models/ApplicationLoadBalancers.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_applicationloadbalancers_patch**
> ApplicationLoadBalancer datacenters_applicationloadbalancers_patch(datacenter_id, application_load_balancer_id, application_load_balancer_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially Modify an Application Load Balancer by ID

Updates the properties of the specified Application Load Balancer within the data center.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    application_load_balancer_properties = ionoscloud.ApplicationLoadBalancerProperties() # ApplicationLoadBalancerProperties | The Application Load Balancer properties to be updated.
    try:
        # Partially Modify an Application Load Balancer by ID
        api_response = api_instance.datacenters_applicationloadbalancers_patch(datacenter_id, application_load_balancer_id, application_load_balancer_properties)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **application_load_balancer_properties** | [**ApplicationLoadBalancerProperties**](../models/ApplicationLoadBalancerProperties.md)| The Application Load Balancer properties to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ApplicationLoadBalancer**](../models/ApplicationLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_applicationloadbalancers_post**
> ApplicationLoadBalancer datacenters_applicationloadbalancers_post(datacenter_id, application_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create an Application Load Balancer

Creates an Application Load Balancer within the data center.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer = ionoscloud.ApplicationLoadBalancer() # ApplicationLoadBalancer | The Application Load Balancer to create.
    try:
        # Create an Application Load Balancer
        api_response = api_instance.datacenters_applicationloadbalancers_post(datacenter_id, application_load_balancer)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer** | [**ApplicationLoadBalancer**](../models/ApplicationLoadBalancer.md)| The Application Load Balancer to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ApplicationLoadBalancer**](../models/ApplicationLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_applicationloadbalancers_put**
> ApplicationLoadBalancer datacenters_applicationloadbalancers_put(datacenter_id, application_load_balancer_id, application_load_balancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify an Application Load Balancer by ID

Modifies the properties of the specified Application Load Balancer within the data center.

### Example

```python
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
    api_instance = ionoscloud.ApplicationLoadBalancersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    application_load_balancer_id = 'application_load_balancer_id_example' # str | The unique ID of the Application Load Balancer.
    application_load_balancer = ionoscloud.ApplicationLoadBalancerPut() # ApplicationLoadBalancerPut | The modified Application Load Balancer.
    try:
        # Modify an Application Load Balancer by ID
        api_response = api_instance.datacenters_applicationloadbalancers_put(datacenter_id, application_load_balancer_id, application_load_balancer)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ApplicationLoadBalancersApi.datacenters_applicationloadbalancers_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **application_load_balancer_id** | **str**| The unique ID of the Application Load Balancer. |  |
| **application_load_balancer** | [**ApplicationLoadBalancerPut**](../models/ApplicationLoadBalancerPut.md)| The modified Application Load Balancer. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ApplicationLoadBalancer**](../models/ApplicationLoadBalancer.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

