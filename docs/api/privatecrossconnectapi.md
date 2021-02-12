# PrivateCrossConnectApi

## PrivateCrossConnectApi

All URIs are relative to [https://api.ionos.com/cloudapi/v5](https://api.ionos.com/cloudapi/v5)

| Method | HTTP request | Description |
| :--- | :--- | :--- |
| [**pccs\_delete**](privatecrossconnectapi.md#pccs_delete) | **DELETE** /pccs/{pccId} | Delete a Private Cross-Connect |
| [**pccs\_find\_by\_id**](privatecrossconnectapi.md#pccs_find_by_id) | **GET** /pccs/{pccId} | Retrieve a Private Cross-Connect |
| [**pccs\_get**](privatecrossconnectapi.md#pccs_get) | **GET** /pccs | List Private Cross-Connects |
| [**pccs\_patch**](privatecrossconnectapi.md#pccs_patch) | **PATCH** /pccs/{pccId} | Partially modify a private cross-connect |
| [**pccs\_post**](privatecrossconnectapi.md#pccs_post) | **POST** /pccs | Create a Private Cross-Connect |

## **pccs\_delete**

> object pccs\_delete\(pcc\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Private Cross-Connect

Delete a private cross-connect if no datacenters are joined to the given PCC

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
    api_instance = ionoscloud.PrivateCrossConnectApi(api_client)
    pcc_id = 'pcc_id_example' # str | The unique ID of the private cross-connect
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Private Cross-Connect
        api_response = api_instance.pccs_delete(pcc_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateCrossConnectApi->pccs_delete: %s\n" % e)
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
    api_instance = ionoscloud.PrivateCrossConnectApi(api_client)
    pcc_id = 'pcc_id_example' # str | The unique ID of the private cross-connect
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Private Cross-Connect
        api_response = api_instance.pccs_delete(pcc_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateCrossConnectApi->pccs_delete: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pcc\_id** | **str** | The unique ID of the private cross-connect |  |
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

## **pccs\_find\_by\_id**

> PrivateCrossConnect pccs\_find\_by\_id\(pcc\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Private Cross-Connect

You can retrieve a private cross-connect by using the resource's ID. This value can be found in the response body when a private cross-connect is created or when you GET a list of private cross-connects.

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
    api_instance = ionoscloud.PrivateCrossConnectApi(api_client)
    pcc_id = 'pcc_id_example' # str | The unique ID of the private cross-connect
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Private Cross-Connect
        api_response = api_instance.pccs_find_by_id(pcc_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateCrossConnectApi->pccs_find_by_id: %s\n" % e)
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
    api_instance = ionoscloud.PrivateCrossConnectApi(api_client)
    pcc_id = 'pcc_id_example' # str | The unique ID of the private cross-connect
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Private Cross-Connect
        api_response = api_instance.pccs_find_by_id(pcc_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateCrossConnectApi->pccs_find_by_id: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pcc\_id** | **str** | The unique ID of the private cross-connect |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**PrivateCrossConnect**](../models/privatecrossconnect.md)

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

## **pccs\_get**

> PrivateCrossConnects pccs\_get\(pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List Private Cross-Connects

You can retrieve a complete list of private cross-connects provisioned under your account

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
    api_instance = ionoscloud.PrivateCrossConnectApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Private Cross-Connects 
        api_response = api_instance.pccs_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateCrossConnectApi->pccs_get: %s\n" % e)
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
    api_instance = ionoscloud.PrivateCrossConnectApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Private Cross-Connects 
        api_response = api_instance.pccs_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateCrossConnectApi->pccs_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**PrivateCrossConnects**](../models/privatecrossconnects.md)

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

## **pccs\_patch**

> PrivateCrossConnect pccs\_patch\(pcc\_id, pcc, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Partially modify a private cross-connect

You can use update private cross-connect to re-name or update its description

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
    api_instance = ionoscloud.PrivateCrossConnectApi(api_client)
    pcc_id = 'pcc_id_example' # str | The unique ID of the private cross-connect
  pcc = ionoscloud.PrivateCrossConnectProperties() # PrivateCrossConnectProperties | Modified properties of private cross-connect
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a private cross-connect
        api_response = api_instance.pccs_patch(pcc_id, pcc, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateCrossConnectApi->pccs_patch: %s\n" % e)
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
    api_instance = ionoscloud.PrivateCrossConnectApi(api_client)
    pcc_id = 'pcc_id_example' # str | The unique ID of the private cross-connect
  pcc = ionoscloud.PrivateCrossConnectProperties() # PrivateCrossConnectProperties | Modified properties of private cross-connect
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a private cross-connect
        api_response = api_instance.pccs_patch(pcc_id, pcc, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateCrossConnectApi->pccs_patch: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pcc\_id** | **str** | The unique ID of the private cross-connect |  |
| **pcc** | [**PrivateCrossConnectProperties**](../models/privatecrossconnectproperties.md) | Modified properties of private cross-connect |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**PrivateCrossConnect**](../models/privatecrossconnect.md)

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

## **pccs\_post**

> PrivateCrossConnect pccs\_post\(pcc, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Create a Private Cross-Connect

You can use this POST method to create a private cross-connect

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
    api_instance = ionoscloud.PrivateCrossConnectApi(api_client)
    pcc = ionoscloud.PrivateCrossConnect() # PrivateCrossConnect | Private Cross-Connect to be created
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Private Cross-Connect
        api_response = api_instance.pccs_post(pcc, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateCrossConnectApi->pccs_post: %s\n" % e)
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
    api_instance = ionoscloud.PrivateCrossConnectApi(api_client)
    pcc = ionoscloud.PrivateCrossConnect() # PrivateCrossConnect | Private Cross-Connect to be created
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Private Cross-Connect
        api_response = api_instance.pccs_post(pcc, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateCrossConnectApi->pccs_post: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pcc** | [**PrivateCrossConnect**](../models/privatecrossconnect.md) | Private Cross-Connect to be created |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**PrivateCrossConnect**](../models/privatecrossconnect.md)

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

