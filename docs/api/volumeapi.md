# VolumeApi

## VolumeApi

All URIs are relative to [https://api.ionos.com/cloudapi/v5](https://api.ionos.com/cloudapi/v5)

| Method | HTTP request | Description |
| :--- | :--- | :--- |
| [**datacenters\_volumes\_create\_snapshot\_post**](volumeapi.md#datacenters_volumes_create_snapshot_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/create-snapshot | Create Volume Snapshot |
| [**datacenters\_volumes\_delete**](volumeapi.md#datacenters_volumes_delete) | **DELETE** /datacenters/{datacenterId}/volumes/{volumeId} | Delete a Volume |
| [**datacenters\_volumes\_find\_by\_id**](volumeapi.md#datacenters_volumes_find_by_id) | **GET** /datacenters/{datacenterId}/volumes/{volumeId} | Retrieve a Volume |
| [**datacenters\_volumes\_get**](volumeapi.md#datacenters_volumes_get) | **GET** /datacenters/{datacenterId}/volumes | List Volumes |
| [**datacenters\_volumes\_patch**](volumeapi.md#datacenters_volumes_patch) | **PATCH** /datacenters/{datacenterId}/volumes/{volumeId} | Partially modify a Volume |
| [**datacenters\_volumes\_post**](volumeapi.md#datacenters_volumes_post) | **POST** /datacenters/{datacenterId}/volumes | Create a Volume |
| [**datacenters\_volumes\_put**](volumeapi.md#datacenters_volumes_put) | **PUT** /datacenters/{datacenterId}/volumes/{volumeId} | Modify a Volume |
| [**datacenters\_volumes\_restore\_snapshot\_post**](volumeapi.md#datacenters_volumes_restore_snapshot_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/restore-snapshot | Restore Volume Snapshot |

## **datacenters\_volumes\_create\_snapshot\_post**

> Snapshot datacenters\_volumes\_create\_snapshot\_post\(datacenter\_id, volume\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number, name=name, description=description, sec\_auth\_protection=sec\_auth\_protection, licence\_type=licence\_type\)

Create Volume Snapshot

Creates a snapshot of a volume within the datacenter. You can use a snapshot to create a new storage volume or to restore a storage volume.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
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
        print('Exception when calling VolumeApi.datacenters_volumes_create_snapshot_post: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
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
        print('Exception when calling VolumeApi.datacenters_volumes_create_snapshot_post: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |
| **name** | **str** | The name of the snapshot | \[optional\] |
| **description** | **str** | The description of the snapshot | \[optional\] |
| **sec\_auth\_protection** | **bool** | Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc. | \[optional\] |
| **licence\_type** | **str** | The OS type of this Snapshot | \[optional\] |

### Return type

[**Snapshot**](../models/snapshot.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/x-www-form-urlencoded
* **Accept**: application/json

## **datacenters\_volumes\_delete**

> object datacenters\_volumes\_delete\(datacenter\_id, volume\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Volume

Deletes the specified volume. This will result in the volume being removed from your datacenter. Use this with caution.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
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
        print('Exception when calling VolumeApi.datacenters_volumes_delete: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
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
        print('Exception when calling VolumeApi.datacenters_volumes_delete: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_volumes\_find\_by\_id**

> Volume datacenters\_volumes\_find\_by\_id\(datacenter\_id, volume\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Volume

Retrieves the attributes of a given Volume

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
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
        print('Exception when calling VolumeApi.datacenters_volumes_find_by_id: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
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
        print('Exception when calling VolumeApi.datacenters_volumes_find_by_id: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Volume**](../models/volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_volumes\_get**

> Volumes datacenters\_volumes\_get\(datacenter\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number, offset=offset, limit=limit\)

List Volumes

Retrieves a list of Volumes.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)
    try:
        # List Volumes 
        api_response = api_instance.datacenters_volumes_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_get: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)
    try:
        # List Volumes 
        api_response = api_instance.datacenters_volumes_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_get: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |
| **offset** | **int** | the first element \(of the total list of elements\) to include in the response \(use together with &lt;code&gt;limit&lt;/code&gt; for pagination\) | \[optional\] \[default to 0\] |
| **limit** | **int** | the maximum number of elements to return \(use together with &lt;code&gt;offset&lt;/code&gt; for pagination\) | \[optional\] \[default to 1000\] |

### Return type

[**Volumes**](../models/volumes.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_volumes\_patch**

> Volume datacenters\_volumes\_patch\(datacenter\_id, volume\_id, volume, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Partially modify a Volume

You can use update attributes of a Volume

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    volume = ionoscloud.VolumeProperties() # VolumeProperties | Modified properties of Volume
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify a Volume
        api_response = api_instance.datacenters_volumes_patch(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_patch: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    volume = ionoscloud.VolumeProperties() # VolumeProperties | Modified properties of Volume
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify a Volume
        api_response = api_instance.datacenters_volumes_patch(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_patch: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **volume** | [**VolumeProperties**](../models/volumeproperties.md) | Modified properties of Volume |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Volume**](../models/volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **datacenters\_volumes\_post**

> Volume datacenters\_volumes\_post\(datacenter\_id, volume, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Create a Volume

Creates a volume within the datacenter. This will not attach the volume to a server. Please see the Servers section for details on how to attach storage volumes

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume = ionoscloud.Volume() # Volume | Volume to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a Volume
        api_response = api_instance.datacenters_volumes_post(datacenter_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_post: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume = ionoscloud.Volume() # Volume | Volume to be created
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a Volume
        api_response = api_instance.datacenters_volumes_post(datacenter_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_post: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **volume** | [**Volume**](../models/volume.md) | Volume to be created |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Volume**](../models/volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **datacenters\_volumes\_put**

> Volume datacenters\_volumes\_put\(datacenter\_id, volume\_id, volume, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a Volume

You can use update attributes of a Volume

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    volume = ionoscloud.Volume() # Volume | Modified Volume
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Volume
        api_response = api_instance.datacenters_volumes_put(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_put: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    volume = ionoscloud.Volume() # Volume | Modified Volume
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Volume
        api_response = api_instance.datacenters_volumes_put(datacenter_id, volume_id, volume, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling VolumeApi.datacenters_volumes_put: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **volume** | [**Volume**](../models/volume.md) | Modified Volume |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Volume**](../models/volume.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **datacenters\_volumes\_restore\_snapshot\_post**

> object datacenters\_volumes\_restore\_snapshot\_post\(datacenter\_id, volume\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number, snapshot\_id=snapshot\_id\)

Restore Volume Snapshot

This will restore a snapshot onto a volume. A snapshot is created as just another image that can be used to create subsequent volumes if you want or to restore an existing volume.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
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
        print('Exception when calling VolumeApi.datacenters_volumes_restore_snapshot_post: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.VolumeApi(api_client)
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
        print('Exception when calling VolumeApi.datacenters_volumes_restore_snapshot_post: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |
| **snapshot\_id** | **str** | This is the ID of the snapshot | \[optional\] |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/x-www-form-urlencoded
* **Accept**: application/json

