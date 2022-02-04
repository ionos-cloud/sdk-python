# KubernetesApi

All URIs are relative to *https://api.ionos.com/cloudapi/v6*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**k8s_delete**](KubernetesApi.md#k8s_delete) | **DELETE** /k8s/{k8sClusterId} | Delete Kubernetes clusters |
| [**k8s_find_by_cluster_id**](KubernetesApi.md#k8s_find_by_cluster_id) | **GET** /k8s/{k8sClusterId} | Retrieve Kubernetes clusters |
| [**k8s_get**](KubernetesApi.md#k8s_get) | **GET** /k8s | List Kubernetes clusters |
| [**k8s_kubeconfig_get**](KubernetesApi.md#k8s_kubeconfig_get) | **GET** /k8s/{k8sClusterId}/kubeconfig | Retrieve Kubernetes configuration files |
| [**k8s_nodepools_delete**](KubernetesApi.md#k8s_nodepools_delete) | **DELETE** /k8s/{k8sClusterId}/nodepools/{nodepoolId} | Delete Kubernetes node pools |
| [**k8s_nodepools_find_by_id**](KubernetesApi.md#k8s_nodepools_find_by_id) | **GET** /k8s/{k8sClusterId}/nodepools/{nodepoolId} | Retrieve Kubernetes node pools |
| [**k8s_nodepools_get**](KubernetesApi.md#k8s_nodepools_get) | **GET** /k8s/{k8sClusterId}/nodepools | List Kubernetes node pools |
| [**k8s_nodepools_nodes_delete**](KubernetesApi.md#k8s_nodepools_nodes_delete) | **DELETE** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId} | Delete Kubernetes nodes |
| [**k8s_nodepools_nodes_find_by_id**](KubernetesApi.md#k8s_nodepools_nodes_find_by_id) | **GET** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId} | Retrieve Kubernetes nodes |
| [**k8s_nodepools_nodes_get**](KubernetesApi.md#k8s_nodepools_nodes_get) | **GET** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes | List Kubernetes nodes |
| [**k8s_nodepools_nodes_replace_post**](KubernetesApi.md#k8s_nodepools_nodes_replace_post) | **POST** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId}/replace | Recreate Kubernetes nodes |
| [**k8s_nodepools_post**](KubernetesApi.md#k8s_nodepools_post) | **POST** /k8s/{k8sClusterId}/nodepools | Create Kubernetes node pools |
| [**k8s_nodepools_put**](KubernetesApi.md#k8s_nodepools_put) | **PUT** /k8s/{k8sClusterId}/nodepools/{nodepoolId} | Modify Kubernetes node pools |
| [**k8s_post**](KubernetesApi.md#k8s_post) | **POST** /k8s | Create Kubernetes clusters |
| [**k8s_put**](KubernetesApi.md#k8s_put) | **PUT** /k8s/{k8sClusterId} | Modify Kubernetes clusters |
| [**k8s_versions_default_get**](KubernetesApi.md#k8s_versions_default_get) | **GET** /k8s/versions/default | Retrieve current default Kubernetes version |
| [**k8s_versions_get**](KubernetesApi.md#k8s_versions_get) | **GET** /k8s/versions | List Kubernetes versions |


# **k8s_delete**
> k8s_delete(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete Kubernetes clusters

Delete the specified Kubernetes cluster.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    try:
        # Delete Kubernetes clusters
        api_instance.k8s_delete(k8s_cluster_id)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
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

# **k8s_find_by_cluster_id**
> KubernetesCluster k8s_find_by_cluster_id(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve Kubernetes clusters

Retrieve the specified Kubernetes cluster.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    try:
        # Retrieve Kubernetes clusters
        api_response = api_instance.k8s_find_by_cluster_id(k8s_cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_find_by_cluster_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**KubernetesCluster**](../models/KubernetesCluster.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **k8s_get**
> KubernetesClusters k8s_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Kubernetes clusters

List all available Kubernetes clusters.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    try:
        # List Kubernetes clusters
        api_response = api_instance.k8s_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**KubernetesClusters**](../models/KubernetesClusters.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **k8s_kubeconfig_get**
> str k8s_kubeconfig_get(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve Kubernetes configuration files

Retrieve a configuration file for the specified Kubernetes cluster, in YAML or JSON format as defined in the Accept header; the default Accept header is application/yaml.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    try:
        # Retrieve Kubernetes configuration files
        api_response = api_instance.k8s_kubeconfig_get(k8s_cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_kubeconfig_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

**str**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml, application/x-yaml, application/json

# **k8s_nodepools_delete**
> k8s_nodepools_delete(k8s_cluster_id, nodepool_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete Kubernetes node pools

Delete the specified Kubernetes node pool.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    try:
        # Delete Kubernetes node pools
        api_instance.k8s_nodepools_delete(k8s_cluster_id, nodepool_id)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_nodepools_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. |  |
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

# **k8s_nodepools_find_by_id**
> KubernetesNodePool k8s_nodepools_find_by_id(k8s_cluster_id, nodepool_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve Kubernetes node pools

Retrieve the specified Kubernetes node pool.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    try:
        # Retrieve Kubernetes node pools
        api_response = api_instance.k8s_nodepools_find_by_id(k8s_cluster_id, nodepool_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_nodepools_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**KubernetesNodePool**](../models/KubernetesNodePool.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **k8s_nodepools_get**
> KubernetesNodePools k8s_nodepools_get(k8s_cluster_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Kubernetes node pools

List all Kubernetes node pools, included the specified Kubernetes cluster.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    try:
        # List Kubernetes node pools
        api_response = api_instance.k8s_nodepools_get(k8s_cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_nodepools_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**KubernetesNodePools**](../models/KubernetesNodePools.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **k8s_nodepools_nodes_delete**
> k8s_nodepools_nodes_delete(k8s_cluster_id, nodepool_id, node_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Delete Kubernetes nodes

Delete the specified Kubernetes node.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    node_id = 'node_id_example' # str | The unique ID of the Kubernetes node.
    try:
        # Delete Kubernetes nodes
        api_instance.k8s_nodepools_nodes_delete(k8s_cluster_id, nodepool_id, node_id)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_nodepools_nodes_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. |  |
| **node_id** | **str**| The unique ID of the Kubernetes node. |  |
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

# **k8s_nodepools_nodes_find_by_id**
> KubernetesNode k8s_nodepools_nodes_find_by_id(k8s_cluster_id, nodepool_id, node_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Retrieve Kubernetes nodes

Retrieve the specified Kubernetes node.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    node_id = 'node_id_example' # str | The unique ID of the Kubernetes node.
    try:
        # Retrieve Kubernetes nodes
        api_response = api_instance.k8s_nodepools_nodes_find_by_id(k8s_cluster_id, nodepool_id, node_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_nodepools_nodes_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. |  |
| **node_id** | **str**| The unique ID of the Kubernetes node. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**KubernetesNode**](../models/KubernetesNode.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **k8s_nodepools_nodes_get**
> KubernetesNodes k8s_nodepools_nodes_get(k8s_cluster_id, nodepool_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

List Kubernetes nodes

List all the nodes, included in the specified Kubernetes node pool.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    try:
        # List Kubernetes nodes
        api_response = api_instance.k8s_nodepools_nodes_get(k8s_cluster_id, nodepool_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_nodepools_nodes_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**KubernetesNodes**](../models/KubernetesNodes.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **k8s_nodepools_nodes_replace_post**
> k8s_nodepools_nodes_replace_post(k8s_cluster_id, nodepool_id, node_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Recreate Kubernetes nodes

Recreate the specified Kubernetes node.  A new node is created and configured by Managed Kubernetes, based on the node pool template. Once the status is  \"Active\", all the pods are migrated from the faulty node, which is then deleted once empty. During this operation, the node pool will have an additional billable  \"Active\" node.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    node_id = 'node_id_example' # str | The unique ID of the Kubernetes node.
    try:
        # Recreate Kubernetes nodes
        api_instance.k8s_nodepools_nodes_replace_post(k8s_cluster_id, nodepool_id, node_id)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_nodepools_nodes_replace_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. |  |
| **node_id** | **str**| The unique ID of the Kubernetes node. |  |
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

# **k8s_nodepools_post**
> KubernetesNodePool k8s_nodepools_post(k8s_cluster_id, kubernetes_node_pool, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create Kubernetes node pools

Create a Kubernetes node pool inside the specified Kubernetes cluster.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    kubernetes_node_pool = ionoscloud.KubernetesNodePoolForPost() # KubernetesNodePoolForPost | The Kubernetes node pool to create.
    try:
        # Create Kubernetes node pools
        api_response = api_instance.k8s_nodepools_post(k8s_cluster_id, kubernetes_node_pool)
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_nodepools_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **kubernetes_node_pool** | [**KubernetesNodePoolForPost**](KubernetesNodePoolForPost.md)| The Kubernetes node pool to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**KubernetesNodePool**](../models/KubernetesNodePool.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **k8s_nodepools_put**
> KubernetesNodePool k8s_nodepools_put(k8s_cluster_id, nodepool_id, kubernetes_node_pool, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify Kubernetes node pools

Modify the specified Kubernetes node pool.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the Kubernetes node pool.
    kubernetes_node_pool = ionoscloud.KubernetesNodePoolForPut() # KubernetesNodePoolForPut | Details of the Kubernetes Node Pool
    try:
        # Modify Kubernetes node pools
        api_response = api_instance.k8s_nodepools_put(k8s_cluster_id, nodepool_id, kubernetes_node_pool)
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_nodepools_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **nodepool_id** | **str**| The unique ID of the Kubernetes node pool. |  |
| **kubernetes_node_pool** | [**KubernetesNodePoolForPut**](KubernetesNodePoolForPut.md)| Details of the Kubernetes Node Pool |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**KubernetesNodePool**](../models/KubernetesNodePool.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **k8s_post**
> KubernetesCluster k8s_post(kubernetes_cluster, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Create Kubernetes clusters

Create a Kubernetes cluster.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    kubernetes_cluster = ionoscloud.KubernetesClusterForPost() # KubernetesClusterForPost | The Kubernetes cluster to create.
    try:
        # Create Kubernetes clusters
        api_response = api_instance.k8s_post(kubernetes_cluster)
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **kubernetes_cluster** | [**KubernetesClusterForPost**](KubernetesClusterForPost.md)| The Kubernetes cluster to create. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**KubernetesCluster**](../models/KubernetesCluster.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **k8s_put**
> KubernetesCluster k8s_put(k8s_cluster_id, kubernetes_cluster, pretty=pretty, depth=depth, x_contract_number=x_contract_number)

Modify Kubernetes clusters

Modify the specified Kubernetes cluster.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    k8s_cluster_id = 'k8s_cluster_id_example' # str | The unique ID of the Kubernetes cluster.
    kubernetes_cluster = ionoscloud.KubernetesClusterForPut() # KubernetesClusterForPut | The modified Kubernetes cluster.
    try:
        # Modify Kubernetes clusters
        api_response = api_instance.k8s_put(k8s_cluster_id, kubernetes_cluster)
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **k8s_cluster_id** | **str**| The unique ID of the Kubernetes cluster. |  |
| **kubernetes_cluster** | [**KubernetesClusterForPut**](KubernetesClusterForPut.md)| The modified Kubernetes cluster. |  |
| **pretty** | **bool**| Controls whether the response is pretty-printed (with indentations and new lines). | [optional] [default to True] |
| **depth** | **int**| Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth&#x3D;0: Only direct properties are included; children (servers and other elements) are not included.  - depth&#x3D;1: Direct properties and children references are included.  - depth&#x3D;2: Direct properties and children properties are included.  - depth&#x3D;3: Direct properties and children properties and children&#39;s children are included.  - depth&#x3D;... and so on | [optional] [default to 0] |
| **x_contract_number** | **int**| Users with multiple contracts must provide the contract number, for which all API requests are to be executed. | [optional]  |

### Return type

[**KubernetesCluster**](../models/KubernetesCluster.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **k8s_versions_default_get**
> str k8s_versions_default_get()

Retrieve current default Kubernetes version

Retrieve current default Kubernetes version for clusters and nodepools.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    try:
        # Retrieve current default Kubernetes version
        api_response = api_instance.k8s_versions_default_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_versions_default_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **k8s_versions_get**
> list[str] k8s_versions_get()

List Kubernetes versions

List available Kubernetes versions.

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
    api_instance = ionoscloud.KubernetesApi(api_client)
    try:
        # List Kubernetes versions
        api_response = api_instance.k8s_versions_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling KubernetesApi.k8s_versions_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

