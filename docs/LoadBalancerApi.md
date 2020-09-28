# ionos_cloud_sdk.LoadBalancerApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datacenters_loadbalancers_balancednics_delete**](LoadBalancerApi.md#datacenters_loadbalancers_balancednics_delete) | **DELETE** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics/{nicId} | Detach a nic from loadbalancer
[**datacenters_loadbalancers_balancednics_find_by_nic**](LoadBalancerApi.md#datacenters_loadbalancers_balancednics_find_by_nic) | **GET** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics/{nicId} | Retrieve a nic attached to Load Balancer
[**datacenters_loadbalancers_balancednics_get**](LoadBalancerApi.md#datacenters_loadbalancers_balancednics_get) | **GET** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics | List Load Balancer Members 
[**datacenters_loadbalancers_balancednics_post**](LoadBalancerApi.md#datacenters_loadbalancers_balancednics_post) | **POST** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics | Attach a nic to Load Balancer
[**datacenters_loadbalancers_delete**](LoadBalancerApi.md#datacenters_loadbalancers_delete) | **DELETE** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Delete a Loadbalancer.
[**datacenters_loadbalancers_find_by_id**](LoadBalancerApi.md#datacenters_loadbalancers_find_by_id) | **GET** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Retrieve a loadbalancer
[**datacenters_loadbalancers_get**](LoadBalancerApi.md#datacenters_loadbalancers_get) | **GET** /datacenters/{datacenterId}/loadbalancers | List Load Balancers
[**datacenters_loadbalancers_patch**](LoadBalancerApi.md#datacenters_loadbalancers_patch) | **PATCH** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Partially modify a Loadbalancer
[**datacenters_loadbalancers_post**](LoadBalancerApi.md#datacenters_loadbalancers_post) | **POST** /datacenters/{datacenterId}/loadbalancers | Create a Load Balancer
[**datacenters_loadbalancers_put**](LoadBalancerApi.md#datacenters_loadbalancers_put) | **PUT** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Modify a Load Balancer


# **datacenters_loadbalancers_balancednics_delete**
> object datacenters_loadbalancers_balancednics_delete(datacenter_id, loadbalancer_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Detach a nic from loadbalancer

This will remove a nic from Load Balancer

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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
nic_id = 'nic_id_example' # str | The unique ID of the NIC
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Detach a nic from loadbalancer
        api_response = api_instance.datacenters_loadbalancers_balancednics_delete(datacenter_id, loadbalancer_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_delete: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
nic_id = 'nic_id_example' # str | The unique ID of the NIC
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Detach a nic from loadbalancer
        api_response = api_instance.datacenters_loadbalancers_balancednics_delete(datacenter_id, loadbalancer_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **loadbalancer_id** | **str**| The unique ID of the Load Balancer | 
 **nic_id** | **str**| The unique ID of the NIC | 
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

# **datacenters_loadbalancers_balancednics_find_by_nic**
> Nic datacenters_loadbalancers_balancednics_find_by_nic(datacenter_id, loadbalancer_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a nic attached to Load Balancer

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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
nic_id = 'nic_id_example' # str | The unique ID of the NIC
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a nic attached to Load Balancer
        api_response = api_instance.datacenters_loadbalancers_balancednics_find_by_nic(datacenter_id, loadbalancer_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_find_by_nic: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
nic_id = 'nic_id_example' # str | The unique ID of the NIC
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a nic attached to Load Balancer
        api_response = api_instance.datacenters_loadbalancers_balancednics_find_by_nic(datacenter_id, loadbalancer_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_find_by_nic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **loadbalancer_id** | **str**| The unique ID of the Load Balancer | 
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

# **datacenters_loadbalancers_balancednics_get**
> BalancedNics datacenters_loadbalancers_balancednics_get(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Load Balancer Members 

You can retrieve a list of nics attached to a Load Balancer

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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Load Balancer Members 
        api_response = api_instance.datacenters_loadbalancers_balancednics_get(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_get: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Load Balancer Members 
        api_response = api_instance.datacenters_loadbalancers_balancednics_get(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **loadbalancer_id** | **str**| The unique ID of the Load Balancer | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**BalancedNics**](BalancedNics.md)

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

# **datacenters_loadbalancers_balancednics_post**
> Nic datacenters_loadbalancers_balancednics_post(datacenter_id, loadbalancer_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Attach a nic to Load Balancer

This will attach a pre-existing nic to a Load Balancer. 

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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
nic = ionos_cloud_sdk.Nic() # Nic | Nic id to be attached
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Attach a nic to Load Balancer
        api_response = api_instance.datacenters_loadbalancers_balancednics_post(datacenter_id, loadbalancer_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_post: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
nic = ionos_cloud_sdk.Nic() # Nic | Nic id to be attached
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Attach a nic to Load Balancer
        api_response = api_instance.datacenters_loadbalancers_balancednics_post(datacenter_id, loadbalancer_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **loadbalancer_id** | **str**| The unique ID of the Load Balancer | 
 **nic** | [**Nic**](Nic.md)| Nic id to be attached | 
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

# **datacenters_loadbalancers_delete**
> object datacenters_loadbalancers_delete(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Loadbalancer.

Removes the specific Loadbalancer

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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Loadbalancer.
        api_response = api_instance.datacenters_loadbalancers_delete(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_delete: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Loadbalancer.
        api_response = api_instance.datacenters_loadbalancers_delete(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **loadbalancer_id** | **str**| The unique ID of the Load Balancer | 
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

# **datacenters_loadbalancers_find_by_id**
> Loadbalancer datacenters_loadbalancers_find_by_id(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a loadbalancer

Retrieves the attributes of a given Loadbalancer

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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a loadbalancer
        api_response = api_instance.datacenters_loadbalancers_find_by_id(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_find_by_id: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a loadbalancer
        api_response = api_instance.datacenters_loadbalancers_find_by_id(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **loadbalancer_id** | **str**| The unique ID of the Load Balancer | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Loadbalancer**](Loadbalancer.md)

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

# **datacenters_loadbalancers_get**
> Loadbalancers datacenters_loadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Load Balancers

Retrieve a list of Load Balancers within the datacenter

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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Load Balancers
        api_response = api_instance.datacenters_loadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_get: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Load Balancers
        api_response = api_instance.datacenters_loadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Loadbalancers**](Loadbalancers.md)

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

# **datacenters_loadbalancers_patch**
> Loadbalancer datacenters_loadbalancers_patch(datacenter_id, loadbalancer_id, loadbalancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify a Loadbalancer

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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
loadbalancer = ionos_cloud_sdk.LoadbalancerProperties() # LoadbalancerProperties | Modified Loadbalancer
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Loadbalancer
        api_response = api_instance.datacenters_loadbalancers_patch(datacenter_id, loadbalancer_id, loadbalancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_patch: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
loadbalancer = ionos_cloud_sdk.LoadbalancerProperties() # LoadbalancerProperties | Modified Loadbalancer
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Loadbalancer
        api_response = api_instance.datacenters_loadbalancers_patch(datacenter_id, loadbalancer_id, loadbalancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **loadbalancer_id** | **str**| The unique ID of the Load Balancer | 
 **loadbalancer** | [**LoadbalancerProperties**](LoadbalancerProperties.md)| Modified Loadbalancer | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Loadbalancer**](Loadbalancer.md)

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

# **datacenters_loadbalancers_post**
> Loadbalancer datacenters_loadbalancers_post(datacenter_id, loadbalancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Load Balancer

Creates a Loadbalancer within the datacenter

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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer = ionos_cloud_sdk.Loadbalancer() # Loadbalancer | Loadbalancer to be created
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Load Balancer
        api_response = api_instance.datacenters_loadbalancers_post(datacenter_id, loadbalancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_post: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer = ionos_cloud_sdk.Loadbalancer() # Loadbalancer | Loadbalancer to be created
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Load Balancer
        api_response = api_instance.datacenters_loadbalancers_post(datacenter_id, loadbalancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **loadbalancer** | [**Loadbalancer**](Loadbalancer.md)| Loadbalancer to be created | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Loadbalancer**](Loadbalancer.md)

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

# **datacenters_loadbalancers_put**
> Loadbalancer datacenters_loadbalancers_put(datacenter_id, loadbalancer_id, loadbalancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Load Balancer

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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
loadbalancer = ionos_cloud_sdk.Loadbalancer() # Loadbalancer | Modified Loadbalancer
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Load Balancer
        api_response = api_instance.datacenters_loadbalancers_put(datacenter_id, loadbalancer_id, loadbalancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_put: %s\n" % e)
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
    api_instance = ionos_cloud_sdk.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
loadbalancer = ionos_cloud_sdk.Loadbalancer() # Loadbalancer | Modified Loadbalancer
pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Load Balancer
        api_response = api_instance.datacenters_loadbalancers_put(datacenter_id, loadbalancer_id, loadbalancer, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datacenter_id** | **str**| The unique ID of the datacenter | 
 **loadbalancer_id** | **str**| The unique ID of the Load Balancer | 
 **loadbalancer** | [**Loadbalancer**](Loadbalancer.md)| Modified Loadbalancer | 
 **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True]
 **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0]
 **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional] 

### Return type

[**Loadbalancer**](Loadbalancer.md)

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

