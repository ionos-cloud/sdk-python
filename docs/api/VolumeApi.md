# VolumeApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_volumes_create_snapshot_post**](VolumeApi.md#datacenters_volumes_create_snapshot_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/create-snapshot | Create Volume Snapshot |
| [**datacenters_volumes_delete**](VolumeApi.md#datacenters_volumes_delete) | **DELETE** /datacenters/{datacenterId}/volumes/{volumeId} | Delete a Volume |
| [**datacenters_volumes_find_by_id**](VolumeApi.md#datacenters_volumes_find_by_id) | **GET** /datacenters/{datacenterId}/volumes/{volumeId} | Retrieve a Volume |
| [**datacenters_volumes_get**](VolumeApi.md#datacenters_volumes_get) | **GET** /datacenters/{datacenterId}/volumes | List Volumes  |
| [**datacenters_volumes_patch**](VolumeApi.md#datacenters_volumes_patch) | **PATCH** /datacenters/{datacenterId}/volumes/{volumeId} | Partially modify a Volume |
| [**datacenters_volumes_post**](VolumeApi.md#datacenters_volumes_post) | **POST** /datacenters/{datacenterId}/volumes | Create a Volume |
| [**datacenters_volumes_put**](VolumeApi.md#datacenters_volumes_put) | **PUT** /datacenters/{datacenterId}/volumes/{volumeId} | Modify a Volume |
| [**datacenters_volumes_restore_snapshot_post**](VolumeApi.md#datacenters_volumes_restore_snapshot_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/restore-snapshot | Restore Volume Snapshot |


# **datacenters_volumes_create_snapshot_post**
> Snapshot datacenters_volumes_create_snapshot_post(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, name=name, description=description, sec_auth_protection=sec_auth_protection, licence_type=licence_type)

Create Volume Snapshot

Creates a snapshot of a volume within the datacenter. You can use a snapshot to create a new storage volume or to restore a storage volume.

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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    try:
        # Create Volume Snapshot
        api_response = api_instance.datacenters_volumes_create_snapshot_post(datacenter_id, volume_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_create_snapshot_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **name** | **str**| The name of the snapshot | [optional]  |
| **description** | **str**| The description of the snapshot | [optional]  |
| **sec_auth_protection** | **bool**| Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc. | [optional]  |
| **licence_type** | **str**| The OS type of this Snapshot | [optional]  |

### Return type

[**Snapshot**](../models/Snapshot.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

# **datacenters_volumes_delete**
> object datacenters_volumes_delete(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Volume

Deletes the specified volume. This will result in the volume being removed from your datacenter. Use this with caution.

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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    try:
        # Delete a Volume
        api_response = api_instance.datacenters_volumes_delete(datacenter_id, volume_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
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

# **datacenters_volumes_find_by_id**
> Volume datacenters_volumes_find_by_id(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Volume

Retrieves the attributes of a given Volume

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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    try:
        # Retrieve a Volume
        api_response = api_instance.datacenters_volumes_find_by_id(datacenter_id, volume_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Volume**](../models/Volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_volumes_get**
> Volumes datacenters_volumes_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List Volumes 

Retrieves a list of Volumes.

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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    try:
        # List Volumes 
        api_response = api_instance.datacenters_volumes_get(datacenter_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with &lt;code&gt;limit&lt;/code&gt; for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with &lt;code&gt;offset&lt;/code&gt; for pagination) | [optional] [default to 1000] |

### Return type

[**Volumes**](../models/Volumes.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_volumes_patch**
> Volume datacenters_volumes_patch(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a Volume

You can use update attributes of a Volume

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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    volume = ionoscloud.VolumeProperties() # VolumeProperties | Modified properties of Volume
    try:
        # Partially modify a Volume
        api_response = api_instance.datacenters_volumes_patch(datacenter_id, volume_id, volume)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
| **volume** | [**VolumeProperties**](VolumeProperties.md)| Modified properties of Volume |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Volume**](../models/Volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_volumes_post**
> Volume datacenters_volumes_post(datacenter_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Volume

Creates a volume within the datacenter. This will not attach the volume to a server. Please see the Servers section for details on how to attach storage volumes

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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume = ionoscloud.Volume() # Volume | Volume to be created
    try:
        # Create a Volume
        api_response = api_instance.datacenters_volumes_post(datacenter_id, volume)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **volume** | [**Volume**](Volume.md)| Volume to be created |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Volume**](../models/Volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_volumes_put**
> Volume datacenters_volumes_put(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Volume

You can use update attributes of a Volume

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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    volume = ionoscloud.Volume() # Volume | Modified Volume
    try:
        # Modify a Volume
        api_response = api_instance.datacenters_volumes_put(datacenter_id, volume_id, volume)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
| **volume** | [**Volume**](Volume.md)| Modified Volume |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Volume**](../models/Volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_volumes_restore_snapshot_post**
> object datacenters_volumes_restore_snapshot_post(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, snapshot_id=snapshot_id)

Restore Volume Snapshot

This will restore a snapshot onto a volume. A snapshot is created as just another image that can be used to create subsequent volumes if you want or to restore an existing volume.

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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    try:
        # Restore Volume Snapshot
        api_response = api_instance.datacenters_volumes_restore_snapshot_post(datacenter_id, volume_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_restore_snapshot_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the datacenter |  |
| **volume_id** | **str**| The unique ID of the Volume |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **snapshot_id** | **str**| This is the ID of the snapshot | [optional]  |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json
