# LocationApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**locations_find_by_region_id**](LocationApi.md#locations_find_by_region_id) | **GET** /locations/{regionId} | List Locations within a region |
| [**locations_find_by_region_id_and_id**](LocationApi.md#locations_find_by_region_id_and_id) | **GET** /locations/{regionId}/{locationId} | Retrieve a Location |
| [**locations_get**](LocationApi.md#locations_get) | **GET** /locations | List Locations |


# **locations_find_by_region_id**
> Locations locations_find_by_region_id(region_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Locations within a region

Retrieve a list of Locations within a world's region

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LocationApi(api_client)
    region_id = 'region_id_example' # str | 
    try:
        # List Locations within a region
        api_response = api_instance.locations_find_by_region_id(region_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LocationApi.locations_find_by_region_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region_id** | **str**|  |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Locations**](../models/Locations.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **locations_find_by_region_id_and_id**
> Location locations_find_by_region_id_and_id(region_id, location_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Location

Retrieves the attributes of a given location

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LocationApi(api_client)
    region_id = 'region_id_example' # str | 
    location_id = 'location_id_example' # str | 
    try:
        # Retrieve a Location
        api_response = api_instance.locations_find_by_region_id_and_id(region_id, location_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LocationApi.locations_find_by_region_id_and_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region_id** | **str**|  |  |
| **location_id** | **str**|  |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Location**](../models/Location.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **locations_get**
> Locations locations_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Locations

Retrieve a list of Locations. This list represents where you can provision your virtual data centers

### Example

```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LocationApi(api_client)
    try:
        # List Locations
        api_response = api_instance.locations_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling LocationApi.locations_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Locations**](../models/Locations.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

