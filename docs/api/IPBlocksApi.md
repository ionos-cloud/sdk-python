# IPBlocksApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**ipblocks_delete**](IPBlocksApi.md#ipblocks_delete) | **DELETE** /ipblocks/{ipblockId} | Delete IP blocks |
| [**ipblocks_find_by_id**](IPBlocksApi.md#ipblocks_find_by_id) | **GET** /ipblocks/{ipblockId} | Retrieve IP blocks |
| [**ipblocks_get**](IPBlocksApi.md#ipblocks_get) | **GET** /ipblocks | List IP blocks  |
| [**ipblocks_patch**](IPBlocksApi.md#ipblocks_patch) | **PATCH** /ipblocks/{ipblockId} | Partially modify IP blocks |
| [**ipblocks_post**](IPBlocksApi.md#ipblocks_post) | **POST** /ipblocks | Reserve IP blocks |
| [**ipblocks_put**](IPBlocksApi.md#ipblocks_put) | **PUT** /ipblocks/{ipblockId} | Modify IP blocks |


# **ipblocks_delete**
> ipblocks_delete(ipblock_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete IP blocks

Remove the specified IP block.

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
    api_instance = ionoscloud.IPBlocksApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the IP block.
    try:
        # Delete IP blocks
        api_instance.ipblocks_delete(ipblock_id)
    except ApiException as e:
        print('Exception when calling IPBlocksApi.ipblocks_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the IP block. |  |
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

# **ipblocks_find_by_id**
> IpBlock ipblocks_find_by_id(ipblock_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve IP blocks

Retrieve the properties of the specified IP block.

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
    api_instance = ionoscloud.IPBlocksApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the IP block.
    try:
        # Retrieve IP blocks
        api_response = api_instance.ipblocks_find_by_id(ipblock_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling IPBlocksApi.ipblocks_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the IP block. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**IpBlock**](../models/IpBlock.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **ipblocks_get**
> IpBlocks ipblocks_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List IP blocks 

List all reserved IP blocks.

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
    api_instance = ionoscloud.IPBlocksApi(api_client)
    try:
        # List IP blocks 
        api_response = api_instance.ipblocks_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling IPBlocksApi.ipblocks_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 100] |

### Return type

[**IpBlocks**](../models/IpBlocks.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **ipblocks_patch**
> IpBlock ipblocks_patch(ipblock_id, ipblock, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify IP blocks

Update the properties of the specified IP block.

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
    api_instance = ionoscloud.IPBlocksApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the IP block.
    ipblock = ionoscloud.IpBlockProperties() # IpBlockProperties | The properties of the IP block to be updated.
    try:
        # Partially modify IP blocks
        api_response = api_instance.ipblocks_patch(ipblock_id, ipblock)
        print(api_response)
    except ApiException as e:
        print('Exception when calling IPBlocksApi.ipblocks_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the IP block. |  |
| **ipblock** | [**IpBlockProperties**](IpBlockProperties.md)| The properties of the IP block to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**IpBlock**](../models/IpBlock.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **ipblocks_post**
> IpBlock ipblocks_post(ipblock, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Reserve IP blocks

Reserve a new IP block.

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
    api_instance = ionoscloud.IPBlocksApi(api_client)
    ipblock = ionoscloud.IpBlock() # IpBlock | The IP block to be reserved.
    try:
        # Reserve IP blocks
        api_response = api_instance.ipblocks_post(ipblock)
        print(api_response)
    except ApiException as e:
        print('Exception when calling IPBlocksApi.ipblocks_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock** | [**IpBlock**](IpBlock.md)| The IP block to be reserved. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**IpBlock**](../models/IpBlock.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **ipblocks_put**
> IpBlock ipblocks_put(ipblock_id, ipblock, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify IP blocks

Modify the properties of the specified IP block.

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
    api_instance = ionoscloud.IPBlocksApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the IP block.
    ipblock = ionoscloud.IpBlock() # IpBlock | The modified IP block.
    try:
        # Modify IP blocks
        api_response = api_instance.ipblocks_put(ipblock_id, ipblock)
        print(api_response)
    except ApiException as e:
        print('Exception when calling IPBlocksApi.ipblocks_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ipblock_id** | **str**| The unique ID of the IP block. |  |
| **ipblock** | [**IpBlock**](IpBlock.md)| The modified IP block. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**IpBlock**](../models/IpBlock.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

