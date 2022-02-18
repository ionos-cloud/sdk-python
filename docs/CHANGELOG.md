# CHANGELOG

## 6.0.2 \(February 18th, 2022\)

### Enhancements:

- support for Token Authentication: new parameters on **ionoscloud.Configuration**: `token` _(instead of api_key)_ and **token_prefix** _(instead of api_key_prefix)_


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
