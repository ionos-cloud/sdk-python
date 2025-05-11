# UserManagementApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**um_groups_delete**](UserManagementApi.md#um_groups_delete) | **DELETE** /um/groups/{groupId} | Delete groups |
| [**um_groups_find_by_id**](UserManagementApi.md#um_groups_find_by_id) | **GET** /um/groups/{groupId} | Retrieve groups |
| [**um_groups_get**](UserManagementApi.md#um_groups_get) | **GET** /um/groups | List all groups |
| [**um_groups_post**](UserManagementApi.md#um_groups_post) | **POST** /um/groups | Create groups |
| [**um_groups_put**](UserManagementApi.md#um_groups_put) | **PUT** /um/groups/{groupId} | Modify groups |
| [**um_groups_resources_get**](UserManagementApi.md#um_groups_resources_get) | **GET** /um/groups/{groupId}/resources | Retrieve group resources |
| [**um_groups_shares_delete**](UserManagementApi.md#um_groups_shares_delete) | **DELETE** /um/groups/{groupId}/shares/{resourceId} | Remove group shares |
| [**um_groups_shares_find_by_resource_id**](UserManagementApi.md#um_groups_shares_find_by_resource_id) | **GET** /um/groups/{groupId}/shares/{resourceId} | Retrieve group shares |
| [**um_groups_shares_get**](UserManagementApi.md#um_groups_shares_get) | **GET** /um/groups/{groupId}/shares | List group shares  |
| [**um_groups_shares_post**](UserManagementApi.md#um_groups_shares_post) | **POST** /um/groups/{groupId}/shares/{resourceId} | Add group shares |
| [**um_groups_shares_put**](UserManagementApi.md#um_groups_shares_put) | **PUT** /um/groups/{groupId}/shares/{resourceId} | Modify group share privileges |
| [**um_groups_users_delete**](UserManagementApi.md#um_groups_users_delete) | **DELETE** /um/groups/{groupId}/users/{userId} | Remove users from groups |
| [**um_groups_users_get**](UserManagementApi.md#um_groups_users_get) | **GET** /um/groups/{groupId}/users | List group members |
| [**um_groups_users_post**](UserManagementApi.md#um_groups_users_post) | **POST** /um/groups/{groupId}/users | Add a Group Member |
| [**um_resources_find_by_type**](UserManagementApi.md#um_resources_find_by_type) | **GET** /um/resources/{resourceType} | List resources by type |
| [**um_resources_find_by_type_and_id**](UserManagementApi.md#um_resources_find_by_type_and_id) | **GET** /um/resources/{resourceType}/{resourceId} | Retrieve resources by type |
| [**um_resources_get**](UserManagementApi.md#um_resources_get) | **GET** /um/resources | List all resources |
| [**um_users_delete**](UserManagementApi.md#um_users_delete) | **DELETE** /um/users/{userId} | Delete users |
| [**um_users_find_by_id**](UserManagementApi.md#um_users_find_by_id) | **GET** /um/users/{userId} | Retrieve users |
| [**um_users_get**](UserManagementApi.md#um_users_get) | **GET** /um/users | List all users  |
| [**um_users_groups_get**](UserManagementApi.md#um_users_groups_get) | **GET** /um/users/{userId}/groups | Retrieve group resources by user ID |
| [**um_users_owns_get**](UserManagementApi.md#um_users_owns_get) | **GET** /um/users/{userId}/owns | Retrieve user resources by user ID |
| [**um_users_post**](UserManagementApi.md#um_users_post) | **POST** /um/users | Create users |
| [**um_users_put**](UserManagementApi.md#um_users_put) | **PUT** /um/users/{userId} | Modify users |


# **um_groups_delete**
> um_groups_delete(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete groups

Remove the specified group.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    try:
        # Delete groups
        api_instance.um_groups_delete(group_id)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
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

# **um_groups_find_by_id**
> Group um_groups_find_by_id(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve groups

Retrieve a group by the group ID. This value is in the response body when the group is created, and in the list of the groups, returned by GET.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    try:
        # Retrieve groups
        api_response = api_instance.um_groups_find_by_id(group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Group**](../models/Group.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_groups_get**
> Groups um_groups_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List all groups

List all the available user groups.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    try:
        # List all groups
        api_response = api_instance.um_groups_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Groups**](../models/Groups.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_groups_post**
> Group um_groups_post(group, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create groups

Create a group.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group = ionoscloud.Group() # Group | The group to create.
    try:
        # Create groups
        api_response = api_instance.um_groups_post(group)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group** | [**Group**](../models/Group.md)| The group to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Group**](../models/Group.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **um_groups_put**
> Group um_groups_put(group_id, group, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify groups

Modify the properties of the specified group.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    group = ionoscloud.Group() # Group | The modified group.
    try:
        # Modify groups
        api_response = api_instance.um_groups_put(group_id, group)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **group** | [**Group**](../models/Group.md)| The modified group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Group**](../models/Group.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **um_groups_resources_get**
> ResourceGroups um_groups_resources_get(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve group resources

List the resources assigned to the group, by group ID.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    try:
        # Retrieve group resources
        api_response = api_instance.um_groups_resources_get(group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_resources_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ResourceGroups**](../models/ResourceGroups.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_groups_shares_delete**
> um_groups_shares_delete(group_id, resource_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Remove group shares

Remove the specified share from the group.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    resource_id = 'resource_id_example' # str | The unique ID of the resource.
    try:
        # Remove group shares
        api_instance.um_groups_shares_delete(group_id, resource_id)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_shares_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **resource_id** | **str**| The unique ID of the resource. |  |
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

# **um_groups_shares_find_by_resource_id**
> GroupShare um_groups_shares_find_by_resource_id(group_id, resource_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve group shares

Retrieve the properties of the specified group share.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    resource_id = 'resource_id_example' # str | The unique ID of the resource.
    try:
        # Retrieve group shares
        api_response = api_instance.um_groups_shares_find_by_resource_id(group_id, resource_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_shares_find_by_resource_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **resource_id** | **str**| The unique ID of the resource. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**GroupShare**](../models/GroupShare.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_groups_shares_get**
> GroupShares um_groups_shares_get(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List group shares 

List all shares and share privileges for the specified group.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    try:
        # List group shares 
        api_response = api_instance.um_groups_shares_get(group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_shares_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**GroupShares**](../models/GroupShares.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_groups_shares_post**
> GroupShare um_groups_shares_post(group_id, resource_id, resource, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Add group shares

Add the specified share to the group.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    resource_id = 'resource_id_example' # str | The unique ID of the resource.
    resource = ionoscloud.GroupShare() # GroupShare | The resource to add.
    try:
        # Add group shares
        api_response = api_instance.um_groups_shares_post(group_id, resource_id, resource)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_shares_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **resource_id** | **str**| The unique ID of the resource. |  |
| **resource** | [**GroupShare**](../models/GroupShare.md)| The resource to add. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**GroupShare**](../models/GroupShare.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_groups_shares_put**
> GroupShare um_groups_shares_put(group_id, resource_id, resource, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify group share privileges

Modify share permissions for the specified group. With an empty body, no updates are performed, and the current share permissions for the group are returned with response code 200.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    resource_id = 'resource_id_example' # str | The unique ID of the resource.
    resource = ionoscloud.GroupShare() # GroupShare | The modified resource
    try:
        # Modify group share privileges
        api_response = api_instance.um_groups_shares_put(group_id, resource_id, resource)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_shares_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **resource_id** | **str**| The unique ID of the resource. |  |
| **resource** | [**GroupShare**](../models/GroupShare.md)| The modified resource |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**GroupShare**](../models/GroupShare.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **um_groups_users_delete**
> um_groups_users_delete(group_id, user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Remove users from groups

Remove the specified user from the group.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    user_id = 'user_id_example' # str | The unique ID of the user.
    try:
        # Remove users from groups
        api_instance.um_groups_users_delete(group_id, user_id)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_users_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **user_id** | **str**| The unique ID of the user. |  |
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

# **um_groups_users_get**
> GroupMembers um_groups_users_get(group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List group members

List all members of the specified user group.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    try:
        # List group members
        api_response = api_instance.um_groups_users_get(group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_users_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**GroupMembers**](../models/GroupMembers.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_groups_users_post**
> User um_groups_users_post(group_id, user, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Add a Group Member

Adds an existing user to the specified group. 

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    group_id = 'group_id_example' # str | The unique ID of the group.
    user = ionoscloud.UserGroupPost() # UserGroupPost | The user to add.
    try:
        # Add a Group Member
        api_response = api_instance.um_groups_users_post(group_id, user)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_groups_users_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **group_id** | **str**| The unique ID of the group. |  |
| **user** | [**UserGroupPost**](../models/UserGroupPost.md)| The user to add. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**User**](../models/User.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **um_resources_find_by_type**
> Resources um_resources_find_by_type(resource_type, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List resources by type

List all resources of the specified type.  Resource types are: {datacenter, snapshot, image, ipblock, pcc, backupunit, k8s}  Resource types are in the list of resources, returned by GET.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    resource_type = 'resource_type_example' # str | The resource type
    try:
        # List resources by type
        api_response = api_instance.um_resources_find_by_type(resource_type)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_resources_find_by_type: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **resource_type** | **str**| The resource type |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Resources**](../models/Resources.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_resources_find_by_type_and_id**
> Resource um_resources_find_by_type_and_id(resource_type, resource_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve resources by type

Retrieve a resource by the resource type and resource ID.  Resource types are: {datacenter, snapshot, image, ipblock, pcc, backupunit, k8s}  Resource types are in the list of resources, returned by GET.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    resource_type = 'resource_type_example' # str | The resource type
    resource_id = 'resource_id_example' # str | The resource ID
    try:
        # Retrieve resources by type
        api_response = api_instance.um_resources_find_by_type_and_id(resource_type, resource_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_resources_find_by_type_and_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **resource_type** | **str**| The resource type |  |
| **resource_id** | **str**| The resource ID |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Resource**](../models/Resource.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_resources_get**
> Resources um_resources_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List all resources

List all the available resources.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    try:
        # List all resources
        api_response = api_instance.um_resources_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_resources_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Resources**](../models/Resources.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_delete**
> um_users_delete(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete users

Delete the specified user.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    try:
        # Delete users
        api_instance.um_users_delete(user_id)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_users_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
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

# **um_users_find_by_id**
> User um_users_find_by_id(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve users

Retrieve user properties by user ID. The user ID is in the response body when the user is created, and in the list of the users, returned by GET.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    try:
        # Retrieve users
        api_response = api_instance.um_users_find_by_id(user_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_users_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**User**](../models/User.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_get**
> Users um_users_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

List all users 

List all the users in your account.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    try:
        # List all users 
        api_response = api_instance.um_users_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_users_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (use together with &lt;code&gt;offset&lt;/code&gt; for pagination). | [optional] [default to 100] |

### Return type

[**Users**](../models/Users.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_groups_get**
> ResourceGroups um_users_groups_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve group resources by user ID

Retrieve group resources of the user by user ID. The user ID is in the response body when the user is created, and in the list of the users, returned by GET.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    try:
        # Retrieve group resources by user ID
        api_response = api_instance.um_users_groups_get(user_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_users_groups_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ResourceGroups**](../models/ResourceGroups.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_owns_get**
> ResourcesUsers um_users_owns_get(user_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve user resources by user ID

Retrieve own resources of the user by user ID. The user ID is in the response body when the user is created, and in the list of the users, returned by GET.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    try:
        # Retrieve user resources by user ID
        api_response = api_instance.um_users_owns_get(user_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_users_owns_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**ResourcesUsers**](../models/ResourcesUsers.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **um_users_post**
> User um_users_post(user, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create users

Create a user.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user = ionoscloud.UserPost() # UserPost | The user to create.
    try:
        # Create users
        api_response = api_instance.um_users_post(user)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_users_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user** | [**UserPost**](../models/UserPost.md)| The user to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**User**](../models/User.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **um_users_put**
> User um_users_put(user_id, user, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify users

Modify the properties of the specified user.

### Example

```python
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
    api_instance = ionoscloud.UserManagementApi(api_client)
    user_id = 'user_id_example' # str | The unique ID of the user.
    user = ionoscloud.UserPut() # UserPut | The modified user
    try:
        # Modify users
        api_response = api_instance.um_users_put(user_id, user)
        print(api_response)
    except ApiException as e:
        print('Exception when calling UserManagementApi.um_users_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **user_id** | **str**| The unique ID of the user. |  |
| **user** | [**UserPut**](../models/UserPut.md)| The modified user |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**User**](../models/User.md)

### Authorization

BasicAuthentication, TokenAuthentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

