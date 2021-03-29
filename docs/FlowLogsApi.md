# FlowLogsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_servers_nics_flowlogs_delete**](FlowLogsApi.md#datacenters_servers_nics_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs/{flowlogId} | Delete a Flow Log |
| [**datacenters_servers_nics_flowlogs_find_by_id**](FlowLogsApi.md#datacenters_servers_nics_flowlogs_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs/{flowlogId} | Retrieve a Flow Log |
| [**datacenters_servers_nics_flowlogs_get**](FlowLogsApi.md#datacenters_servers_nics_flowlogs_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs | List Flow Logs |
| [**datacenters_servers_nics_flowlogs_patch**](FlowLogsApi.md#datacenters_servers_nics_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs/{flowlogId} | Partially update a Flow Log |
| [**datacenters_servers_nics_flowlogs_post**](FlowLogsApi.md#datacenters_servers_nics_flowlogs_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs | Create a Flow Log |
| [**datacenters_servers_nics_flowlogs_put**](FlowLogsApi.md#datacenters_servers_nics_flowlogs_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs/{flowlogId} | Modify a Flow Log |


# **datacenters_servers_nics_flowlogs_delete**
> object datacenters_servers_nics_flowlogs_delete(datacenter_id, server_id, nic_id, flowlog_id, pretty=pretty, depth=depth)

Delete a Flow Log

Removes the specified Flow Log.

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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    flowlog_id = 'flowlog_id_example' # str | The unique ID of the Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Delete a Flow Log
        api_response = api_instance.datacenters_servers_nics_flowlogs_delete(datacenter_id, server_id, nic_id, flowlog_id, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_delete: %s\n' % e)
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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    flowlog_id = 'flowlog_id_example' # str | The unique ID of the Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Delete a Flow Log
        api_response = api_instance.datacenters_servers_nics_flowlogs_delete(datacenter_id, server_id, nic_id, flowlog_id, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **flowlog_id** | **str**| The unique ID of the Flow Log |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_flowlogs_find_by_id**
> FlowLog datacenters_servers_nics_flowlogs_find_by_id(datacenter_id, server_id, nic_id, flowlog_id, pretty=pretty, depth=depth)

Retrieve a Flow Log

Retrieves the attributes of a given Flow Log.

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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    flowlog_id = 'flowlog_id_example' # str | The unique ID of the Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Retrieve a Flow Log
        api_response = api_instance.datacenters_servers_nics_flowlogs_find_by_id(datacenter_id, server_id, nic_id, flowlog_id, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_find_by_id: %s\n' % e)
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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    flowlog_id = 'flowlog_id_example' # str | The unique ID of the Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Retrieve a Flow Log
        api_response = api_instance.datacenters_servers_nics_flowlogs_find_by_id(datacenter_id, server_id, nic_id, flowlog_id, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **flowlog_id** | **str**| The unique ID of the Flow Log |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_flowlogs_get**
> FlowLogs datacenters_servers_nics_flowlogs_get(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, offset=offset, limit=limit)

List Flow Logs

Retrieves a list of Flow Logs associated with a particular network interface.

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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # List Flow Logs
        api_response = api_instance.datacenters_servers_nics_flowlogs_get(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_get: %s\n' % e)
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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # List Flow Logs
        api_response = api_instance.datacenters_servers_nics_flowlogs_get(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
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

# **datacenters_servers_nics_flowlogs_patch**
> FlowLog datacenters_servers_nics_flowlogs_patch(datacenter_id, server_id, nic_id, flowlog_id, flowlog, pretty=pretty, depth=depth)

Partially update a Flow Log

This will partially update a Flow Log record.

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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    flowlog_id = 'flowlog_id_example' # str | The unique ID of the Flow Log
    flowlog = ionoscloud.FlowLogProperties() # FlowLogProperties | Modified Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Partially update a Flow Log
        api_response = api_instance.datacenters_servers_nics_flowlogs_patch(datacenter_id, server_id, nic_id, flowlog_id, flowlog, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_patch: %s\n' % e)
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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    flowlog_id = 'flowlog_id_example' # str | The unique ID of the Flow Log
    flowlog = ionoscloud.FlowLogProperties() # FlowLogProperties | Modified Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Partially update a Flow Log
        api_response = api_instance.datacenters_servers_nics_flowlogs_patch(datacenter_id, server_id, nic_id, flowlog_id, flowlog, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **flowlog_id** | **str**| The unique ID of the Flow Log |  |
| **flowlog** | [**FlowLogProperties**](FlowLogProperties.md)| Modified Flow Log |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_nics_flowlogs_post**
> FlowLog datacenters_servers_nics_flowlogs_post(datacenter_id, server_id, nic_id, flowlog, pretty=pretty, depth=depth)

Create a Flow Log

This will add a Flow Log to the network interface.

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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    flowlog = ionoscloud.FlowLog() # FlowLog | Flow Log to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Create a Flow Log
        api_response = api_instance.datacenters_servers_nics_flowlogs_post(datacenter_id, server_id, nic_id, flowlog, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_post: %s\n' % e)
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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    flowlog = ionoscloud.FlowLog() # FlowLog | Flow Log to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Create a Flow Log
        api_response = api_instance.datacenters_servers_nics_flowlogs_post(datacenter_id, server_id, nic_id, flowlog, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **flowlog** | [**FlowLog**](FlowLog.md)| Flow Log to be created |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_nics_flowlogs_put**
> FlowLog datacenters_servers_nics_flowlogs_put(datacenter_id, server_id, nic_id, flowlog_id, flowlog, pretty=pretty, depth=depth)

Modify a Flow Log

This will update a Flow Log record.

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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    flowlog_id = 'flowlog_id_example' # str | The unique ID of the Flow Log
    flowlog = ionoscloud.FlowLogPut() # FlowLogPut | Modified Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Modify a Flow Log
        api_response = api_instance.datacenters_servers_nics_flowlogs_put(datacenter_id, server_id, nic_id, flowlog_id, flowlog, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_put: %s\n' % e)
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
    api_instance = ionoscloud.FlowLogsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    flowlog_id = 'flowlog_id_example' # str | The unique ID of the Flow Log
    flowlog = ionoscloud.FlowLogPut() # FlowLogPut | Modified Flow Log
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    try:
        # Modify a Flow Log
        api_response = api_instance.datacenters_servers_nics_flowlogs_put(datacenter_id, server_id, nic_id, flowlog_id, flowlog, pretty=pretty, depth=depth)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling FlowLogsApi.datacenters_servers_nics_flowlogs_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **flowlog_id** | **str**| The unique ID of the Flow Log |  |
| **flowlog** | [**FlowLogPut**](FlowLogPut.md)| Modified Flow Log |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

