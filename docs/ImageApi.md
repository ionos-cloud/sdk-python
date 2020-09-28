# ionos_cloud_sdk.ImageApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_delete**](ImageApi.md#images_delete) | **DELETE** /images/{imageId} | Delete an Image
[**images_find_by_id**](ImageApi.md#images_find_by_id) | **GET** /images/{imageId} | Retrieve an Image
[**images_get**](ImageApi.md#images_get) | **GET** /images | List Images 
[**images_patch**](ImageApi.md#images_patch) | **PATCH** /images/{imageId} | Partially modify an Image
[**images_put**](ImageApi.md#images_put) | **PUT** /images/{imageId} | Modify an Image


# **images_delete**
> object images_delete(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete an Image

Deletes the specified image. This operation is permitted on private image only.

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
    api_instance = ionos_cloud_sdk.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete an Image
        api_response = api_instance.images_delete(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->images_delete: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete an Image
        api_response = api_instance.images_delete(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->images_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 
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

# **images_find_by_id**
> Image images_find_by_id(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve an Image

Retrieves the attributes of a given image.

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
    api_instance = ionos_cloud_sdk.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve an Image
        api_response = api_instance.images_find_by_id(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->images_find_by_id: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve an Image
        api_response = api_instance.images_find_by_id(image_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->images_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Image**](Image.md)

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

# **images_get**
> Images images_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Images 

Retrieve a list of images within the datacenter

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
    api_instance = ionos_cloud_sdk.ImageApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Images 
        api_response = api_instance.images_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->images_get: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.ImageApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Images 
        api_response = api_instance.images_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Images**](Images.md)

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

# **images_patch**
> Image images_patch(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify an Image

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
    api_instance = ionos_cloud_sdk.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
image = ionos_cloud_sdk.ImageProperties() # ImageProperties | Modified Image
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify an Image
        api_response = api_instance.images_patch(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->images_patch: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
image = ionos_cloud_sdk.ImageProperties() # ImageProperties | Modified Image
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify an Image
        api_response = api_instance.images_patch(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->images_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 
 **image** | [**ImageProperties**](ImageProperties.md)| Modified Image | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Image**](Image.md)

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

# **images_put**
> Image images_put(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify an Image

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
    api_instance = ionos_cloud_sdk.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
image = ionos_cloud_sdk.Image() # Image | Modified Image
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify an Image
        api_response = api_instance.images_put(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->images_put: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.ImageApi(api_client)
    image_id = 'image_id_example' # str | 
image = ionos_cloud_sdk.Image() # Image | Modified Image
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify an Image
        api_response = api_instance.images_put(image_id, image, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImageApi->images_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 
 **image** | [**Image**](Image.md)| Modified Image | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Image**](Image.md)

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

