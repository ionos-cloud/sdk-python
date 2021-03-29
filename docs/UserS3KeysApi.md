# UserS3KeysApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**um_users_s3keys_delete**](UserS3KeysApi.md#um_users_s3keys_delete) | **DELETE** /um/users/{userId}/s3keys/{keyId} | Delete an S3 Key |
| [**um_users_s3keys_find_by_key_id**](UserS3KeysApi.md#um_users_s3keys_find_by_key_id) | **GET** /um/users/{userId}/s3keys/{keyId} | Retrieve given S3 Key belonging to the given User |
| [**um_users_s3keys_get**](UserS3KeysApi.md#um_users_s3keys_get) | **GET** /um/users/{userId}/s3keys | Retrieve a User&#39;s S3 keys |
| [**um_users_s3keys_post**](UserS3KeysApi.md#um_users_s3keys_post) | **POST** /um/users/{userId}/s3keys | Create a S3 Key for the given User |
| [**um_users_s3keys_put**](UserS3KeysApi.md#um_users_s3keys_put) | **PUT** /um/users/{userId}/s3keys/{keyId} | Modify a S3 key having the given key id |
| [**um_users_s3ssourl_get**](UserS3KeysApi.md#um_users_s3ssourl_get) | **GET** /um/users/{userId}/s3ssourl | Retrieve S3 object storage single signon URL for the given user |


# **um_users_s3keys_delete**
> object um_users_s3keys_delete(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete an S3 Key

Delete an S3 key.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
    key_id = 'key_id_example' # str | The unique access key ID of the S3 key
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete an S3 Key
        api_response = api_instance.um_users_s3keys_delete(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_delete: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
    key_id = 'key_id_example' # str | The unique access key ID of the S3 key
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete an S3 Key
        api_response = api_instance.um_users_s3keys_delete(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user |  |
| **key_id** | **str**| The unique access key ID of the S3 key |  |
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

# **um_users_s3keys_find_by_key_id**
> S3Key um_users_s3keys_find_by_key_id(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve given S3 Key belonging to the given User

You can retrieve S3 key belonging to the given User. This user Id can be found in the response body when a user is created or when you GET a list of users. The key Id can be found in the response body when a S3 key is created or when you GET a list of all S3 keys of a user

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
    key_id = 'key_id_example' # str | The unique access key ID of the S3 key
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve given S3 Key belonging to the given User
        api_response = api_instance.um_users_s3keys_find_by_key_id(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_find_by_key_id: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
    key_id = 'key_id_example' # str | The unique access key ID of the S3 key
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve given S3 Key belonging to the given User
        api_response = api_instance.um_users_s3keys_find_by_key_id(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_find_by_key_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user |  |
| **key_id** | **str**| The unique access key ID of the S3 key |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**S3Key**](S3Key.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_s3keys_get**
> S3Keys um_users_s3keys_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a User's S3 keys

You can retrieve S3 keys owned by a user by using the users ID. This user Id can be found in the response body when a user is created or when you GET a list of users.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a User's S3 keys
        api_response = api_instance.um_users_s3keys_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_get: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a User's S3 keys
        api_response = api_instance.um_users_s3keys_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**S3Keys**](S3Keys.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_s3keys_post**
> S3Key um_users_s3keys_post(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a S3 Key for the given User

Creates a S3 key for the given user. This user Id can be found in the response body when a user is created or when you GET a list of users. Maximum of 5 keys can be generated for a given user

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a S3 Key for the given User
        api_response = api_instance.um_users_s3keys_post(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_post: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Create a S3 Key for the given User
        api_response = api_instance.um_users_s3keys_post(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**S3Key**](S3Key.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_s3keys_put**
> S3Key um_users_s3keys_put(user_id, key_id, s3_key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a S3 key having the given key id

You can enable or disable a given S3 key.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | 
    key_id = 'key_id_example' # str | The unique access key ID of the S3 key
    s3_key = ionoscloud.S3Key() # S3Key | Modified S3 key
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a S3 key having the given key id
        api_response = api_instance.um_users_s3keys_put(user_id, key_id, s3_key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_put: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | 
    key_id = 'key_id_example' # str | The unique access key ID of the S3 key
    s3_key = ionoscloud.S3Key() # S3Key | Modified S3 key
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a S3 key having the given key id
        api_response = api_instance.um_users_s3keys_put(user_id, key_id, s3_key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**|  |  |
| **key_id** | **str**| The unique access key ID of the S3 key |  |
| **s3_key** | [**S3Key**](S3Key.md)| Modified S3 key |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**S3Key**](S3Key.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **um_users_s3ssourl_get**
> S3ObjectStorageSSO um_users_s3ssourl_get(user_id, pretty=pretty, x_contract_number=x_contract_number)

Retrieve S3 object storage single signon URL for the given user

You can retrieve S3 object storage single signon URL for the given user. This user Id can be found in the response body when a user is created or when you GET a list of users.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve S3 object storage single signon URL for the given user
        api_response = api_instance.um_users_s3ssourl_get(user_id, pretty=pretty, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3ssourl_get: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
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
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve S3 object storage single signon URL for the given user
        api_response = api_instance.um_users_s3ssourl_get(user_id, pretty=pretty, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3ssourl_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**S3ObjectStorageSSO**](S3ObjectStorageSSO.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

