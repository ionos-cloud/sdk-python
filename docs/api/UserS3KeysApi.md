# UserS3KeysApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**um_users_s3keys_delete**](UserS3KeysApi.md#um_users_s3keys_delete) | **DELETE** /um/users/{userId}/s3keys/{keyId} | Delete Object storage keys |
| [**um_users_s3keys_find_by_key_id**](UserS3KeysApi.md#um_users_s3keys_find_by_key_id) | **GET** /um/users/{userId}/s3keys/{keyId} | Retrieve user Object storage keys by key ID |
| [**um_users_s3keys_get**](UserS3KeysApi.md#um_users_s3keys_get) | **GET** /um/users/{userId}/s3keys | List user Object storage keys |
| [**um_users_s3keys_post**](UserS3KeysApi.md#um_users_s3keys_post) | **POST** /um/users/{userId}/s3keys | Create user Object storage keys |
| [**um_users_s3keys_put**](UserS3KeysApi.md#um_users_s3keys_put) | **PUT** /um/users/{userId}/s3keys/{keyId} | Modify a Object storage Key by Key ID |
| [**um_users_s3ssourl_get**](UserS3KeysApi.md#um_users_s3ssourl_get) | **GET** /um/users/{userId}/s3ssourl | Retrieve Object storage single sign-on URLs |


# **um_users_s3keys_delete**
> um_users_s3keys_delete(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete Object storage keys

Delete the specified user Object storage key.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    key_id = 'key_id_example' # str | The unique ID of the Object storage key.
    try:
        # Delete Object storage keys
        api_instance.um_users_s3keys_delete(user_id, key_id)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
| **key_id** | **str**| The unique ID of the Object storage key. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

void (empty response body)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_s3keys_find_by_key_id**
> S3Key um_users_s3keys_find_by_key_id(user_id, key_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve user Object storage keys by key ID

Retrieve the specified user Object storage key. The user ID is in the response body when the user is created, and in the list of the users, returned by GET. The key ID is in the response body when the Object storage key is created, and in the list of all user Object storage keys, returned by GET.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    key_id = 'key_id_example' # str | The unique ID of the Object storage key.
    try:
        # Retrieve user Object storage keys by key ID
        api_response = api_instance.um_users_s3keys_find_by_key_id(user_id, key_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_find_by_key_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
| **key_id** | **str**| The unique ID of the Object storage key. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**S3Key**](../models/S3Key.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_s3keys_get**
> S3Keys um_users_s3keys_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List user Object storage keys

List Object storage keys by user ID. The user ID is in the response body when the user is created, and in the list of the users, returned by GET.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    try:
        # List user Object storage keys
        api_response = api_instance.um_users_s3keys_get(user_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**S3Keys**](../models/S3Keys.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_s3keys_post**
> S3Key um_users_s3keys_post(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create user Object storage keys

Create an Object storage key for the specified user. The user ID is in the response body when the user is created, and in the list of the users, returned by GET. A maximum of five keys per user can be generated.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    try:
        # Create user Object storage keys
        api_response = api_instance.um_users_s3keys_post(user_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**S3Key**](../models/S3Key.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_s3keys_put**
> S3Key um_users_s3keys_put(user_id, key_id, s3_key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Object storage Key by Key ID

Enables or disables the specified user Object storage key.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    key_id = 'key_id_example' # str | The unique ID of the Object storage key.
    s3_key = ionoscloud.S3Key() # S3Key | The modified Object storage key.
    try:
        # Modify a Object storage Key by Key ID
        api_response = api_instance.um_users_s3keys_put(user_id, key_id, s3_key)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3keys_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
| **key_id** | **str**| The unique ID of the Object storage key. |  |
| **s3_key** | [**S3Key**](../models/S3Key.md)| The modified Object storage key. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**S3Key**](../models/S3Key.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **um_users_s3ssourl_get**
> S3ObjectStorageSSO um_users_s3ssourl_get(user_id, pretty=pretty, x_contract_number=x_contract_number)

Retrieve Object storage single sign-on URLs

Retrieve Ionos Object Storage single sign-on URLs for the the specified user. The user ID is in the response body when the user is created, and in the list of the users, returned by GET.

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v6
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v6',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.UserS3KeysApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    try:
        # Retrieve Object storage single sign-on URLs
        api_response = api_instance.um_users_s3ssourl_get(user_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserS3KeysApi.um_users_s3ssourl_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**S3ObjectStorageSSO**](../models/S3ObjectStorageSSO.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

