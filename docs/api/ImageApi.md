# ImageApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**images_delete**](ImageApi.md#images_delete) | **DELETE** /images/{imageId} | Delete an Image |
| [**images_find_by_id**](ImageApi.md#images_find_by_id) | **GET** /images/{imageId} | Retrieve an Image |
| [**images_get**](ImageApi.md#images_get) | **GET** /images | List Images  |
| [**images_patch**](ImageApi.md#images_patch) | **PATCH** /images/{imageId} | Partially modify an Image |
| [**images_put**](ImageApi.md#images_put) | **PUT** /images/{imageId} | Modify an Image |


# **images_delete**
> object images_delete(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete an Image

Deletes the specified image. This operation is permitted on private image only.

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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    try:
        # Delete an Image
        api_response = api_instance.images_delete(image_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **image_id** | **str**|  |  |
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

# **images_find_by_id**
> Image images_find_by_id(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve an Image

Retrieves the attributes of a given image.

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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    try:
        # Retrieve an Image
        api_response = api_instance.images_find_by_id(image_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **image_id** | **str**|  |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Image**](../models/Image.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **images_get**
> Images images_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Images 

Retrieve a list of images within the datacenter

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
    api_instance = ionoscloud.ImageApi(api_client)
    try:
        # List Images 
        api_response = api_instance.images_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Images**](../models/Images.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **images_patch**
> Image images_patch(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify an Image

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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    image = ionoscloud.ImageProperties() # ImageProperties | Modified Image
    try:
        # Partially modify an Image
        api_response = api_instance.images_patch(image_id, image)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **image_id** | **str**|  |  |
| **image** | [**ImageProperties**](ImageProperties.md)| Modified Image |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Image**](../models/Image.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **images_put**
> Image images_put(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify an Image

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
    api_instance = ionoscloud.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
    image = ionoscloud.Image() # Image | Modified Image
    try:
        # Modify an Image
        api_response = api_instance.images_put(image_id, image)
        print(api_response)
    except ApiException as e:
        print('Exception when calling ImageApi.images_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **image_id** | **str**|  |  |
| **image** | [**Image**](Image.md)| Modified Image |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Image**](../models/Image.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json
