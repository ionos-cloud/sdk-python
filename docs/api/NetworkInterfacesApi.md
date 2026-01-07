# NetworkInterfacesApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_servers_nics_delete**](NetworkInterfacesApi.md#datacenters_servers_nics_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Delete NICs |
| [**datacenters_servers_nics_find_by_id**](NetworkInterfacesApi.md#datacenters_servers_nics_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Retrieve NICs |
| [**datacenters_servers_nics_get**](NetworkInterfacesApi.md#datacenters_servers_nics_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics | List NICs |
| [**datacenters_servers_nics_patch**](NetworkInterfacesApi.md#datacenters_servers_nics_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Partially modify NICs |
| [**datacenters_servers_nics_post**](NetworkInterfacesApi.md#datacenters_servers_nics_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/nics | Create a NIC |
| [**datacenters_servers_nics_put**](NetworkInterfacesApi.md#datacenters_servers_nics_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Modify NICs |


# **datacenters_servers_nics_delete**
> datacenters_servers_nics_delete(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete NICs

Remove the specified NIC.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    nic_id = 'nic_id_example' # str | The unique ID of the NIC.
    try:
        # Delete NICs
        api_instance.datacenters_servers_nics_delete(datacenter_id, server_id, nic_id)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **nic_id** | **str**| The unique ID of the NIC. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

void (empty response body)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_find_by_id**
> Nic datacenters_servers_nics_find_by_id(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve NICs

Retrieve the properties of the specified NIC.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    nic_id = 'nic_id_example' # str | The unique ID of the NIC.
    try:
        # Retrieve NICs
        api_response = api_instance.datacenters_servers_nics_find_by_id(datacenter_id, server_id, nic_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **nic_id** | **str**| The unique ID of the NIC. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Nic**](../models/Nic.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_get**
> Nics datacenters_servers_nics_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List NICs

List all NICs, attached to the specified server.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    try:
        # List NICs
        api_response = api_instance.datacenters_servers_nics_get(datacenter_id, server_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000] |

### Return type

[**Nics**](../models/Nics.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_nics_patch**
> Nic datacenters_servers_nics_patch(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify NICs

Update the properties of the specified NIC.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    nic_id = 'nic_id_example' # str | The unique ID of the NIC.
    nic = ionoscloud.NicProperties() # NicProperties | The properties of the NIC to be updated.
    try:
        # Partially modify NICs
        api_response = api_instance.datacenters_servers_nics_patch(datacenter_id, server_id, nic_id, nic)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **nic_id** | **str**| The unique ID of the NIC. |  |
| **nic** | [**NicProperties**](../models/NicProperties.md)| The properties of the NIC to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Nic**](../models/Nic.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_nics_post**
> Nic datacenters_servers_nics_post(datacenter_id, server_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a NIC

Adds a NIC to the specified server. The combined total of NICs and attached volumes cannot exceed 24 per server.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    nic = ionoscloud.Nic() # Nic | The NIC to create.
    try:
        # Create a NIC
        api_response = api_instance.datacenters_servers_nics_post(datacenter_id, server_id, nic)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **nic** | [**Nic**](../models/Nic.md)| The NIC to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Nic**](../models/Nic.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_nics_put**
> Nic datacenters_servers_nics_put(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify NICs

Modify the properties of the specified NIC.

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
    api_instance = ionoscloud.NetworkInterfacesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    nic_id = 'nic_id_example' # str | The unique ID of the NIC.
    nic = ionoscloud.NicPut() # NicPut | The modified NIC
    try:
        # Modify NICs
        api_response = api_instance.datacenters_servers_nics_put(datacenter_id, server_id, nic_id, nic)
        print(api_response)
    except ApiException as e:
        print('Exception when calling NetworkInterfacesApi.datacenters_servers_nics_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **nic_id** | **str**| The unique ID of the NIC. |  |
| **nic** | [**NicPut**](../models/NicPut.md)| The modified NIC |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Nic**](../models/Nic.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

