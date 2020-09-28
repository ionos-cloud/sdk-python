# ionos_cloud_sdk.VolumeApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datacenters_volumes_create_snapshot_post**](VolumeApi.md#datacenters_volumes_create_snapshot_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/create-snapshot | Create Volume Snapshot
[**datacenters_volumes_delete**](VolumeApi.md#datacenters_volumes_delete) | **DELETE** /datacenters/{datacenterId}/volumes/{volumeId} | Delete a Volume
[**datacenters_volumes_find_by_id**](VolumeApi.md#datacenters_volumes_find_by_id) | **GET** /datacenters/{datacenterId}/volumes/{volumeId} | Retrieve a Volume
[**datacenters_volumes_get**](VolumeApi.md#datacenters_volumes_get) | **GET** /datacenters/{datacenterId}/volumes | List Volumes 
[**datacenters_volumes_patch**](VolumeApi.md#datacenters_volumes_patch) | **PATCH** /datacenters/{datacenterId}/volumes/{volumeId} | Partially modify a Volume
[**datacenters_volumes_post**](VolumeApi.md#datacenters_volumes_post) | **POST** /datacenters/{datacenterId}/volumes | Create a Volume
[**datacenters_volumes_put**](VolumeApi.md#datacenters_volumes_put) | **PUT** /datacenters/{datacenterId}/volumes/{volumeId} | Modify a Volume
[**datacenters_volumes_restore_snapshot_post**](VolumeApi.md#datacenters_volumes_restore_snapshot_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/restore-snapshot | Restore Volume Snapshot


# **datacenters_volumes_create_snapshot_post**
> Snapshot datacenters_volumes_create_snapshot_post(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, name=name, description=description, sec_auth_protection=sec_auth_protection, licence_type=licence_type)

Create Volume Snapshot

Creates a snapshot of a volume within the datacenter. You can use a snapshot to create a new storage volume or to restore a storage volume.

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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
name = 'name_example' # str | The name of the snapshot (optional)
description = 'description_example' # str | The description of the snapshot (optional)
sec_auth_protection = True # bool | Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc. (optional)
licence_type = 'licence_type_example' # str | The OS type of this Snapshot (optional)

    try:
        # Create Volume Snapshot
        api_response = api_instance.datacenters_volumes_create_snapshot_post(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, name=name, description=description, sec_auth_protection=sec_auth_protection, licence_type=licence_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_create_snapshot_post: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
name = 'name_example' # str | The name of the snapshot (optional)
description = 'description_example' # str | The description of the snapshot (optional)
sec_auth_protection = True # bool | Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc. (optional)
licence_type = 'licence_type_example' # str | The OS type of this Snapshot (optional)

    try:
        # Create Volume Snapshot
        api_response = api_instance.datacenters_volumes_create_snapshot_post(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, name=name, description=description, sec_auth_protection=sec_auth_protection, licence_type=licence_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_create_snapshot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **volume_id** | **str**| The unique ID of the Volume | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 
 **name** | **str**| The name of the snapshot | [optional] 
 **description** | **str**| The description of the snapshot | [optional] 
 **sec_auth_protection** | **bool**| Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc. | [optional] 
 **licence_type** | **str**| The OS type of this Snapshot | [optional] 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[Basic Authentication](../README.md#Basic Authentication), [Token Authentication](../README.md#Token Authentication)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successful operation |  * X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response.  <br>  * X-RateLimit-Limit - Average number of requests allowed per minute <br>  * X-RateLimit-Burst - Maximum number of concurrent API requests allowed <br>  * Location - Callback URL to poll async operation status <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacenters_volumes_delete**
> object datacenters_volumes_delete(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Volume

Deletes the specified volume. This will result in the volume being removed from your datacenter. Use this with caution.

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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Volume
        api_response = api_instance.datacenters_volumes_delete(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_delete: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Volume
        api_response = api_instance.datacenters_volumes_delete(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **volume_id** | **str**| The unique ID of the Volume | 
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

# **datacenters_volumes_find_by_id**
> Volume datacenters_volumes_find_by_id(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Volume

Retrieves the attributes of a given Volume

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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Volume
        api_response = api_instance.datacenters_volumes_find_by_id(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_find_by_id: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Volume
        api_response = api_instance.datacenters_volumes_find_by_id(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **volume_id** | **str**| The unique ID of the Volume | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Volume**](Volume.md)

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

# **datacenters_volumes_get**
> Volumes datacenters_volumes_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Volumes 

Retrieves a list of Volumes.

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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Volumes 
        api_response = api_instance.datacenters_volumes_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_get: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Volumes 
        api_response = api_instance.datacenters_volumes_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Volumes**](Volumes.md)

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

# **datacenters_volumes_patch**
> Volume datacenters_volumes_patch(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a Volume

You can use update attributes of a Volume

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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
volume = ionos_cloud_sdk.VolumeProperties() # VolumeProperties | Modified properties of Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Volume
        api_response = api_instance.datacenters_volumes_patch(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_patch: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
volume = ionos_cloud_sdk.VolumeProperties() # VolumeProperties | Modified properties of Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Volume
        api_response = api_instance.datacenters_volumes_patch(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **volume_id** | **str**| The unique ID of the Volume | 
 **volume** | [**VolumeProperties**](VolumeProperties.md)| Modified properties of Volume | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Volume**](Volume.md)

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

# **datacenters_volumes_post**
> Volume datacenters_volumes_post(datacenter_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Volume

Creates a volume within the datacenter. This will not attach the volume to a server. Please see the Servers section for details on how to attach storage volumes

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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume = ionos_cloud_sdk.Volume() # Volume | Volume to be created
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Volume
        api_response = api_instance.datacenters_volumes_post(datacenter_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_post: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume = ionos_cloud_sdk.Volume() # Volume | Volume to be created
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Volume
        api_response = api_instance.datacenters_volumes_post(datacenter_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **volume** | [**Volume**](Volume.md)| Volume to be created | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Volume**](Volume.md)

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

# **datacenters_volumes_put**
> Volume datacenters_volumes_put(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Volume

You can use update attributes of a Volume

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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
volume = ionos_cloud_sdk.Volume() # Volume | Modified Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Volume
        api_response = api_instance.datacenters_volumes_put(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_put: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
volume = ionos_cloud_sdk.Volume() # Volume | Modified Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Volume
        api_response = api_instance.datacenters_volumes_put(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **volume_id** | **str**| The unique ID of the Volume | 
 **volume** | [**Volume**](Volume.md)| Modified Volume | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Volume**](Volume.md)

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

# **datacenters_volumes_restore_snapshot_post**
> object datacenters_volumes_restore_snapshot_post(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, snapshot_id=snapshot_id)

Restore Volume Snapshot

This will restore a snapshot onto a volume. A snapshot is created as just another image that can be used to create subsequent volumes if you want or to restore an existing volume.

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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
snapshot_id = 'snapshot_id_example' # str | This is the ID of the snapshot (optional)

    try:
        # Restore Volume Snapshot
        api_response = api_instance.datacenters_volumes_restore_snapshot_post(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, snapshot_id=snapshot_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_restore_snapshot_post: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
volume_id = 'volume_id_example' # str | The unique ID of the Volume
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
snapshot_id = 'snapshot_id_example' # str | This is the ID of the snapshot (optional)

    try:
        # Restore Volume Snapshot
        api_response = api_instance.datacenters_volumes_restore_snapshot_post(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, snapshot_id=snapshot_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->datacenters_volumes_restore_snapshot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **volume_id** | **str**| The unique ID of the Volume | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 
 **snapshot_id** | **str**| This is the ID of the snapshot | [optional] 

### Return type

**object**

### Authorization

[Basic Authentication](../README.md#Basic Authentication), [Token Authentication](../README.md#Token Authentication)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successful operation |  * X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response.  <br>  * X-RateLimit-Limit - Average number of requests allowed per minute <br>  * X-RateLimit-Burst - Maximum number of concurrent API requests allowed <br>  * Location - Callback URL to poll async operation status <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 402 (trial access), 403 (insufficient permissions), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), 503 (maintenance) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

