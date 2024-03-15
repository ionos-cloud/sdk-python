# LocationsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**locations_find_by_region_id**](LocationsApi.md#locations_find_by_region_id) | **GET** /locations/{regionId} | Get Locations within a Region |
| [**locations_find_by_region_id_and_id**](LocationsApi.md#locations_find_by_region_id_and_id) | **GET** /locations/{regionId}/{locationId} | Get Location by ID |
| [**locations_get**](LocationsApi.md#locations_get) | **GET** /locations | Get Locations |


# **locations_find_by_region_id**
> Locations locations_find_by_region_id(region_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Locations within a Region

Retrieves the available locations in a region specified by its ID. The 'regionId' consists of the two character identifier of the region (country), e.g., 'de'.

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
    api_instance = ionoscloud.LocationsApi(api_client)
    region_id = 'region_id_example' # str | The unique ID of the region.
    try:
        # Get Locations within a Region
        api_response = api_instance.locations_find_by_region_id(region_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LocationsApi.locations_find_by_region_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region_id** | **str**| The unique ID of the region. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Locations**](../models/Locations.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **locations_find_by_region_id_and_id**
> Location locations_find_by_region_id_and_id(region_id, location_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Location by ID

Retrieves the information about the location specified by its ID. The 'locationId' consists of the three-digit identifier of the city according to the IATA code.

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
    api_instance = ionoscloud.LocationsApi(api_client)
    region_id = 'region_id_example' # str | The unique ID of the region.
    location_id = 'location_id_example' # str | The unique ID of the location.
    try:
        # Get Location by ID
        api_response = api_instance.locations_find_by_region_id_and_id(region_id, location_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling LocationsApi.locations_find_by_region_id_and_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **region_id** | **str**| The unique ID of the region. |  |
| **location_id** | **str**| The unique ID of the location. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Location**](../models/Location.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **locations_get**
> Locations locations_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Get Locations

Retrieves the available physical locations where you can deploy cloud resources in a VDC.    A location is identified by a combination of the following characters:    * a two-character **regionId**, which represents a country (example: 'de')    * a three-character **locationId**, which represents a city. The 'locationId' is typically based on the IATA code of the city's airport (example: 'txl').    >Note that 'locations' are read-only and cannot be changed.

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
    api_instance = ionoscloud.LocationsApi(api_client)
    try:
        # Get Locations
        api_response = api_instance.locations_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling LocationsApi.locations_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Locations**](../models/Locations.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

