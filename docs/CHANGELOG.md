# CHANGELOG


## 5.0.8 \(April 8th, 2022\)

### Enhancements:
* added support for filter query parameters on GET requests
* added support for http proxy (_**IONOS_HTTP_PROXY**_ and _**IONOS_HTTP_PROXY_HEADERS**_ environment variables)


## 5.0.7 \(February 22th, 2022\)

### Bug fixes:
* bug fixes for Token Authentication on volume resource



## 5.0.6 \(February 18th, 2022\)

### Enhancements:

* support for Token Authentication: new parameters on **ionoscloud.Configuration**: `token` _(instead of api_key)_ and **token_prefix** _(instead of api_key_prefix)_
* new licence type: `WINDOWS2022`
* **UserPropertiesPut** new property: `password`
* **KubernetesNodePoolPropertiesForPut**: `name` is no longer a required parameter