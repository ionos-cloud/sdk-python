# SnapshotApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**snapshots_delete**](SnapshotApi.md#snapshots_delete) | **DELETE** /snapshots/{snapshotId} | Delete a Snapshot |
| [**snapshots_find_by_id**](SnapshotApi.md#snapshots_find_by_id) | **GET** /snapshots/{snapshotId} | Retrieve a Snapshot by its uuid. |
| [**snapshots_get**](SnapshotApi.md#snapshots_get) | **GET** /snapshots | List Snapshots  |
| [**snapshots_patch**](SnapshotApi.md#snapshots_patch) | **PATCH** /snapshots/{snapshotId} | Partially modify a Snapshot |
| [**snapshots_put**](SnapshotApi.md#snapshots_put) | **PUT** /snapshots/{snapshotId} | Modify a Snapshot |


# **snapshots_delete**
> object snapshots_delete(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Snapshot

Deletes the specified Snapshot.

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
    api_instance = ionoscloud.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    try:
        # Delete a Snapshot
        api_response = api_instance.snapshots_delete(snapshot_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotApi.snapshots_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the Snapshot |  |
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

# **snapshots_find_by_id**
> Snapshot snapshots_find_by_id(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Snapshot by its uuid.

Retrieves the attributes of a given Snapshot.

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
    api_instance = ionoscloud.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    try:
        # Retrieve a Snapshot by its uuid.
        api_response = api_instance.snapshots_find_by_id(snapshot_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotApi.snapshots_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the Snapshot |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Snapshot**](../models/Snapshot.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_get**
> Snapshots snapshots_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Snapshots 

Retrieve a list of available snapshots.

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
    api_instance = ionoscloud.SnapshotApi(api_client)
    try:
        # List Snapshots 
        api_response = api_instance.snapshots_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotApi.snapshots_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Snapshots**](../models/Snapshots.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_patch**
> Snapshot snapshots_patch(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a Snapshot

You can use this method to update attributes of a Snapshot.

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
    api_instance = ionoscloud.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    snapshot = ionoscloud.SnapshotProperties() # SnapshotProperties | Modified Snapshot
    try:
        # Partially modify a Snapshot
        api_response = api_instance.snapshots_patch(snapshot_id, snapshot)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotApi.snapshots_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the Snapshot |  |
| **snapshot** | [**SnapshotProperties**](SnapshotProperties.md)| Modified Snapshot |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Snapshot**](../models/Snapshot.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **snapshots_put**
> Snapshot snapshots_put(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Snapshot

You can use update attributes of a resource

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
    api_instance = ionoscloud.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    snapshot = ionoscloud.Snapshot() # Snapshot | Modified Snapshot
    try:
        # Modify a Snapshot
        api_response = api_instance.snapshots_put(snapshot_id, snapshot)
        print(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotApi.snapshots_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the Snapshot |  |
| **snapshot** | [**Snapshot**](Snapshot.md)| Modified Snapshot |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Snapshot**](../models/Snapshot.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

