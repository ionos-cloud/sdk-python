# VolumesApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**datacenters_volumes_create_snapshot_post**](VolumesApi.md#datacenters_volumes_create_snapshot_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/create-snapshot | Create volume snapshots |
| [**datacenters_volumes_delete**](VolumesApi.md#datacenters_volumes_delete) | **DELETE** /datacenters/{datacenterId}/volumes/{volumeId} | Delete volumes |
| [**datacenters_volumes_find_by_id**](VolumesApi.md#datacenters_volumes_find_by_id) | **GET** /datacenters/{datacenterId}/volumes/{volumeId} | Retrieve volumes |
| [**datacenters_volumes_get**](VolumesApi.md#datacenters_volumes_get) | **GET** /datacenters/{datacenterId}/volumes | List volumes |
| [**datacenters_volumes_patch**](VolumesApi.md#datacenters_volumes_patch) | **PATCH** /datacenters/{datacenterId}/volumes/{volumeId} | Partially modify volumes |
| [**datacenters_volumes_post**](VolumesApi.md#datacenters_volumes_post) | **POST** /datacenters/{datacenterId}/volumes | Create a Volume |
| [**datacenters_volumes_put**](VolumesApi.md#datacenters_volumes_put) | **PUT** /datacenters/{datacenterId}/volumes/{volumeId} | Modify a Volume by ID |
| [**datacenters_volumes_restore_snapshot_post**](VolumesApi.md#datacenters_volumes_restore_snapshot_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/restore-snapshot | Restore volume snapshots |


# **datacenters_volumes_create_snapshot_post**
> Snapshot datacenters_volumes_create_snapshot_post(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, name=name, description=description, sec_auth_protection=sec_auth_protection, licence_type=licence_type)

Create volume snapshots

Create a snapshot of the specified volume within the data center; this snapshot can later be used to restore this volume.

### Example

```python
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
    api_instance = ionoscloud.VolumesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    try:
        # Create volume snapshots
        api_response = api_instance.datacenters_volumes_create_snapshot_post(datacenter_id, volume_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumesApi.datacenters_volumes_create_snapshot_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |
| **name** | **str**| Snapshot name | [optional]  |
| **description** | **str**| Snapshot description | [optional]  |
| **sec_auth_protection** | **bool**| Flag for enabling extra protection for this snapshot, such as two-step verification. | [optional]  |
| **licence_type** | **str**| The OS type for this snapshot. | [optional]  |

### Return type

[**Snapshot**](../models/Snapshot.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

# **datacenters_volumes_delete**
> datacenters_volumes_delete(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete volumes

Delete the specified volume within the data center. Use with caution, the volume will be permanently removed!

### Example

```python
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
    api_instance = ionoscloud.VolumesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    try:
        # Delete volumes
        api_instance.datacenters_volumes_delete(datacenter_id, volume_id)
    except ApiException as e:
        print('Exception when calling VolumesApi.datacenters_volumes_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
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

# **datacenters_volumes_find_by_id**
> Volume datacenters_volumes_find_by_id(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve volumes

Retrieve the properties of the specified volume within the data center.

### Example

```python
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
    api_instance = ionoscloud.VolumesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    try:
        # Retrieve volumes
        api_response = api_instance.datacenters_volumes_find_by_id(datacenter_id, volume_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumesApi.datacenters_volumes_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Volume**](../models/Volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_volumes_get**
> Volumes datacenters_volumes_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List volumes

List all the volumes within the data center.

### Example

```python
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
    api_instance = ionoscloud.VolumesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    try:
        # List volumes
        api_response = api_instance.datacenters_volumes_get(datacenter_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumesApi.datacenters_volumes_get: %s\n' % e)
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

[**Volumes**](../models/Volumes.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **datacenters_volumes_patch**
> Volume datacenters_volumes_patch(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify volumes

Update the properties of the specified storage volume within the data center.

### Example

```python
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
    api_instance = ionoscloud.VolumesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    volume = ionoscloud.VolumeProperties() # VolumeProperties | The properties of the volume to be updated.
    try:
        # Partially modify volumes
        api_response = api_instance.datacenters_volumes_patch(datacenter_id, volume_id, volume)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumesApi.datacenters_volumes_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
| **volume** | [**VolumeProperties**](../models/VolumeProperties.md)| The properties of the volume to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

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

Creates a storage volume within the specified data center. The volume will not be attached! Attaching volumes is described in the Servers section.

### Example

```python
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
    api_instance = ionoscloud.VolumesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume = ionoscloud.Volume() # Volume | The volume to create.
    try:
        # Create a Volume
        api_response = api_instance.datacenters_volumes_post(datacenter_id, volume)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumesApi.datacenters_volumes_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume** | [**Volume**](../models/Volume.md)| The volume to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Volume**](../models/Volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_volumes_put**
> Volume datacenters_volumes_put(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Volume by ID

Modifies the properties of the specified volume within the data center.

### Example

```python
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
    api_instance = ionoscloud.VolumesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    volume = ionoscloud.Volume() # Volume | The modified volume
    try:
        # Modify a Volume by ID
        api_response = api_instance.datacenters_volumes_put(datacenter_id, volume_id, volume)
        print(api_response)
    except ApiException as e:
        print('Exception when calling VolumesApi.datacenters_volumes_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
| **volume** | [**Volume**](../models/Volume.md)| The modified volume |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Volume**](../models/Volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **datacenters_volumes_restore_snapshot_post**
> datacenters_volumes_restore_snapshot_post(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, snapshot_id=snapshot_id)

Restore volume snapshots

Restore a snapshot for the specified volume within the data center. A snapshot is an image of a volume, which can be used to restore this volume at a later time.

### Example

```python
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
    api_instance = ionoscloud.VolumesApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the data center.
    volume_id = 'volume_id_example' # str | The unique ID of the volume.
    try:
        # Restore volume snapshots
        api_instance.datacenters_volumes_restore_snapshot_post(datacenter_id, volume_id)
    except ApiException as e:
        print('Exception when calling VolumesApi.datacenters_volumes_restore_snapshot_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **datacenter_id** | **str**| The unique ID of the data center. |  |
| **volume_id** | **str**| The unique ID of the volume. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |
| **snapshot_id** | **str**| The unique ID of the snapshot. | [optional]  |

### Return type

void (empty response body)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

