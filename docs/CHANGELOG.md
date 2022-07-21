# CHANGELOG

## 6.1.2 \(July 21st, 2022\)

### Fixes:

* added asn1crypto as required module


## 6.1.1 \(July 14th, 2022\)

### Features
- Added `manage_dbaas` field in `model_group_properties.py` : provides privilege for a group to manage DBaaS related functionality. Admin users already here this enabled by default.
- Added `delete_volumes` to `datacenters_servers_delete`: If true, all attached storage volumes will also be deleted.
- Added `boot_order` to volume properties : Determines whether the volume will be used as a boot volume. Set to &#x60;NONE&#x60;, the volume will not be used as boot volume. Set to &#x60;PRIMARY&#x60;, the volume will be used as boot volume and all other volumes must be set to &#x60;NONE&#x60;. Set to &#x60;AUTO&#x60; or &#x60;null&#x60; requires all volumes to be set to &#x60;AUTO&#x60; or &#x60;null&#x60;; this will use the legacy behavior, which is to use the volume as a boot volume only if there are no other volumes or cdrom devices. | [optional] [default to 'AUTO'] |
- Added certificate pinning to sdk python. Enabling certificate pinning allows you to bypass normal certificate checking, by supplying a SHA256 or SHA1 fingerprint of the leaf cert to be checked against what the server provides.

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
