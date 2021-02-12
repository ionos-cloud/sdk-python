# BackupUnitApi

## BackupUnitApi

All URIs are relative to [https://api.ionos.com/cloudapi/v5](https://api.ionos.com/cloudapi/v5)

| Method | HTTP request | Description |
| :--- | :--- | :--- |
| [**backupunits\_delete**](backupunitapi.md#backupunits_delete) | **DELETE** /backupunits/{backupunitId} | Delete a Backup Unit |
| [**backupunits\_find\_by\_id**](backupunitapi.md#backupunits_find_by_id) | **GET** /backupunits/{backupunitId} | Returns the specified backup Unit |
| [**backupunits\_get**](backupunitapi.md#backupunits_get) | **GET** /backupunits | List Backup Units |
| [**backupunits\_patch**](backupunitapi.md#backupunits_patch) | **PATCH** /backupunits/{backupunitId} | Partially modify a Backup Unit |
| [**backupunits\_post**](backupunitapi.md#backupunits_post) | **POST** /backupunits | Create a Backup Unit |
| [**backupunits\_put**](backupunitapi.md#backupunits_put) | **PUT** /backupunits/{backupunitId} | Modify a Backup Unit |
| [**backupunits\_ssourl\_get**](backupunitapi.md#backupunits_ssourl_get) | **GET** /backupunits/{backupunitId}/ssourl | Returns a single signon URL for the specified backup Unit. |

## **backupunits\_delete**

> object backupunits\_delete\(backupunit\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Backup Unit

NOTE: Running through the deletion process will delete: - the backup plans inside the Backup Unit. - all backups associated with the Backup Unit. - the backup user and finally also the unit

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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup Unit
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Backup Unit
        api_response = api_instance.backupunits_delete(backupunit_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_delete: %s\n" % e)
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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup Unit
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Backup Unit
        api_response = api_instance.backupunits_delete(backupunit_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_delete: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **backupunit\_id** | **str** | The unique ID of the backup Unit |  |
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

## **backupunits\_find\_by\_id**

> BackupUnit backupunits\_find\_by\_id\(backupunit\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Returns the specified backup Unit

You can retrieve the details of an specific backup unit.

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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Returns the specified backup Unit
        api_response = api_instance.backupunits_find_by_id(backupunit_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_find_by_id: %s\n" % e)
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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Returns the specified backup Unit
        api_response = api_instance.backupunits_find_by_id(backupunit_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_find_by_id: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **backupunit\_id** | **str** | The unique ID of the backup unit |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**BackupUnit**](../models/backupunit.md)

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

## **backupunits\_get**

> BackupUnits backupunits\_get\(pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List Backup Units

You can retrieve a complete list of backup Units that you have access to.

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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Backup Units 
        api_response = api_instance.backupunits_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_get: %s\n" % e)
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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Backup Units 
        api_response = api_instance.backupunits_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**BackupUnits**](../models/backupunits.md)

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

## **backupunits\_patch**

> BackupUnit backupunits\_patch\(backupunit\_id, backup\_unit\_properties, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Partially modify a Backup Unit

You can use update a backup Unit properties

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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit
  backup_unit_properties = ionoscloud.BackupUnitProperties() # BackupUnitProperties | Modified backup Unit properties
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Backup Unit
        api_response = api_instance.backupunits_patch(backupunit_id, backup_unit_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_patch: %s\n" % e)
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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit
  backup_unit_properties = ionoscloud.BackupUnitProperties() # BackupUnitProperties | Modified backup Unit properties
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Partially modify a Backup Unit
        api_response = api_instance.backupunits_patch(backupunit_id, backup_unit_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_patch: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **backupunit\_id** | **str** | The unique ID of the backup unit |  |
| **backup\_unit\_properties** | [**BackupUnitProperties**](../models/backupunitproperties.md) | Modified backup Unit properties |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**BackupUnit**](../models/backupunit.md)

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

## **backupunits\_post**

> BackupUnit backupunits\_post\(backup\_unit, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Create a Backup Unit

Create a Backup Unit. A Backup Unit is considered a resource like a virtual datacenter, IP Block, snapshot, etc. It shall be shareable via groups inside our User Management Feature

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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backup_unit = ionoscloud.BackupUnit() # BackupUnit | Payload containing data to create a new Backup Unit
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Backup Unit
        api_response = api_instance.backupunits_post(backup_unit, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_post: %s\n" % e)
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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backup_unit = ionoscloud.BackupUnit() # BackupUnit | Payload containing data to create a new Backup Unit
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Backup Unit
        api_response = api_instance.backupunits_post(backup_unit, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_post: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **backup\_unit** | [**BackupUnit**](../models/backupunit.md) | Payload containing data to create a new Backup Unit |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**BackupUnit**](../models/backupunit.md)

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

## **backupunits\_put**

> BackupUnit backupunits\_put\(backupunit\_id, backup\_unit, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a Backup Unit

You can use update a backup Unit properties

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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit
  backup_unit = ionoscloud.BackupUnit() # BackupUnit | Modified backup Unit
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Backup Unit
        api_response = api_instance.backupunits_put(backupunit_id, backup_unit, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_put: %s\n" % e)
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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit
  backup_unit = ionoscloud.BackupUnit() # BackupUnit | Modified backup Unit
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a Backup Unit
        api_response = api_instance.backupunits_put(backupunit_id, backup_unit, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_put: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **backupunit\_id** | **str** | The unique ID of the backup unit |  |
| **backup\_unit** | [**BackupUnit**](../models/backupunit.md) | Modified backup Unit |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**BackupUnit**](../models/backupunit.md)

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

## **backupunits\_ssourl\_get**

> BackupUnitSSO backupunits\_ssourl\_get\(backupunit\_id, pretty=pretty, x\_contract\_number=x\_contract\_number\)

Returns a single signon URL for the specified backup Unit.

Returns a single signon URL for the specified backup Unit.

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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique UUID of the backup unit
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Returns a single signon URL for the specified backup Unit.
        api_response = api_instance.backupunits_ssourl_get(backupunit_id, pretty=pretty, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_ssourl_get: %s\n" % e)
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
    api_instance = ionoscloud.BackupUnitApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique UUID of the backup unit
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Returns a single signon URL for the specified backup Unit.
        api_response = api_instance.backupunits_ssourl_get(backupunit_id, pretty=pretty, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupUnitApi->backupunits_ssourl_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **backupunit\_id** | **str** | The unique UUID of the backup unit |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**BackupUnitSSO**](../models/backupunitsso.md)

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

