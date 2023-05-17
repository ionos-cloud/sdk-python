# PrivateCrossConnectsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**pccs_delete**](PrivateCrossConnectsApi.md#pccs_delete) | **DELETE** /pccs/{pccId} | Delete private Cross-Connects |
| [**pccs_find_by_id**](PrivateCrossConnectsApi.md#pccs_find_by_id) | **GET** /pccs/{pccId} | Retrieve private Cross-Connects |
| [**pccs_get**](PrivateCrossConnectsApi.md#pccs_get) | **GET** /pccs | List private Cross-Connects |
| [**pccs_patch**](PrivateCrossConnectsApi.md#pccs_patch) | **PATCH** /pccs/{pccId} | Partially modify private Cross-Connects |
| [**pccs_post**](PrivateCrossConnectsApi.md#pccs_post) | **POST** /pccs | Create a Private Cross-Connect |


# **pccs_delete**
> pccs_delete(pcc_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete private Cross-Connects

Remove the specified private Cross-Connect (only if not connected to any data centers).

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
    api_instance = ionoscloud.PrivateCrossConnectsApi(api_client)
    pcc_id = 'pcc_id_example' # str | The unique ID of the private Cross-Connect.
    try:
        # Delete private Cross-Connects
        api_instance.pccs_delete(pcc_id)
    except ApiException as e:
        print('Exception when calling PrivateCrossConnectsApi.pccs_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pcc_id** | **str**| The unique ID of the private Cross-Connect. |  |
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

# **pccs_find_by_id**
> PrivateCrossConnect pccs_find_by_id(pcc_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve private Cross-Connects

Retrieve a private Cross-Connect by the resource ID. Cross-Connect ID is in the response body when the private Cross-Connect is created, and in the list of private Cross-Connects, returned by GET.

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
    api_instance = ionoscloud.PrivateCrossConnectsApi(api_client)
    pcc_id = 'pcc_id_example' # str | The unique ID of the private Cross-Connect.
    try:
        # Retrieve private Cross-Connects
        api_response = api_instance.pccs_find_by_id(pcc_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling PrivateCrossConnectsApi.pccs_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pcc_id** | **str**| The unique ID of the private Cross-Connect. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**PrivateCrossConnect**](../models/PrivateCrossConnect.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **pccs_get**
> PrivateCrossConnects pccs_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List private Cross-Connects

List all private Cross-Connects for your account.

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
    api_instance = ionoscloud.PrivateCrossConnectsApi(api_client)
    try:
        # List private Cross-Connects
        api_response = api_instance.pccs_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling PrivateCrossConnectsApi.pccs_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**PrivateCrossConnects**](../models/PrivateCrossConnects.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **pccs_patch**
> PrivateCrossConnect pccs_patch(pcc_id, pcc, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify private Cross-Connects

Update the properties of the specified private Cross-Connect.

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
    api_instance = ionoscloud.PrivateCrossConnectsApi(api_client)
    pcc_id = 'pcc_id_example' # str | The unique ID of the private Cross-Connect.
    pcc = ionoscloud.PrivateCrossConnectProperties() # PrivateCrossConnectProperties | The properties of the private Cross-Connect to be updated.
    try:
        # Partially modify private Cross-Connects
        api_response = api_instance.pccs_patch(pcc_id, pcc)
        print(api_response)
    except ApiException as e:
        print('Exception when calling PrivateCrossConnectsApi.pccs_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pcc_id** | **str**| The unique ID of the private Cross-Connect. |  |
| **pcc** | [**PrivateCrossConnectProperties**](../models/PrivateCrossConnectProperties.md)| The properties of the private Cross-Connect to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**PrivateCrossConnect**](../models/PrivateCrossConnect.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **pccs_post**
> PrivateCrossConnect pccs_post(pcc, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Private Cross-Connect

Creates a private Cross-Connect.

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
    api_instance = ionoscloud.PrivateCrossConnectsApi(api_client)
    pcc = ionoscloud.PrivateCrossConnect() # PrivateCrossConnect | The private Cross-Connect to create.
    try:
        # Create a Private Cross-Connect
        api_response = api_instance.pccs_post(pcc)
        print(api_response)
    except ApiException as e:
        print('Exception when calling PrivateCrossConnectsApi.pccs_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pcc** | [**PrivateCrossConnect**](../models/PrivateCrossConnect.md)| The private Cross-Connect to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**PrivateCrossConnect**](../models/PrivateCrossConnect.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

