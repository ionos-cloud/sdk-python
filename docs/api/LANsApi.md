# LANsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_lans_delete**](LANsApi.md#datacenters_lans_delete) | **DELETE** /datacenters/{datacenterId}/lans/{lanId} | Delete LANs |
| [**datacenters_lans_find_by_id**](LANsApi.md#datacenters_lans_find_by_id) | **GET** /datacenters/{datacenterId}/lans/{lanId} | Retrieve LANs |
| [**datacenters_lans_get**](LANsApi.md#datacenters_lans_get) | **GET** /datacenters/{datacenterId}/lans | List LANs |
| [**datacenters_lans_nics_find_by_id**](LANsApi.md#datacenters_lans_nics_find_by_id) | **GET** /datacenters/{datacenterId}/lans/{lanId}/nics/{nicId} | Retrieve attached NICs |
| [**datacenters_lans_nics_get**](LANsApi.md#datacenters_lans_nics_get) | **GET** /datacenters/{datacenterId}/lans/{lanId}/nics | List LAN members |
| [**datacenters_lans_nics_post**](LANsApi.md#datacenters_lans_nics_post) | **POST** /datacenters/{datacenterId}/lans/{lanId}/nics | Attach NICs |
| [**datacenters_lans_patch**](LANsApi.md#datacenters_lans_patch) | **PATCH** /datacenters/{datacenterId}/lans/{lanId} | Partially modify LANs |
| [**datacenters_lans_post**](LANsApi.md#datacenters_lans_post) | **POST** /datacenters/{datacenterId}/lans | Create LANs |
| [**datacenters_lans_put**](LANsApi.md#datacenters_lans_put) | **PUT** /datacenters/{datacenterId}/lans/{lanId} | Modify LANs |


# **datacenters_lans_delete**
> datacenters_lans_delete(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete LANs

Delete the specified LAN within the data center.

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
    api_instance = ionoscloud.LANsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    lan_id = 'lan_id_example' # str | The unique ID of the LAN.
    try:
        # Delete LANs
        api_instance.datacenters_lans_delete(datacenter_id, lan_id)
    except ApiException as e:
        print('Exception when calling LANsApi.datacenters_lans_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **lan_id** | **str**| The unique ID of the LAN. |  |
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

# **datacenters_lans_find_by_id**
> Lan datacenters_lans_find_by_id(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve LANs

Retrieve the properties of the specified LAN within the data center.

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
    api_instance = ionoscloud.LANsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    lan_id = 'lan_id_example' # str | The unique ID of the LAN.
    try:
        # Retrieve LANs
        api_response = api_instance.datacenters_lans_find_by_id(datacenter_id, lan_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LANsApi.datacenters_lans_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **lan_id** | **str**| The unique ID of the LAN. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Lan**](../models/Lan.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_lans_get**
> Lans datacenters_lans_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List LANs

List all LANs within the data center.

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
    api_instance = ionoscloud.LANsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    try:
        # List LANs
        api_response = api_instance.datacenters_lans_get(datacenter_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LANsApi.datacenters_lans_get: %s\n' % e)
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

[**Lans**](../models/Lans.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_lans_nics_find_by_id**
> Nic datacenters_lans_nics_find_by_id(datacenter_id, lan_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve attached NICs

Retrieve the properties of the NIC, attached to the specified LAN.

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
    api_instance = ionoscloud.LANsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    lan_id = 'lan_id_example' # str | The unique ID of the LAN.
    nic_id = 'nic_id_example' # str | The unique ID of the NIC.
    try:
        # Retrieve attached NICs
        api_response = api_instance.datacenters_lans_nics_find_by_id(datacenter_id, lan_id, nic_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LANsApi.datacenters_lans_nics_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **lan_id** | **str**| The unique ID of the LAN. |  |
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

# **datacenters_lans_nics_get**
> LanNics datacenters_lans_nics_get(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List LAN members

List all NICs, attached to the specified LAN.

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
    api_instance = ionoscloud.LANsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    lan_id = 'lan_id_example' # str | The unique ID of the LAN.
    try:
        # List LAN members
        api_response = api_instance.datacenters_lans_nics_get(datacenter_id, lan_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LANsApi.datacenters_lans_nics_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **lan_id** | **str**| The unique ID of the LAN. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000] |

### Return type

[**LanNics**](../models/LanNics.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_lans_nics_post**
> Nic datacenters_lans_nics_post(datacenter_id, lan_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Attach NICs

Attach an existing NIC to the specified LAN.

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
    api_instance = ionoscloud.LANsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    lan_id = 'lan_id_example' # str | The unique ID of the LAN.
    nic = ionoscloud.Nic() # Nic | The NIC to be attached.
    try:
        # Attach NICs
        api_response = api_instance.datacenters_lans_nics_post(datacenter_id, lan_id, nic)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LANsApi.datacenters_lans_nics_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **lan_id** | **str**| The unique ID of the LAN. |  |
| **nic** | [**Nic**](../models/Nic.md)| The NIC to be attached. |  |
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

# **datacenters_lans_patch**
> Lan datacenters_lans_patch(datacenter_id, lan_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify LANs

Update the properties of the specified LAN within the data center.

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
    api_instance = ionoscloud.LANsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    lan_id = 'lan_id_example' # str | The unique ID of the LAN.
    lan = ionoscloud.LanProperties() # LanProperties | The properties of the LAN to be updated.
    try:
        # Partially modify LANs
        api_response = api_instance.datacenters_lans_patch(datacenter_id, lan_id, lan)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LANsApi.datacenters_lans_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **lan_id** | **str**| The unique ID of the LAN. |  |
| **lan** | [**LanProperties**](../models/LanProperties.md)| The properties of the LAN to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Lan**](../models/Lan.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_lans_post**
> Lan datacenters_lans_post(datacenter_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create LANs

Creates a LAN within the data center.

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
    api_instance = ionoscloud.LANsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    lan = ionoscloud.Lan() # Lan | The LAN to create.
    try:
        # Create LANs
        api_response = api_instance.datacenters_lans_post(datacenter_id, lan)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LANsApi.datacenters_lans_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **lan** | [**Lan**](../models/Lan.md)| The LAN to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Lan**](../models/Lan.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_lans_put**
> Lan datacenters_lans_put(datacenter_id, lan_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify LANs

Modify the properties of the specified LAN within the data center.

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
    api_instance = ionoscloud.LANsApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    lan_id = 'lan_id_example' # str | The unique ID of the LAN.
    lan = ionoscloud.Lan() # Lan | The modified LAN
    try:
        # Modify LANs
        api_response = api_instance.datacenters_lans_put(datacenter_id, lan_id, lan)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LANsApi.datacenters_lans_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **lan_id** | **str**| The unique ID of the LAN. |  |
| **lan** | [**Lan**](../models/Lan.md)| The modified LAN |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Lan**](../models/Lan.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

