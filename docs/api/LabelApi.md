# LabelApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_labels_delete**](LabelApi.md#datacenters_labels_delete) | **DELETE** /datacenters/{datacenterId}/labels/{key} | Delete a Label from Data Center |
| [**datacenters_labels_find_by_key**](LabelApi.md#datacenters_labels_find_by_key) | **GET** /datacenters/{datacenterId}/labels/{key} | Retrieve a Label of Data Center |
| [**datacenters_labels_get**](LabelApi.md#datacenters_labels_get) | **GET** /datacenters/{datacenterId}/labels | List all Data Center Labels |
| [**datacenters_labels_post**](LabelApi.md#datacenters_labels_post) | **POST** /datacenters/{datacenterId}/labels | Add a Label to Data Center |
| [**datacenters_labels_put**](LabelApi.md#datacenters_labels_put) | **PUT** /datacenters/{datacenterId}/labels/{key} | Modify a Label of Data Center |
| [**datacenters_servers_labels_delete**](LabelApi.md#datacenters_servers_labels_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Delete a Label from Server |
| [**datacenters_servers_labels_find_by_key**](LabelApi.md#datacenters_servers_labels_find_by_key) | **GET** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Retrieve a Label of Server |
| [**datacenters_servers_labels_get**](LabelApi.md#datacenters_servers_labels_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/labels | List all Server Labels |
| [**datacenters_servers_labels_post**](LabelApi.md#datacenters_servers_labels_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/labels | Add a Label to Server |
| [**datacenters_servers_labels_put**](LabelApi.md#datacenters_servers_labels_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Modify a Label of Server |
| [**datacenters_volumes_labels_delete**](LabelApi.md#datacenters_volumes_labels_delete) | **DELETE** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Delete a Label from Volume |
| [**datacenters_volumes_labels_find_by_key**](LabelApi.md#datacenters_volumes_labels_find_by_key) | **GET** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Retrieve a Label of Volume |
| [**datacenters_volumes_labels_get**](LabelApi.md#datacenters_volumes_labels_get) | **GET** /datacenters/{datacenterId}/volumes/{volumeId}/labels | List all Volume Labels |
| [**datacenters_volumes_labels_post**](LabelApi.md#datacenters_volumes_labels_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/labels | Add a Label to Volume |
| [**datacenters_volumes_labels_put**](LabelApi.md#datacenters_volumes_labels_put) | **PUT** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Modify a Label of Volume |
| [**ipblocks_labels_delete**](LabelApi.md#ipblocks_labels_delete) | **DELETE** /ipblocks/{ipblockId}/labels/{key} | Delete a Label from IP Block |
| [**ipblocks_labels_find_by_key**](LabelApi.md#ipblocks_labels_find_by_key) | **GET** /ipblocks/{ipblockId}/labels/{key} | Retrieve a Label of IP Block |
| [**ipblocks_labels_get**](LabelApi.md#ipblocks_labels_get) | **GET** /ipblocks/{ipblockId}/labels | List all Ip Block Labels |
| [**ipblocks_labels_post**](LabelApi.md#ipblocks_labels_post) | **POST** /ipblocks/{ipblockId}/labels | Add a Label to IP Block |
| [**ipblocks_labels_put**](LabelApi.md#ipblocks_labels_put) | **PUT** /ipblocks/{ipblockId}/labels/{key} | Modify a Label of IP Block |
| [**labels_find_by_urn**](LabelApi.md#labels_find_by_urn) | **GET** /labels/{labelurn} | Returns the label by its URN. |
| [**labels_get**](LabelApi.md#labels_get) | **GET** /labels | List Labels  |
| [**snapshots_labels_delete**](LabelApi.md#snapshots_labels_delete) | **DELETE** /snapshots/{snapshotId}/labels/{key} | Delete a Label from Snapshot |
| [**snapshots_labels_find_by_key**](LabelApi.md#snapshots_labels_find_by_key) | **GET** /snapshots/{snapshotId}/labels/{key} | Retrieve a Label of Snapshot |
| [**snapshots_labels_get**](LabelApi.md#snapshots_labels_get) | **GET** /snapshots/{snapshotId}/labels | List all Snapshot Labels |
| [**snapshots_labels_post**](LabelApi.md#snapshots_labels_post) | **POST** /snapshots/{snapshotId}/labels | Add a Label to Snapshot |
| [**snapshots_labels_put**](LabelApi.md#snapshots_labels_put) | **PUT** /snapshots/{snapshotId}/labels/{key} | Modify a Label of Snapshot |


# **datacenters_labels_delete**
> object datacenters_labels_delete(datacenter_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Label from Data Center

This will remove a label from the data center.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    key = 'key_example' # str | The key of the Label
    try:
        # Delete a Label from Data Center
        api_response = api_instance.datacenters_labels_delete(datacenter_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Data Center |  |
| **key** | **str**| The key of the Label |  |
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

# **datacenters_labels_find_by_key**
> LabelResource datacenters_labels_find_by_key(datacenter_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Label of Data Center

This will retrieve the properties of a associated label to a data center.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    key = 'key_example' # str | The key of the Label
    try:
        # Retrieve a Label of Data Center
        api_response = api_instance.datacenters_labels_find_by_key(datacenter_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_find_by_key: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Data Center |  |
| **key** | **str**| The key of the Label |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_labels_get**
> LabelResources datacenters_labels_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List all Data Center Labels

You can retrieve a list of all labels associated with a data center

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    try:
        # List all Data Center Labels
        api_response = api_instance.datacenters_labels_get(datacenter_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Data Center |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with &lt;code&gt;limit&lt;/code&gt; for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with &lt;code&gt;offset&lt;/code&gt; for pagination) | [optional] [default to 1000] |

### Return type

[**LabelResources**](../models/LabelResources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_labels_post**
> LabelResource datacenters_labels_post(datacenter_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Add a Label to Data Center

This will add a label to the data center.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    try:
        # Add a Label to Data Center
        api_response = api_instance.datacenters_labels_post(datacenter_id, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Data Center |  |
| **label** | [**LabelResource**](LabelResource.md)| Label to be added |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_labels_put**
> LabelResource datacenters_labels_put(datacenter_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Label of Data Center

This will modify the value of the label on a data center.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    try:
        # Modify a Label of Data Center
        api_response = api_instance.datacenters_labels_put(datacenter_id, key, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Data Center |  |
| **key** | **str**| The key of the Label |  |
| **label** | [**LabelResource**](LabelResource.md)| Modified Label |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_labels_delete**
> object datacenters_servers_labels_delete(datacenter_id, server_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Label from Server

This will remove a label from the server.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    key = 'key_example' # str | The key of the Label
    try:
        # Delete a Label from Server
        api_response = api_instance.datacenters_servers_labels_delete(datacenter_id, server_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **key** | **str**| The key of the Label |  |
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

# **datacenters_servers_labels_find_by_key**
> LabelResource datacenters_servers_labels_find_by_key(datacenter_id, server_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Label of Server

This will retrieve the properties of a associated label to a server.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    key = 'key_example' # str | The key of the Label
    try:
        # Retrieve a Label of Server
        api_response = api_instance.datacenters_servers_labels_find_by_key(datacenter_id, server_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_find_by_key: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **key** | **str**| The key of the Label |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_labels_get**
> LabelResources datacenters_servers_labels_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List all Server Labels

You can retrieve a list of all labels associated with a server

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    try:
        # List all Server Labels
        api_response = api_instance.datacenters_servers_labels_get(datacenter_id, server_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with &lt;code&gt;limit&lt;/code&gt; for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with &lt;code&gt;offset&lt;/code&gt; for pagination) | [optional] [default to 1000] |

### Return type

[**LabelResources**](../models/LabelResources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_servers_labels_post**
> LabelResource datacenters_servers_labels_post(datacenter_id, server_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Add a Label to Server

This will add a label to the server.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    try:
        # Add a Label to Server
        api_response = api_instance.datacenters_servers_labels_post(datacenter_id, server_id, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **label** | [**LabelResource**](LabelResource.md)| Label to be added |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_servers_labels_put**
> LabelResource datacenters_servers_labels_put(datacenter_id, server_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Label of Server

This will modify the value of the label on a server.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    try:
        # Modify a Label of Server
        api_response = api_instance.datacenters_servers_labels_put(datacenter_id, server_id, key, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Datacenter |  |
| **server_id** | **str**| The unique ID of the Server |  |
| **key** | **str**| The key of the Label |  |
| **label** | [**LabelResource**](LabelResource.md)| Modified Label |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_volumes_labels_delete**
> object datacenters_volumes_labels_delete(datacenter_id, volume_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Label from Volume

This will remove a label from the volume.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    key = 'key_example' # str | The key of the Label
    try:
        # Delete a Label from Volume
        api_response = api_instance.datacenters_volumes_labels_delete(datacenter_id, volume_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
| **key** | **str**| The key of the Label |  |
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

# **datacenters_volumes_labels_find_by_key**
> LabelResource datacenters_volumes_labels_find_by_key(datacenter_id, volume_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Label of Volume

This will retrieve the properties of a associated label to a volume.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    key = 'key_example' # str | The key of the Label
    try:
        # Retrieve a Label of Volume
        api_response = api_instance.datacenters_volumes_labels_find_by_key(datacenter_id, volume_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_find_by_key: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
| **key** | **str**| The key of the Label |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_volumes_labels_get**
> LabelResources datacenters_volumes_labels_get(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List all Volume Labels

You can retrieve a list of all labels associated with a volume

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    try:
        # List all Volume Labels
        api_response = api_instance.datacenters_volumes_labels_get(datacenter_id, volume_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with &lt;code&gt;limit&lt;/code&gt; for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with &lt;code&gt;offset&lt;/code&gt; for pagination) | [optional] [default to 1000] |

### Return type

[**LabelResources**](../models/LabelResources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_volumes_labels_post**
> LabelResource datacenters_volumes_labels_post(datacenter_id, volume_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Add a Label to Volume

This will add a label to the volume.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    try:
        # Add a Label to Volume
        api_response = api_instance.datacenters_volumes_labels_post(datacenter_id, volume_id, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
| **label** | [**LabelResource**](LabelResource.md)| Label to be added |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_volumes_labels_put**
> LabelResource datacenters_volumes_labels_put(datacenter_id, volume_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Label of Volume

This will modify the value of the label on a volume.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    try:
        # Modify a Label of Volume
        api_response = api_instance.datacenters_volumes_labels_put(datacenter_id, volume_id, key, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the Datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
| **key** | **str**| The key of the Label |  |
| **label** | [**LabelResource**](LabelResource.md)| Modified Label |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **ipblocks_labels_delete**
> object ipblocks_labels_delete(ipblock_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Label from IP Block

This will remove a label from the Ip Block.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    key = 'key_example' # str | The key of the Label
    try:
        # Delete a Label from IP Block
        api_response = api_instance.ipblocks_labels_delete(ipblock_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the Ip Block |  |
| **key** | **str**| The key of the Label |  |
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

# **ipblocks_labels_find_by_key**
> LabelResource ipblocks_labels_find_by_key(ipblock_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Label of IP Block

This will retrieve the properties of a associated label to a Ip Block.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    key = 'key_example' # str | The key of the Label
    try:
        # Retrieve a Label of IP Block
        api_response = api_instance.ipblocks_labels_find_by_key(ipblock_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_find_by_key: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the Ip Block |  |
| **key** | **str**| The key of the Label |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **ipblocks_labels_get**
> LabelResources ipblocks_labels_get(ipblock_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List all Ip Block Labels

You can retrieve a list of all labels associated with a IP Block

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    try:
        # List all Ip Block Labels
        api_response = api_instance.ipblocks_labels_get(ipblock_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the Ip Block |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResources**](../models/LabelResources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **ipblocks_labels_post**
> LabelResource ipblocks_labels_post(ipblock_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Add a Label to IP Block

This will add a label to the Ip Block.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    try:
        # Add a Label to IP Block
        api_response = api_instance.ipblocks_labels_post(ipblock_id, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the Ip Block |  |
| **label** | [**LabelResource**](LabelResource.md)| Label to be added |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **ipblocks_labels_put**
> LabelResource ipblocks_labels_put(ipblock_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Label of IP Block

This will modify the value of the label on a Ip Block.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    try:
        # Modify a Label of IP Block
        api_response = api_instance.ipblocks_labels_put(ipblock_id, key, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the Ip Block |  |
| **key** | **str**| The key of the Label |  |
| **label** | [**LabelResource**](LabelResource.md)| Modified Label |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **labels_find_by_urn**
> Label labels_find_by_urn(labelurn, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Returns the label by its URN.

You can retrieve the details of a specific label using its URN. A URN is for uniqueness of a Label and composed using urn:label:<resource_type>:<resource_uuid>:<key>

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    labelurn = 'labelurn_example' # str | The URN representing the unique ID of the label. A URN is for uniqueness of a Label and composed using urn:label:<resource_type>:<resource_uuid>:<key>
    try:
        # Returns the label by its URN.
        api_response = api_instance.labels_find_by_urn(labelurn)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.labels_find_by_urn: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **labelurn** | **str**| The URN representing the unique ID of the label. A URN is for uniqueness of a Label and composed using urn:label:&lt;resource_type&gt;:&lt;resource_uuid&gt;:&lt;key&gt; |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Label**](../models/Label.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **labels_get**
> Labels labels_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Labels 

You can retrieve a complete list of labels that you have access to.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    try:
        # List Labels 
        api_response = api_instance.labels_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Labels**](../models/Labels.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_labels_delete**
> object snapshots_labels_delete(snapshot_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Label from Snapshot

This will remove a label from the snapshot.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    key = 'key_example' # str | The key of the Label
    try:
        # Delete a Label from Snapshot
        api_response = api_instance.snapshots_labels_delete(snapshot_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the Snapshot |  |
| **key** | **str**| The key of the Label |  |
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

# **snapshots_labels_find_by_key**
> LabelResource snapshots_labels_find_by_key(snapshot_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Label of Snapshot

This will retrieve the properties of a associated label to a snapshot.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    key = 'key_example' # str | The key of the Label
    try:
        # Retrieve a Label of Snapshot
        api_response = api_instance.snapshots_labels_find_by_key(snapshot_id, key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_find_by_key: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the Snapshot |  |
| **key** | **str**| The key of the Label |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_labels_get**
> LabelResources snapshots_labels_get(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List all Snapshot Labels

You can retrieve a list of all labels associated with a snapshot

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    try:
        # List all Snapshot Labels
        api_response = api_instance.snapshots_labels_get(snapshot_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the Snapshot |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResources**](../models/LabelResources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_labels_post**
> LabelResource snapshots_labels_post(snapshot_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Add a Label to Snapshot

This will add a label to the snapshot.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    try:
        # Add a Label to Snapshot
        api_response = api_instance.snapshots_labels_post(snapshot_id, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the Snapshot |  |
| **label** | [**LabelResource**](LabelResource.md)| Label to be added |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **snapshots_labels_put**
> LabelResource snapshots_labels_put(snapshot_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Label of Snapshot

This will modify the value of the label on a snapshot.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    try:
        # Modify a Label of Snapshot
        api_response = api_instance.snapshots_labels_put(snapshot_id, key, label)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the Snapshot |  |
| **key** | **str**| The key of the Label |  |
| **label** | [**LabelResource**](LabelResource.md)| Modified Label |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**LabelResource**](../models/LabelResource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

