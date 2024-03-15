# TemplatesApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**templates_find_by_id**](TemplatesApi.md#templates_find_by_id) | **GET** /templates/{templateId} | Get Cubes Template by ID |
| [**templates_get**](TemplatesApi.md#templates_get) | **GET** /templates | Get Cubes Templates |


# **templates_find_by_id**
> Template templates_find_by_id(template_id, depth=depth)

Get Cubes Template by ID

Retrieves the properties of the Cubes template specified by its ID.

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
    api_instance = ionoscloud.TemplatesApi(api_client)
    template_id = 'template_id_example' # str | The unique template ID.
    try:
        # Get Cubes Template by ID
        api_response = api_instance.templates_find_by_id(template_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling TemplatesApi.templates_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **template_id** | **str**| The unique template ID. |  |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**Template**](../models/Template.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **templates_get**
> Templates templates_get(depth=depth)

Get Cubes Templates

Retrieves all available templates.  Templates provide a pre-defined configuration for Cube servers.    >Templates are read-only and cannot be created, modified, or deleted by users.

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
    api_instance = ionoscloud.TemplatesApi(api_client)
    try:
        # Get Cubes Templates
        api_response = api_instance.templates_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling TemplatesApi.templates_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |

### Return type

[**Templates**](../models/Templates.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

