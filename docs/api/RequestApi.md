# RequestApi

All URIs are relative to *https://api.ionos.com/cloudapi/v5*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**requests_find_by_id**](RequestApi.md#requests_find_by_id) | **GET** /requests/{requestId} | Retrieve a Request |
| [**requests_get**](RequestApi.md#requests_get) | **GET** /requests | List Requests |
| [**requests_status_get**](RequestApi.md#requests_status_get) | **GET** /requests/{requestId}/status | Retrieve Request Status |


# **requests_find_by_id**
> Request requests_find_by_id(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve a Request

Retrieves the attributes of a given request.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.RequestApi(api_client)
    request_id = 'request_id_example' # str | 
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Request
        api_response = api_instance.requests_find_by_id(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling RequestApi.requests_find_by_id: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.RequestApi(api_client)
    request_id = 'request_id_example' # str | 
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Request
        api_response = api_instance.requests_find_by_id(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling RequestApi.requests_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **request_id** | **str**|  |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**Request**](Request.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **requests_get**
> Requests requests_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number, filter_status=filter_status, filter_created_after=filter_created_after, filter_created_before=filter_created_before, filter_created_date=filter_created_date, filter_created_by=filter_created_by, filter_etag=filter_etag, filter_request_status=filter_request_status, filter_method=filter_method, filter_headers=filter_headers, filter_body=filter_body, filter_url=filter_url, offset=offset, limit=limit)

List Requests

Retrieve a list of API requests.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.RequestApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    filter_status = 'filter_status_example' # str | Request filter to fetch all requests based on a particular status [QUEUED, RUNNING, DONE, FAILED]. It doesn't depend on depth query parameter (optional)
    filter_created_after = 'filter_created_after_example' # str | Request filter to fetch all requests created after the specified date. It doesn't depend on depth query parameter. Date format e.g. 2021-01-01+00:00:00 (optional)
    filter_created_before = 'filter_created_before_example' # str | Request filter to fetch all requests created before the specified date. It doesn't depend on depth query parameter. Date format e.g. 2021-01-01+00:00:00 (optional)
    filter_created_date = 'filter_created_date_example' # str | Response filter to select and display only the requests that contains the specified createdDate. The value is case insensitive and it  depends on depth query parameter that should have a value greater than 0. Date format e.g. 2020-11-16T17:42:59Z (optional)
    filter_created_by = 'filter_created_by_example' # str | Response filter to select and display only the requests that contains the specified createdBy. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_etag = 'filter_etag_example' # str | Response filter to select and display only the requests that contains the specified etag. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_request_status = 'filter_request_status_example' # str | Response filter to select and display only the requests that contains the specified requestStatus. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_method = 'filter_method_example' # str | Response filter to select and display only the requests that contains the specified method. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_headers = 'filter_headers_example' # str | Response filter to select and display only the requests that contains the specified headers. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_body = 'filter_body_example' # str | Response filter to select and display only the requests that contains the specified body. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_url = 'filter_url_example' # str | Response filter to select and display only the requests that contains the specified url. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)
    try:
        # List Requests
        api_response = api_instance.requests_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number, filter_status=filter_status, filter_created_after=filter_created_after, filter_created_before=filter_created_before, filter_created_date=filter_created_date, filter_created_by=filter_created_by, filter_etag=filter_etag, filter_request_status=filter_request_status, filter_method=filter_method, filter_headers=filter_headers, filter_body=filter_body, filter_url=filter_url, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling RequestApi.requests_get: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.RequestApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    filter_status = 'filter_status_example' # str | Request filter to fetch all requests based on a particular status [QUEUED, RUNNING, DONE, FAILED]. It doesn't depend on depth query parameter (optional)
    filter_created_after = 'filter_created_after_example' # str | Request filter to fetch all requests created after the specified date. It doesn't depend on depth query parameter. Date format e.g. 2021-01-01+00:00:00 (optional)
    filter_created_before = 'filter_created_before_example' # str | Request filter to fetch all requests created before the specified date. It doesn't depend on depth query parameter. Date format e.g. 2021-01-01+00:00:00 (optional)
    filter_created_date = 'filter_created_date_example' # str | Response filter to select and display only the requests that contains the specified createdDate. The value is case insensitive and it  depends on depth query parameter that should have a value greater than 0. Date format e.g. 2020-11-16T17:42:59Z (optional)
    filter_created_by = 'filter_created_by_example' # str | Response filter to select and display only the requests that contains the specified createdBy. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_etag = 'filter_etag_example' # str | Response filter to select and display only the requests that contains the specified etag. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_request_status = 'filter_request_status_example' # str | Response filter to select and display only the requests that contains the specified requestStatus. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_method = 'filter_method_example' # str | Response filter to select and display only the requests that contains the specified method. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_headers = 'filter_headers_example' # str | Response filter to select and display only the requests that contains the specified headers. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_body = 'filter_body_example' # str | Response filter to select and display only the requests that contains the specified body. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    filter_url = 'filter_url_example' # str | Response filter to select and display only the requests that contains the specified url. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)
    try:
        # List Requests
        api_response = api_instance.requests_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number, filter_status=filter_status, filter_created_after=filter_created_after, filter_created_before=filter_created_before, filter_created_date=filter_created_date, filter_created_by=filter_created_by, filter_etag=filter_etag, filter_request_status=filter_request_status, filter_method=filter_method, filter_headers=filter_headers, filter_body=filter_body, filter_url=filter_url, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling RequestApi.requests_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |
| **filter_status** | **str**| Request filter to fetch all requests based on a particular status [QUEUED, RUNNING, DONE, FAILED]. It doesn&#39;t depend on depth query parameter | [optional]  |
| **filter_created_after** | **str**| Request filter to fetch all requests created after the specified date. It doesn&#39;t depend on depth query parameter. Date format e.g. 2021-01-01+00:00:00 | [optional]  |
| **filter_created_before** | **str**| Request filter to fetch all requests created before the specified date. It doesn&#39;t depend on depth query parameter. Date format e.g. 2021-01-01+00:00:00 | [optional]  |
| **filter_created_date** | **str**| Response filter to select and display only the requests that contains the specified createdDate. The value is case insensitive and it  depends on depth query parameter that should have a value greater than 0. Date format e.g. 2020-11-16T17:42:59Z | [optional]  |
| **filter_created_by** | **str**| Response filter to select and display only the requests that contains the specified createdBy. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  | [optional]  |
| **filter_etag** | **str**| Response filter to select and display only the requests that contains the specified etag. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  | [optional]  |
| **filter_request_status** | **str**| Response filter to select and display only the requests that contains the specified requestStatus. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  | [optional]  |
| **filter_method** | **str**| Response filter to select and display only the requests that contains the specified method. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  | [optional]  |
| **filter_headers** | **str**| Response filter to select and display only the requests that contains the specified headers. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  | [optional]  |
| **filter_body** | **str**| Response filter to select and display only the requests that contains the specified body. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  | [optional]  |
| **filter_url** | **str**| Response filter to select and display only the requests that contains the specified url. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0.  | [optional]  |
| **offset** | **int**| the first element (of the total list of elements) to include in the response (use together with &lt;code&gt;limit&lt;/code&gt; for pagination) | [optional] [default to 0] |
| **limit** | **int**| the maximum number of elements to return (use together with &lt;code&gt;offset&lt;/code&gt; for pagination) | [optional] [default to 1000] |

### Return type

[**Requests**](Requests.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **requests_status_get**
> RequestStatus requests_status_get(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve Request Status

Retrieves the status of a given request.

### Example

* Basic Authentication (Basic Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.RequestApi(api_client)
    request_id = 'request_id_example' # str | 
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve Request Status
        api_response = api_instance.requests_status_get(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling RequestApi.requests_status_get: %s\n' % e)
```

* Api Key Authentication (Token Authentication):
```python
from __future__ import print_function
import time
import ionoscloud
from ionoscloud.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
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
    api_instance = ionoscloud.RequestApi(api_client)
    request_id = 'request_id_example' # str | 
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve Request Status
        api_response = api_instance.requests_status_get(request_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling RequestApi.requests_status_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **request_id** | **str**|  |  |
| **pretty** | **bool**| Controls whether response is pretty-printed (with indentation and new lines) | [optional] [default to True] |
| **depth** | **int**| Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth&#x3D;0: only direct properties are included. Children (servers etc.) are not included  - depth&#x3D;1: direct properties and children references are included  - depth&#x3D;2: direct properties and children properties are included  - depth&#x3D;3: direct properties and children properties and children&#39;s children are included  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users having more than 1 contract need to provide contract number, against which all API requests should be executed | [optional]  |

### Return type

[**RequestStatus**](RequestStatus.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

