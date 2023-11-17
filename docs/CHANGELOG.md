# CHANGELOG

## 6.1.8
### Features:
Added support for **Private Kubernetes Clusters**:
- New parameters on `KubernetesClusterProperties` and `KubernetesClusterPropertiesForPost`: `location`, `nat_gateway_ip`, `node_subnet` and `public`

### Fixes:
- Fixed wrong parsing of `IONOS_HTTP_PROXY_HEADERS` by @hegerdes

## 6.1.7
### Features:
Added support for **IPv6**:

- New parameter on `DatacenterProperties`: `ipv6_cidr_block`
- New parameter on `LanProperties` and `LanPropertiesPost`: `ipv6_cidr_block`
- New parameters on `NicProperties`: `dhcpv6`, `ipv6_cidr_block` and `ipv6_ips`

More details about IPv6 configuration can be found [here](https://docs.ionos.com/cloud/compute-engine/networks/ipv6).

### Fixes:
- Fixed wrong error being shown when timeout is reached inside `wait_for`.

## 6.1.6
## Features:
- New licenceType supported: **RHEL**


## 6.1.4 \(July 14th, 2022\)
### Fixes:
- fix `manage_dbaas` typo in `model_group_properties.py`

## 6.1.3 \(July 14th, 2022\)
### Known issues:
- typo in `manage_dbaas` field in `model_group_properties.py` - generated as `manage_d_baa_s`

## 6.1.2 \(July 14th, 2022\)
### Fixes:
- fix: added asn1crypto as required module

## 6.1.1 \(July 14th, 2022\)
### Features
- added `manage_dbaas` field in `model_group_properties.py` : provides privilege for a group to manage DBaaS related functionality. Admin users already here this enabled by default.
- added `delete_volumes` to `datacenters_servers_delete`: If true, all attached storage volumes will also be deleted.
- added `boot_order` to volume properties : Determines whether the volume will be used as a boot volume. Set to &#x60;NONE&#x60;, the volume will not be used as boot volume. Set to &#x60;PRIMARY&#x60;, the volume will be used as boot volume and all other volumes must be set to &#x60;NONE&#x60;. Set to &#x60;AUTO&#x60; or &#x60;null&#x60; requires all volumes to be set to &#x60;AUTO&#x60; or &#x60;null&#x60;; this will use the legacy behavior, which is to use the volume as a boot volume only if there are no other volumes or cdrom devices. | [optional] [default to 'AUTO'] |
- added certificate pinning to sdk python. Enabling certificate pinning allows you to bypass normal certificate checking, by supplying a SHA256 or SHA1 fingerprint of the leaf cert to be checked against what the server provides.

## 6.1.0 \(June 15th, 2022\)

### Enhancements:

* added Application Load Balancer and Target Group, 18 new models and 2 new APIs

## 6.0.4 \(May 17th, 2022\)

### Fixes:

* removed parameter for `KubernetesClusterProperties`, `KubernetesClusterPropertiesForPost` models: `public`
* removed parameter for `KubernetesNodePoolProperties` model: `gateway_ip`


## 6.0.3 \(April 7th, 2022\)

### Enhancements:

* added support for filter query parameters on GET requests
* added support for http proxy (_**IONOS_HTTP_PROXY**_ and _**IONOS_HTTP_PROXY_HEADERS**_ environment variables)


## 6.0.2 \(February 18th, 2022\)

### Enhancements:

* support for Token Authentication: new parameters on **ionoscloud.Configuration**: `token` _(instead of api_key)_ and **token_prefix** _(instead of api_key_prefix)_


## 6.0.1 \(February 4th, 2022\)

### Enhancements:

* new licence type: `WINDOWS2022`
* new parameter on **KubernetesClusterProperties**, **KubernetesClusterPropertiesForPost** models: `public`
* new parameter on **KubernetesNodePoolProperties** model: `gateway_ip`
* new read-only parameter on **VolumeProperties** model: `boot_server`


## 6.0.0 \(December 9th, 2021\)

### Misc:

* new Python requirements: **Python ≥ 3.5**
* **LansApi** class renamed to **LANsApi**
* `backupunits_patch()` method parameter _backup_unit_properties_ changed to _backup_unit_
* **UserPropertiesPut** new property: `password`
* **KubernetesNodePoolPropertiesForPut**: `name` is no longer a required parameter
* `k8s_nodepools_put()` method parameter _kubernetes_node_pool_for_put_ changed to _kubernetes_node_pool_
* `k8s_nodepools_post()` method parameter _kubernetes_node_pool_ type is **KubernetesNodePoolForPost** instead of **KubernetesNodePool**
