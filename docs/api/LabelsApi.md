# LabelsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_labels_delete**](LabelsApi.md#datacenters_labels_delete) | **DELETE** /datacenters/{datacenterId}/labels/{key} | Delete data center labels |
| [**datacenters_labels_find_by_key**](LabelsApi.md#datacenters_labels_find_by_key) | **GET** /datacenters/{datacenterId}/labels/{key} | Retrieve data center labels |
| [**datacenters_labels_get**](LabelsApi.md#datacenters_labels_get) | **GET** /datacenters/{datacenterId}/labels | List data center labels |
| [**datacenters_labels_post**](LabelsApi.md#datacenters_labels_post) | **POST** /datacenters/{datacenterId}/labels | Create a Data Center Label |
| [**datacenters_labels_put**](LabelsApi.md#datacenters_labels_put) | **PUT** /datacenters/{datacenterId}/labels/{key} | Modify a Data Center Label by Key |
| [**datacenters_servers_labels_delete**](LabelsApi.md#datacenters_servers_labels_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Delete server labels |
| [**datacenters_servers_labels_find_by_key**](LabelsApi.md#datacenters_servers_labels_find_by_key) | **GET** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Retrieve server labels |
| [**datacenters_servers_labels_get**](LabelsApi.md#datacenters_servers_labels_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/labels | List server labels |
| [**datacenters_servers_labels_post**](LabelsApi.md#datacenters_servers_labels_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/labels | Create a Server Label |
| [**datacenters_servers_labels_put**](LabelsApi.md#datacenters_servers_labels_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Modify a Server Label |
| [**datacenters_volumes_labels_delete**](LabelsApi.md#datacenters_volumes_labels_delete) | **DELETE** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Delete volume labels |
| [**datacenters_volumes_labels_find_by_key**](LabelsApi.md#datacenters_volumes_labels_find_by_key) | **GET** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Retrieve volume labels |
| [**datacenters_volumes_labels_get**](LabelsApi.md#datacenters_volumes_labels_get) | **GET** /datacenters/{datacenterId}/volumes/{volumeId}/labels | List volume labels |
| [**datacenters_volumes_labels_post**](LabelsApi.md#datacenters_volumes_labels_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/labels | Create a Volume Label |
| [**datacenters_volumes_labels_put**](LabelsApi.md#datacenters_volumes_labels_put) | **PUT** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Modify a Volume Label |
| [**ipblocks_labels_delete**](LabelsApi.md#ipblocks_labels_delete) | **DELETE** /ipblocks/{ipblockId}/labels/{key} | Delete IP block labels |
| [**ipblocks_labels_find_by_key**](LabelsApi.md#ipblocks_labels_find_by_key) | **GET** /ipblocks/{ipblockId}/labels/{key} | Retrieve IP block labels |
| [**ipblocks_labels_get**](LabelsApi.md#ipblocks_labels_get) | **GET** /ipblocks/{ipblockId}/labels | List IP block labels |
| [**ipblocks_labels_post**](LabelsApi.md#ipblocks_labels_post) | **POST** /ipblocks/{ipblockId}/labels | Create IP block labels |
| [**ipblocks_labels_put**](LabelsApi.md#ipblocks_labels_put) | **PUT** /ipblocks/{ipblockId}/labels/{key} | Modify a IP Block Label by ID |
| [**labels_find_by_urn**](LabelsApi.md#labels_find_by_urn) | **GET** /labels/{labelurn} | Retrieve labels by URN |
| [**labels_get**](LabelsApi.md#labels_get) | **GET** /labels | List labels  |
| [**snapshots_labels_delete**](LabelsApi.md#snapshots_labels_delete) | **DELETE** /snapshots/{snapshotId}/labels/{key} | Delete snapshot labels |
| [**snapshots_labels_find_by_key**](LabelsApi.md#snapshots_labels_find_by_key) | **GET** /snapshots/{snapshotId}/labels/{key} | Retrieve snapshot labels |
| [**snapshots_labels_get**](LabelsApi.md#snapshots_labels_get) | **GET** /snapshots/{snapshotId}/labels | List snapshot labels |
| [**snapshots_labels_post**](LabelsApi.md#snapshots_labels_post) | **POST** /snapshots/{snapshotId}/labels | Create a Snapshot Label |
| [**snapshots_labels_put**](LabelsApi.md#snapshots_labels_put) | **PUT** /snapshots/{snapshotId}/labels/{key} | Modify a Snapshot Label by ID |


# **datacenters_labels_delete**
> datacenters_labels_delete(datacenter_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete data center labels

Delete the specified data center label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    key = 'key_example' # str | The label key
    try:
        # Delete data center labels
        api_instance.datacenters_labels_delete(datacenter_id, key)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_labels_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **key** | **str**| The label key |  |
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

# **datacenters_labels_find_by_key**
> LabelResource datacenters_labels_find_by_key(datacenter_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve data center labels

Retrieve the properties of the specified data center label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    key = 'key_example' # str | The label key
    try:
        # Retrieve data center labels
        api_response = api_instance.datacenters_labels_find_by_key(datacenter_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_labels_find_by_key: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **key** | **str**| The label key |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_labels_get**
> LabelResources datacenters_labels_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List data center labels

List all the the labels for the specified data center.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    try:
        # List data center labels
        api_response = api_instance.datacenters_labels_get(datacenter_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResources**](../models/LabelResources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_labels_post**
> LabelResource datacenters_labels_post(datacenter_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Data Center Label

Adds a new label to the specified data center.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    label = ionoscloud.LabelResource() # LabelResource | The label to create.
    try:
        # Create a Data Center Label
        api_response = api_instance.datacenters_labels_post(datacenter_id, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_labels_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **label** | [**LabelResource**](../models/LabelResource.md)| The label to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_labels_put**
> LabelResource datacenters_labels_put(datacenter_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Data Center Label by Key

Modifies the specified data center label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    key = 'key_example' # str | The label key
    label = ionoscloud.LabelResource() # LabelResource | The modified label
    try:
        # Modify a Data Center Label by Key
        api_response = api_instance.datacenters_labels_put(datacenter_id, key, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_labels_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **key** | **str**| The label key |  |
| **label** | [**LabelResource**](../models/LabelResource.md)| The modified label |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_labels_delete**
> datacenters_servers_labels_delete(datacenter_id, server_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete server labels

Delete the specified server label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    key = 'key_example' # str | The label key
    try:
        # Delete server labels
        api_instance.datacenters_servers_labels_delete(datacenter_id, server_id, key)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_servers_labels_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **key** | **str**| The label key |  |
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

# **datacenters_servers_labels_find_by_key**
> LabelResource datacenters_servers_labels_find_by_key(datacenter_id, server_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve server labels

Retrieve the properties of the specified server label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    key = 'key_example' # str | The label key
    try:
        # Retrieve server labels
        api_response = api_instance.datacenters_servers_labels_find_by_key(datacenter_id, server_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_servers_labels_find_by_key: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **key** | **str**| The label key |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_labels_get**
> LabelResources datacenters_servers_labels_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List server labels

List all the the labels for the specified server.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    try:
        # List server labels
        api_response = api_instance.datacenters_servers_labels_get(datacenter_id, server_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_servers_labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResources**](../models/LabelResources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_labels_post**
> LabelResource datacenters_servers_labels_post(datacenter_id, server_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Server Label

Adds a new label to the specified server.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    label = ionoscloud.LabelResource() # LabelResource | The label to create.
    try:
        # Create a Server Label
        api_response = api_instance.datacenters_servers_labels_post(datacenter_id, server_id, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_servers_labels_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **label** | [**LabelResource**](../models/LabelResource.md)| The label to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_labels_put**
> LabelResource datacenters_servers_labels_put(datacenter_id, server_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Server Label

Modifies the specified server label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    server_id = 'server_id_example' # str | The unique ID of the server.
    key = 'key_example' # str | The label key
    label = ionoscloud.LabelResource() # LabelResource | The modified label
    try:
        # Modify a Server Label
        api_response = api_instance.datacenters_servers_labels_put(datacenter_id, server_id, key, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_servers_labels_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **server_id** | **str**| The unique ID of the server. |  |
| **key** | **str**| The label key |  |
| **label** | [**LabelResource**](../models/LabelResource.md)| The modified label |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_volumes_labels_delete**
> datacenters_volumes_labels_delete(datacenter_id, volume_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete volume labels

Delete the specified volume label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    key = 'key_example' # str | The label key
    try:
        # Delete volume labels
        api_instance.datacenters_volumes_labels_delete(datacenter_id, volume_id, key)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_volumes_labels_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
| **key** | **str**| The label key |  |
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

# **datacenters_volumes_labels_find_by_key**
> LabelResource datacenters_volumes_labels_find_by_key(datacenter_id, volume_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve volume labels

Retrieve the properties of the specified volume label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    key = 'key_example' # str | The label key
    try:
        # Retrieve volume labels
        api_response = api_instance.datacenters_volumes_labels_find_by_key(datacenter_id, volume_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_volumes_labels_find_by_key: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
| **key** | **str**| The label key |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_volumes_labels_get**
> LabelResources datacenters_volumes_labels_get(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List volume labels

List all the the labels for the specified volume.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    try:
        # List volume labels
        api_response = api_instance.datacenters_volumes_labels_get(datacenter_id, volume_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_volumes_labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResources**](../models/LabelResources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_volumes_labels_post**
> LabelResource datacenters_volumes_labels_post(datacenter_id, volume_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Volume Label

Adds a new label to the specified volume.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    label = ionoscloud.LabelResource() # LabelResource | The label to create.
    try:
        # Create a Volume Label
        api_response = api_instance.datacenters_volumes_labels_post(datacenter_id, volume_id, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_volumes_labels_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
| **label** | [**LabelResource**](../models/LabelResource.md)| The label to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_volumes_labels_put**
> LabelResource datacenters_volumes_labels_put(datacenter_id, volume_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Volume Label

Modifies the specified volume label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    key = 'key_example' # str | The label key
    label = ionoscloud.LabelResource() # LabelResource | The modified label
    try:
        # Modify a Volume Label
        api_response = api_instance.datacenters_volumes_labels_put(datacenter_id, volume_id, key, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.datacenters_volumes_labels_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
| **key** | **str**| The label key |  |
| **label** | [**LabelResource**](../models/LabelResource.md)| The modified label |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **ipblocks_labels_delete**
> ipblocks_labels_delete(ipblock_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete IP block labels

Delete the specified IP block label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the IP block.
    key = 'key_example' # str | The label key
    try:
        # Delete IP block labels
        api_instance.ipblocks_labels_delete(ipblock_id, key)
    except ApiException as e:
        print('Exception when calling LabelsApi.ipblocks_labels_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the IP block. |  |
| **key** | **str**| The label key |  |
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

# **ipblocks_labels_find_by_key**
> LabelResource ipblocks_labels_find_by_key(ipblock_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve IP block labels

Retrieve the properties of the specified IP block label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the IP block.
    key = 'key_example' # str | The label key
    try:
        # Retrieve IP block labels
        api_response = api_instance.ipblocks_labels_find_by_key(ipblock_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.ipblocks_labels_find_by_key: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the IP block. |  |
| **key** | **str**| The label key |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **ipblocks_labels_get**
> LabelResources ipblocks_labels_get(ipblock_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List IP block labels

List all the the labels for the specified IP block.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the IP block.
    try:
        # List IP block labels
        api_response = api_instance.ipblocks_labels_get(ipblock_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.ipblocks_labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the IP block. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResources**](../models/LabelResources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **ipblocks_labels_post**
> LabelResource ipblocks_labels_post(ipblock_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create IP block labels

Add a new label to the specified IP block.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the IP block.
    label = ionoscloud.LabelResource() # LabelResource | The label to create.
    try:
        # Create IP block labels
        api_response = api_instance.ipblocks_labels_post(ipblock_id, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.ipblocks_labels_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the IP block. |  |
| **label** | [**LabelResource**](../models/LabelResource.md)| The label to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **ipblocks_labels_put**
> LabelResource ipblocks_labels_put(ipblock_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a IP Block Label by ID

Modifies the specified IP block label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the IP block.
    key = 'key_example' # str | The label key
    label = ionoscloud.LabelResource() # LabelResource | The modified label
    try:
        # Modify a IP Block Label by ID
        api_response = api_instance.ipblocks_labels_put(ipblock_id, key, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.ipblocks_labels_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the IP block. |  |
| **key** | **str**| The label key |  |
| **label** | [**LabelResource**](../models/LabelResource.md)| The modified label |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **labels_find_by_urn**
> Label labels_find_by_urn(labelurn, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve labels by URN

Retrieve a label by label URN.  The URN is unique for each label, and consists of:  urn:label:<resource_type>:<resource_uuid>:<key>

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
    api_instance = ionoscloud.LabelsApi(api_client)
    labelurn = 'labelurn_example' # str | The label URN; URN is unique for each label, and consists of:  urn:label:<resource_type>:<resource_uuid>:<key><key>
    try:
        # Retrieve labels by URN
        api_response = api_instance.labels_find_by_urn(labelurn)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.labels_find_by_urn: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **labelurn** | **str**| The label URN; URN is unique for each label, and consists of:  urn:label:&lt;resource_type&gt;:&lt;resource_uuid&gt;:&lt;key&gt;&lt;key&gt; |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Label**](../models/Label.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **labels_get**
> Labels labels_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List labels 

List all available labels.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    try:
        # List labels 
        api_response = api_instance.labels_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Labels**](../models/Labels.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_labels_delete**
> snapshots_labels_delete(snapshot_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete snapshot labels

Delete the specified snapshot label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the snapshot.
    key = 'key_example' # str | The label key
    try:
        # Delete snapshot labels
        api_instance.snapshots_labels_delete(snapshot_id, key)
    except ApiException as e:
        print('Exception when calling LabelsApi.snapshots_labels_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the snapshot. |  |
| **key** | **str**| The label key |  |
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

# **snapshots_labels_find_by_key**
> LabelResource snapshots_labels_find_by_key(snapshot_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve snapshot labels

Retrieve the properties of the specified snapshot label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the snapshot.
    key = 'key_example' # str | The label key
    try:
        # Retrieve snapshot labels
        api_response = api_instance.snapshots_labels_find_by_key(snapshot_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.snapshots_labels_find_by_key: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the snapshot. |  |
| **key** | **str**| The label key |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_labels_get**
> LabelResources snapshots_labels_get(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List snapshot labels

List all the the labels for the specified snapshot.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the snapshot.
    try:
        # List snapshot labels
        api_response = api_instance.snapshots_labels_get(snapshot_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.snapshots_labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the snapshot. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResources**](../models/LabelResources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_labels_post**
> LabelResource snapshots_labels_post(snapshot_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Snapshot Label

Adds a new label to the specified snapshot.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the snapshot.
    label = ionoscloud.LabelResource() # LabelResource | The label to create.
    try:
        # Create a Snapshot Label
        api_response = api_instance.snapshots_labels_post(snapshot_id, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.snapshots_labels_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the snapshot. |  |
| **label** | [**LabelResource**](../models/LabelResource.md)| The label to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **snapshots_labels_put**
> LabelResource snapshots_labels_put(snapshot_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Snapshot Label by ID

Modifies the specified snapshot label.

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
    api_instance = ionoscloud.LabelsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the snapshot.
    key = 'key_example' # str | The label key
    label = ionoscloud.LabelResource() # LabelResource | The modified label
    try:
        # Modify a Snapshot Label by ID
        api_response = api_instance.snapshots_labels_put(snapshot_id, key, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelsApi.snapshots_labels_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the snapshot. |  |
| **key** | **str**| The label key |  |
| **label** | [**LabelResource**](../models/LabelResource.md)| The modified label |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

