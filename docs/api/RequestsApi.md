# RequestsApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**requests_find_by_id**](RequestsApi.md#requests_find_by_id) | **GET** /requests/{requestId} | Retrieve requests |
| [**requests_get**](RequestsApi.md#requests_get) | **GET** /requests | List requests |
| [**requests_status_get**](RequestsApi.md#requests_status_get) | **GET** /requests/{requestId}/status | Retrieve request status |


# **requests_find_by_id**
> Request requests_find_by_id(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve requests

Retrieve the properties of the specified request.

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
    api_instance = ionoscloud.RequestsApi(api_client)
    request_id = 'request_id_example' # str | The unique ID of the request.
    try:
        # Retrieve requests
        api_response = api_instance.requests_find_by_id(request_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling RequestsApi.requests_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **request_id** | **str**| The unique ID of the request. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**Request**](../models/Request.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **requests_get**
> Requests requests_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number, filter_status=filter_status, filter_created_after=filter_created_after, filter_created_before=filter_created_before, filter_created_date=filter_created_date, filter_created_by=filter_created_by, filter_etag=filter_etag, filter_request_status=filter_request_status, filter_method=filter_method, filter_headers=filter_headers, filter_body=filter_body, filter_url=filter_url, offset=offset, limit=limit)

List requests

List all API requests.

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
    api_instance = ionoscloud.RequestsApi(api_client)
    try:
        # List requests
        api_response = api_instance.requests_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling RequestsApi.requests_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |
| **filter_status** | **str**| Filter the list by request status [QUEUED, RUNNING, DONE, FAILED]. Filter is not affected by the depth query parameter. | [optional]  |
| **filter_created_after** | **str**| Filter the list to only include the requests created after the date, specified in the yyyy-MM-dd HH:mm:ss format. Filter is not affected by the depth query parameter. | [optional]  |
| **filter_created_before** | **str**| Filter the list to only include the requests created before the date, specified in the yyyy-MM-dd HH:mm:ss format. Filter is not affected by the depth query parameter. | [optional]  |
| **filter_created_date** | **str**| Filter the list to only include the requests that contain the createdDate, specified in the yyyy-MM-dd HH:mm:ss format. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero. | [optional]  |
| **filter_created_by** | **str**| Filter the list to only include the requests that contain the createdBy, specified in the yyyy-MM-dd HH:mm:ss format. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero.  | [optional]  |
| **filter_etag** | **str**| Filter the list to only include the requests that contain the specified etag. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero.  | [optional]  |
| **filter_request_status** | **str**| Filter the list to only include the requests that contain the specified requestStatus. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero.  | [optional]  |
| **filter_method** | **str**| Filter the list to only include the requests that contain the specified method. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero.  | [optional]  |
| **filter_headers** | **str**| Filter the list to only include the requests that contain the specified headers. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero.  | [optional]  |
| **filter_body** | **str**| Filter the list to only include the requests that contain the specified body. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero.  | [optional]  |
| **filter_url** | **str**| Filter the list to only include the requests that contain the specified URL. The value is not case-sensitive, and the filter requires that the depth query parameter value is greater than zero.  | [optional]  |
| **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 1000] |

### Return type

[**Requests**](../models/Requests.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **requests_status_get**
> RequestStatus requests_status_get(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve request status

Retrieve the status of the specified request.

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
    api_instance = ionoscloud.RequestsApi(api_client)
    request_id = 'request_id_example' # str | The unique ID of the request.
    try:
        # Retrieve request status
        api_response = api_instance.requests_status_get(request_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling RequestsApi.requests_status_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **request_id** | **str**| The unique ID of the request. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**RequestStatus**](../models/RequestStatus.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

