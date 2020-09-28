# ionos_cloud_sdk.SnapshotApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snapshots_delete**](SnapshotApi.md#snapshots_delete) | **DELETE** /snapshots/{snapshotId} | Delete a Snapshot
[**snapshots_find_by_id**](SnapshotApi.md#snapshots_find_by_id) | **GET** /snapshots/{snapshotId} | Retrieve a Snapshot by its uuid.
[**snapshots_get**](SnapshotApi.md#snapshots_get) | **GET** /snapshots | List Snapshots 
[**snapshots_patch**](SnapshotApi.md#snapshots_patch) | **PATCH** /snapshots/{snapshotId} | Partially modify a Snapshot
[**snapshots_put**](SnapshotApi.md#snapshots_put) | **PUT** /snapshots/{snapshotId} | Modify a Snapshot


# **snapshots_delete**
> object snapshots_delete(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Snapshot

Deletes the specified Snapshot.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionos_cloud_sdk
from ionos_cloud_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_sdk.Configuration(
    host = "https://api.ionos.com/cloudapi/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below

# Configure HTTP basic authorization: Basic Authentication
configuration = ionos_cloud_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ionos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_sdk.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Snapshot
        api_response = api_instance.snapshots_delete(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotApi->snapshots_delete: %s\n" % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionos_cloud_sdk
from ionos_cloud_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_sdk.Configuration(
    host = "https://api.ionos.com/cloudapi/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below

# Configure HTTP basic authorization: Basic Authentication
configuration = ionos_cloud_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ionos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_sdk.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Snapshot
        api_response = api_instance.snapshots_delete(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotApi->snapshots_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| The unique ID of the Snapshot | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

**object**

### Authorization

[Basic Authentication](../README.md#Basic Authentication), [Token Authentication](../README.md#Token Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successful operation |  * X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response.  <br>  * X-RateLimit-Limit - Average number of requests allowed per minute <br>  * X-RateLimit-Burst - Maximum number of concurrent API requests allowed <br>  * Location - Callback URL to poll async operation status <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_find_by_id**
> Snapshot snapshots_find_by_id(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Snapshot by its uuid.

Retrieves the attributes of a given Snapshot.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionos_cloud_sdk
from ionos_cloud_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_sdk.Configuration(
    host = "https://api.ionos.com/cloudapi/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below

# Configure HTTP basic authorization: Basic Authentication
configuration = ionos_cloud_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ionos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_sdk.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Snapshot by its uuid.
        api_response = api_instance.snapshots_find_by_id(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotApi->snapshots_find_by_id: %s\n" % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionos_cloud_sdk
from ionos_cloud_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_sdk.Configuration(
    host = "https://api.ionos.com/cloudapi/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below

# Configure HTTP basic authorization: Basic Authentication
configuration = ionos_cloud_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ionos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_sdk.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Snapshot by its uuid.
        api_response = api_instance.snapshots_find_by_id(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotApi->snapshots_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| The unique ID of the Snapshot | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[Basic Authentication](../README.md#Basic Authentication), [Token Authentication](../README.md#Token Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response.  <br>  * X-RateLimit-Limit - Average number of requests allowed per minute <br>  * X-RateLimit-Burst - Maximum number of concurrent API requests allowed <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_get**
> Snapshots snapshots_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Snapshots 

Retrieve a list of available snapshots.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionos_cloud_sdk
from ionos_cloud_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_sdk.Configuration(
    host = "https://api.ionos.com/cloudapi/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below

# Configure HTTP basic authorization: Basic Authentication
configuration = ionos_cloud_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ionos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_sdk.SnapshotApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Snapshots 
        api_response = api_instance.snapshots_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotApi->snapshots_get: %s\n" % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionos_cloud_sdk
from ionos_cloud_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_sdk.Configuration(
    host = "https://api.ionos.com/cloudapi/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below

# Configure HTTP basic authorization: Basic Authentication
configuration = ionos_cloud_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ionos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_sdk.SnapshotApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Snapshots 
        api_response = api_instance.snapshots_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotApi->snapshots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Snapshots**](Snapshots.md)

### Authorization

[Basic Authentication](../README.md#Basic Authentication), [Token Authentication](../README.md#Token Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response.  <br>  * X-RateLimit-Limit - Average number of requests allowed per minute <br>  * X-RateLimit-Burst - Maximum number of concurrent API requests allowed <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_patch**
> Snapshot snapshots_patch(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a Snapshot

You can use this method to update attributes of a Snapshot.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionos_cloud_sdk
from ionos_cloud_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_sdk.Configuration(
    host = "https://api.ionos.com/cloudapi/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below

# Configure HTTP basic authorization: Basic Authentication
configuration = ionos_cloud_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ionos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_sdk.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
snapshot = ionos_cloud_sdk.SnapshotProperties() # SnapshotProperties | Modified Snapshot
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Snapshot
        api_response = api_instance.snapshots_patch(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotApi->snapshots_patch: %s\n" % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionos_cloud_sdk
from ionos_cloud_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_sdk.Configuration(
    host = "https://api.ionos.com/cloudapi/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below

# Configure HTTP basic authorization: Basic Authentication
configuration = ionos_cloud_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ionos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_sdk.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
snapshot = ionos_cloud_sdk.SnapshotProperties() # SnapshotProperties | Modified Snapshot
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Snapshot
        api_response = api_instance.snapshots_patch(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotApi->snapshots_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| The unique ID of the Snapshot | 
 **snapshot** | [**SnapshotProperties**](SnapshotProperties.md)| Modified Snapshot | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[Basic Authentication](../README.md#Basic Authentication), [Token Authentication](../README.md#Token Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successful operation |  * X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response.  <br>  * X-RateLimit-Limit - Average number of requests allowed per minute <br>  * X-RateLimit-Burst - Maximum number of concurrent API requests allowed <br>  * Location - Callback URL to poll async operation status <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_put**
> Snapshot snapshots_put(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Snapshot

You can use update attributes of a resource

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionos_cloud_sdk
from ionos_cloud_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_sdk.Configuration(
    host = "https://api.ionos.com/cloudapi/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below

# Configure HTTP basic authorization: Basic Authentication
configuration = ionos_cloud_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ionos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_sdk.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
snapshot = ionos_cloud_sdk.Snapshot() # Snapshot | Modified Snapshot
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Snapshot
        api_response = api_instance.snapshots_put(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotApi->snapshots_put: %s\n" % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionos_cloud_sdk
from ionos_cloud_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionos_cloud_sdk.Configuration(
    host = "https://api.ionos.com/cloudapi/v5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples with auth method are provided below

# Configure HTTP basic authorization: Basic Authentication
configuration = ionos_cloud_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with ionos_cloud_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionos_cloud_sdk.SnapshotApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
snapshot = ionos_cloud_sdk.Snapshot() # Snapshot | Modified Snapshot
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Snapshot
        api_response = api_instance.snapshots_put(snapshot_id, snapshot, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotApi->snapshots_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| The unique ID of the Snapshot | 
 **snapshot** | [**Snapshot**](Snapshot.md)| Modified Snapshot | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[Basic Authentication](../README.md#Basic Authentication), [Token Authentication](../README.md#Token Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successful operation |  * X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response.  <br>  * X-RateLimit-Limit - Average number of requests allowed per minute <br>  * X-RateLimit-Burst - Maximum number of concurrent API requests allowed <br>  * Location - Callback URL to poll async operation status <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

