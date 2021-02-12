# UserManagementApi

## UserManagementApi

All URIs are relative to [https://api.ionos.com/cloudapi/v5](https://api.ionos.com/cloudapi/v5)

| Method | HTTP request | Description |
| :--- | :--- | :--- |
| [**um\_groups\_delete**](usermanagementapi.md#um_groups_delete) | **DELETE** /um/groups/{groupId} | Delete a Group |
| [**um\_groups\_find\_by\_id**](usermanagementapi.md#um_groups_find_by_id) | **GET** /um/groups/{groupId} | Retrieve a Group |
| [**um\_groups\_get**](usermanagementapi.md#um_groups_get) | **GET** /um/groups | List All Groups. |
| [**um\_groups\_post**](usermanagementapi.md#um_groups_post) | **POST** /um/groups | Create a Group |
| [**um\_groups\_put**](usermanagementapi.md#um_groups_put) | **PUT** /um/groups/{groupId} | Modify a group |
| [**um\_groups\_resources\_get**](usermanagementapi.md#um_groups_resources_get) | **GET** /um/groups/{groupId}/resources | Retrieve resources assigned to a group |
| [**um\_groups\_shares\_delete**](usermanagementapi.md#um_groups_shares_delete) | **DELETE** /um/groups/{groupId}/shares/{resourceId} | Remove a resource from a group |
| [**um\_groups\_shares\_find\_by\_resource\_id**](usermanagementapi.md#um_groups_shares_find_by_resource_id) | **GET** /um/groups/{groupId}/shares/{resourceId} | Retrieve a group share |
| [**um\_groups\_shares\_get**](usermanagementapi.md#um_groups_shares_get) | **GET** /um/groups/{groupId}/shares | List Group Shares |
| [**um\_groups\_shares\_post**](usermanagementapi.md#um_groups_shares_post) | **POST** /um/groups/{groupId}/shares/{resourceId} | Add a resource to a group |
| [**um\_groups\_shares\_put**](usermanagementapi.md#um_groups_shares_put) | **PUT** /um/groups/{groupId}/shares/{resourceId} | Modify resource permissions of a group |
| [**um\_groups\_users\_delete**](usermanagementapi.md#um_groups_users_delete) | **DELETE** /um/groups/{groupId}/users/{userId} | Remove a user from a group |
| [**um\_groups\_users\_get**](usermanagementapi.md#um_groups_users_get) | **GET** /um/groups/{groupId}/users | List Group Members |
| [**um\_groups\_users\_post**](usermanagementapi.md#um_groups_users_post) | **POST** /um/groups/{groupId}/users | Add a user to a group |
| [**um\_resources\_find\_by\_type**](usermanagementapi.md#um_resources_find_by_type) | **GET** /um/resources/{resourceType} | Retrieve a list of Resources by type. |
| [**um\_resources\_find\_by\_type\_and\_id**](usermanagementapi.md#um_resources_find_by_type_and_id) | **GET** /um/resources/{resourceType}/{resourceId} | Retrieve a Resource by type. |
| [**um\_resources\_get**](usermanagementapi.md#um_resources_get) | **GET** /um/resources | List All Resources. |
| [**um\_users\_delete**](usermanagementapi.md#um_users_delete) | **DELETE** /um/users/{userId} | Delete a User |
| [**um\_users\_find\_by\_id**](usermanagementapi.md#um_users_find_by_id) | **GET** /um/users/{userId} | Retrieve a User |
| [**um\_users\_get**](usermanagementapi.md#um_users_get) | **GET** /um/users | List all Users |
| [**um\_users\_groups\_get**](usermanagementapi.md#um_users_groups_get) | **GET** /um/users/{userId}/groups | Retrieve a User's group resources |
| [**um\_users\_owns\_get**](usermanagementapi.md#um_users_owns_get) | **GET** /um/users/{userId}/owns | Retrieve a User's own resources |
| [**um\_users\_post**](usermanagementapi.md#um_users_post) | **POST** /um/users | Create a user |
| [**um\_users\_put**](usermanagementapi.md#um_users_put) | **PUT** /um/users/{userId} | Modify a user |
| [**um\_users\_s3keys\_delete**](usermanagementapi.md#um_users_s3keys_delete) | **DELETE** /um/users/{userId}/s3keys/{keyId} | Delete a S3 key |
| [**um\_users\_s3keys\_find\_by\_key\_id**](usermanagementapi.md#um_users_s3keys_find_by_key_id) | **GET** /um/users/{userId}/s3keys/{keyId} | Retrieve given S3 key belonging to the given User |
| [**um\_users\_s3keys\_get**](usermanagementapi.md#um_users_s3keys_get) | **GET** /um/users/{userId}/s3keys | Retrieve a User's S3 keys |
| [**um\_users\_s3keys\_post**](usermanagementapi.md#um_users_s3keys_post) | **POST** /um/users/{userId}/s3keys | Create a S3 key for the given user |
| [**um\_users\_s3keys\_put**](usermanagementapi.md#um_users_s3keys_put) | **PUT** /um/users/{userId}/s3keys/{keyId} | Modify a S3 key having the given key id |
| [**um\_users\_s3ssourl\_get**](usermanagementapi.md#um_users_s3ssourl_get) | **GET** /um/users/{userId}/s3ssourl | Retrieve S3 object storage single signon URL for the given user |

## **um\_groups\_delete**

> object um\_groups\_delete\(group\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Group

Delete a group

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Group
        api_response = api_instance.um_groups_delete(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_delete: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a Group
        api_response = api_instance.um_groups_delete(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_delete: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** | The unique ID of the group |  |
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

## **um\_groups\_find\_by\_id**

> Group um\_groups\_find\_by\_id\(group\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Group

You can retrieve a group by using the group ID. This value can be found in the response body when a group is created or when you GET a list of groups.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Group
        api_response = api_instance.um_groups_find_by_id(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_find_by_id: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Group
        api_response = api_instance.um_groups_find_by_id(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_find_by_id: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** | The unique ID of the group |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Group**](../models/group.md)

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

## **um\_groups\_get**

> Groups um\_groups\_get\(pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List All Groups.

You can retrieve a complete list of all groups that you have access to

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List All Groups.
        api_response = api_instance.um_groups_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_get: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List All Groups.
        api_response = api_instance.um_groups_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Groups**](../models/groups.md)

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

## **um\_groups\_post**

> Group um\_groups\_post\(group, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Create a Group

You can use this POST method to create a group

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group = ionoscloud.Group() # Group | Group to be created
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Group
        api_response = api_instance.um_groups_post(group, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_post: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group = ionoscloud.Group() # Group | Group to be created
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a Group
        api_response = api_instance.um_groups_post(group, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_post: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group** | [**Group**](../models/group.md) | Group to be created |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Group**](../models/group.md)

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

## **um\_groups\_put**

> Group um\_groups\_put\(group\_id, group, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a group

You can use this method to update properties of the group.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group
  group = ionoscloud.Group() # Group | Modified properties of the Group
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a group
        api_response = api_instance.um_groups_put(group_id, group, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_put: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group
  group = ionoscloud.Group() # Group | Modified properties of the Group
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a group
        api_response = api_instance.um_groups_put(group_id, group, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_put: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** | The unique ID of the group |  |
| **group** | [**Group**](../models/group.md) | Modified properties of the Group |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Group**](../models/group.md)

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

## **um\_groups\_resources\_get**

> ResourceGroups um\_groups\_resources\_get\(group\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve resources assigned to a group

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve resources assigned to a group
        api_response = api_instance.um_groups_resources_get(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_resources_get: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve resources assigned to a group
        api_response = api_instance.um_groups_resources_get(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_resources_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** | The unique ID of the group |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**ResourceGroups**](../models/resourcegroups.md)

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

## **um\_groups\_shares\_delete**

> object um\_groups\_shares\_delete\(group\_id, resource\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Remove a resource from a group

This will remove a resource from a group

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  resource_id = 'resource_id_example' # str | 
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Remove a resource from a group
        api_response = api_instance.um_groups_shares_delete(group_id, resource_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_shares_delete: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  resource_id = 'resource_id_example' # str | 
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Remove a resource from a group
        api_response = api_instance.um_groups_shares_delete(group_id, resource_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_shares_delete: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** |  |  |
| **resource\_id** | **str** |  |  |
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

## **um\_groups\_shares\_find\_by\_resource\_id**

> GroupShare um\_groups\_shares\_find\_by\_resource\_id\(group\_id, resource\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a group share

This will retrieve the properties of a group share.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  resource_id = 'resource_id_example' # str | 
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a group share
        api_response = api_instance.um_groups_shares_find_by_resource_id(group_id, resource_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_shares_find_by_resource_id: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  resource_id = 'resource_id_example' # str | 
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a group share
        api_response = api_instance.um_groups_shares_find_by_resource_id(group_id, resource_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_shares_find_by_resource_id: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** |  |  |
| **resource\_id** | **str** |  |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**GroupShare**](../models/groupshare.md)

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

## **um\_groups\_shares\_get**

> GroupShares um\_groups\_shares\_get\(group\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List Group Shares

You can retrieve a list of all resources along with their permissions of the group

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Group Shares 
        api_response = api_instance.um_groups_shares_get(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_shares_get: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Group Shares 
        api_response = api_instance.um_groups_shares_get(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_shares_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** |  |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**GroupShares**](../models/groupshares.md)

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

## **um\_groups\_shares\_post**

> GroupShare um\_groups\_shares\_post\(group\_id, resource\_id, resource, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Add a resource to a group

This will add a resource to the group.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  resource_id = 'resource_id_example' # str | 
  resource = ionoscloud.GroupShare() # GroupShare | Resource to be added
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Add a resource to a group
        api_response = api_instance.um_groups_shares_post(group_id, resource_id, resource, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_shares_post: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  resource_id = 'resource_id_example' # str | 
  resource = ionoscloud.GroupShare() # GroupShare | Resource to be added
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Add a resource to a group
        api_response = api_instance.um_groups_shares_post(group_id, resource_id, resource, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_shares_post: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** |  |  |
| **resource\_id** | **str** |  |  |
| **resource** | [**GroupShare**](../models/groupshare.md) | Resource to be added |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**GroupShare**](../models/groupshare.md)

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

## **um\_groups\_shares\_put**

> GroupShare um\_groups\_shares\_put\(group\_id, resource\_id, resource, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify resource permissions of a group

You can use update resource permissions of a group. If empty body will be provided, no updates will happen, instead you will be returned the current permissions of resource in a group. In this case response code will be 200

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  resource_id = 'resource_id_example' # str | 
  resource = ionoscloud.GroupShare() # GroupShare | Modified Resource
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify resource permissions of a group
        api_response = api_instance.um_groups_shares_put(group_id, resource_id, resource, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_shares_put: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  resource_id = 'resource_id_example' # str | 
  resource = ionoscloud.GroupShare() # GroupShare | Modified Resource
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify resource permissions of a group
        api_response = api_instance.um_groups_shares_put(group_id, resource_id, resource, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_shares_put: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** |  |  |
| **resource\_id** | **str** |  |  |
| **resource** | [**GroupShare**](../models/groupshare.md) | Modified Resource |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**GroupShare**](../models/groupshare.md)

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

## **um\_groups\_users\_delete**

> object um\_groups\_users\_delete\(group\_id, user\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Remove a user from a group

This will remove a user from a group

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  user_id = 'user_id_example' # str | 
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Remove a user from a group
        api_response = api_instance.um_groups_users_delete(group_id, user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_users_delete: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  user_id = 'user_id_example' # str | 
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Remove a user from a group
        api_response = api_instance.um_groups_users_delete(group_id, user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_users_delete: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** |  |  |
| **user\_id** | **str** |  |  |
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

## **um\_groups\_users\_get**

> GroupMembers um\_groups\_users\_get\(group\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List Group Members

You can retrieve a list of users who are members of the group

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Group Members 
        api_response = api_instance.um_groups_users_get(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_users_get: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List Group Members 
        api_response = api_instance.um_groups_users_get(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_users_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** |  |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**GroupMembers**](../models/groupmembers.md)

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

## **um\_groups\_users\_post**

> User um\_groups\_users\_post\(group\_id, user, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Add a user to a group

This will attach a pre-existing user to a group.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  user = ionoscloud.User() # User | User to be added
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Add a user to a group
        api_response = api_instance.um_groups_users_post(group_id, user, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_users_post: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | 
  user = ionoscloud.User() # User | User to be added
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Add a user to a group
        api_response = api_instance.um_groups_users_post(group_id, user, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_groups_users_post: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **group\_id** | **str** |  |  |
| **user** | [**User**](../models/user.md) | User to be added |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**User**](../models/user.md)

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

## **um\_resources\_find\_by\_type**

> Resources um\_resources\_find\_by\_type\(resource\_type, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a list of Resources by type.

You can retrieve a list of resources by using the type. Allowed values are { datacenter, snapshot, image, ipblock, pcc, backupunit, k8s }. This value of resource type also be found in the response body when you GET a list of all resources.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    resource_type = 'resource_type_example' # str | The resource Type
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a list of Resources by type.
        api_response = api_instance.um_resources_find_by_type(resource_type, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_resources_find_by_type: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    resource_type = 'resource_type_example' # str | The resource Type
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a list of Resources by type.
        api_response = api_instance.um_resources_find_by_type(resource_type, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_resources_find_by_type: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **resource\_type** | **str** | The resource Type |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Resources**](../models/resources.md)

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

## **um\_resources\_find\_by\_type\_and\_id**

> Resource um\_resources\_find\_by\_type\_and\_id\(resource\_type, resource\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Resource by type.

You can retrieve a resource by using the type and its uuid. Allowed values for types are { datacenter, snapshot, image, ipblock, pcc, backupunit, k8s }. The value of resource type can also be found in the response body when you GET a list of all resources.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    resource_type = 'resource_type_example' # str | The resource Type
  resource_id = 'resource_id_example' # str | The resource Uuid
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Resource by type.
        api_response = api_instance.um_resources_find_by_type_and_id(resource_type, resource_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_resources_find_by_type_and_id: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    resource_type = 'resource_type_example' # str | The resource Type
  resource_id = 'resource_id_example' # str | The resource Uuid
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a Resource by type.
        api_response = api_instance.um_resources_find_by_type_and_id(resource_type, resource_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_resources_find_by_type_and_id: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **resource\_type** | **str** | The resource Type |  |
| **resource\_id** | **str** | The resource Uuid |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Resource**](../models/resource.md)

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

## **um\_resources\_get**

> Resources um\_resources\_get\(pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List All Resources.

You can retrieve a complete list of all resources that you have access to

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List All Resources.
        api_response = api_instance.um_resources_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_resources_get: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List All Resources.
        api_response = api_instance.um_resources_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_resources_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Resources**](../models/resources.md)

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

## **um\_users\_delete**

> object um\_users\_delete\(user\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a User

Delete a user

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a User
        api_response = api_instance.um_users_delete(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_delete: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a User
        api_response = api_instance.um_users_delete(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_delete: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** | The unique ID of the user |  |
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

## **um\_users\_find\_by\_id**

> User um\_users\_find\_by\_id\(user\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a User

You can retrieve user details by using the users ID. This value can be found in the response body when a user is created or when you GET a list of users.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a User
        api_response = api_instance.um_users_find_by_id(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_find_by_id: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a User
        api_response = api_instance.um_users_find_by_id(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_find_by_id: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** | The unique ID of the user |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**User**](../models/user.md)

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

## **um\_users\_get**

> Users um\_users\_get\(pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List all Users

You can retrieve a complete list of users under your account

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List all Users 
        api_response = api_instance.um_users_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_get: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # List all Users 
        api_response = api_instance.um_users_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Users**](../models/users.md)

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

## **um\_users\_groups\_get**

> ResourceGroups um\_users\_groups\_get\(user\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a User's group resources

You can retrieve group resources of user by using the users ID. This value can be found in the response body when a user is created or when you GET a list of users.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a User's group resources
        api_response = api_instance.um_users_groups_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_groups_get: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a User's group resources
        api_response = api_instance.um_users_groups_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_groups_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** | The unique ID of the user |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**ResourceGroups**](../models/resourcegroups.md)

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

## **um\_users\_owns\_get**

> ResourcesUsers um\_users\_owns\_get\(user\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a User's own resources

You can retrieve resources owned by using the users ID. This value can be found in the response body when a user is created or when you GET a list of users.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a User's own resources
        api_response = api_instance.um_users_owns_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_owns_get: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a User's own resources
        api_response = api_instance.um_users_owns_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_owns_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** | The unique ID of the user |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**ResourcesUsers**](../models/resourcesusers.md)

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

## **um\_users\_post**

> User um\_users\_post\(user, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Create a user

You can use this POST method to create a user

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user = ionoscloud.User() # User | User to be created
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a user
        api_response = api_instance.um_users_post(user, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_post: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user = ionoscloud.User() # User | User to be created
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a user
        api_response = api_instance.um_users_post(user, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_post: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user** | [**User**](../models/user.md) | User to be created |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**User**](../models/user.md)

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

## **um\_users\_put**

> User um\_users\_put\(user\_id, user, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a user

You can use update attributes of a User

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
  user = ionoscloud.User() # User | Modified user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a user
        api_response = api_instance.um_users_put(user_id, user, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_put: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
  user = ionoscloud.User() # User | Modified user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a user
        api_response = api_instance.um_users_put(user_id, user, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_put: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** |  |  |
| **user** | [**User**](../models/user.md) | Modified user |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**User**](../models/user.md)

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

## **um\_users\_s3keys\_delete**

> object um\_users\_s3keys\_delete\(user\_id, key\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a S3 key

Delete a S3 key

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  key_id = 'key_id_example' # str | The unique access key ID of the S3 key
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a S3 key
        api_response = api_instance.um_users_s3keys_delete(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3keys_delete: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  key_id = 'key_id_example' # str | The unique access key ID of the S3 key
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Delete a S3 key
        api_response = api_instance.um_users_s3keys_delete(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3keys_delete: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** | The unique ID of the user |  |
| **key\_id** | **str** | The unique access key ID of the S3 key |  |
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

## **um\_users\_s3keys\_find\_by\_key\_id**

> S3Key um\_users\_s3keys\_find\_by\_key\_id\(user\_id, key\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve given S3 key belonging to the given User

You can retrieve S3 key belonging to the given User. This user Id can be found in the response body when a user is created or when you GET a list of users. The key Id can be found in the response body when a S3 key is created or when you GET a list of all S3 keys of a user

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  key_id = 'key_id_example' # str | The unique access key ID of the S3 key
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve given S3 key belonging to the given User
        api_response = api_instance.um_users_s3keys_find_by_key_id(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3keys_find_by_key_id: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  key_id = 'key_id_example' # str | The unique access key ID of the S3 key
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve given S3 key belonging to the given User
        api_response = api_instance.um_users_s3keys_find_by_key_id(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3keys_find_by_key_id: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** | The unique ID of the user |  |
| **key\_id** | **str** | The unique access key ID of the S3 key |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**S3Key**](../models/s3key.md)

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

## **um\_users\_s3keys\_get**

> S3Keys um\_users\_s3keys\_get\(user\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a User's S3 keys

You can retrieve S3 keys owned by a user by using the users ID. This user Id can be found in the response body when a user is created or when you GET a list of users.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a User's S3 keys
        api_response = api_instance.um_users_s3keys_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3keys_get: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve a User's S3 keys
        api_response = api_instance.um_users_s3keys_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3keys_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** | The unique ID of the user |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**S3Keys**](../models/s3keys.md)

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

## **um\_users\_s3keys\_post**

> S3Key um\_users\_s3keys\_post\(user\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Create a S3 key for the given user

Creates a S3 key for the given user. This user Id can be found in the response body when a user is created or when you GET a list of users. Maximum of 5 keys can be generated for a given user

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a S3 key for the given user
        api_response = api_instance.um_users_s3keys_post(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3keys_post: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Create a S3 key for the given user
        api_response = api_instance.um_users_s3keys_post(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3keys_post: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** | The unique ID of the user |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**S3Key**](../models/s3key.md)

### Authorization

[Basic Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Basic%20Authentication), [Token Authentication](https://github.com/ionos-cloud/sdk-python/tree/0f3f774f320d84336515f4ee45f93d8dc4a92d05/README.md#Token%20Authentication)

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| :--- | :--- | :--- |
| **200** | successful operation |  _X-RateLimit-Remaining - Number of requests which can still be made without triggering a failure response._     __ X-RateLimit-Limit - Average number of requests allowed per minute     _X-RateLimit-Burst - Maximum number of concurrent API requests allowed_    __ Location - Callback URL to poll async operation status   |
| **0** | Any erroneous status code: 400 \(parse error\), 401 \(auth error\), 402 \(trial access\), 403 \(insufficient permissions\), 404 \(not found\), 405 \(unsupported HTTP method\), 415 \(unsupported content type, 422 \(validation error\), 429 \(request rate limit exceeded\), 500 \(server error\), 503 \(maintenance\) | - |

## **um\_users\_s3keys\_put**

> S3Key um\_users\_s3keys\_put\(user\_id, key\_id, s3\_key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a S3 key having the given key id

You can enable or disable a given S3 key

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
  key_id = 'key_id_example' # str | The unique access key ID of the S3 key
  s3_key = ionoscloud.S3Key() # S3Key | Modified s3 key
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a S3 key having the given key id
        api_response = api_instance.um_users_s3keys_put(user_id, key_id, s3_key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3keys_put: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | 
  key_id = 'key_id_example' # str | The unique access key ID of the S3 key
  s3_key = ionoscloud.S3Key() # S3Key | Modified s3 key
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Modify a S3 key having the given key id
        api_response = api_instance.um_users_s3keys_put(user_id, key_id, s3_key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3keys_put: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** |  |  |
| **key\_id** | **str** | The unique access key ID of the S3 key |  |
| **s3\_key** | [**S3Key**](../models/s3key.md) | Modified s3 key |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**S3Key**](../models/s3key.md)

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

## **um\_users\_s3ssourl\_get**

> S3ObjectStorageSSO um\_users\_s3ssourl\_get\(user\_id, pretty=pretty, x\_contract\_number=x\_contract\_number\)

Retrieve S3 object storage single signon URL for the given user

You can retrieve S3 object storage single signon URL for the given user. This user Id can be found in the response body when a user is created or when you GET a list of users.

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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve S3 object storage single signon URL for the given user
        api_response = api_instance.um_users_s3ssourl_get(user_id, pretty=pretty, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3ssourl_get: %s\n" % e)
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
  pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
  x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)

    try:
        # Retrieve S3 object storage single signon URL for the given user
        api_response = api_instance.um_users_s3ssourl_get(user_id, pretty=pretty, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserManagementApi->um_users_s3ssourl_get: %s\n" % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **user\_id** | **str** | The unique ID of the user |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**S3ObjectStorageSSO**](../models/s3objectstoragesso.md)

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

