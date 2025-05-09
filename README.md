![CI](https://github.com/ionos-cloud/sdk-resources/workflows/[%20CI%20]%20CloudApi%20V6%20/%20Python/badge.svg)
[![Gitter](https://img.shields.io/gitter/room/ionos-cloud/sdk-general)](https://gitter.im/ionos-cloud/sdk-general)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ionos-cloud_sdk-python&metric=alert_status)](https://sonarcloud.io/summary?id=ionos-cloud_sdk-python)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=ionos-cloud_sdk-python&metric=bugs)](https://sonarcloud.io/summary/new_code?id=ionos-cloud_sdk-python)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ionos-cloud_sdk-python&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=ionos-cloud_sdk-python)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ionos-cloud_sdk-python&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=ionos-cloud_sdk-python)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ionos-cloud_sdk-python&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=ionos-cloud_sdk-python)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=ionos-cloud_sdk-python&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=ionos-cloud_sdk-python)
[![Release](https://img.shields.io/github/v/release/ionos-cloud/sdk-python.svg)](https://github.com/ionos-cloud/sdk-python/releases/latest)
[![Release Date](https://img.shields.io/github/release-date/ionos-cloud/sdk-python.svg)](https://github.com/ionos-cloud/sdk-python/releases/latest)

![Alt text](.github/IONOS.CLOUD.BLU.svg?raw=true "Title")


# Python API client for ionoscloud


IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool. 

 Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.

## Overview
The IONOS Cloud SDK for Python provides you with access to the IONOS Cloud API. The client library supports both simple and complex requests. It is designed for developers who are building applications in Python. The SDK for Python wraps the IONOS Cloud API. All API operations are performed over SSL and authenticated using your IONOS Cloud portal credentials. The API can be accessed within an instance running in IONOS Cloud or directly over the Internet from any application that can send an HTTPS request and receive an HTTPS response.


### Installation & Usage

**Requirements:**
- Python >= 3.5

### pip install

Since this package is hosted on [Pypi](https://pypi.org/) you can install it by using:

```bash
pip install ionoscloud
```

If the python package is hosted on a repository, you can install directly using:

```bash
pip install git+https://github.com/ionos-cloud/sdk-python.git
```

Note: you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ionos-cloud/sdk-python.git`

Then import the package:

```python
import ionoscloud
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```bash
python setup.py install --user
```

or `sudo python setup.py install` to install the package for all users

Then import the package:

```python
import ionoscloud
```

> **_NOTE:_**  The Python SDK does not support Python 2. It only supports Python >= 3.5.

### Authentication

All available server URLs are:

- *https://api.ionos.com/cloudapi/v6* - No description provided

By default, *https://api.ionos.com/cloudapi/v6* is used, however this can be overriden at authentication, either
by setting the `IONOS_API_URL` environment variable or by specifying the `host` parameter when
initializing the sdk client.

The username and password **or** the authentication token can be manually specified when initializing the SDK client:

```python
configuration = ionoscloud.Configuration(
                username='YOUR_USERNAME',
                password='YOUR_PASSWORD',
                token='YOUR_TOKEN',
                host='API_URL'
                )
client = ionoscloud.ApiClient(configuration)
```

Environment variables can also be used. This is an example of how one would do that:

```python
import os

configuration = ionoscloud.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                token=os.environ.get('IONOS_TOKEN'),
                host=os.environ.get('IONOS_API_URL'),
                )
client = ionoscloud.ApiClient(configuration)
```

**Warning**: Make sure to follow the Information Security Best Practices when using credentials within your code or storing them in a file.


### HTTP proxies

You can use http proxies by setting the following environment variables:
- `IONOS_HTTP_PROXY` - proxy URL
- `IONOS_HTTP_PROXY_HEADERS` - proxy headers

Each line in `IONOS_HTTP_PROXY_HEADERS` represents one header, where the header name and value is separated by a colon. Newline characters within a value need to be escaped. See this example:
```
Connection: Keep-Alive
User-Info: MyID
User-Group: my long\nheader value
```


### Depth

Many of the _List_ or _Get_ operations will accept an optional _depth_ argument. Setting this to a value between 0 and 5 affects the amount of data that is returned. The details returned vary depending on the resource being queried, but it generally follows this pattern. By default, the SDK sets the _depth_ argument to the maximum value.

| Depth | Description |
| :--- | :--- |
| 0 | Only direct properties are included. Children are not included. |
| 1 | Direct properties and children's references are returned. |
| 2 | Direct properties and children's properties are returned. |
| 3 | Direct properties, children's properties, and descendants' references are returned. |
| 4 | Direct properties, children's properties, and descendants' properties are returned. |
| 5 | Returns all available properties. |

### Pretty

The operations will also accept an optional _pretty_ argument. Setting this to a value of `true` or `false` controls whether the response is pretty-printed \(with indentation and new lines\). By default, the SDK sets the _pretty_ argument to `true`.

### Changing the base URL

Base URL for the HTTP operation can be changed in the following way:

```python
import os

configuration = ionoscloud.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                host=os.environ.get('IONOS_API_URL'),
                server_index=None,
                )
client = ionoscloud.ApiClient(configuration)
```

## Certificate pinning:

You can enable certificate pinning if you want to bypass the normal certificate checking procedure,
by doing the following:

Set env variable IONOS_PINNED_CERT=<insert_sha256_public_fingerprint_here>

You can get the sha256 fingerprint most easily from the browser by inspecting the certificate.


## Documentation for API Endpoints

All URIs are relative to *https://api.ionos.com/cloudapi/v6*
<details >
    <summary title="Click to toggle">API Endpoints table</summary>


| Class | Method | HTTP request | Description |
| ------------- | ------------- | ------------- | ------------- |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_delete**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_delete) | **DELETE** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Delete an Application Load Balancer by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_find_by_application_load_balancer_id**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_find_by_application_load_balancer_id) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Get an Application Load Balancer by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_flowlogs_delete**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Delete an ALB Flow Log by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Get an ALB Flow Log by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_flowlogs_get**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_get) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs | Get ALB Flow Logs |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_flowlogs_patch**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Partially Modify an ALB Flow Log by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_flowlogs_post**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_post) | **POST** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs | Create an ALB Flow Log |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_flowlogs_put**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_flowlogs_put) | **PUT** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId} | Modify an ALB Flow Log by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_forwardingrules_delete**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_delete) | **DELETE** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Delete an ALB Forwarding Rule by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Get an ALB Forwarding Rule by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_forwardingrules_get**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_get) | **GET** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules | Get ALB Forwarding Rules |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_forwardingrules_patch**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_patch) | **PATCH** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Partially modify an ALB Forwarding Rule by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_forwardingrules_post**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_post) | **POST** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules | Create an ALB Forwarding Rule |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_forwardingrules_put**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_forwardingrules_put) | **PUT** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId} | Modify an ALB Forwarding Rule by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_get**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_get) | **GET** /datacenters/{datacenterId}/applicationloadbalancers | Get Application Load Balancers |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_patch**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_patch) | **PATCH** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Partially Modify an Application Load Balancer by ID |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_post**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_post) | **POST** /datacenters/{datacenterId}/applicationloadbalancers | Create an Application Load Balancer |
| ApplicationLoadBalancersApi | [**datacenters_applicationloadbalancers_put**](docs/api/ApplicationLoadBalancersApi.md#datacenters_applicationloadbalancers_put) | **PUT** /datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId} | Modify an Application Load Balancer by ID |
| BackupUnitsApi | [**backupunits_delete**](docs/api/BackupUnitsApi.md#backupunits_delete) | **DELETE** /backupunits/{backupunitId} | Delete backup units |
| BackupUnitsApi | [**backupunits_find_by_id**](docs/api/BackupUnitsApi.md#backupunits_find_by_id) | **GET** /backupunits/{backupunitId} | Retrieve backup units |
| BackupUnitsApi | [**backupunits_get**](docs/api/BackupUnitsApi.md#backupunits_get) | **GET** /backupunits | List backup units |
| BackupUnitsApi | [**backupunits_patch**](docs/api/BackupUnitsApi.md#backupunits_patch) | **PATCH** /backupunits/{backupunitId} | Partially modify backup units |
| BackupUnitsApi | [**backupunits_post**](docs/api/BackupUnitsApi.md#backupunits_post) | **POST** /backupunits | Create backup units |
| BackupUnitsApi | [**backupunits_put**](docs/api/BackupUnitsApi.md#backupunits_put) | **PUT** /backupunits/{backupunitId} | Modify backup units |
| BackupUnitsApi | [**backupunits_ssourl_get**](docs/api/BackupUnitsApi.md#backupunits_ssourl_get) | **GET** /backupunits/{backupunitId}/ssourl | Retrieve BU single sign-on URLs |
| ContractResourcesApi | [**contracts_get**](docs/api/ContractResourcesApi.md#contracts_get) | **GET** /contracts | Get Contract Information |
| DataCentersApi | [**datacenters_delete**](docs/api/DataCentersApi.md#datacenters_delete) | **DELETE** /datacenters/{datacenterId} | Delete data centers |
| DataCentersApi | [**datacenters_find_by_id**](docs/api/DataCentersApi.md#datacenters_find_by_id) | **GET** /datacenters/{datacenterId} | Retrieve data centers |
| DataCentersApi | [**datacenters_get**](docs/api/DataCentersApi.md#datacenters_get) | **GET** /datacenters | List your data centers |
| DataCentersApi | [**datacenters_patch**](docs/api/DataCentersApi.md#datacenters_patch) | **PATCH** /datacenters/{datacenterId} | Partially modify a Data Center by ID |
| DataCentersApi | [**datacenters_post**](docs/api/DataCentersApi.md#datacenters_post) | **POST** /datacenters | Create a Data Center |
| DataCentersApi | [**datacenters_put**](docs/api/DataCentersApi.md#datacenters_put) | **PUT** /datacenters/{datacenterId} | Modify a Data Center by ID |
| FirewallRulesApi | [**datacenters_servers_nics_firewallrules_delete**](docs/api/FirewallRulesApi.md#datacenters_servers_nics_firewallrules_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Delete firewall rules |
| FirewallRulesApi | [**datacenters_servers_nics_firewallrules_find_by_id**](docs/api/FirewallRulesApi.md#datacenters_servers_nics_firewallrules_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Retrieve firewall rules |
| FirewallRulesApi | [**datacenters_servers_nics_firewallrules_get**](docs/api/FirewallRulesApi.md#datacenters_servers_nics_firewallrules_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules | List firewall rules |
| FirewallRulesApi | [**datacenters_servers_nics_firewallrules_patch**](docs/api/FirewallRulesApi.md#datacenters_servers_nics_firewallrules_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Partially modify firewall rules |
| FirewallRulesApi | [**datacenters_servers_nics_firewallrules_post**](docs/api/FirewallRulesApi.md#datacenters_servers_nics_firewallrules_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules | Create a Firewall Rule |
| FirewallRulesApi | [**datacenters_servers_nics_firewallrules_put**](docs/api/FirewallRulesApi.md#datacenters_servers_nics_firewallrules_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/firewallrules/{firewallruleId} | Modify a Firewall Rule |
| FlowLogsApi | [**datacenters_servers_nics_flowlogs_delete**](docs/api/FlowLogsApi.md#datacenters_servers_nics_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs/{flowlogId} | Delete Flow Logs |
| FlowLogsApi | [**datacenters_servers_nics_flowlogs_find_by_id**](docs/api/FlowLogsApi.md#datacenters_servers_nics_flowlogs_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs/{flowlogId} | Retrieve Flow Logs |
| FlowLogsApi | [**datacenters_servers_nics_flowlogs_get**](docs/api/FlowLogsApi.md#datacenters_servers_nics_flowlogs_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs | List Flow Logs |
| FlowLogsApi | [**datacenters_servers_nics_flowlogs_patch**](docs/api/FlowLogsApi.md#datacenters_servers_nics_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs/{flowlogId} | Partially modify Flow Logs |
| FlowLogsApi | [**datacenters_servers_nics_flowlogs_post**](docs/api/FlowLogsApi.md#datacenters_servers_nics_flowlogs_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs | Create a Flow Log |
| FlowLogsApi | [**datacenters_servers_nics_flowlogs_put**](docs/api/FlowLogsApi.md#datacenters_servers_nics_flowlogs_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/flowlogs/{flowlogId} | Modify Flow Logs |
| IPBlocksApi | [**ipblocks_delete**](docs/api/IPBlocksApi.md#ipblocks_delete) | **DELETE** /ipblocks/{ipblockId} | Delete IP blocks |
| IPBlocksApi | [**ipblocks_find_by_id**](docs/api/IPBlocksApi.md#ipblocks_find_by_id) | **GET** /ipblocks/{ipblockId} | Retrieve IP blocks |
| IPBlocksApi | [**ipblocks_get**](docs/api/IPBlocksApi.md#ipblocks_get) | **GET** /ipblocks | List IP blocks  |
| IPBlocksApi | [**ipblocks_patch**](docs/api/IPBlocksApi.md#ipblocks_patch) | **PATCH** /ipblocks/{ipblockId} | Partially modify IP blocks |
| IPBlocksApi | [**ipblocks_post**](docs/api/IPBlocksApi.md#ipblocks_post) | **POST** /ipblocks | Reserve a IP Block |
| IPBlocksApi | [**ipblocks_put**](docs/api/IPBlocksApi.md#ipblocks_put) | **PUT** /ipblocks/{ipblockId} | Modify a IP Block by ID |
| ImagesApi | [**images_delete**](docs/api/ImagesApi.md#images_delete) | **DELETE** /images/{imageId} | Delete images |
| ImagesApi | [**images_find_by_id**](docs/api/ImagesApi.md#images_find_by_id) | **GET** /images/{imageId} | Retrieve images |
| ImagesApi | [**images_get**](docs/api/ImagesApi.md#images_get) | **GET** /images | List images |
| ImagesApi | [**images_patch**](docs/api/ImagesApi.md#images_patch) | **PATCH** /images/{imageId} | Partially modify images |
| ImagesApi | [**images_put**](docs/api/ImagesApi.md#images_put) | **PUT** /images/{imageId} | Modify an Image by ID |
| KubernetesApi | [**k8s_delete**](docs/api/KubernetesApi.md#k8s_delete) | **DELETE** /k8s/{k8sClusterId} | Delete a Kubernetes Cluster by ID |
| KubernetesApi | [**k8s_find_by_cluster_id**](docs/api/KubernetesApi.md#k8s_find_by_cluster_id) | **GET** /k8s/{k8sClusterId} | Get a Kubernetes Cluster by ID |
| KubernetesApi | [**k8s_get**](docs/api/KubernetesApi.md#k8s_get) | **GET** /k8s | Get Kubernetes Clusters |
| KubernetesApi | [**k8s_kubeconfig_get**](docs/api/KubernetesApi.md#k8s_kubeconfig_get) | **GET** /k8s/{k8sClusterId}/kubeconfig | Get Kubernetes Configuration File |
| KubernetesApi | [**k8s_nodepools_delete**](docs/api/KubernetesApi.md#k8s_nodepools_delete) | **DELETE** /k8s/{k8sClusterId}/nodepools/{nodepoolId} | Delete a Kubernetes Node Pool by ID |
| KubernetesApi | [**k8s_nodepools_find_by_id**](docs/api/KubernetesApi.md#k8s_nodepools_find_by_id) | **GET** /k8s/{k8sClusterId}/nodepools/{nodepoolId} | Get a Kubernetes Node Pool by ID |
| KubernetesApi | [**k8s_nodepools_get**](docs/api/KubernetesApi.md#k8s_nodepools_get) | **GET** /k8s/{k8sClusterId}/nodepools | Get Kubernetes Node Pools |
| KubernetesApi | [**k8s_nodepools_nodes_delete**](docs/api/KubernetesApi.md#k8s_nodepools_nodes_delete) | **DELETE** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId} | Delete a Kubernetes Node by ID |
| KubernetesApi | [**k8s_nodepools_nodes_find_by_id**](docs/api/KubernetesApi.md#k8s_nodepools_nodes_find_by_id) | **GET** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId} | Get Kubernetes Node by ID |
| KubernetesApi | [**k8s_nodepools_nodes_get**](docs/api/KubernetesApi.md#k8s_nodepools_nodes_get) | **GET** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes | Get Kubernetes Nodes |
| KubernetesApi | [**k8s_nodepools_nodes_replace_post**](docs/api/KubernetesApi.md#k8s_nodepools_nodes_replace_post) | **POST** /k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId}/replace | Recreate a Kubernetes Node by ID |
| KubernetesApi | [**k8s_nodepools_post**](docs/api/KubernetesApi.md#k8s_nodepools_post) | **POST** /k8s/{k8sClusterId}/nodepools | Create a Kubernetes Node Pool |
| KubernetesApi | [**k8s_nodepools_put**](docs/api/KubernetesApi.md#k8s_nodepools_put) | **PUT** /k8s/{k8sClusterId}/nodepools/{nodepoolId} | Modify a Kubernetes Node Pool by ID |
| KubernetesApi | [**k8s_post**](docs/api/KubernetesApi.md#k8s_post) | **POST** /k8s | Create a Kubernetes Cluster |
| KubernetesApi | [**k8s_put**](docs/api/KubernetesApi.md#k8s_put) | **PUT** /k8s/{k8sClusterId} | Modify a Kubernetes Cluster by ID |
| KubernetesApi | [**k8s_versions_default_get**](docs/api/KubernetesApi.md#k8s_versions_default_get) | **GET** /k8s/versions/default | Get Default Kubernetes Version |
| KubernetesApi | [**k8s_versions_get**](docs/api/KubernetesApi.md#k8s_versions_get) | **GET** /k8s/versions | Get Kubernetes Versions |
| LANsApi | [**datacenters_lans_delete**](docs/api/LANsApi.md#datacenters_lans_delete) | **DELETE** /datacenters/{datacenterId}/lans/{lanId} | Delete LANs |
| LANsApi | [**datacenters_lans_find_by_id**](docs/api/LANsApi.md#datacenters_lans_find_by_id) | **GET** /datacenters/{datacenterId}/lans/{lanId} | Retrieve LANs |
| LANsApi | [**datacenters_lans_get**](docs/api/LANsApi.md#datacenters_lans_get) | **GET** /datacenters/{datacenterId}/lans | List LANs |
| LANsApi | [**datacenters_lans_nics_find_by_id**](docs/api/LANsApi.md#datacenters_lans_nics_find_by_id) | **GET** /datacenters/{datacenterId}/lans/{lanId}/nics/{nicId} | Retrieve attached NICs |
| LANsApi | [**datacenters_lans_nics_get**](docs/api/LANsApi.md#datacenters_lans_nics_get) | **GET** /datacenters/{datacenterId}/lans/{lanId}/nics | List LAN members |
| LANsApi | [**datacenters_lans_nics_post**](docs/api/LANsApi.md#datacenters_lans_nics_post) | **POST** /datacenters/{datacenterId}/lans/{lanId}/nics | Attach NICs |
| LANsApi | [**datacenters_lans_patch**](docs/api/LANsApi.md#datacenters_lans_patch) | **PATCH** /datacenters/{datacenterId}/lans/{lanId} | Partially modify LANs |
| LANsApi | [**datacenters_lans_post**](docs/api/LANsApi.md#datacenters_lans_post) | **POST** /datacenters/{datacenterId}/lans | Create LANs |
| LANsApi | [**datacenters_lans_put**](docs/api/LANsApi.md#datacenters_lans_put) | **PUT** /datacenters/{datacenterId}/lans/{lanId} | Modify LANs |
| LabelsApi | [**datacenters_labels_delete**](docs/api/LabelsApi.md#datacenters_labels_delete) | **DELETE** /datacenters/{datacenterId}/labels/{key} | Delete data center labels |
| LabelsApi | [**datacenters_labels_find_by_key**](docs/api/LabelsApi.md#datacenters_labels_find_by_key) | **GET** /datacenters/{datacenterId}/labels/{key} | Retrieve data center labels |
| LabelsApi | [**datacenters_labels_get**](docs/api/LabelsApi.md#datacenters_labels_get) | **GET** /datacenters/{datacenterId}/labels | List data center labels |
| LabelsApi | [**datacenters_labels_post**](docs/api/LabelsApi.md#datacenters_labels_post) | **POST** /datacenters/{datacenterId}/labels | Create a Data Center Label |
| LabelsApi | [**datacenters_labels_put**](docs/api/LabelsApi.md#datacenters_labels_put) | **PUT** /datacenters/{datacenterId}/labels/{key} | Modify a Data Center Label by Key |
| LabelsApi | [**datacenters_servers_labels_delete**](docs/api/LabelsApi.md#datacenters_servers_labels_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Delete server labels |
| LabelsApi | [**datacenters_servers_labels_find_by_key**](docs/api/LabelsApi.md#datacenters_servers_labels_find_by_key) | **GET** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Retrieve server labels |
| LabelsApi | [**datacenters_servers_labels_get**](docs/api/LabelsApi.md#datacenters_servers_labels_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/labels | List server labels |
| LabelsApi | [**datacenters_servers_labels_post**](docs/api/LabelsApi.md#datacenters_servers_labels_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/labels | Create a Server Label |
| LabelsApi | [**datacenters_servers_labels_put**](docs/api/LabelsApi.md#datacenters_servers_labels_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Modify a Server Label |
| LabelsApi | [**datacenters_volumes_labels_delete**](docs/api/LabelsApi.md#datacenters_volumes_labels_delete) | **DELETE** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Delete volume labels |
| LabelsApi | [**datacenters_volumes_labels_find_by_key**](docs/api/LabelsApi.md#datacenters_volumes_labels_find_by_key) | **GET** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Retrieve volume labels |
| LabelsApi | [**datacenters_volumes_labels_get**](docs/api/LabelsApi.md#datacenters_volumes_labels_get) | **GET** /datacenters/{datacenterId}/volumes/{volumeId}/labels | List volume labels |
| LabelsApi | [**datacenters_volumes_labels_post**](docs/api/LabelsApi.md#datacenters_volumes_labels_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/labels | Create a Volume Label |
| LabelsApi | [**datacenters_volumes_labels_put**](docs/api/LabelsApi.md#datacenters_volumes_labels_put) | **PUT** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Modify a Volume Label |
| LabelsApi | [**images_labels_delete**](docs/api/LabelsApi.md#images_labels_delete) | **DELETE** /images/{imageId}/labels/{key} | Delete image label |
| LabelsApi | [**images_labels_find_by_key**](docs/api/LabelsApi.md#images_labels_find_by_key) | **GET** /images/{imageId}/labels/{key} | Retrieve image labels |
| LabelsApi | [**images_labels_get**](docs/api/LabelsApi.md#images_labels_get) | **GET** /images/{imageId}/labels | List image labels |
| LabelsApi | [**images_labels_post**](docs/api/LabelsApi.md#images_labels_post) | **POST** /images/{imageId}/labels | Create an Image Label |
| LabelsApi | [**images_labels_put**](docs/api/LabelsApi.md#images_labels_put) | **PUT** /images/{imageId}/labels/{key} | Modify an Image Label by Key |
| LabelsApi | [**ipblocks_labels_delete**](docs/api/LabelsApi.md#ipblocks_labels_delete) | **DELETE** /ipblocks/{ipblockId}/labels/{key} | Delete IP block labels |
| LabelsApi | [**ipblocks_labels_find_by_key**](docs/api/LabelsApi.md#ipblocks_labels_find_by_key) | **GET** /ipblocks/{ipblockId}/labels/{key} | Retrieve IP block labels |
| LabelsApi | [**ipblocks_labels_get**](docs/api/LabelsApi.md#ipblocks_labels_get) | **GET** /ipblocks/{ipblockId}/labels | List IP block labels |
| LabelsApi | [**ipblocks_labels_post**](docs/api/LabelsApi.md#ipblocks_labels_post) | **POST** /ipblocks/{ipblockId}/labels | Create IP block labels |
| LabelsApi | [**ipblocks_labels_put**](docs/api/LabelsApi.md#ipblocks_labels_put) | **PUT** /ipblocks/{ipblockId}/labels/{key} | Modify a IP Block Label by ID |
| LabelsApi | [**labels_find_by_urn**](docs/api/LabelsApi.md#labels_find_by_urn) | **GET** /labels/{labelurn} | Retrieve labels by URN |
| LabelsApi | [**labels_get**](docs/api/LabelsApi.md#labels_get) | **GET** /labels | List labels  |
| LabelsApi | [**snapshots_labels_delete**](docs/api/LabelsApi.md#snapshots_labels_delete) | **DELETE** /snapshots/{snapshotId}/labels/{key} | Delete snapshot labels |
| LabelsApi | [**snapshots_labels_find_by_key**](docs/api/LabelsApi.md#snapshots_labels_find_by_key) | **GET** /snapshots/{snapshotId}/labels/{key} | Retrieve snapshot labels |
| LabelsApi | [**snapshots_labels_get**](docs/api/LabelsApi.md#snapshots_labels_get) | **GET** /snapshots/{snapshotId}/labels | List snapshot labels |
| LabelsApi | [**snapshots_labels_post**](docs/api/LabelsApi.md#snapshots_labels_post) | **POST** /snapshots/{snapshotId}/labels | Create a Snapshot Label |
| LabelsApi | [**snapshots_labels_put**](docs/api/LabelsApi.md#snapshots_labels_put) | **PUT** /snapshots/{snapshotId}/labels/{key} | Modify a Snapshot Label by ID |
| LoadBalancersApi | [**datacenters_loadbalancers_balancednics_delete**](docs/api/LoadBalancersApi.md#datacenters_loadbalancers_balancednics_delete) | **DELETE** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics/{nicId} | Detach balanced NICs |
| LoadBalancersApi | [**datacenters_loadbalancers_balancednics_find_by_nic_id**](docs/api/LoadBalancersApi.md#datacenters_loadbalancers_balancednics_find_by_nic_id) | **GET** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics/{nicId} | Retrieve balanced NICs |
| LoadBalancersApi | [**datacenters_loadbalancers_balancednics_get**](docs/api/LoadBalancersApi.md#datacenters_loadbalancers_balancednics_get) | **GET** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics | List balanced NICs |
| LoadBalancersApi | [**datacenters_loadbalancers_balancednics_post**](docs/api/LoadBalancersApi.md#datacenters_loadbalancers_balancednics_post) | **POST** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId}/balancednics | Attach balanced NICs |
| LoadBalancersApi | [**datacenters_loadbalancers_delete**](docs/api/LoadBalancersApi.md#datacenters_loadbalancers_delete) | **DELETE** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Delete Load Balancers |
| LoadBalancersApi | [**datacenters_loadbalancers_find_by_id**](docs/api/LoadBalancersApi.md#datacenters_loadbalancers_find_by_id) | **GET** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Retrieve Load Balancers |
| LoadBalancersApi | [**datacenters_loadbalancers_get**](docs/api/LoadBalancersApi.md#datacenters_loadbalancers_get) | **GET** /datacenters/{datacenterId}/loadbalancers | List Load Balancers |
| LoadBalancersApi | [**datacenters_loadbalancers_patch**](docs/api/LoadBalancersApi.md#datacenters_loadbalancers_patch) | **PATCH** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Partially modify Load Balancers |
| LoadBalancersApi | [**datacenters_loadbalancers_post**](docs/api/LoadBalancersApi.md#datacenters_loadbalancers_post) | **POST** /datacenters/{datacenterId}/loadbalancers | Create a Load Balancer |
| LoadBalancersApi | [**datacenters_loadbalancers_put**](docs/api/LoadBalancersApi.md#datacenters_loadbalancers_put) | **PUT** /datacenters/{datacenterId}/loadbalancers/{loadbalancerId} | Modify a Load Balancer by ID |
| LocationsApi | [**locations_find_by_region_id**](docs/api/LocationsApi.md#locations_find_by_region_id) | **GET** /locations/{regionId} | Get Locations within a Region |
| LocationsApi | [**locations_find_by_region_id_and_id**](docs/api/LocationsApi.md#locations_find_by_region_id_and_id) | **GET** /locations/{regionId}/{locationId} | Get Location by ID |
| LocationsApi | [**locations_get**](docs/api/LocationsApi.md#locations_get) | **GET** /locations | Get Locations |
| NATGatewaysApi | [**datacenters_natgateways_delete**](docs/api/NATGatewaysApi.md#datacenters_natgateways_delete) | **DELETE** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Delete NAT Gateways |
| NATGatewaysApi | [**datacenters_natgateways_find_by_nat_gateway_id**](docs/api/NATGatewaysApi.md#datacenters_natgateways_find_by_nat_gateway_id) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Retrieve NAT Gateways |
| NATGatewaysApi | [**datacenters_natgateways_flowlogs_delete**](docs/api/NATGatewaysApi.md#datacenters_natgateways_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Delete NAT Gateway Flow Logs |
| NATGatewaysApi | [**datacenters_natgateways_flowlogs_find_by_flow_log_id**](docs/api/NATGatewaysApi.md#datacenters_natgateways_flowlogs_find_by_flow_log_id) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Retrieve NAT Gateway Flow Logs |
| NATGatewaysApi | [**datacenters_natgateways_flowlogs_get**](docs/api/NATGatewaysApi.md#datacenters_natgateways_flowlogs_get) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs | List NAT Gateway Flow Logs |
| NATGatewaysApi | [**datacenters_natgateways_flowlogs_patch**](docs/api/NATGatewaysApi.md#datacenters_natgateways_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Partially modify NAT Gateway Flow Logs |
| NATGatewaysApi | [**datacenters_natgateways_flowlogs_post**](docs/api/NATGatewaysApi.md#datacenters_natgateways_flowlogs_post) | **POST** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs | Create a NAT Gateway Flow Log |
| NATGatewaysApi | [**datacenters_natgateways_flowlogs_put**](docs/api/NATGatewaysApi.md#datacenters_natgateways_flowlogs_put) | **PUT** /datacenters/{datacenterId}/natgateways/{natGatewayId}/flowlogs/{flowLogId} | Modify NAT Gateway Flow Logs |
| NATGatewaysApi | [**datacenters_natgateways_get**](docs/api/NATGatewaysApi.md#datacenters_natgateways_get) | **GET** /datacenters/{datacenterId}/natgateways | List NAT Gateways |
| NATGatewaysApi | [**datacenters_natgateways_patch**](docs/api/NATGatewaysApi.md#datacenters_natgateways_patch) | **PATCH** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Partially modify NAT Gateways |
| NATGatewaysApi | [**datacenters_natgateways_post**](docs/api/NATGatewaysApi.md#datacenters_natgateways_post) | **POST** /datacenters/{datacenterId}/natgateways | Create a NAT Gateway |
| NATGatewaysApi | [**datacenters_natgateways_put**](docs/api/NATGatewaysApi.md#datacenters_natgateways_put) | **PUT** /datacenters/{datacenterId}/natgateways/{natGatewayId} | Modify NAT Gateways |
| NATGatewaysApi | [**datacenters_natgateways_rules_delete**](docs/api/NATGatewaysApi.md#datacenters_natgateways_rules_delete) | **DELETE** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Delete NAT Gateway rules |
| NATGatewaysApi | [**datacenters_natgateways_rules_find_by_nat_gateway_rule_id**](docs/api/NATGatewaysApi.md#datacenters_natgateways_rules_find_by_nat_gateway_rule_id) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Retrieve NAT Gateway rules |
| NATGatewaysApi | [**datacenters_natgateways_rules_get**](docs/api/NATGatewaysApi.md#datacenters_natgateways_rules_get) | **GET** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules | List NAT Gateway rules |
| NATGatewaysApi | [**datacenters_natgateways_rules_patch**](docs/api/NATGatewaysApi.md#datacenters_natgateways_rules_patch) | **PATCH** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Partially Modify a NAT Gateway Rule by ID |
| NATGatewaysApi | [**datacenters_natgateways_rules_post**](docs/api/NATGatewaysApi.md#datacenters_natgateways_rules_post) | **POST** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules | Create a NAT Gateway Rule |
| NATGatewaysApi | [**datacenters_natgateways_rules_put**](docs/api/NATGatewaysApi.md#datacenters_natgateways_rules_put) | **PUT** /datacenters/{datacenterId}/natgateways/{natGatewayId}/rules/{natGatewayRuleId} | Modify a NAT Gateway Rule by ID |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_delete**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_delete) | **DELETE** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Delete Network Load Balancers |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_find_by_network_load_balancer_id**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_find_by_network_load_balancer_id) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Retrieve Network Load Balancers |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_flowlogs_delete**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_delete) | **DELETE** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Delete NLB Flow Logs |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Retrieve NLB Flow Logs |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_flowlogs_get**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_get) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs | List NLB Flow Logs |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_flowlogs_patch**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_patch) | **PATCH** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Partially modify NLB Flow Logs |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_flowlogs_post**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_post) | **POST** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs | Create a NLB Flow Log |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_flowlogs_put**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_flowlogs_put) | **PUT** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId} | Modify NLB Flow Logs |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_forwardingrules_delete**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_delete) | **DELETE** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Delete NLB forwarding rules |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Retrieve NLB forwarding rules |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_forwardingrules_get**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_get) | **GET** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules | List NLB forwarding rules |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_forwardingrules_patch**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_patch) | **PATCH** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Partially modify NLB forwarding rules |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_forwardingrules_post**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_post) | **POST** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules | Create a NLB Forwarding Rule |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_forwardingrules_put**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_forwardingrules_put) | **PUT** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId} | Modify NLB forwarding rules |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_get**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_get) | **GET** /datacenters/{datacenterId}/networkloadbalancers | List Network Load Balancers |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_patch**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_patch) | **PATCH** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Partially modify Network Load Balancers |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_post**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_post) | **POST** /datacenters/{datacenterId}/networkloadbalancers | Create a Network Load Balancer |
| NetworkLoadBalancersApi | [**datacenters_networkloadbalancers_put**](docs/api/NetworkLoadBalancersApi.md#datacenters_networkloadbalancers_put) | **PUT** /datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId} | Modify Network Load Balancers |
| NetworkInterfacesApi | [**datacenters_servers_nics_delete**](docs/api/NetworkInterfacesApi.md#datacenters_servers_nics_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Delete NICs |
| NetworkInterfacesApi | [**datacenters_servers_nics_find_by_id**](docs/api/NetworkInterfacesApi.md#datacenters_servers_nics_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Retrieve NICs |
| NetworkInterfacesApi | [**datacenters_servers_nics_get**](docs/api/NetworkInterfacesApi.md#datacenters_servers_nics_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/nics | List NICs |
| NetworkInterfacesApi | [**datacenters_servers_nics_patch**](docs/api/NetworkInterfacesApi.md#datacenters_servers_nics_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Partially modify NICs |
| NetworkInterfacesApi | [**datacenters_servers_nics_post**](docs/api/NetworkInterfacesApi.md#datacenters_servers_nics_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/nics | Create a NIC |
| NetworkInterfacesApi | [**datacenters_servers_nics_put**](docs/api/NetworkInterfacesApi.md#datacenters_servers_nics_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId} | Modify NICs |
| PrivateCrossConnectsApi | [**pccs_delete**](docs/api/PrivateCrossConnectsApi.md#pccs_delete) | **DELETE** /pccs/{pccId} | Delete Private Cross-Connects |
| PrivateCrossConnectsApi | [**pccs_find_by_id**](docs/api/PrivateCrossConnectsApi.md#pccs_find_by_id) | **GET** /pccs/{pccId} | Retrieve a Cross Connect |
| PrivateCrossConnectsApi | [**pccs_get**](docs/api/PrivateCrossConnectsApi.md#pccs_get) | **GET** /pccs | List Private Cross-Connects |
| PrivateCrossConnectsApi | [**pccs_patch**](docs/api/PrivateCrossConnectsApi.md#pccs_patch) | **PATCH** /pccs/{pccId} | Partially modify a Private Cross-Connects |
| PrivateCrossConnectsApi | [**pccs_post**](docs/api/PrivateCrossConnectsApi.md#pccs_post) | **POST** /pccs | Create a Cross Connect |
| RequestsApi | [**requests_find_by_id**](docs/api/RequestsApi.md#requests_find_by_id) | **GET** /requests/{requestId} | Retrieve requests |
| RequestsApi | [**requests_get**](docs/api/RequestsApi.md#requests_get) | **GET** /requests | List requests |
| RequestsApi | [**requests_status_get**](docs/api/RequestsApi.md#requests_status_get) | **GET** /requests/{requestId}/status | Retrieve request status |
| SecurityGroupsApi | [**datacenters_securitygroups_delete**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_delete) | **DELETE** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Delete a Security Group |
| SecurityGroupsApi | [**datacenters_securitygroups_find_by_id**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_find_by_id) | **GET** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Retrieve a Security Group |
| SecurityGroupsApi | [**datacenters_securitygroups_firewallrules_delete**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_firewallrules_delete) | **DELETE** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Remove a Firewall Rule from a Security Group |
| SecurityGroupsApi | [**datacenters_securitygroups_firewallrules_post**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_firewallrules_post) | **POST** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules | Create Firewall rule to a Security Group |
| SecurityGroupsApi | [**datacenters_securitygroups_get**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_get) | **GET** /datacenters/{datacenterId}/securitygroups | List Security Groups |
| SecurityGroupsApi | [**datacenters_securitygroups_patch**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_patch) | **PATCH** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Partially modify Security Group |
| SecurityGroupsApi | [**datacenters_securitygroups_post**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_post) | **POST** /datacenters/{datacenterId}/securitygroups | Create a Security Group |
| SecurityGroupsApi | [**datacenters_securitygroups_put**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_put) | **PUT** /datacenters/{datacenterId}/securitygroups/{securityGroupId} | Modify Security Group |
| SecurityGroupsApi | [**datacenters_securitygroups_rules_find_by_id**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_rules_find_by_id) | **GET** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Retrieve security group rule by id |
| SecurityGroupsApi | [**datacenters_securitygroups_rules_get**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_rules_get) | **GET** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules | List Security Group rules |
| SecurityGroupsApi | [**datacenters_securitygroups_rules_patch**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_rules_patch) | **PATCH** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Partially modify Security Group Rules |
| SecurityGroupsApi | [**datacenters_securitygroups_rules_put**](docs/api/SecurityGroupsApi.md#datacenters_securitygroups_rules_put) | **PUT** /datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId} | Modify a Security Group Rule |
| SecurityGroupsApi | [**datacenters_servers_nics_securitygroups_put**](docs/api/SecurityGroupsApi.md#datacenters_servers_nics_securitygroups_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/securitygroups | Attach a list of Security Groups to a NIC |
| SecurityGroupsApi | [**datacenters_servers_securitygroups_put**](docs/api/SecurityGroupsApi.md#datacenters_servers_securitygroups_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/securitygroups | Attach a list of Security Groups to a Server |
| ServersApi | [**datacenters_servers_cdroms_delete**](docs/api/ServersApi.md#datacenters_servers_cdroms_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/cdroms/{cdromId} | Detach a CD-ROM by ID |
| ServersApi | [**datacenters_servers_cdroms_find_by_id**](docs/api/ServersApi.md#datacenters_servers_cdroms_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/cdroms/{cdromId} | Get Attached CD-ROM by ID |
| ServersApi | [**datacenters_servers_cdroms_get**](docs/api/ServersApi.md#datacenters_servers_cdroms_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/cdroms | Get Attached CD-ROMs  |
| ServersApi | [**datacenters_servers_cdroms_post**](docs/api/ServersApi.md#datacenters_servers_cdroms_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/cdroms | Attach a CD-ROM |
| ServersApi | [**datacenters_servers_delete**](docs/api/ServersApi.md#datacenters_servers_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId} | Delete servers |
| ServersApi | [**datacenters_servers_find_by_id**](docs/api/ServersApi.md#datacenters_servers_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId} | Retrieve servers by ID |
| ServersApi | [**datacenters_servers_get**](docs/api/ServersApi.md#datacenters_servers_get) | **GET** /datacenters/{datacenterId}/servers | List servers  |
| ServersApi | [**datacenters_servers_patch**](docs/api/ServersApi.md#datacenters_servers_patch) | **PATCH** /datacenters/{datacenterId}/servers/{serverId} | Partially modify servers |
| ServersApi | [**datacenters_servers_post**](docs/api/ServersApi.md#datacenters_servers_post) | **POST** /datacenters/{datacenterId}/servers | Create a Server |
| ServersApi | [**datacenters_servers_put**](docs/api/ServersApi.md#datacenters_servers_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId} | Modify a Server by ID |
| ServersApi | [**datacenters_servers_reboot_post**](docs/api/ServersApi.md#datacenters_servers_reboot_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/reboot | Reboot servers |
| ServersApi | [**datacenters_servers_remote_console_get**](docs/api/ServersApi.md#datacenters_servers_remote_console_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/remoteconsole | Get Remote Console link |
| ServersApi | [**datacenters_servers_resume_post**](docs/api/ServersApi.md#datacenters_servers_resume_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/resume | Resume a Cube Server by ID |
| ServersApi | [**datacenters_servers_start_post**](docs/api/ServersApi.md#datacenters_servers_start_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/start | Start an Enterprise Server by ID |
| ServersApi | [**datacenters_servers_stop_post**](docs/api/ServersApi.md#datacenters_servers_stop_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/stop | Stop an Enterprise Server by ID |
| ServersApi | [**datacenters_servers_suspend_post**](docs/api/ServersApi.md#datacenters_servers_suspend_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/suspend | Suspend a Cube Server by ID |
| ServersApi | [**datacenters_servers_token_get**](docs/api/ServersApi.md#datacenters_servers_token_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/token | Get JSON Web Token |
| ServersApi | [**datacenters_servers_upgrade_post**](docs/api/ServersApi.md#datacenters_servers_upgrade_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/upgrade | Upgrade a Server by ID |
| ServersApi | [**datacenters_servers_volumes_delete**](docs/api/ServersApi.md#datacenters_servers_volumes_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/volumes/{volumeId} | Detach a Volume by ID |
| ServersApi | [**datacenters_servers_volumes_find_by_id**](docs/api/ServersApi.md#datacenters_servers_volumes_find_by_id) | **GET** /datacenters/{datacenterId}/servers/{serverId}/volumes/{volumeId} | Get Attached Volume by ID |
| ServersApi | [**datacenters_servers_volumes_get**](docs/api/ServersApi.md#datacenters_servers_volumes_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/volumes | Get Attached Volumes |
| ServersApi | [**datacenters_servers_volumes_post**](docs/api/ServersApi.md#datacenters_servers_volumes_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/volumes | Attach a Volume to a Server |
| SnapshotsApi | [**snapshots_delete**](docs/api/SnapshotsApi.md#snapshots_delete) | **DELETE** /snapshots/{snapshotId} | Delete snapshots |
| SnapshotsApi | [**snapshots_find_by_id**](docs/api/SnapshotsApi.md#snapshots_find_by_id) | **GET** /snapshots/{snapshotId} | Retrieve snapshots by ID |
| SnapshotsApi | [**snapshots_get**](docs/api/SnapshotsApi.md#snapshots_get) | **GET** /snapshots | List snapshots |
| SnapshotsApi | [**snapshots_patch**](docs/api/SnapshotsApi.md#snapshots_patch) | **PATCH** /snapshots/{snapshotId} | Partially modify snapshots |
| SnapshotsApi | [**snapshots_put**](docs/api/SnapshotsApi.md#snapshots_put) | **PUT** /snapshots/{snapshotId} | Modify a Snapshot by ID |
| TargetGroupsApi | [**target_groups_delete**](docs/api/TargetGroupsApi.md#target_groups_delete) | **DELETE** /targetgroups/{targetGroupId} | Delete a Target Group by ID |
| TargetGroupsApi | [**targetgroups_find_by_target_group_id**](docs/api/TargetGroupsApi.md#targetgroups_find_by_target_group_id) | **GET** /targetgroups/{targetGroupId} | Get a Target Group by ID |
| TargetGroupsApi | [**targetgroups_get**](docs/api/TargetGroupsApi.md#targetgroups_get) | **GET** /targetgroups | Get Target Groups |
| TargetGroupsApi | [**targetgroups_patch**](docs/api/TargetGroupsApi.md#targetgroups_patch) | **PATCH** /targetgroups/{targetGroupId} | Partially Modify a Target Group by ID |
| TargetGroupsApi | [**targetgroups_post**](docs/api/TargetGroupsApi.md#targetgroups_post) | **POST** /targetgroups | Create a Target Group |
| TargetGroupsApi | [**targetgroups_put**](docs/api/TargetGroupsApi.md#targetgroups_put) | **PUT** /targetgroups/{targetGroupId} | Modify a Target Group by ID |
| TemplatesApi | [**templates_find_by_id**](docs/api/TemplatesApi.md#templates_find_by_id) | **GET** /templates/{templateId} | Get Cubes Template by ID |
| TemplatesApi | [**templates_get**](docs/api/TemplatesApi.md#templates_get) | **GET** /templates | Get Cubes Templates |
| UserS3KeysApi | [**um_users_s3keys_delete**](docs/api/UserS3KeysApi.md#um_users_s3keys_delete) | **DELETE** /um/users/{userId}/s3keys/{keyId} | Delete Object storage keys |
| UserS3KeysApi | [**um_users_s3keys_find_by_key_id**](docs/api/UserS3KeysApi.md#um_users_s3keys_find_by_key_id) | **GET** /um/users/{userId}/s3keys/{keyId} | Retrieve user Object storage keys by key ID |
| UserS3KeysApi | [**um_users_s3keys_get**](docs/api/UserS3KeysApi.md#um_users_s3keys_get) | **GET** /um/users/{userId}/s3keys | List user Object storage keys |
| UserS3KeysApi | [**um_users_s3keys_post**](docs/api/UserS3KeysApi.md#um_users_s3keys_post) | **POST** /um/users/{userId}/s3keys | Create user Object storage keys |
| UserS3KeysApi | [**um_users_s3keys_put**](docs/api/UserS3KeysApi.md#um_users_s3keys_put) | **PUT** /um/users/{userId}/s3keys/{keyId} | Modify a Object storage Key by Key ID |
| UserS3KeysApi | [**um_users_s3ssourl_get**](docs/api/UserS3KeysApi.md#um_users_s3ssourl_get) | **GET** /um/users/{userId}/s3ssourl | Retrieve Object storage single sign-on URLs |
| UserManagementApi | [**um_groups_delete**](docs/api/UserManagementApi.md#um_groups_delete) | **DELETE** /um/groups/{groupId} | Delete groups |
| UserManagementApi | [**um_groups_find_by_id**](docs/api/UserManagementApi.md#um_groups_find_by_id) | **GET** /um/groups/{groupId} | Retrieve groups |
| UserManagementApi | [**um_groups_get**](docs/api/UserManagementApi.md#um_groups_get) | **GET** /um/groups | List all groups |
| UserManagementApi | [**um_groups_post**](docs/api/UserManagementApi.md#um_groups_post) | **POST** /um/groups | Create groups |
| UserManagementApi | [**um_groups_put**](docs/api/UserManagementApi.md#um_groups_put) | **PUT** /um/groups/{groupId} | Modify groups |
| UserManagementApi | [**um_groups_resources_get**](docs/api/UserManagementApi.md#um_groups_resources_get) | **GET** /um/groups/{groupId}/resources | Retrieve group resources |
| UserManagementApi | [**um_groups_shares_delete**](docs/api/UserManagementApi.md#um_groups_shares_delete) | **DELETE** /um/groups/{groupId}/shares/{resourceId} | Remove group shares |
| UserManagementApi | [**um_groups_shares_find_by_resource_id**](docs/api/UserManagementApi.md#um_groups_shares_find_by_resource_id) | **GET** /um/groups/{groupId}/shares/{resourceId} | Retrieve group shares |
| UserManagementApi | [**um_groups_shares_get**](docs/api/UserManagementApi.md#um_groups_shares_get) | **GET** /um/groups/{groupId}/shares | List group shares  |
| UserManagementApi | [**um_groups_shares_post**](docs/api/UserManagementApi.md#um_groups_shares_post) | **POST** /um/groups/{groupId}/shares/{resourceId} | Add group shares |
| UserManagementApi | [**um_groups_shares_put**](docs/api/UserManagementApi.md#um_groups_shares_put) | **PUT** /um/groups/{groupId}/shares/{resourceId} | Modify group share privileges |
| UserManagementApi | [**um_groups_users_delete**](docs/api/UserManagementApi.md#um_groups_users_delete) | **DELETE** /um/groups/{groupId}/users/{userId} | Remove users from groups |
| UserManagementApi | [**um_groups_users_get**](docs/api/UserManagementApi.md#um_groups_users_get) | **GET** /um/groups/{groupId}/users | List group members |
| UserManagementApi | [**um_groups_users_post**](docs/api/UserManagementApi.md#um_groups_users_post) | **POST** /um/groups/{groupId}/users | Add a Group Member |
| UserManagementApi | [**um_resources_find_by_type**](docs/api/UserManagementApi.md#um_resources_find_by_type) | **GET** /um/resources/{resourceType} | List resources by type |
| UserManagementApi | [**um_resources_find_by_type_and_id**](docs/api/UserManagementApi.md#um_resources_find_by_type_and_id) | **GET** /um/resources/{resourceType}/{resourceId} | Retrieve resources by type |
| UserManagementApi | [**um_resources_get**](docs/api/UserManagementApi.md#um_resources_get) | **GET** /um/resources | List all resources |
| UserManagementApi | [**um_users_delete**](docs/api/UserManagementApi.md#um_users_delete) | **DELETE** /um/users/{userId} | Delete users |
| UserManagementApi | [**um_users_find_by_id**](docs/api/UserManagementApi.md#um_users_find_by_id) | **GET** /um/users/{userId} | Retrieve users |
| UserManagementApi | [**um_users_get**](docs/api/UserManagementApi.md#um_users_get) | **GET** /um/users | List all users  |
| UserManagementApi | [**um_users_groups_get**](docs/api/UserManagementApi.md#um_users_groups_get) | **GET** /um/users/{userId}/groups | Retrieve group resources by user ID |
| UserManagementApi | [**um_users_owns_get**](docs/api/UserManagementApi.md#um_users_owns_get) | **GET** /um/users/{userId}/owns | Retrieve user resources by user ID |
| UserManagementApi | [**um_users_post**](docs/api/UserManagementApi.md#um_users_post) | **POST** /um/users | Create users |
| UserManagementApi | [**um_users_put**](docs/api/UserManagementApi.md#um_users_put) | **PUT** /um/users/{userId} | Modify users |
| VolumesApi | [**datacenters_volumes_create_snapshot_post**](docs/api/VolumesApi.md#datacenters_volumes_create_snapshot_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/create-snapshot | Create volume snapshots |
| VolumesApi | [**datacenters_volumes_delete**](docs/api/VolumesApi.md#datacenters_volumes_delete) | **DELETE** /datacenters/{datacenterId}/volumes/{volumeId} | Delete volumes |
| VolumesApi | [**datacenters_volumes_find_by_id**](docs/api/VolumesApi.md#datacenters_volumes_find_by_id) | **GET** /datacenters/{datacenterId}/volumes/{volumeId} | Retrieve volumes |
| VolumesApi | [**datacenters_volumes_get**](docs/api/VolumesApi.md#datacenters_volumes_get) | **GET** /datacenters/{datacenterId}/volumes | List volumes |
| VolumesApi | [**datacenters_volumes_patch**](docs/api/VolumesApi.md#datacenters_volumes_patch) | **PATCH** /datacenters/{datacenterId}/volumes/{volumeId} | Partially modify volumes |
| VolumesApi | [**datacenters_volumes_post**](docs/api/VolumesApi.md#datacenters_volumes_post) | **POST** /datacenters/{datacenterId}/volumes | Create a Volume |
| VolumesApi | [**datacenters_volumes_put**](docs/api/VolumesApi.md#datacenters_volumes_put) | **PUT** /datacenters/{datacenterId}/volumes/{volumeId} | Modify a Volume by ID |
| VolumesApi | [**datacenters_volumes_restore_snapshot_post**](docs/api/VolumesApi.md#datacenters_volumes_restore_snapshot_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/restore-snapshot | Restore volume snapshots |
| Api | [**api_info_get**](docs/api/Api.md#api_info_get) | **GET** / | Get API information |

</details>

## Documentation For Models

All URIs are relative to *https://api.ionos.com/cloudapi/v6*
<details >
<summary title="Click to toggle">API models list</summary>

 - [ApplicationLoadBalancer](docs/models/ApplicationLoadBalancer)
 - [ApplicationLoadBalancerEntities](docs/models/ApplicationLoadBalancerEntities)
 - [ApplicationLoadBalancerForwardingRule](docs/models/ApplicationLoadBalancerForwardingRule)
 - [ApplicationLoadBalancerForwardingRuleProperties](docs/models/ApplicationLoadBalancerForwardingRuleProperties)
 - [ApplicationLoadBalancerForwardingRulePut](docs/models/ApplicationLoadBalancerForwardingRulePut)
 - [ApplicationLoadBalancerForwardingRules](docs/models/ApplicationLoadBalancerForwardingRules)
 - [ApplicationLoadBalancerHttpRule](docs/models/ApplicationLoadBalancerHttpRule)
 - [ApplicationLoadBalancerHttpRuleCondition](docs/models/ApplicationLoadBalancerHttpRuleCondition)
 - [ApplicationLoadBalancerProperties](docs/models/ApplicationLoadBalancerProperties)
 - [ApplicationLoadBalancerPut](docs/models/ApplicationLoadBalancerPut)
 - [ApplicationLoadBalancers](docs/models/ApplicationLoadBalancers)
 - [AttachedVolumes](docs/models/AttachedVolumes)
 - [BackupUnit](docs/models/BackupUnit)
 - [BackupUnitProperties](docs/models/BackupUnitProperties)
 - [BackupUnitSSO](docs/models/BackupUnitSSO)
 - [BackupUnits](docs/models/BackupUnits)
 - [BalancedNics](docs/models/BalancedNics)
 - [Cdroms](docs/models/Cdroms)
 - [ConnectableDatacenter](docs/models/ConnectableDatacenter)
 - [Contract](docs/models/Contract)
 - [ContractProperties](docs/models/ContractProperties)
 - [Contracts](docs/models/Contracts)
 - [CpuArchitectureProperties](docs/models/CpuArchitectureProperties)
 - [CreateSnapshot](docs/models/CreateSnapshot)
 - [CreateSnapshotProperties](docs/models/CreateSnapshotProperties)
 - [DataCenterEntities](docs/models/DataCenterEntities)
 - [Datacenter](docs/models/Datacenter)
 - [DatacenterElementMetadata](docs/models/DatacenterElementMetadata)
 - [DatacenterPost](docs/models/DatacenterPost)
 - [DatacenterProperties](docs/models/DatacenterProperties)
 - [DatacenterPropertiesPost](docs/models/DatacenterPropertiesPost)
 - [DatacenterPropertiesPut](docs/models/DatacenterPropertiesPut)
 - [DatacenterPut](docs/models/DatacenterPut)
 - [Datacenters](docs/models/Datacenters)
 - [Error](docs/models/Error)
 - [ErrorMessage](docs/models/ErrorMessage)
 - [FirewallRule](docs/models/FirewallRule)
 - [FirewallRules](docs/models/FirewallRules)
 - [FirewallruleProperties](docs/models/FirewallruleProperties)
 - [FlowLog](docs/models/FlowLog)
 - [FlowLogProperties](docs/models/FlowLogProperties)
 - [FlowLogPut](docs/models/FlowLogPut)
 - [FlowLogs](docs/models/FlowLogs)
 - [Group](docs/models/Group)
 - [GroupEntities](docs/models/GroupEntities)
 - [GroupMembers](docs/models/GroupMembers)
 - [GroupProperties](docs/models/GroupProperties)
 - [GroupShare](docs/models/GroupShare)
 - [GroupShareProperties](docs/models/GroupShareProperties)
 - [GroupShares](docs/models/GroupShares)
 - [GroupUsers](docs/models/GroupUsers)
 - [Groups](docs/models/Groups)
 - [IPFailover](docs/models/IPFailover)
 - [Image](docs/models/Image)
 - [ImageProperties](docs/models/ImageProperties)
 - [Images](docs/models/Images)
 - [Info](docs/models/Info)
 - [IpBlock](docs/models/IpBlock)
 - [IpBlockProperties](docs/models/IpBlockProperties)
 - [IpBlocks](docs/models/IpBlocks)
 - [IpConsumer](docs/models/IpConsumer)
 - [KubernetesAutoScaling](docs/models/KubernetesAutoScaling)
 - [KubernetesCluster](docs/models/KubernetesCluster)
 - [KubernetesClusterEntities](docs/models/KubernetesClusterEntities)
 - [KubernetesClusterForPost](docs/models/KubernetesClusterForPost)
 - [KubernetesClusterForPut](docs/models/KubernetesClusterForPut)
 - [KubernetesClusterProperties](docs/models/KubernetesClusterProperties)
 - [KubernetesClusterPropertiesForPost](docs/models/KubernetesClusterPropertiesForPost)
 - [KubernetesClusterPropertiesForPut](docs/models/KubernetesClusterPropertiesForPut)
 - [KubernetesClusters](docs/models/KubernetesClusters)
 - [KubernetesMaintenanceWindow](docs/models/KubernetesMaintenanceWindow)
 - [KubernetesNode](docs/models/KubernetesNode)
 - [KubernetesNodeMetadata](docs/models/KubernetesNodeMetadata)
 - [KubernetesNodePool](docs/models/KubernetesNodePool)
 - [KubernetesNodePoolForPost](docs/models/KubernetesNodePoolForPost)
 - [KubernetesNodePoolForPut](docs/models/KubernetesNodePoolForPut)
 - [KubernetesNodePoolLan](docs/models/KubernetesNodePoolLan)
 - [KubernetesNodePoolLanRoutes](docs/models/KubernetesNodePoolLanRoutes)
 - [KubernetesNodePoolProperties](docs/models/KubernetesNodePoolProperties)
 - [KubernetesNodePoolPropertiesForPost](docs/models/KubernetesNodePoolPropertiesForPost)
 - [KubernetesNodePoolPropertiesForPut](docs/models/KubernetesNodePoolPropertiesForPut)
 - [KubernetesNodePoolServerType](docs/models/KubernetesNodePoolServerType)
 - [KubernetesNodePools](docs/models/KubernetesNodePools)
 - [KubernetesNodeProperties](docs/models/KubernetesNodeProperties)
 - [KubernetesNodes](docs/models/KubernetesNodes)
 - [Label](docs/models/Label)
 - [LabelProperties](docs/models/LabelProperties)
 - [LabelResource](docs/models/LabelResource)
 - [LabelResourceProperties](docs/models/LabelResourceProperties)
 - [LabelResources](docs/models/LabelResources)
 - [Labels](docs/models/Labels)
 - [Lan](docs/models/Lan)
 - [LanEntities](docs/models/LanEntities)
 - [LanNics](docs/models/LanNics)
 - [LanProperties](docs/models/LanProperties)
 - [Lans](docs/models/Lans)
 - [ListOfIds](docs/models/ListOfIds)
 - [Loadbalancer](docs/models/Loadbalancer)
 - [LoadbalancerEntities](docs/models/LoadbalancerEntities)
 - [LoadbalancerProperties](docs/models/LoadbalancerProperties)
 - [Loadbalancers](docs/models/Loadbalancers)
 - [Location](docs/models/Location)
 - [LocationProperties](docs/models/LocationProperties)
 - [Locations](docs/models/Locations)
 - [NatGateway](docs/models/NatGateway)
 - [NatGatewayEntities](docs/models/NatGatewayEntities)
 - [NatGatewayLanProperties](docs/models/NatGatewayLanProperties)
 - [NatGatewayProperties](docs/models/NatGatewayProperties)
 - [NatGatewayPut](docs/models/NatGatewayPut)
 - [NatGatewayRule](docs/models/NatGatewayRule)
 - [NatGatewayRuleProperties](docs/models/NatGatewayRuleProperties)
 - [NatGatewayRuleProtocol](docs/models/NatGatewayRuleProtocol)
 - [NatGatewayRulePut](docs/models/NatGatewayRulePut)
 - [NatGatewayRuleType](docs/models/NatGatewayRuleType)
 - [NatGatewayRules](docs/models/NatGatewayRules)
 - [NatGateways](docs/models/NatGateways)
 - [NetworkLoadBalancer](docs/models/NetworkLoadBalancer)
 - [NetworkLoadBalancerEntities](docs/models/NetworkLoadBalancerEntities)
 - [NetworkLoadBalancerForwardingRule](docs/models/NetworkLoadBalancerForwardingRule)
 - [NetworkLoadBalancerForwardingRuleHealthCheck](docs/models/NetworkLoadBalancerForwardingRuleHealthCheck)
 - [NetworkLoadBalancerForwardingRuleProperties](docs/models/NetworkLoadBalancerForwardingRuleProperties)
 - [NetworkLoadBalancerForwardingRulePut](docs/models/NetworkLoadBalancerForwardingRulePut)
 - [NetworkLoadBalancerForwardingRuleTarget](docs/models/NetworkLoadBalancerForwardingRuleTarget)
 - [NetworkLoadBalancerForwardingRuleTargetHealthCheck](docs/models/NetworkLoadBalancerForwardingRuleTargetHealthCheck)
 - [NetworkLoadBalancerForwardingRules](docs/models/NetworkLoadBalancerForwardingRules)
 - [NetworkLoadBalancerProperties](docs/models/NetworkLoadBalancerProperties)
 - [NetworkLoadBalancerPut](docs/models/NetworkLoadBalancerPut)
 - [NetworkLoadBalancers](docs/models/NetworkLoadBalancers)
 - [Nic](docs/models/Nic)
 - [NicEntities](docs/models/NicEntities)
 - [NicProperties](docs/models/NicProperties)
 - [NicPut](docs/models/NicPut)
 - [Nics](docs/models/Nics)
 - [NoStateMetaData](docs/models/NoStateMetaData)
 - [PaginationLinks](docs/models/PaginationLinks)
 - [Peer](docs/models/Peer)
 - [PrivateCrossConnect](docs/models/PrivateCrossConnect)
 - [PrivateCrossConnectProperties](docs/models/PrivateCrossConnectProperties)
 - [PrivateCrossConnects](docs/models/PrivateCrossConnects)
 - [RemoteConsoleUrl](docs/models/RemoteConsoleUrl)
 - [Request](docs/models/Request)
 - [RequestMetadata](docs/models/RequestMetadata)
 - [RequestProperties](docs/models/RequestProperties)
 - [RequestStatus](docs/models/RequestStatus)
 - [RequestStatusMetadata](docs/models/RequestStatusMetadata)
 - [RequestTarget](docs/models/RequestTarget)
 - [Requests](docs/models/Requests)
 - [Resource](docs/models/Resource)
 - [ResourceEntities](docs/models/ResourceEntities)
 - [ResourceGroups](docs/models/ResourceGroups)
 - [ResourceLimits](docs/models/ResourceLimits)
 - [ResourceProperties](docs/models/ResourceProperties)
 - [ResourceReference](docs/models/ResourceReference)
 - [Resources](docs/models/Resources)
 - [ResourcesUsers](docs/models/ResourcesUsers)
 - [RestoreSnapshot](docs/models/RestoreSnapshot)
 - [RestoreSnapshotProperties](docs/models/RestoreSnapshotProperties)
 - [S3Bucket](docs/models/S3Bucket)
 - [S3Key](docs/models/S3Key)
 - [S3KeyMetadata](docs/models/S3KeyMetadata)
 - [S3KeyProperties](docs/models/S3KeyProperties)
 - [S3Keys](docs/models/S3Keys)
 - [S3ObjectStorageSSO](docs/models/S3ObjectStorageSSO)
 - [SecurityGroup](docs/models/SecurityGroup)
 - [SecurityGroupEntities](docs/models/SecurityGroupEntities)
 - [SecurityGroupEntitiesRequest](docs/models/SecurityGroupEntitiesRequest)
 - [SecurityGroupProperties](docs/models/SecurityGroupProperties)
 - [SecurityGroupRequest](docs/models/SecurityGroupRequest)
 - [SecurityGroups](docs/models/SecurityGroups)
 - [Server](docs/models/Server)
 - [ServerEntities](docs/models/ServerEntities)
 - [ServerProperties](docs/models/ServerProperties)
 - [Servers](docs/models/Servers)
 - [Snapshot](docs/models/Snapshot)
 - [SnapshotProperties](docs/models/SnapshotProperties)
 - [Snapshots](docs/models/Snapshots)
 - [TargetGroup](docs/models/TargetGroup)
 - [TargetGroupHealthCheck](docs/models/TargetGroupHealthCheck)
 - [TargetGroupHttpHealthCheck](docs/models/TargetGroupHttpHealthCheck)
 - [TargetGroupProperties](docs/models/TargetGroupProperties)
 - [TargetGroupPut](docs/models/TargetGroupPut)
 - [TargetGroupTarget](docs/models/TargetGroupTarget)
 - [TargetGroups](docs/models/TargetGroups)
 - [TargetPortRange](docs/models/TargetPortRange)
 - [Template](docs/models/Template)
 - [TemplateProperties](docs/models/TemplateProperties)
 - [Templates](docs/models/Templates)
 - [Token](docs/models/Token)
 - [Type](docs/models/Type)
 - [User](docs/models/User)
 - [UserGroupPost](docs/models/UserGroupPost)
 - [UserMetadata](docs/models/UserMetadata)
 - [UserPost](docs/models/UserPost)
 - [UserProperties](docs/models/UserProperties)
 - [UserPropertiesPost](docs/models/UserPropertiesPost)
 - [UserPropertiesPut](docs/models/UserPropertiesPut)
 - [UserPut](docs/models/UserPut)
 - [Users](docs/models/Users)
 - [UsersEntities](docs/models/UsersEntities)
 - [Volume](docs/models/Volume)
 - [VolumeProperties](docs/models/VolumeProperties)
 - [Volumes](docs/models/Volumes)


[[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

</details>
