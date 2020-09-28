# ionos_cloud_sdk.LanApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datacenters_lans_delete**](LanApi.md#datacenters_lans_delete) | **DELETE** /datacenters/{datacenterId}/lans/{lanId} | Delete a Lan.
[**datacenters_lans_find_by_id**](LanApi.md#datacenters_lans_find_by_id) | **GET** /datacenters/{datacenterId}/lans/{lanId} | Retrieve a Lan
[**datacenters_lans_get**](LanApi.md#datacenters_lans_get) | **GET** /datacenters/{datacenterId}/lans | List Lans
[**datacenters_lans_nics_find_by_id**](LanApi.md#datacenters_lans_nics_find_by_id) | **GET** /datacenters/{datacenterId}/lans/{lanId}/nics/{nicId} | Retrieve a nic attached to lan
[**datacenters_lans_nics_get**](LanApi.md#datacenters_lans_nics_get) | **GET** /datacenters/{datacenterId}/lans/{lanId}/nics | List Lan Members 
[**datacenters_lans_nics_post**](LanApi.md#datacenters_lans_nics_post) | **POST** /datacenters/{datacenterId}/lans/{lanId}/nics | Attach a nic
[**datacenters_lans_patch**](LanApi.md#datacenters_lans_patch) | **PATCH** /datacenters/{datacenterId}/lans/{lanId} | Partially modify a Lan
[**datacenters_lans_post**](LanApi.md#datacenters_lans_post) | **POST** /datacenters/{datacenterId}/lans | Create a Lan
[**datacenters_lans_put**](LanApi.md#datacenters_lans_put) | **PUT** /datacenters/{datacenterId}/lans/{lanId} | Modify a Lan


# **datacenters_lans_delete**
> object datacenters_lans_delete(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Lan.

Removes the specific Lan

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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Lan.
        api_response = api_instance.datacenters_lans_delete(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_delete: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Lan.
        api_response = api_instance.datacenters_lans_delete(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **lan_id** | **str**| The unique ID of the LAN | 
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

# **datacenters_lans_find_by_id**
> Lan datacenters_lans_find_by_id(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Lan

Retrieves the attributes of a given LAN

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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Lan
        api_response = api_instance.datacenters_lans_find_by_id(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_find_by_id: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Lan
        api_response = api_instance.datacenters_lans_find_by_id(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **lan_id** | **str**| The unique ID of the LAN | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Lan**](Lan.md)

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

# **datacenters_lans_get**
> Lans datacenters_lans_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Lans

Retrieve a list of LANs within the datacenter

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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Lans
        api_response = api_instance.datacenters_lans_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_get: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Lans
        api_response = api_instance.datacenters_lans_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Lans**](Lans.md)

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

# **datacenters_lans_nics_find_by_id**
> Nic datacenters_lans_nics_find_by_id(datacenter_id, lan_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a nic attached to lan

This will retrieve the properties of an attached nic.

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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
nic_id = 'nic_id_example' # str | The unique ID of the NIC
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a nic attached to lan
        api_response = api_instance.datacenters_lans_nics_find_by_id(datacenter_id, lan_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_nics_find_by_id: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
nic_id = 'nic_id_example' # str | The unique ID of the NIC
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a nic attached to lan
        api_response = api_instance.datacenters_lans_nics_find_by_id(datacenter_id, lan_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_nics_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **lan_id** | **str**| The unique ID of the LAN | 
 **nic_id** | **str**| The unique ID of the NIC | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Nic**](Nic.md)

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

# **datacenters_lans_nics_get**
> LanNics datacenters_lans_nics_get(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Lan Members 

You can retrieve a list of nics attached to a lan

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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Lan Members 
        api_response = api_instance.datacenters_lans_nics_get(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_nics_get: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Lan Members 
        api_response = api_instance.datacenters_lans_nics_get(datacenter_id, lan_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_nics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **lan_id** | **str**| The unique ID of the LAN | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**LanNics**](LanNics.md)

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

# **datacenters_lans_nics_post**
> Nic datacenters_lans_nics_post(datacenter_id, lan_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Attach a nic

This will attach a pre-existing nic to a lan. 

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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
nic = ionos_cloud_sdk.Nic() # Nic | Nic to be attached
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Attach a nic
        api_response = api_instance.datacenters_lans_nics_post(datacenter_id, lan_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_nics_post: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
nic = ionos_cloud_sdk.Nic() # Nic | Nic to be attached
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Attach a nic
        api_response = api_instance.datacenters_lans_nics_post(datacenter_id, lan_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_nics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **lan_id** | **str**| The unique ID of the LAN | 
 **nic** | [**Nic**](Nic.md)| Nic to be attached | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Nic**](Nic.md)

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

# **datacenters_lans_patch**
> Lan datacenters_lans_patch(datacenter_id, lan_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a Lan

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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
lan = ionos_cloud_sdk.LanProperties() # LanProperties | Modified Lan
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Lan
        api_response = api_instance.datacenters_lans_patch(datacenter_id, lan_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_patch: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
lan = ionos_cloud_sdk.LanProperties() # LanProperties | Modified Lan
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Lan
        api_response = api_instance.datacenters_lans_patch(datacenter_id, lan_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **lan_id** | **str**| The unique ID of the LAN | 
 **lan** | [**LanProperties**](LanProperties.md)| Modified Lan | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Lan**](Lan.md)

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

# **datacenters_lans_post**
> LanPost datacenters_lans_post(datacenter_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Lan

Creates a LAN within the datacenter

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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan = ionos_cloud_sdk.LanPost() # LanPost | Lan to be created
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Lan
        api_response = api_instance.datacenters_lans_post(datacenter_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_post: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan = ionos_cloud_sdk.LanPost() # LanPost | Lan to be created
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Lan
        api_response = api_instance.datacenters_lans_post(datacenter_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **lan** | [**LanPost**](LanPost.md)| Lan to be created | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**LanPost**](LanPost.md)

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

# **datacenters_lans_put**
> Lan datacenters_lans_put(datacenter_id, lan_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Lan

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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
lan = ionos_cloud_sdk.Lan() # Lan | Modified Lan
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Lan
        api_response = api_instance.datacenters_lans_put(datacenter_id, lan_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_put: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LanApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
lan_id = 'lan_id_example' # str | The unique ID of the LAN
lan = ionos_cloud_sdk.Lan() # Lan | Modified Lan
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Lan
        api_response = api_instance.datacenters_lans_put(datacenter_id, lan_id, lan, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanApi->datacenters_lans_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **lan_id** | **str**| The unique ID of the LAN | 
 **lan** | [**Lan**](Lan.md)| Modified Lan | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Lan**](Lan.md)

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

