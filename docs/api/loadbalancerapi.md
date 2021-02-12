# LoadBalancerApi

## LoadBalancerApi

All URIs are relative to [https://api.ionos.com/cloudapi/v5](https://api.ionos.com/cloudapi/v5)

| Method | HTTP request | Description |
| :--- | :--- | :--- |
| [**datacenters\_loadbalancers\_balancednics\_delete**](loadbalancerapi.md#datacenters_loadbalancers_balancednics_delete) | **DELETE** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics/{nicId} | Detach a nic from loadbalancer |
| [**datacenters\_loadbalancers\_balancednics\_find\_by\_nic\_id**](loadbalancerapi.md#datacenters_loadbalancers_balancednics_find_by_nic_id) | **GET** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics/{nicId} | Retrieve a nic attached to Load Balancer |
| [**datacenters\_loadbalancers\_balancednics\_get**](loadbalancerapi.md#datacenters_loadbalancers_balancednics_get) | **GET** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics | List Load Balancer Members |
| [**datacenters\_loadbalancers\_balancednics\_post**](loadbalancerapi.md#datacenters_loadbalancers_balancednics_post) | **POST** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics | Attach a nic to Load Balancer |
| [**datacenters\_loadbalancers\_delete**](loadbalancerapi.md#datacenters_loadbalancers_delete) | **DELETE** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Delete a Loadbalancer. |
| [**datacenters\_loadbalancers\_find\_by\_id**](loadbalancerapi.md#datacenters_loadbalancers_find_by_id) | **GET** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Retrieve a loadbalancer |
| [**datacenters\_loadbalancers\_get**](loadbalancerapi.md#datacenters_loadbalancers_get) | **GET** /datacenters/{datacenterId}/loadbalancers | List Load Balancers |
| [**datacenters\_loadbalancers\_patch**](loadbalancerapi.md#datacenters_loadbalancers_patch) | **PATCH** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Partially modify a Loadbalancer |
| [**datacenters\_loadbalancers\_post**](loadbalancerapi.md#datacenters_loadbalancers_post) | **POST** /datacenters/{datacenterId}/loadbalancers | Create a Load Balancer |
| [**datacenters\_loadbalancers\_put**](loadbalancerapi.md#datacenters_loadbalancers_put) | **PUT** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Modify a Load Balancer |

## **datacenters\_loadbalancers\_balancednics\_delete**

> object datacenters\_loadbalancers\_balancednics\_delete\(datacenter\_id, loadbalancer\_id, nic\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Detach a nic from loadbalancer

This will remove a nic from Load Balancer

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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
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

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **loadbalancer\_id** | **str** | The unique ID of the Load Balancer |  |
| **nic\_id** | **str** | The unique ID of the NIC |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

**object**

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **202** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute     _X-RateLimit-Burst - Maximum number of concurrent API requests allowed_    __ Location - Callback URL to poll async operation status   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

## **datacenters\_loadbalancers\_balancednics\_find\_by\_nic\_id**

> Nic datacenters\_loadbalancers\_balancednics\_find\_by\_nic\_id\(datacenter\_id, loadbalancer\_id, nic\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a nic attached to Load Balancer

This will retrieve the properties of an attached nic.

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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a nic attached to Load Balancer
        api_response = api_instance.datacenters_loadbalancers_balancednics_find_by_nic_id(datacenter_id, loadbalancer_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_find_by_nic_id: %s\n" % e)
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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a nic attached to Load Balancer
        api_response = api_instance.datacenters_loadbalancers_balancednics_find_by_nic_id(datacenter_id, loadbalancer_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_find_by_nic_id: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **loadbalancer\_id** | **str** | The unique ID of the Load Balancer |  |
| **nic\_id** | **str** | The unique ID of the NIC |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Nic**](../models/nic.md)

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **200** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute    \* X-RateLimit-Burst - Maximum number of concurrent API requests allowed   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

## **datacenters\_loadbalancers\_balancednics\_get**

> BalancedNics datacenters\_loadbalancers\_balancednics\_get\(datacenter\_id, loadbalancer\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number, offset=offset, limit=limit\)

List Load Balancer Members

You can retrieve a list of nics attached to a Load Balancer

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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
  offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
  limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)

    try:
        # List Load Balancer Members 
        api_response = api_instance.datacenters_loadbalancers_balancednics_get(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_get: %s\n" % e)
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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
  offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
  limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)

    try:
        # List Load Balancer Members 
        api_response = api_instance.datacenters_loadbalancers_balancednics_get(datacenter_id, loadbalancer_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_balancednics_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **loadbalancer\_id** | **str** | The unique ID of the Load Balancer |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |
| **offset** | **int** | the first element \(of the total list of elements\) to include in the response \(use together with &lt;code&gt;limit&lt;/code&gt; for pagination\) | \[optional\] \[default to 0\] |
| **limit** | **int** | the maximum number of elements to return \(use together with &lt;code&gt;offset&lt;/code&gt; for pagination\) | \[optional\] \[default to 1000\] |

### Return type

[**BalancedNics**](../models/balancednics.md)

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **200** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute    \* X-RateLimit-Burst - Maximum number of concurrent API requests allowed   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

## **datacenters\_loadbalancers\_balancednics\_post**

> Nic datacenters\_loadbalancers\_balancednics\_post\(datacenter\_id, loadbalancer\_id, nic, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Attach a nic to Load Balancer

This will attach a pre-existing nic to a Load Balancer.

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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
  nic = ionoscloud.Nic() # Nic | Nic id to be attached
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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
  nic = ionoscloud.Nic() # Nic | Nic id to be attached
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

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **loadbalancer\_id** | **str** | The unique ID of the Load Balancer |  |
| **nic** | [**Nic**](../models/nic.md) | Nic id to be attached |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Nic**](../models/nic.md)

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **202** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute     _X-RateLimit-Burst - Maximum number of concurrent API requests allowed_    __ Location - Callback URL to poll async operation status   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

## **datacenters\_loadbalancers\_delete**

> object datacenters\_loadbalancers\_delete\(datacenter\_id, loadbalancer\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Loadbalancer.

Removes the specific Loadbalancer

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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
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

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **loadbalancer\_id** | **str** | The unique ID of the Load Balancer |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

**object**

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **202** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute     _X-RateLimit-Burst - Maximum number of concurrent API requests allowed_    __ Location - Callback URL to poll async operation status   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

## **datacenters\_loadbalancers\_find\_by\_id**

> Loadbalancer datacenters\_loadbalancers\_find\_by\_id\(datacenter\_id, loadbalancer\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a loadbalancer

Retrieves the attributes of a given Loadbalancer

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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
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

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **loadbalancer\_id** | **str** | The unique ID of the Load Balancer |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Loadbalancer**](../models/loadbalancer.md)

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **200** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute    \* X-RateLimit-Burst - Maximum number of concurrent API requests allowed   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

## **datacenters\_loadbalancers\_get**

> Loadbalancers datacenters\_loadbalancers\_get\(datacenter\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number, offset=offset, limit=limit\)

List Load Balancers

Retrieve a list of Load Balancers within the datacenter

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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
  offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
  limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)

    try:
        # List Load Balancers
        api_response = api_instance.datacenters_loadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_get: %s\n" % e)
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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
  offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
  limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)

    try:
        # List Load Balancers
        api_response = api_instance.datacenters_loadbalancers_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoadBalancerApi->datacenters_loadbalancers_get: %s\n" % e)
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

[**Loadbalancers**](../models/loadbalancers.md)

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **200** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute    \* X-RateLimit-Burst - Maximum number of concurrent API requests allowed   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

## **datacenters\_loadbalancers\_patch**

> Loadbalancer datacenters\_loadbalancers\_patch\(datacenter\_id, loadbalancer\_id, loadbalancer, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Partially modify a Loadbalancer

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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
  loadbalancer = ionoscloud.LoadbalancerProperties() # LoadbalancerProperties | Modified Loadbalancer
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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
  loadbalancer = ionoscloud.LoadbalancerProperties() # LoadbalancerProperties | Modified Loadbalancer
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

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **loadbalancer\_id** | **str** | The unique ID of the Load Balancer |  |
| **loadbalancer** | [**LoadbalancerProperties**](../models/loadbalancerproperties.md) | Modified Loadbalancer |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Loadbalancer**](../models/loadbalancer.md)

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **202** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute     _X-RateLimit-Burst - Maximum number of concurrent API requests allowed_    __ Location - Callback URL to poll async operation status   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

## **datacenters\_loadbalancers\_post**

> Loadbalancer datacenters\_loadbalancers\_post\(datacenter\_id, loadbalancer, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Create a Load Balancer

Creates a Loadbalancer within the datacenter

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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer = ionoscloud.Loadbalancer() # Loadbalancer | Loadbalancer to be created
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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer = ionoscloud.Loadbalancer() # Loadbalancer | Loadbalancer to be created
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

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **loadbalancer** | [**Loadbalancer**](../models/loadbalancer.md) | Loadbalancer to be created |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Loadbalancer**](../models/loadbalancer.md)

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **202** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute     _X-RateLimit-Burst - Maximum number of concurrent API requests allowed_    __ Location - Callback URL to poll async operation status   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

## **datacenters\_loadbalancers\_put**

> Loadbalancer datacenters\_loadbalancers\_put\(datacenter\_id, loadbalancer\_id, loadbalancer, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a Load Balancer

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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
  loadbalancer = ionoscloud.Loadbalancer() # Loadbalancer | Modified Loadbalancer
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
    host = "https://api.ionos.com/cloudapi/v5"
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration = ionoscloud.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
  )
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LoadBalancerApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  loadbalancer_id = 'loadbalancer_id_example' # str | The unique ID of the Load Balancer
  loadbalancer = ionoscloud.Loadbalancer() # Loadbalancer | Modified Loadbalancer
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

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **loadbalancer\_id** | **str** | The unique ID of the Load Balancer |  |
| **loadbalancer** | [**Loadbalancer**](../models/loadbalancer.md) | Modified Loadbalancer |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Loadbalancer**](../models/loadbalancer.md)

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **202** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute     _X-RateLimit-Burst - Maximum number of concurrent API requests allowed_    __ Location - Callback URL to poll async operation status   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

