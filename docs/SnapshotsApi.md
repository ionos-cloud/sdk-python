# SnapshotsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**snapshots_delete**](SnapshotsApi.md#snapshots_delete) | **DELETE** /snapshots/{snapshotId} | Delete a Snapshot |
| [**snapshots_find_by_id**](SnapshotsApi.md#snapshots_find_by_id) | **GET** /snapshots/{snapshotId} | Retrieve a Snapshot by its uuid. |
| [**snapshots_get**](SnapshotsApi.md#snapshots_get) | **GET** /snapshots | List Snapshots |
| [**snapshots_patch**](SnapshotsApi.md#snapshots_patch) | **PATCH** /snapshots/{snapshotId} | Partially modify a Snapshot |
| [**snapshots_put**](SnapshotsApi.md#snapshots_put) | **PUT** /snapshots/{snapshotId} | Modify a Snapshot |


# **snapshots_delete**
> object snapshots_delete(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Snapshot

Deletes the specified snapshot.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Snapshot
        api_response = api_instance.snapshots_delete(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_delete: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Snapshot
        api_response = api_instance.snapshots_delete(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_delete: %s\n' % e)
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

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Snapshot by its uuid.
        api_response = api_instance.snapshots_find_by_id(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_find_by_id: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Snapshot by its uuid.
        api_response = api_instance.snapshots_find_by_id(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **snapshot_id** | **str**| The unique ID of the Snapshot |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Snapshot**](Snapshot.md)

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

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SnapshotsApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List Snapshots
        api_response = api_instance.snapshots_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_get: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SnapshotsApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List Snapshots
        api_response = api_instance.snapshots_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Snapshots**](Snapshots.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **snapshots_patch**
> Snapshot snapshots_patch(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a Snapshot

You can use this method to update attributes of a snapshot.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    snapshot = ionoscloud.SnapshotProperties() # SnapshotProperties | Modified Snapshot
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify a Snapshot
        api_response = api_instance.snapshots_patch(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_patch: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    snapshot = ionoscloud.SnapshotProperties() # SnapshotProperties | Modified Snapshot
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify a Snapshot
        api_response = api_instance.snapshots_patch(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_patch: %s\n' % e)
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

[**Snapshot**](Snapshot.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **snapshots_put**
> Snapshot snapshots_put(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Snapshot

You can use update attributes of a resource.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure HTTP basic authorization: Basic Authentication
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    snapshot = ionoscloud.Snapshot() # Snapshot | Modified Snapshot
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Snapshot
        api_response = api_instance.snapshots_put(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_put: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below
# Configure Api Key access token for authorization: Token Authentication
configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
}
# Enter a context with an instance of the API client
with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    snapshot = ionoscloud.Snapshot() # Snapshot | Modified Snapshot
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Snapshot
        api_response = api_instance.snapshots_put(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling SnapshotsApi.snapshots_put: %s\n' % e)
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

[**Snapshot**](Snapshot.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

