# CHANGELOG

## 6.0.0 \(December 9th, 2021\)

### Misc:

* new Python requirements: **Python ≥ 3.5**
* **LansApi** class renamed to **LANsApi**
* `backupunits_patch()` method parameter _backup_unit_properties_ changed to _backup_unit_
* **UserPropertiesPut** new property: `password`
* **KubernetesNodePoolPropertiesForPut**: `name` is no longer a required parameter
* `k8s_nodepools_put()` method parameter _kubernetes_node_pool_for_put_ changed to _kubernetes_node_pool_
* `k8s_nodepools_post()` method parameter _kubernetes_node_pool_ type is **KubernetesNodePoolForPost** instead of **KubernetesNodePool**