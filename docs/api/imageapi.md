# ImageApi

## ImageApi

All URIs are relative to [https://api.ionos.com/cloudapi/v5](https://api.ionos.com/cloudapi/v5)

| Method | HTTP request | Description |
| :--- | :--- | :--- |
| [**images\_delete**](imageapi.md#images_delete) | **DELETE** /images/{imageId} | Delete an Image |
| [**images\_find\_by\_id**](imageapi.md#images_find_by_id) | **GET** /images/{imageId} | Retrieve an Image |
| [**images\_get**](imageapi.md#images_get) | **GET** /images | List Images |
| [**images\_patch**](imageapi.md#images_patch) | **PATCH** /images/{imageId} | Partially modify an Image |
| [**images\_put**](imageapi.md#images_put) | **PUT** /images/{imageId} | Modify an Image |

## **images\_delete**

> object images\_delete\(image\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete an Image

Deletes the specified image. This operation is permitted on private image only.

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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete an Image
        api_response = api_instance.images_delete(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_delete: %s\n' % e)
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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete an Image
        api_response = api_instance.images_delete(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_delete: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **image\_id** | **str** |  |  |
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

## **images\_find\_by\_id**

> Image images\_find\_by\_id\(image\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve an Image

Retrieves the attributes of a given image.

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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve an Image
        api_response = api_instance.images_find_by_id(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_find_by_id: %s\n' % e)
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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve an Image
        api_response = api_instance.images_find_by_id(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_find_by_id: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **image\_id** | **str** |  |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Image**](../models/image.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **images\_get**

> Images images\_get\(pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List Images

Retrieve a list of images within the datacenter

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
    api_instance = ionoscloud.ImageApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List Images 
        api_response = api_instance.images_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_get: %s\n' % e)
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
    api_instance = ionoscloud.ImageApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List Images 
        api_response = api_instance.images_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_get: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Images**](../models/images.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **images\_patch**

> Image images\_patch\(image\_id, image, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Partially modify an Image

You can use update attributes of a resource

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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    image = ionoscloud.ImageProperties() # ImageProperties | Modified Image
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify an Image
        api_response = api_instance.images_patch(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_patch: %s\n' % e)
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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    image = ionoscloud.ImageProperties() # ImageProperties | Modified Image
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Partially modify an Image
        api_response = api_instance.images_patch(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_patch: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **image\_id** | **str** |  |  |
| **image** | [**ImageProperties**](../models/imageproperties.md) | Modified Image |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Image**](../models/image.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **images\_put**

> Image images\_put\(image\_id, image, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify an Image

You can use update attributes of a resource

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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    image = ionoscloud.Image() # Image | Modified Image
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify an Image
        api_response = api_instance.images_put(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_put: %s\n' % e)
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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    image = ionoscloud.Image() # Image | Modified Image
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify an Image
        api_response = api_instance.images_put(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_put: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **image\_id** | **str** |  |  |
| **image** | [**Image**](../models/image.md) | Modified Image |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Image**](../models/image.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

