# DataCentersApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_delete**](DataCentersApi.md#datacenters_delete) | **DELETE** /datacenters/{datacenterId} | Delete data centers |
| [**datacenters_find_by_id**](DataCentersApi.md#datacenters_find_by_id) | **GET** /datacenters/{datacenterId} | Retrieve data centers |
| [**datacenters_get**](DataCentersApi.md#datacenters_get) | **GET** /datacenters | List your data centers |
| [**datacenters_patch**](DataCentersApi.md#datacenters_patch) | **PATCH** /datacenters/{datacenterId} | Partially modify a Data Center by ID |
| [**datacenters_post**](DataCentersApi.md#datacenters_post) | **POST** /datacenters | Create a Data Center |
| [**datacenters_put**](DataCentersApi.md#datacenters_put) | **PUT** /datacenters/{datacenterId} | Modify a Data Center by ID |


# **datacenters_delete**
> datacenters_delete(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete data centers

Delete the specified data center and all the elements it contains. This method is destructive and should be used carefully.

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
    api_instance = ionoscloud.DataCentersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    try:
        # Delete data centers
        api_instance.datacenters_delete(datacenter_id)
    except ApiException as e:
        print('Exception when calling DataCentersApi.datacenters_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
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

# **datacenters_find_by_id**
> Datacenter datacenters_find_by_id(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve data centers

Retrieve data centers by resource ID. This value is in the response body when the data center is created, and in the list of the data centers, returned by GET.

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
    api_instance = ionoscloud.DataCentersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    try:
        # Retrieve data centers
        api_response = api_instance.datacenters_find_by_id(datacenter_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataCentersApi.datacenters_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Datacenter**](../models/Datacenter.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_get**
> Datacenters datacenters_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List your data centers

List the data centers for your account. Default limit is the first 100 items; use pagination query parameters for listing more items.

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
    api_instance = ionoscloud.DataCentersApi(api_client)
    try:
        # List your data centers
        api_response = api_instance.datacenters_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataCentersApi.datacenters_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000] |

### Return type

[**Datacenters**](../models/Datacenters.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_patch**
> Datacenter datacenters_patch(datacenter_id, datacenter, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a Data Center by ID

Updates the properties of the specified data center, rename it, or change the description.

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
    api_instance = ionoscloud.DataCentersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    datacenter = ionoscloud.DatacenterProperties() # DatacenterProperties | The properties of the data center to be updated.
    try:
        # Partially modify a Data Center by ID
        api_response = api_instance.datacenters_patch(datacenter_id, datacenter)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataCentersApi.datacenters_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **datacenter** | [**DatacenterProperties**](../models/DatacenterProperties.md)| The properties of the data center to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Datacenter**](../models/Datacenter.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_post**
> Datacenter datacenters_post(datacenter, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Data Center

Creates new data centers, and data centers that already contain elements, such as servers and storage volumes.  Virtual data centers are the foundation of the platform; they act as logical containers for all other objects you create, such as servers and storage volumes. You can provision as many data centers as needed. Data centers have their own private networks and are logically segmented from each other to create isolation.

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
    api_instance = ionoscloud.DataCentersApi(api_client)
    datacenter = ionoscloud.Datacenter() # Datacenter | The data center to create.
    try:
        # Create a Data Center
        api_response = api_instance.datacenters_post(datacenter)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataCentersApi.datacenters_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter** | [**Datacenter**](../models/Datacenter.md)| The data center to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Datacenter**](../models/Datacenter.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_put**
> Datacenter datacenters_put(datacenter_id, datacenter, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Data Center by ID

Modifies the properties of the specified data center, rename it, or change the description.

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
    api_instance = ionoscloud.DataCentersApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    datacenter = ionoscloud.Datacenter() # Datacenter | The modified data center.
    try:
        # Modify a Data Center by ID
        api_response = api_instance.datacenters_put(datacenter_id, datacenter)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataCentersApi.datacenters_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **datacenter** | [**Datacenter**](../models/Datacenter.md)| The modified data center. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Datacenter**](../models/Datacenter.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

