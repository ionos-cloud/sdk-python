# BackupUnitsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**backupunits_delete**](BackupUnitsApi.md#backupunits_delete) | **DELETE** /backupunits/{backupunitId} | Delete backup units |
| [**backupunits_find_by_id**](BackupUnitsApi.md#backupunits_find_by_id) | **GET** /backupunits/{backupunitId} | Retrieve backup units |
| [**backupunits_get**](BackupUnitsApi.md#backupunits_get) | **GET** /backupunits | List backup units |
| [**backupunits_patch**](BackupUnitsApi.md#backupunits_patch) | **PATCH** /backupunits/{backupunitId} | Partially modify backup units |
| [**backupunits_post**](BackupUnitsApi.md#backupunits_post) | **POST** /backupunits | Create backup units |
| [**backupunits_put**](BackupUnitsApi.md#backupunits_put) | **PUT** /backupunits/{backupunitId} | Modify backup units |
| [**backupunits_ssourl_get**](BackupUnitsApi.md#backupunits_ssourl_get) | **GET** /backupunits/{backupunitId}/ssourl | Retrieve BU single sign-on URLs |


# **backupunits_delete**
> backupunits_delete(backupunit_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete backup units

Remove the specified backup unit.  This process will delete: 1) The backup plans inside the backup unit 2) All backups, associated with this backup unit 3) The backup user 4) The backup unit itself

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
    api_instance = ionoscloud.BackupUnitsApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit.
    try:
        # Delete backup units
        api_instance.backupunits_delete(backupunit_id)
    except ApiException as e:
        print('Exception when calling BackupUnitsApi.backupunits_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **backupunit_id** | **str**| The unique ID of the backup unit. |  |
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

# **backupunits_find_by_id**
> BackupUnit backupunits_find_by_id(backupunit_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve backup units

Retrieve the properties of the specified backup unit.

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
    api_instance = ionoscloud.BackupUnitsApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit.
    try:
        # Retrieve backup units
        api_response = api_instance.backupunits_find_by_id(backupunit_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling BackupUnitsApi.backupunits_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **backupunit_id** | **str**| The unique ID of the backup unit. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**BackupUnit**](../models/BackupUnit.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **backupunits_get**
> BackupUnits backupunits_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List backup units

List all available backup units.

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
    api_instance = ionoscloud.BackupUnitsApi(api_client)
    try:
        # List backup units
        api_response = api_instance.backupunits_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling BackupUnitsApi.backupunits_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**BackupUnits**](../models/BackupUnits.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **backupunits_patch**
> BackupUnit backupunits_patch(backupunit_id, backup_unit, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Partially modify backup units

Update the properties of the specified backup unit.

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
    api_instance = ionoscloud.BackupUnitsApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit.
    backup_unit = ionoscloud.BackupUnitProperties() # BackupUnitProperties | The properties of the backup unit to be updated.
    try:
        # Partially modify backup units
        api_response = api_instance.backupunits_patch(backupunit_id, backup_unit)
        print(api_response)
    except ApiException as e:
        print('Exception when calling BackupUnitsApi.backupunits_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **backupunit_id** | **str**| The unique ID of the backup unit. |  |
| **backup_unit** | [**BackupUnitProperties**](../models/BackupUnitProperties.md)| The properties of the backup unit to be updated. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**BackupUnit**](../models/BackupUnit.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **backupunits_post**
> BackupUnit backupunits_post(backup_unit, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create backup units

Create a backup unit. Backup units are resources, same as storage volumes or snapshots; they can be shared through groups in User management. 

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
    api_instance = ionoscloud.BackupUnitsApi(api_client)
    backup_unit = ionoscloud.BackupUnit() # BackupUnit | The backup unit to create.
    try:
        # Create backup units
        api_response = api_instance.backupunits_post(backup_unit)
        print(api_response)
    except ApiException as e:
        print('Exception when calling BackupUnitsApi.backupunits_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **backup_unit** | [**BackupUnit**](../models/BackupUnit.md)| The backup unit to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**BackupUnit**](../models/BackupUnit.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **backupunits_put**
> BackupUnit backupunits_put(backupunit_id, backup_unit, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify backup units

Modify the properties of the specified backup unit.

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
    api_instance = ionoscloud.BackupUnitsApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit.
    backup_unit = ionoscloud.BackupUnit() # BackupUnit | The modified backup unit.
    try:
        # Modify backup units
        api_response = api_instance.backupunits_put(backupunit_id, backup_unit)
        print(api_response)
    except ApiException as e:
        print('Exception when calling BackupUnitsApi.backupunits_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **backupunit_id** | **str**| The unique ID of the backup unit. |  |
| **backup_unit** | [**BackupUnit**](../models/BackupUnit.md)| The modified backup unit. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**BackupUnit**](../models/BackupUnit.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **backupunits_ssourl_get**
> BackupUnitSSO backupunits_ssourl_get(backupunit_id, pretty=pretty, x_contract_number=x_contract_number)

Retrieve BU single sign-on URLs

Retrieve a single sign-on URL for the specified backup unit.

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
    api_instance = ionoscloud.BackupUnitsApi(api_client)
    backupunit_id = 'backupunit_id_example' # str | The unique ID of the backup unit.
    try:
        # Retrieve BU single sign-on URLs
        api_response = api_instance.backupunits_ssourl_get(backupunit_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling BackupUnitsApi.backupunits_ssourl_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **backupunit_id** | **str**| The unique ID of the backup unit. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**BackupUnitSSO**](../models/BackupUnitSSO.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

