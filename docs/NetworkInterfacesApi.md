# NetworkInterfacesApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_servers_nics_delete**](NetworkInterfacesApi.md#datacenters_servers_nics_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Delete a Network Interface |
| [**datacenters_servers_nics_find_by_id**](NetworkInterfacesApi.md#datacenters_servers_nics_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Retrieve a Network Interface |
| [**datacenters_servers_nics_get**](NetworkInterfacesApi.md#datacenters_servers_nics_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics | List Network Interfaces |
| [**datacenters_servers_nics_patch**](NetworkInterfacesApi.md#datacenters_servers_nics_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Partially Modify a Network Interface |
| [**datacenters_servers_nics_post**](NetworkInterfacesApi.md#datacenters_servers_nics_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/nics | Create a Network Interface |
| [**datacenters_servers_nics_put**](NetworkInterfacesApi.md#datacenters_servers_nics_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Modify a Network Interface |


# **datacenters_servers_nics_delete**
> object datacenters_servers_nics_delete(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Network Interface

Deletes the specified network interface.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Network Interface
        api_response = api_instance.datacenters_servers_nics_delete(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_delete: %s\n' % e)
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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Network Interface
        api_response = api_instance.datacenters_servers_nics_delete(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_delete: %s\n' % e)
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

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_find_by_id**
> Nic datacenters_servers_nics_find_by_id(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Network Interface

Retrieves the attributes of a given network interface.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Network Interface
        api_response = api_instance.datacenters_servers_nics_find_by_id(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_find_by_id: %s\n' % e)
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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Network Interface
        api_response = api_instance.datacenters_servers_nics_find_by_id(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_find_by_id: %s\n' % e)
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

### Return type

[**Nic**](Nic.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_get**
> Nics datacenters_servers_nics_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List Network Interfaces

Retrieves a list of network interfaces.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # List Network Interfaces
        api_response = api_instance.datacenters_servers_nics_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_get: %s\n' % e)
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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with limit for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with offset for pagination) (optional) (default to 1000)
    try:
        # List Network Interfaces
        api_response = api_instance.datacenters_servers_nics_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with limit for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with offset for pagination) | [optional] [default to 1000] |

### Return type

[**Nics**](Nics.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_patch**
> Nic datacenters_servers_nics_patch(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially Modify a Network Interface

You can use update attributes of a network interface.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    nic = ionoscloud.NicProperties() # NicProperties | Modified properties of Nic
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially Modify a Network Interface
        api_response = api_instance.datacenters_servers_nics_patch(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_patch: %s\n' % e)
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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    nic = ionoscloud.NicProperties() # NicProperties | Modified properties of Nic
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially Modify a Network Interface
        api_response = api_instance.datacenters_servers_nics_patch(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **nic** | [**NicProperties**](NicProperties.md)| Modified properties of Nic |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Nic**](Nic.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_nics_post**
> Nic datacenters_servers_nics_post(datacenter_id, server_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Network Interface

Adds a network interface to the target server. Combined count of network interfaces and volumes attached to the server should not exceed size 24.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic = ionoscloud.Nic() # Nic | Nic to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a Network Interface
        api_response = api_instance.datacenters_servers_nics_post(datacenter_id, server_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_post: %s\n' % e)
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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic = ionoscloud.Nic() # Nic | Nic to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a Network Interface
        api_response = api_instance.datacenters_servers_nics_post(datacenter_id, server_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic** | [**Nic**](Nic.md)| Nic to be created |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Nic**](Nic.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_nics_put**
> Nic datacenters_servers_nics_put(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Network Interface

You can use update attributes of a network interface.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    nic = ionoscloud.NicPut() # NicPut | Modified Nic
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Network Interface
        api_response = api_instance.datacenters_servers_nics_put(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_put: %s\n' % e)
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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    nic_id = 'nic_id_example' # str | The unique ID of the NIC
    nic = ionoscloud.NicPut() # NicPut | Modified Nic
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Network Interface
        api_response = api_instance.datacenters_servers_nics_put(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **nic_id** | **str**| The unique ID of the NIC |  |
| **nic** | [**NicPut**](NicPut.md)| Modified Nic |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Nic**](Nic.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

