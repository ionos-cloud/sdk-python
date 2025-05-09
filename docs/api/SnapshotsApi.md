# SnapshotsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**snapshots_delete**](SnapshotsApi.md#snapshots_delete) | **DELETE** /snapshots/{snapshotId} | Delete snapshots |
| [**snapshots_find_by_id**](SnapshotsApi.md#snapshots_find_by_id) | **GET** /snapshots/{snapshotId} | Retrieve snapshots by ID |
| [**snapshots_get**](SnapshotsApi.md#snapshots_get) | **GET** /snapshots | List snapshots |
| [**snapshots_patch**](SnapshotsApi.md#snapshots_patch) | **PATCH** /snapshots/{snapshotId} | Partially modify snapshots |
| [**snapshots_put**](SnapshotsApi.md#snapshots_put) | **PUT** /snapshots/{snapshotId} | Modify a Snapshot by ID |


# **snapshots_delete**
> snapshots_delete(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete snapshots

Deletes the specified snapshot.

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
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the snapshot.
    try:
        # Delete snapshots
        api_instance.snapshots_delete(snapshot_id)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the snapshot. |  |
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

# **snapshots_find_by_id**
> Snapshot snapshots_find_by_id(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve snapshots by ID

Retrieve the properties of the specified snapshot.

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
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the snapshot.
    try:
        # Retrieve snapshots by ID
        api_response = api_instance.snapshots_find_by_id(snapshot_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the snapshot. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Snapshot**](../models/Snapshot.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_get**
> Snapshots snapshots_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List snapshots

List all available snapshots.

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
    api_instance = ionoscloud.SnapshotsApi(api_client)
    try:
        # List snapshots
        api_response = api_instance.snapshots_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Snapshots**](../models/Snapshots.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_patch**
> Snapshot snapshots_patch(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify snapshots

Update the properties of the specified snapshot.

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
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the snapshot.
    snapshot = ionoscloud.SnapshotProperties() # SnapshotProperties | The properties of the snapshot to be updated.
    try:
        # Partially modify snapshots
        api_response = api_instance.snapshots_patch(snapshot_id, snapshot)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the snapshot. |  |
| **snapshot** | [**SnapshotProperties**](../models/SnapshotProperties.md)| The properties of the snapshot to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Snapshot**](../models/Snapshot.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **snapshots_put**
> Snapshot snapshots_put(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Snapshot by ID

Modifies the properties of the specified snapshot.

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
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the snapshot.
    snapshot = ionoscloud.Snapshot() # Snapshot | The modified snapshot
    try:
        # Modify a Snapshot by ID
        api_response = api_instance.snapshots_put(snapshot_id, snapshot)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the snapshot. |  |
| **snapshot** | [**Snapshot**](../models/Snapshot.md)| The modified snapshot |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Snapshot**](../models/Snapshot.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

