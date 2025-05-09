from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud.api_client import ApiClient
from ionoscloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class KubernetesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def k8s_delete(self, k8s_cluster_id, **kwargs):  # noqa: E501
        """Delete a Kubernetes Cluster by ID  # noqa: E501

        Deletes the K8s cluster specified  by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_delete(k8s_cluster_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_delete_with_http_info(k8s_cluster_id, **kwargs)  # noqa: E501

    def k8s_delete_with_http_info(self, k8s_cluster_id, **kwargs):  # noqa: E501
        """Delete a Kubernetes Cluster by ID  # noqa: E501

        Deletes the K8s cluster specified  by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_delete_with_http_info(k8s_cluster_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_find_by_cluster_id(self, k8s_cluster_id, **kwargs):  # noqa: E501
        """Get a Kubernetes Cluster by ID  # noqa: E501

        Retrieves the K8s cluster specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_find_by_cluster_id(k8s_cluster_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the K8s cluster to be retrieved. (required)
        :type k8s_cluster_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: KubernetesCluster
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_find_by_cluster_id_with_http_info(k8s_cluster_id, **kwargs)  # noqa: E501

    def k8s_find_by_cluster_id_with_http_info(self, k8s_cluster_id, **kwargs):  # noqa: E501
        """Get a Kubernetes Cluster by ID  # noqa: E501

        Retrieves the K8s cluster specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_find_by_cluster_id_with_http_info(k8s_cluster_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the K8s cluster to be retrieved. (required)
        :type k8s_cluster_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(KubernetesCluster, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_find_by_cluster_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_find_by_cluster_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_find_by_cluster_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_find_by_cluster_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'KubernetesCluster'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_get(self, **kwargs):  # noqa: E501
        """Get Kubernetes Clusters  # noqa: E501

        Retrieves a list of all K8s clusters provisioned under your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_get(async_req=True)
        >>> result = thread.get()

        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: KubernetesClusters
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_get_with_http_info(**kwargs)  # noqa: E501

    def k8s_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Kubernetes Clusters  # noqa: E501

        Retrieves a list of all K8s clusters provisioned under your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(KubernetesClusters, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'KubernetesClusters'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_kubeconfig_get(self, k8s_cluster_id, **kwargs):  # noqa: E501
        """Get Kubernetes Configuration File  # noqa: E501

        Retrieves the configuration file for the specified K8s cluster. You can define the format (YAML or JSON) of the returned file in the Accept header. By default, 'application/yaml' is specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_kubeconfig_get(k8s_cluster_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: str
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_kubeconfig_get_with_http_info(k8s_cluster_id, **kwargs)  # noqa: E501

    def k8s_kubeconfig_get_with_http_info(self, k8s_cluster_id, **kwargs):  # noqa: E501
        """Get Kubernetes Configuration File  # noqa: E501

        Retrieves the configuration file for the specified K8s cluster. You can define the format (YAML or JSON) of the returned file in the Accept header. By default, 'application/yaml' is specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_kubeconfig_get_with_http_info(k8s_cluster_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_kubeconfig_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_kubeconfig_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_kubeconfig_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_kubeconfig_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/yaml', 'application/x-yaml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'str'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}/kubeconfig', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_nodepools_delete(self, k8s_cluster_id, nodepool_id, **kwargs):  # noqa: E501
        """Delete a Kubernetes Node Pool by ID  # noqa: E501

        Deletes the K8s node pool specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_delete(k8s_cluster_id, nodepool_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_nodepools_delete_with_http_info(k8s_cluster_id, nodepool_id, **kwargs)  # noqa: E501

    def k8s_nodepools_delete_with_http_info(self, k8s_cluster_id, nodepool_id, **kwargs):  # noqa: E501
        """Delete a Kubernetes Node Pool by ID  # noqa: E501

        Deletes the K8s node pool specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_delete_with_http_info(k8s_cluster_id, nodepool_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'nodepool_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_nodepools_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_nodepools_delete`")  # noqa: E501
        # verify the required parameter 'nodepool_id' is set
        if self.api_client.client_side_validation and ('nodepool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nodepool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nodepool_id` when calling `k8s_nodepools_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501
        if 'nodepool_id' in local_var_params:
            path_params['nodepoolId'] = local_var_params['nodepool_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}/nodepools/{nodepoolId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_nodepools_find_by_id(self, k8s_cluster_id, nodepool_id, **kwargs):  # noqa: E501
        """Get a Kubernetes Node Pool by ID  # noqa: E501

        Retrieves the K8s node pool specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_find_by_id(k8s_cluster_id, nodepool_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: KubernetesNodePool
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_nodepools_find_by_id_with_http_info(k8s_cluster_id, nodepool_id, **kwargs)  # noqa: E501

    def k8s_nodepools_find_by_id_with_http_info(self, k8s_cluster_id, nodepool_id, **kwargs):  # noqa: E501
        """Get a Kubernetes Node Pool by ID  # noqa: E501

        Retrieves the K8s node pool specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_find_by_id_with_http_info(k8s_cluster_id, nodepool_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(KubernetesNodePool, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'nodepool_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_nodepools_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_nodepools_find_by_id`")  # noqa: E501
        # verify the required parameter 'nodepool_id' is set
        if self.api_client.client_side_validation and ('nodepool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nodepool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nodepool_id` when calling `k8s_nodepools_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501
        if 'nodepool_id' in local_var_params:
            path_params['nodepoolId'] = local_var_params['nodepool_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'KubernetesNodePool'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}/nodepools/{nodepoolId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_nodepools_get(self, k8s_cluster_id, **kwargs):  # noqa: E501
        """Get Kubernetes Node Pools  # noqa: E501

        Retrieves a list of K8s node pools of a cluster specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_get(k8s_cluster_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: KubernetesNodePools
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_nodepools_get_with_http_info(k8s_cluster_id, **kwargs)  # noqa: E501

    def k8s_nodepools_get_with_http_info(self, k8s_cluster_id, **kwargs):  # noqa: E501
        """Get Kubernetes Node Pools  # noqa: E501

        Retrieves a list of K8s node pools of a cluster specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_get_with_http_info(k8s_cluster_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(KubernetesNodePools, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_nodepools_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_nodepools_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'KubernetesNodePools'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}/nodepools', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_nodepools_nodes_delete(self, k8s_cluster_id, nodepool_id, node_id, **kwargs):  # noqa: E501
        """Delete a Kubernetes Node by ID  # noqa: E501

        Deletes the K8s node specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_nodes_delete(k8s_cluster_id, nodepool_id, node_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param node_id: The unique ID of the Kubernetes node. (required)
        :type node_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_nodepools_nodes_delete_with_http_info(k8s_cluster_id, nodepool_id, node_id, **kwargs)  # noqa: E501

    def k8s_nodepools_nodes_delete_with_http_info(self, k8s_cluster_id, nodepool_id, node_id, **kwargs):  # noqa: E501
        """Delete a Kubernetes Node by ID  # noqa: E501

        Deletes the K8s node specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_nodes_delete_with_http_info(k8s_cluster_id, nodepool_id, node_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param node_id: The unique ID of the Kubernetes node. (required)
        :type node_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'nodepool_id',
            'node_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_nodepools_nodes_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_nodepools_nodes_delete`")  # noqa: E501
        # verify the required parameter 'nodepool_id' is set
        if self.api_client.client_side_validation and ('nodepool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nodepool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nodepool_id` when calling `k8s_nodepools_nodes_delete`")  # noqa: E501
        # verify the required parameter 'node_id' is set
        if self.api_client.client_side_validation and ('node_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['node_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `node_id` when calling `k8s_nodepools_nodes_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_nodes_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_nodes_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501
        if 'nodepool_id' in local_var_params:
            path_params['nodepoolId'] = local_var_params['nodepool_id']  # noqa: E501
        if 'node_id' in local_var_params:
            path_params['nodeId'] = local_var_params['node_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_nodepools_nodes_find_by_id(self, k8s_cluster_id, nodepool_id, node_id, **kwargs):  # noqa: E501
        """Get Kubernetes Node by ID  # noqa: E501

        Retrieves the K8s node specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_nodes_find_by_id(k8s_cluster_id, nodepool_id, node_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param node_id: The unique ID of the Kubernetes node. (required)
        :type node_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: KubernetesNode
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_nodepools_nodes_find_by_id_with_http_info(k8s_cluster_id, nodepool_id, node_id, **kwargs)  # noqa: E501

    def k8s_nodepools_nodes_find_by_id_with_http_info(self, k8s_cluster_id, nodepool_id, node_id, **kwargs):  # noqa: E501
        """Get Kubernetes Node by ID  # noqa: E501

        Retrieves the K8s node specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_nodes_find_by_id_with_http_info(k8s_cluster_id, nodepool_id, node_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param node_id: The unique ID of the Kubernetes node. (required)
        :type node_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(KubernetesNode, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'nodepool_id',
            'node_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_nodepools_nodes_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_nodepools_nodes_find_by_id`")  # noqa: E501
        # verify the required parameter 'nodepool_id' is set
        if self.api_client.client_side_validation and ('nodepool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nodepool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nodepool_id` when calling `k8s_nodepools_nodes_find_by_id`")  # noqa: E501
        # verify the required parameter 'node_id' is set
        if self.api_client.client_side_validation and ('node_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['node_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `node_id` when calling `k8s_nodepools_nodes_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_nodes_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_nodes_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501
        if 'nodepool_id' in local_var_params:
            path_params['nodepoolId'] = local_var_params['nodepool_id']  # noqa: E501
        if 'node_id' in local_var_params:
            path_params['nodeId'] = local_var_params['node_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'KubernetesNode'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_nodepools_nodes_get(self, k8s_cluster_id, nodepool_id, **kwargs):  # noqa: E501
        """Get Kubernetes Nodes  # noqa: E501

        Retrieves the list of all K8s nodes of the specified node pool.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_nodes_get(k8s_cluster_id, nodepool_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: KubernetesNodes
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_nodepools_nodes_get_with_http_info(k8s_cluster_id, nodepool_id, **kwargs)  # noqa: E501

    def k8s_nodepools_nodes_get_with_http_info(self, k8s_cluster_id, nodepool_id, **kwargs):  # noqa: E501
        """Get Kubernetes Nodes  # noqa: E501

        Retrieves the list of all K8s nodes of the specified node pool.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_nodes_get_with_http_info(k8s_cluster_id, nodepool_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(KubernetesNodes, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'nodepool_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_nodepools_nodes_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_nodepools_nodes_get`")  # noqa: E501
        # verify the required parameter 'nodepool_id' is set
        if self.api_client.client_side_validation and ('nodepool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nodepool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nodepool_id` when calling `k8s_nodepools_nodes_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_nodes_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_nodes_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501
        if 'nodepool_id' in local_var_params:
            path_params['nodepoolId'] = local_var_params['nodepool_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'KubernetesNodes'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_nodepools_nodes_replace_post(self, k8s_cluster_id, nodepool_id, node_id, **kwargs):  # noqa: E501
        """Recreate a Kubernetes Node by ID  # noqa: E501

        Recreates the K8s node specified by its ID.  If a node becomes unusable, Managed Kubernetes allows you to recreate it with a configuration based on the node pool template. Once the status is 'Active,' all the pods from the failed node will be migrated to the new node. The node pool has an additional billable 'active' node during this process.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_nodes_replace_post(k8s_cluster_id, nodepool_id, node_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param node_id: The unique ID of the Kubernetes node. (required)
        :type node_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_nodepools_nodes_replace_post_with_http_info(k8s_cluster_id, nodepool_id, node_id, **kwargs)  # noqa: E501

    def k8s_nodepools_nodes_replace_post_with_http_info(self, k8s_cluster_id, nodepool_id, node_id, **kwargs):  # noqa: E501
        """Recreate a Kubernetes Node by ID  # noqa: E501

        Recreates the K8s node specified by its ID.  If a node becomes unusable, Managed Kubernetes allows you to recreate it with a configuration based on the node pool template. Once the status is 'Active,' all the pods from the failed node will be migrated to the new node. The node pool has an additional billable 'active' node during this process.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_nodes_replace_post_with_http_info(k8s_cluster_id, nodepool_id, node_id, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param node_id: The unique ID of the Kubernetes node. (required)
        :type node_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'nodepool_id',
            'node_id',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_nodepools_nodes_replace_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_nodepools_nodes_replace_post`")  # noqa: E501
        # verify the required parameter 'nodepool_id' is set
        if self.api_client.client_side_validation and ('nodepool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nodepool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nodepool_id` when calling `k8s_nodepools_nodes_replace_post`")  # noqa: E501
        # verify the required parameter 'node_id' is set
        if self.api_client.client_side_validation and ('node_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['node_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `node_id` when calling `k8s_nodepools_nodes_replace_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_nodes_replace_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_nodes_replace_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501
        if 'nodepool_id' in local_var_params:
            path_params['nodepoolId'] = local_var_params['nodepool_id']  # noqa: E501
        if 'node_id' in local_var_params:
            path_params['nodeId'] = local_var_params['node_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}/nodepools/{nodepoolId}/nodes/{nodeId}/replace', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_nodepools_post(self, k8s_cluster_id, kubernetes_node_pool, **kwargs):  # noqa: E501
        """Create a Kubernetes Node Pool  # noqa: E501

        Creates a node pool inside the specified K8s cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_post(k8s_cluster_id, kubernetes_node_pool, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param kubernetes_node_pool: The Kubernetes node pool to create. (required)
        :type kubernetes_node_pool: KubernetesNodePoolForPost
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: KubernetesNodePool
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_nodepools_post_with_http_info(k8s_cluster_id, kubernetes_node_pool, **kwargs)  # noqa: E501

    def k8s_nodepools_post_with_http_info(self, k8s_cluster_id, kubernetes_node_pool, **kwargs):  # noqa: E501
        """Create a Kubernetes Node Pool  # noqa: E501

        Creates a node pool inside the specified K8s cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_post_with_http_info(k8s_cluster_id, kubernetes_node_pool, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param kubernetes_node_pool: The Kubernetes node pool to create. (required)
        :type kubernetes_node_pool: KubernetesNodePoolForPost
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(KubernetesNodePool, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'kubernetes_node_pool',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_nodepools_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_nodepools_post`")  # noqa: E501
        # verify the required parameter 'kubernetes_node_pool' is set
        if self.api_client.client_side_validation and ('kubernetes_node_pool' not in local_var_params or  # noqa: E501
                                                        local_var_params['kubernetes_node_pool'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `kubernetes_node_pool` when calling `k8s_nodepools_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'kubernetes_node_pool' in local_var_params:
            body_params = local_var_params['kubernetes_node_pool']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'KubernetesNodePool'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}/nodepools', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_nodepools_put(self, k8s_cluster_id, nodepool_id, kubernetes_node_pool, **kwargs):  # noqa: E501
        """Modify a Kubernetes Node Pool by ID  # noqa: E501

        Modifies the K8s node pool specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_put(k8s_cluster_id, nodepool_id, kubernetes_node_pool, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param kubernetes_node_pool: Details of the Kubernetes Node Pool (required)
        :type kubernetes_node_pool: KubernetesNodePoolForPut
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: KubernetesNodePool
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_nodepools_put_with_http_info(k8s_cluster_id, nodepool_id, kubernetes_node_pool, **kwargs)  # noqa: E501

    def k8s_nodepools_put_with_http_info(self, k8s_cluster_id, nodepool_id, kubernetes_node_pool, **kwargs):  # noqa: E501
        """Modify a Kubernetes Node Pool by ID  # noqa: E501

        Modifies the K8s node pool specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_nodepools_put_with_http_info(k8s_cluster_id, nodepool_id, kubernetes_node_pool, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param nodepool_id: The unique ID of the Kubernetes node pool. (required)
        :type nodepool_id: str
        :param kubernetes_node_pool: Details of the Kubernetes Node Pool (required)
        :type kubernetes_node_pool: KubernetesNodePoolForPut
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(KubernetesNodePool, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'nodepool_id',
            'kubernetes_node_pool',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_nodepools_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_nodepools_put`")  # noqa: E501
        # verify the required parameter 'nodepool_id' is set
        if self.api_client.client_side_validation and ('nodepool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nodepool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nodepool_id` when calling `k8s_nodepools_put`")  # noqa: E501
        # verify the required parameter 'kubernetes_node_pool' is set
        if self.api_client.client_side_validation and ('kubernetes_node_pool' not in local_var_params or  # noqa: E501
                                                        local_var_params['kubernetes_node_pool'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `kubernetes_node_pool` when calling `k8s_nodepools_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_nodepools_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501
        if 'nodepool_id' in local_var_params:
            path_params['nodepoolId'] = local_var_params['nodepool_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'kubernetes_node_pool' in local_var_params:
            body_params = local_var_params['kubernetes_node_pool']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'KubernetesNodePool'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}/nodepools/{nodepoolId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_post(self, kubernetes_cluster, **kwargs):  # noqa: E501
        """Create a Kubernetes Cluster  # noqa: E501

        Creates a K8s cluster provisioned under your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_post(kubernetes_cluster, async_req=True)
        >>> result = thread.get()

        :param kubernetes_cluster: The Kubernetes cluster to create. (required)
        :type kubernetes_cluster: KubernetesClusterForPost
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: KubernetesCluster
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_post_with_http_info(kubernetes_cluster, **kwargs)  # noqa: E501

    def k8s_post_with_http_info(self, kubernetes_cluster, **kwargs):  # noqa: E501
        """Create a Kubernetes Cluster  # noqa: E501

        Creates a K8s cluster provisioned under your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_post_with_http_info(kubernetes_cluster, async_req=True)
        >>> result = thread.get()

        :param kubernetes_cluster: The Kubernetes cluster to create. (required)
        :type kubernetes_cluster: KubernetesClusterForPost
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(KubernetesCluster, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'kubernetes_cluster',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'kubernetes_cluster' is set
        if self.api_client.client_side_validation and ('kubernetes_cluster' not in local_var_params or  # noqa: E501
                                                        local_var_params['kubernetes_cluster'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `kubernetes_cluster` when calling `k8s_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'kubernetes_cluster' in local_var_params:
            body_params = local_var_params['kubernetes_cluster']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'KubernetesCluster'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_put(self, k8s_cluster_id, kubernetes_cluster, **kwargs):  # noqa: E501
        """Modify a Kubernetes Cluster by ID  # noqa: E501

        Modifies the K8s cluster specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_put(k8s_cluster_id, kubernetes_cluster, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param kubernetes_cluster: The modified Kubernetes cluster. (required)
        :type kubernetes_cluster: KubernetesClusterForPut
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: KubernetesCluster
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_put_with_http_info(k8s_cluster_id, kubernetes_cluster, **kwargs)  # noqa: E501

    def k8s_put_with_http_info(self, k8s_cluster_id, kubernetes_cluster, **kwargs):  # noqa: E501
        """Modify a Kubernetes Cluster by ID  # noqa: E501

        Modifies the K8s cluster specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_put_with_http_info(k8s_cluster_id, kubernetes_cluster, async_req=True)
        >>> result = thread.get()

        :param k8s_cluster_id: The unique ID of the Kubernetes cluster. (required)
        :type k8s_cluster_id: str
        :param kubernetes_cluster: The modified Kubernetes cluster. (required)
        :type kubernetes_cluster: KubernetesClusterForPut
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(KubernetesCluster, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'k8s_cluster_id',
            'kubernetes_cluster',
            'pretty',
            'depth',
            'x_contract_number'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'k8s_cluster_id' is set
        if self.api_client.client_side_validation and ('k8s_cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['k8s_cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `k8s_cluster_id` when calling `k8s_put`")  # noqa: E501
        # verify the required parameter 'kubernetes_cluster' is set
        if self.api_client.client_side_validation and ('kubernetes_cluster' not in local_var_params or  # noqa: E501
                                                        local_var_params['kubernetes_cluster'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `kubernetes_cluster` when calling `k8s_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `k8s_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'k8s_cluster_id' in local_var_params:
            path_params['k8sClusterId'] = local_var_params['k8s_cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}
        if 'x_contract_number' in local_var_params:
            header_params['X-Contract-Number'] = local_var_params['x_contract_number']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'kubernetes_cluster' in local_var_params:
            body_params = local_var_params['kubernetes_cluster']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'KubernetesCluster'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/{k8sClusterId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_versions_default_get(self, **kwargs):  # noqa: E501
        """Get Default Kubernetes Version  # noqa: E501

        Retrieves the current default K8s version to be used by the clusters and node pools.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_versions_default_get(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: str
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_versions_default_get_with_http_info(**kwargs)  # noqa: E501

    def k8s_versions_default_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Default Kubernetes Version  # noqa: E501

        Retrieves the current default K8s version to be used by the clusters and node pools.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_versions_default_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_versions_default_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'str'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/versions/default', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def k8s_versions_get(self, **kwargs):  # noqa: E501
        """Get Kubernetes Versions  # noqa: E501

        Lists available K8s versions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_versions_get(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[str]
        """
        kwargs['_return_http_data_only'] = True
        return self.k8s_versions_get_with_http_info(**kwargs)  # noqa: E501

    def k8s_versions_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Kubernetes Versions  # noqa: E501

        Lists available K8s versions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.k8s_versions_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[str], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k8s_versions_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'list[str]'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/k8s/versions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
