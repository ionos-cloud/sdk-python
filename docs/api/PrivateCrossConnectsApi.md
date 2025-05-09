# PrivateCrossConnectsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**pccs_delete**](PrivateCrossConnectsApi.md#pccs_delete) | **DELETE** /pccs/{pccId} | Delete Private Cross-Connects |
| [**pccs_find_by_id**](PrivateCrossConnectsApi.md#pccs_find_by_id) | **GET** /pccs/{pccId} | Retrieve a Cross Connect |
| [**pccs_get**](PrivateCrossConnectsApi.md#pccs_get) | **GET** /pccs | List Private Cross-Connects |
| [**pccs_patch**](PrivateCrossConnectsApi.md#pccs_patch) | **PATCH** /pccs/{pccId} | Partially modify a Private Cross-Connects |
| [**pccs_post**](PrivateCrossConnectsApi.md#pccs_post) | **POST** /pccs | Create a Cross Connect |


# **pccs_delete**
> pccs_delete(pcc_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete Private Cross-Connects

Remove the specified Cross Connect. Cross connect can be deleted only if it is not connected to any LANs. For non administrator users a cross connect can be deleted only if you are granted access via the user groups you are member of.

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
    pcc_id = 'pcc_id_example' # str | The unique ID of the Cross Connect.
    try:
        # Delete Private Cross-Connects
        api_instance.pccs_delete(pcc_id)
    except ApiException as e:
        print('Exception when calling PrivateCrossConnectsApi.pccs_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pcc_id** | **str**| The unique ID of the Cross Connect. |  |
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

# **pccs_find_by_id**
> PrivateCrossConnect pccs_find_by_id(pcc_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Cross Connect

Retrieve a Cross Connect by the resource ID. Cross Connect ID is in the response body when the Cross Connect is created and in the list of Private Cross-Connects, returned by GET. For contract owner and administrators all Private Cross-Connects in your contract can be retrieved. For non administrator users it only returns the cross connects you are granted access via the user groups you are member of.

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
    pcc_id = 'pcc_id_example' # str | The unique ID of the Cross Connect.
    try:
        # Retrieve a Cross Connect
        api_response = api_instance.pccs_find_by_id(pcc_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling PrivateCrossConnectsApi.pccs_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pcc_id** | **str**| The unique ID of the Cross Connect. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**PrivateCrossConnect**](../models/PrivateCrossConnect.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **pccs_get**
> PrivateCrossConnects pccs_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Private Cross-Connects

List all Private Cross-Connects. For contract owner and administrators it returns all Private Cross-Connects in your contract. For non administrator users it only returns the Private Cross-Connects you are granted access via the user groups you are member of.

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
        # List Private Cross-Connects
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

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **pccs_patch**
> PrivateCrossConnect pccs_patch(pcc_id, pcc, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a Private Cross-Connects

Update the properties of the specified Cross Connect.For non administrator users you can only update the Private Cross-Connects you are granted access via the user groups you are member of

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
    pcc_id = 'pcc_id_example' # str | The unique ID of the Cross Connect.
    pcc = ionoscloud.PrivateCrossConnectProperties() # PrivateCrossConnectProperties | The properties of the Cross Connect to be updated.
    try:
        # Partially modify a Private Cross-Connects
        api_response = api_instance.pccs_patch(pcc_id, pcc)
        print(api_response)
    except ApiException as e:
        print('Exception when calling PrivateCrossConnectsApi.pccs_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pcc_id** | **str**| The unique ID of the Cross Connect. |  |
| **pcc** | [**PrivateCrossConnectProperties**](../models/PrivateCrossConnectProperties.md)| The properties of the Cross Connect to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**PrivateCrossConnect**](../models/PrivateCrossConnect.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **pccs_post**
> PrivateCrossConnect pccs_post(pcc, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Cross Connect

Creates a Cross-Connect. Only contract owners, administrators and users with createPcc user privilege can create a cross connect. Please note that connecting a LAN to a cross connect is to be done via the /lan endpoint.

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
    pcc = ionoscloud.PrivateCrossConnect() # PrivateCrossConnect | The Cross Connect to create.
    try:
        # Create a Cross Connect
        api_response = api_instance.pccs_post(pcc)
        print(api_response)
    except ApiException as e:
        print('Exception when calling PrivateCrossConnectsApi.pccs_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pcc** | [**PrivateCrossConnect**](../models/PrivateCrossConnect.md)| The Cross Connect to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**PrivateCrossConnect**](../models/PrivateCrossConnect.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

