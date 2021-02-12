# NicApi

## NicApi

All URIs are relative to [https://api.ionos.com/cloudapi/v5](https://api.ionos.com/cloudapi/v5)

| Method | HTTP request | Description |
| :--- | :--- | :--- |
| [**datacenters\_servers\_nics\_delete**](nicapi.md#datacenters_servers_nics_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Delete a Nic |
| [**datacenters\_servers\_nics\_find\_by\_id**](nicapi.md#datacenters_servers_nics_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Retrieve a Nic |
| [**datacenters\_servers\_nics\_firewallrules\_delete**](nicapi.md#datacenters_servers_nics_firewallrules_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Delete a Firewall Rule |
| [**datacenters\_servers\_nics\_firewallrules\_find\_by\_id**](nicapi.md#datacenters_servers_nics_firewallrules_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Retrieve a Firewall Rule |
| [**datacenters\_servers\_nics\_firewallrules\_get**](nicapi.md#datacenters_servers_nics_firewallrules_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules | List Firewall Rules |
| [**datacenters\_servers\_nics\_firewallrules\_patch**](nicapi.md#datacenters_servers_nics_firewallrules_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Partially modify a Firewall Rule |
| [**datacenters\_servers\_nics\_firewallrules\_post**](nicapi.md#datacenters_servers_nics_firewallrules_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules | Create a Firewall Rule |
| [**datacenters\_servers\_nics\_firewallrules\_put**](nicapi.md#datacenters_servers_nics_firewallrules_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Modify a Firewall Rule |
| [**datacenters\_servers\_nics\_get**](nicapi.md#datacenters_servers_nics_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics | List Nics |
| [**datacenters\_servers\_nics\_patch**](nicapi.md#datacenters_servers_nics_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Partially modify a Nic |
| [**datacenters\_servers\_nics\_post**](nicapi.md#datacenters_servers_nics_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/nics | Create a Nic |
| [**datacenters\_servers\_nics\_put**](nicapi.md#datacenters_servers_nics_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Modify a Nic |

## **datacenters\_servers\_nics\_delete**

> object datacenters\_servers\_nics\_delete\(datacenter\_id, server\_id, nic\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Nic

Deletes the specified NIC.

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Nic
        api_response = api_instance.datacenters_servers_nics_delete(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_delete: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Nic
        api_response = api_instance.datacenters_servers_nics_delete(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_delete: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
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

## **datacenters\_servers\_nics\_find\_by\_id**

> Nic datacenters\_servers\_nics\_find\_by\_id\(datacenter\_id, server\_id, nic\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Nic

Retrieves the attributes of a given NIC

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Nic
        api_response = api_instance.datacenters_servers_nics_find_by_id(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_find_by_id: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Nic
        api_response = api_instance.datacenters_servers_nics_find_by_id(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_find_by_id: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
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

## **datacenters\_servers\_nics\_firewallrules\_delete**

> object datacenters\_servers\_nics\_firewallrules\_delete\(datacenter\_id, server\_id, nic\_id, firewallrule\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Firewall Rule

Removes the specific Firewall Rule

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_delete(datacenter_id, server_id, nic_id, firewallrule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_delete: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_delete(datacenter_id, server_id, nic_id, firewallrule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_delete: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **nic\_id** | **str** | The unique ID of the NIC |  |
| **firewallrule\_id** | **str** | The unique ID of the Firewall Rule |  |
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

## **datacenters\_servers\_nics\_firewallrules\_find\_by\_id**

> FirewallRule datacenters\_servers\_nics\_firewallrules\_find\_by\_id\(datacenter\_id, server\_id, nic\_id, firewallrule\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Firewall Rule

Retrieves the attributes of a given Firewall Rule.

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_find_by_id(datacenter_id, server_id, nic_id, firewallrule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_find_by_id: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_find_by_id(datacenter_id, server_id, nic_id, firewallrule_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_find_by_id: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **nic\_id** | **str** | The unique ID of the NIC |  |
| **firewallrule\_id** | **str** | The unique ID of the Firewall Rule |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**FirewallRule**](../models/firewallrule.md)

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

## **datacenters\_servers\_nics\_firewallrules\_get**

> FirewallRules datacenters\_servers\_nics\_firewallrules\_get\(datacenter\_id, server\_id, nic\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number, offset=offset, limit=limit\)

List Firewall Rules

Retrieves a list of firewall rules associated with a particular NIC

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
  offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
  limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)

    try:
        # List Firewall Rules 
        api_response = api_instance.datacenters_servers_nics_firewallrules_get(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_get: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
  offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
  limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)

    try:
        # List Firewall Rules 
        api_response = api_instance.datacenters_servers_nics_firewallrules_get(datacenter_id, server_id, nic_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **nic\_id** | **str** | The unique ID of the NIC |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |
| **offset** | **int** | the first element \(of the total list of elements\) to include in the response \(use together with &lt;code&gt;limit&lt;/code&gt; for pagination\) | \[optional\] \[default to 0\] |
| **limit** | **int** | the maximum number of elements to return \(use together with &lt;code&gt;offset&lt;/code&gt; for pagination\) | \[optional\] \[default to 1000\] |

### Return type

[**FirewallRules**](../models/firewallrules.md)

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

## **datacenters\_servers\_nics\_firewallrules\_patch**

> FirewallRule datacenters\_servers\_nics\_firewallrules\_patch\(datacenter\_id, server\_id, nic\_id, firewallrule\_id, firewallrule, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Partially modify a Firewall Rule

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
  firewallrule = ionoscloud.FirewallruleProperties() # FirewallruleProperties | Modified Firewall Rule
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_patch(datacenter_id, server_id, nic_id, firewallrule_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_patch: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
  firewallrule = ionoscloud.FirewallruleProperties() # FirewallruleProperties | Modified Firewall Rule
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_patch(datacenter_id, server_id, nic_id, firewallrule_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_patch: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **nic\_id** | **str** | The unique ID of the NIC |  |
| **firewallrule\_id** | **str** | The unique ID of the Firewall Rule |  |
| **firewallrule** | [**FirewallruleProperties**](../models/firewallruleproperties.md) | Modified Firewall Rule |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**FirewallRule**](../models/firewallrule.md)

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

## **datacenters\_servers\_nics\_firewallrules\_post**

> FirewallRule datacenters\_servers\_nics\_firewallrules\_post\(datacenter\_id, server\_id, nic\_id, firewallrule, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Create a Firewall Rule

This will add a Firewall Rule to the NIC

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  firewallrule = ionoscloud.FirewallRule() # FirewallRule | Firewall Rule to be created
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_post(datacenter_id, server_id, nic_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_post: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  firewallrule = ionoscloud.FirewallRule() # FirewallRule | Firewall Rule to be created
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_post(datacenter_id, server_id, nic_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_post: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the server |  |
| **nic\_id** | **str** | The unique ID of the NIC |  |
| **firewallrule** | [**FirewallRule**](../models/firewallrule.md) | Firewall Rule to be created |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**FirewallRule**](../models/firewallrule.md)

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

## **datacenters\_servers\_nics\_firewallrules\_put**

> FirewallRule datacenters\_servers\_nics\_firewallrules\_put\(datacenter\_id, server\_id, nic\_id, firewallrule\_id, firewallrule, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a Firewall Rule

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
  firewallrule = ionoscloud.FirewallRule() # FirewallRule | Modified Firewall Rule
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_put(datacenter_id, server_id, nic_id, firewallrule_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_put: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  firewallrule_id = 'firewallrule_id_example' # str | The unique ID of the Firewall Rule
  firewallrule = ionoscloud.FirewallRule() # FirewallRule | Modified Firewall Rule
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Firewall Rule
        api_response = api_instance.datacenters_servers_nics_firewallrules_put(datacenter_id, server_id, nic_id, firewallrule_id, firewallrule, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_firewallrules_put: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **nic\_id** | **str** | The unique ID of the NIC |  |
| **firewallrule\_id** | **str** | The unique ID of the Firewall Rule |  |
| **firewallrule** | [**FirewallRule**](../models/firewallrule.md) | Modified Firewall Rule |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**FirewallRule**](../models/firewallrule.md)

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

## **datacenters\_servers\_nics\_get**

> Nics datacenters\_servers\_nics\_get\(datacenter\_id, server\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number, offset=offset, limit=limit\)

List Nics

Retrieves a list of NICs.

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
  offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
  limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)

    try:
        # List Nics 
        api_response = api_instance.datacenters_servers_nics_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_get: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
  offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
  limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)

    try:
        # List Nics 
        api_response = api_instance.datacenters_servers_nics_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |
| **offset** | **int** | the first element \(of the total list of elements\) to include in the response \(use together with &lt;code&gt;limit&lt;/code&gt; for pagination\) | \[optional\] \[default to 0\] |
| **limit** | **int** | the maximum number of elements to return \(use together with &lt;code&gt;offset&lt;/code&gt; for pagination\) | \[optional\] \[default to 1000\] |

### Return type

[**Nics**](../models/nics.md)

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

## **datacenters\_servers\_nics\_patch**

> Nic datacenters\_servers\_nics\_patch\(datacenter\_id, server\_id, nic\_id, nic, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Partially modify a Nic

You can use update attributes of a Nic

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  nic = ionoscloud.NicProperties() # NicProperties | Modified properties of Nic
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Nic
        api_response = api_instance.datacenters_servers_nics_patch(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_patch: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  nic = ionoscloud.NicProperties() # NicProperties | Modified properties of Nic
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Nic
        api_response = api_instance.datacenters_servers_nics_patch(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_patch: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **nic\_id** | **str** | The unique ID of the NIC |  |
| **nic** | [**NicProperties**](../models/nicproperties.md) | Modified properties of Nic |  |
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

## **datacenters\_servers\_nics\_post**

> Nic datacenters\_servers\_nics\_post\(datacenter\_id, server\_id, nic, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Create a Nic

Adds a NIC to the target server. Combine count of Nics and volumes attached to the server should not exceed size 24.

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic = ionoscloud.Nic() # Nic | Nic to be created
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Nic
        api_response = api_instance.datacenters_servers_nics_post(datacenter_id, server_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_post: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic = ionoscloud.Nic() # Nic | Nic to be created
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Nic
        api_response = api_instance.datacenters_servers_nics_post(datacenter_id, server_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_post: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **nic** | [**Nic**](../models/nic.md) | Nic to be created |  |
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

## **datacenters\_servers\_nics\_put**

> Nic datacenters\_servers\_nics\_put\(datacenter\_id, server\_id, nic\_id, nic, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a Nic

You can use update attributes of a Nic

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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  nic = ionoscloud.Nic() # Nic | Modified Nic
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Nic
        api_response = api_instance.datacenters_servers_nics_put(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_put: %s\n" % e)
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
    api_instance = ionoscloud.NicApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the datacenter
  server_id = 'server_id_example' # str | The unique ID of the Server
  nic_id = 'nic_id_example' # str | The unique ID of the NIC
  nic = ionoscloud.Nic() # Nic | Modified Nic
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Nic
        api_response = api_instance.datacenters_servers_nics_put(datacenter_id, server_id, nic_id, nic, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NicApi->datacenters_servers_nics_put: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **nic\_id** | **str** | The unique ID of the NIC |  |
| **nic** | [**Nic**](../models/nic.md) | Modified Nic |  |
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

