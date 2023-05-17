# TargetGroupsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**target_groups_delete**](TargetGroupsApi.md#target_groups_delete) | **DELETE** /targetgroups/{targetGroupId} | Delete a Target Group by ID |
| [**targetgroups_find_by_target_group_id**](TargetGroupsApi.md#targetgroups_find_by_target_group_id) | **GET** /targetgroups/{targetGroupId} | Get a Target Group by ID |
| [**targetgroups_get**](TargetGroupsApi.md#targetgroups_get) | **GET** /targetgroups | Get Target Groups |
| [**targetgroups_patch**](TargetGroupsApi.md#targetgroups_patch) | **PATCH** /targetgroups/{targetGroupId} | Partially Modify a Target Group by ID |
| [**targetgroups_post**](TargetGroupsApi.md#targetgroups_post) | **POST** /targetgroups | Create a Target Group |
| [**targetgroups_put**](TargetGroupsApi.md#targetgroups_put) | **PUT** /targetgroups/{targetGroupId} | Modify a Target Group by ID |


# **target_groups_delete**
> target_groups_delete(target_group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete a Target Group by ID

Deletes the target group specified by its ID.

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
    api_instance = ionoscloud.TargetGroupsApi(api_client)
    target_group_id = 'target_group_id_example' # str | The unique ID of the target group.
    try:
        # Delete a Target Group by ID
        api_instance.target_groups_delete(target_group_id)
    except ApiException as e:
        print('Exception when calling TargetGroupsApi.target_groups_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **target_group_id** | **str**| The unique ID of the target group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

void (empty response body)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **targetgroups_find_by_target_group_id**
> TargetGroup targetgroups_find_by_target_group_id(target_group_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get a Target Group by ID

Retrieves the properties of the target group specified by its ID.

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
    api_instance = ionoscloud.TargetGroupsApi(api_client)
    target_group_id = 'target_group_id_example' # str | The unique ID of the target group.
    try:
        # Get a Target Group by ID
        api_response = api_instance.targetgroups_find_by_target_group_id(target_group_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling TargetGroupsApi.targetgroups_find_by_target_group_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **target_group_id** | **str**| The unique ID of the target group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**TargetGroup**](../models/TargetGroup.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **targetgroups_get**
> TargetGroups targetgroups_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)

Get Target Groups

Lists target groups.  A target group is a set of one or more registered targets. You must specify an IP address, a port number, and a weight for each target. Any object with an IP address in your VDC can be a target, for example, a VM, another load balancer, etc. You can register a target with multiple target groups.

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
    api_instance = ionoscloud.TargetGroupsApi(api_client)
    try:
        # Get Target Groups
        api_response = api_instance.targetgroups_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling TargetGroupsApi.targetgroups_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (used together with &lt;b&gt;&lt;i&gt;offset&lt;/i&gt;&lt;/b&gt; for pagination). It must not exceed &lt;b&gt;&lt;i&gt;200&lt;/i&gt;&lt;/b&gt;. | [optional] [default to 100] |

### Return type

[**TargetGroups**](../models/TargetGroups.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **targetgroups_patch**
> TargetGroup targetgroups_patch(target_group_id, target_group_properties, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially Modify a Target Group by ID

Updates the properties of the target group specified by its ID.

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
    api_instance = ionoscloud.TargetGroupsApi(api_client)
    target_group_id = 'target_group_id_example' # str | The unique ID of the target group.
    target_group_properties = ionoscloud.TargetGroupProperties() # TargetGroupProperties | The target group properties to be updated.
    try:
        # Partially Modify a Target Group by ID
        api_response = api_instance.targetgroups_patch(target_group_id, target_group_properties)
        print(api_response)
    except ApiException as e:
        print('Exception when calling TargetGroupsApi.targetgroups_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **target_group_id** | **str**| The unique ID of the target group. |  |
| **target_group_properties** | [**TargetGroupProperties**](../models/TargetGroupProperties.md)| The target group properties to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**TargetGroup**](../models/TargetGroup.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **targetgroups_post**
> TargetGroup targetgroups_post(target_group, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create a Target Group

Creates a target group.

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
    api_instance = ionoscloud.TargetGroupsApi(api_client)
    target_group = ionoscloud.TargetGroup() # TargetGroup | The target group to create.
    try:
        # Create a Target Group
        api_response = api_instance.targetgroups_post(target_group)
        print(api_response)
    except ApiException as e:
        print('Exception when calling TargetGroupsApi.targetgroups_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **target_group** | [**TargetGroup**](../models/TargetGroup.md)| The target group to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**TargetGroup**](../models/TargetGroup.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **targetgroups_put**
> TargetGroup targetgroups_put(target_group_id, target_group, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify a Target Group by ID

Modifies the properties of the target group specified by its ID.

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
    api_instance = ionoscloud.TargetGroupsApi(api_client)
    target_group_id = 'target_group_id_example' # str | The unique ID of the target group.
    target_group = ionoscloud.TargetGroupPut() # TargetGroupPut | The modified target group.
    try:
        # Modify a Target Group by ID
        api_response = api_instance.targetgroups_put(target_group_id, target_group)
        print(api_response)
    except ApiException as e:
        print('Exception when calling TargetGroupsApi.targetgroups_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **target_group_id** | **str**| The unique ID of the target group. |  |
| **target_group** | [**TargetGroupPut**](../models/TargetGroupPut.md)| The modified target group. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**TargetGroup**](../models/TargetGroup.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

