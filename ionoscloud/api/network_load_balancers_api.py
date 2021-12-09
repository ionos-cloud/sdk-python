from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud.api_client import ApiClient
from ionoscloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class NetworkLoadBalancersApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def datacenters_networkloadbalancers_delete(self, datacenter_id, network_load_balancer_id, **kwargs):  # noqa: E501
        """Delete Network Load Balancers  # noqa: E501

        Remove the specified Network Load Balancer from the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_delete(datacenter_id, network_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        return self.datacenters_networkloadbalancers_delete_with_http_info(datacenter_id, network_load_balancer_id, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_delete_with_http_info(self, datacenter_id, network_load_balancer_id, **kwargs):  # noqa: E501
        """Delete Network Load Balancers  # noqa: E501

        Remove the specified Network Load Balancer from the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_delete_with_http_info(datacenter_id, network_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
            'datacenter_id',
            'network_load_balancer_id',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_delete`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501

        query_params = []
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
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}', 'DELETE',
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

    def datacenters_networkloadbalancers_find_by_network_load_balancer_id(self, datacenter_id, network_load_balancer_id, **kwargs):  # noqa: E501
        """Retrieve Network Load Balancers  # noqa: E501

        Retrieve the properties of the specified Network Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_find_by_network_load_balancer_id(datacenter_id, network_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: NetworkLoadBalancer
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_find_by_network_load_balancer_id_with_http_info(datacenter_id, network_load_balancer_id, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_find_by_network_load_balancer_id_with_http_info(self, datacenter_id, network_load_balancer_id, **kwargs):  # noqa: E501
        """Retrieve Network Load Balancers  # noqa: E501

        Retrieve the properties of the specified Network Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_find_by_network_load_balancer_id_with_http_info(datacenter_id, network_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(NetworkLoadBalancer, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_find_by_network_load_balancer_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_find_by_network_load_balancer_id`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_find_by_network_load_balancer_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_find_by_network_load_balancer_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_find_by_network_load_balancer_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501

        query_params = []
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
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NetworkLoadBalancer'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}', 'GET',
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

    def datacenters_networkloadbalancers_flowlogs_delete(self, datacenter_id, network_load_balancer_id, flow_log_id, **kwargs):  # noqa: E501
        """Delete NLB Flow Logs  # noqa: E501

        Delete the specified Network Load Balancer Flow Log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_delete(datacenter_id, network_load_balancer_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param flow_log_id: The unique ID of the Flow Log. (required)
        :type flow_log_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        return self.datacenters_networkloadbalancers_flowlogs_delete_with_http_info(datacenter_id, network_load_balancer_id, flow_log_id, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_flowlogs_delete_with_http_info(self, datacenter_id, network_load_balancer_id, flow_log_id, **kwargs):  # noqa: E501
        """Delete NLB Flow Logs  # noqa: E501

        Delete the specified Network Load Balancer Flow Log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_delete_with_http_info(datacenter_id, network_load_balancer_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param flow_log_id: The unique ID of the Flow Log. (required)
        :type flow_log_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
            'datacenter_id',
            'network_load_balancer_id',
            'flow_log_id',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_flowlogs_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_flowlogs_delete`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_flowlogs_delete`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_networkloadbalancers_flowlogs_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

        query_params = []
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
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId}', 'DELETE',
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

    def datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id(self, datacenter_id, network_load_balancer_id, flow_log_id, **kwargs):  # noqa: E501
        """Retrieve NLB Flow Logs  # noqa: E501

        Retrieve the specified Network Load Balancer Flow Log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, network_load_balancer_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param flow_log_id: The unique ID of the Flow Log. (required)
        :type flow_log_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id_with_http_info(datacenter_id, network_load_balancer_id, flow_log_id, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id_with_http_info(self, datacenter_id, network_load_balancer_id, flow_log_id, **kwargs):  # noqa: E501
        """Retrieve NLB Flow Logs  # noqa: E501

        Retrieve the specified Network Load Balancer Flow Log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id_with_http_info(datacenter_id, network_load_balancer_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param flow_log_id: The unique ID of the Flow Log. (required)
        :type flow_log_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
            'flow_log_id',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_find_by_flow_log_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

        query_params = []
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
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId}', 'GET',
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

    def datacenters_networkloadbalancers_flowlogs_get(self, datacenter_id, network_load_balancer_id, **kwargs):  # noqa: E501
        """List NLB Flow Logs  # noqa: E501

        List all the Flow Logs for the specified Network Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_get(datacenter_id, network_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: FlowLogs
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_flowlogs_get_with_http_info(datacenter_id, network_load_balancer_id, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_flowlogs_get_with_http_info(self, datacenter_id, network_load_balancer_id, **kwargs):  # noqa: E501
        """List NLB Flow Logs  # noqa: E501

        List all the Flow Logs for the specified Network Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_get_with_http_info(datacenter_id, network_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(FlowLogs, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_flowlogs_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_flowlogs_get`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_flowlogs_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501

        query_params = []
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
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'FlowLogs'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs', 'GET',
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

    def datacenters_networkloadbalancers_flowlogs_patch(self, datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log_properties, **kwargs):  # noqa: E501
        """Partially modify NLB Flow Logs  # noqa: E501

        Update the properties of the specified Network Load Balancer Flow Log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_patch(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param flow_log_id: The unique ID of the Flow Log. (required)
        :type flow_log_id: str
        :param network_load_balancer_flow_log_properties: The properties of the Flow Log to be updated. (required)
        :type network_load_balancer_flow_log_properties: FlowLogProperties
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_flowlogs_patch_with_http_info(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log_properties, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_flowlogs_patch_with_http_info(self, datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log_properties, **kwargs):  # noqa: E501
        """Partially modify NLB Flow Logs  # noqa: E501

        Update the properties of the specified Network Load Balancer Flow Log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_patch_with_http_info(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param flow_log_id: The unique ID of the Flow Log. (required)
        :type flow_log_id: str
        :param network_load_balancer_flow_log_properties: The properties of the Flow Log to be updated. (required)
        :type network_load_balancer_flow_log_properties: FlowLogProperties
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
            'flow_log_id',
            'network_load_balancer_flow_log_properties',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_flowlogs_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_flowlogs_patch`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_flowlogs_patch`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_networkloadbalancers_flowlogs_patch`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_flow_log_properties' is set
        if self.api_client.client_side_validation and ('network_load_balancer_flow_log_properties' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_flow_log_properties'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_flow_log_properties` when calling `datacenters_networkloadbalancers_flowlogs_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

        query_params = []
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
        if 'network_load_balancer_flow_log_properties' in local_var_params:
            body_params = local_var_params['network_load_balancer_flow_log_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId}', 'PATCH',
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

    def datacenters_networkloadbalancers_flowlogs_post(self, datacenter_id, network_load_balancer_id, network_load_balancer_flow_log, **kwargs):  # noqa: E501
        """Create NLB Flow Logs  # noqa: E501

        Add a new Flow Log for the Network Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_post(datacenter_id, network_load_balancer_id, network_load_balancer_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param network_load_balancer_flow_log: The Flow Log to create. (required)
        :type network_load_balancer_flow_log: FlowLog
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_flowlogs_post_with_http_info(datacenter_id, network_load_balancer_id, network_load_balancer_flow_log, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_flowlogs_post_with_http_info(self, datacenter_id, network_load_balancer_id, network_load_balancer_flow_log, **kwargs):  # noqa: E501
        """Create NLB Flow Logs  # noqa: E501

        Add a new Flow Log for the Network Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_post_with_http_info(datacenter_id, network_load_balancer_id, network_load_balancer_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param network_load_balancer_flow_log: The Flow Log to create. (required)
        :type network_load_balancer_flow_log: FlowLog
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
            'network_load_balancer_flow_log',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_flowlogs_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_flowlogs_post`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_flowlogs_post`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_flow_log' is set
        if self.api_client.client_side_validation and ('network_load_balancer_flow_log' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_flow_log'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_flow_log` when calling `datacenters_networkloadbalancers_flowlogs_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501

        query_params = []
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
        if 'network_load_balancer_flow_log' in local_var_params:
            body_params = local_var_params['network_load_balancer_flow_log']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs', 'POST',
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

    def datacenters_networkloadbalancers_flowlogs_put(self, datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log, **kwargs):  # noqa: E501
        """Modify NLB Flow Logs  # noqa: E501

        Modify the specified Network Load Balancer Flow Log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_put(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param flow_log_id: The unique ID of the Flow Log. (required)
        :type flow_log_id: str
        :param network_load_balancer_flow_log: The modified NLB Flow Log. (required)
        :type network_load_balancer_flow_log: FlowLogPut
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_flowlogs_put_with_http_info(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_flowlogs_put_with_http_info(self, datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log, **kwargs):  # noqa: E501
        """Modify NLB Flow Logs  # noqa: E501

        Modify the specified Network Load Balancer Flow Log.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_flowlogs_put_with_http_info(datacenter_id, network_load_balancer_id, flow_log_id, network_load_balancer_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param flow_log_id: The unique ID of the Flow Log. (required)
        :type flow_log_id: str
        :param network_load_balancer_flow_log: The modified NLB Flow Log. (required)
        :type network_load_balancer_flow_log: FlowLogPut
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
            'flow_log_id',
            'network_load_balancer_flow_log',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_flowlogs_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_flowlogs_put`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_flowlogs_put`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_networkloadbalancers_flowlogs_put`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_flow_log' is set
        if self.api_client.client_side_validation and ('network_load_balancer_flow_log' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_flow_log'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_flow_log` when calling `datacenters_networkloadbalancers_flowlogs_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_flowlogs_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

        query_params = []
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
        if 'network_load_balancer_flow_log' in local_var_params:
            body_params = local_var_params['network_load_balancer_flow_log']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/flowlogs/{flowLogId}', 'PUT',
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

    def datacenters_networkloadbalancers_forwardingrules_delete(self, datacenter_id, network_load_balancer_id, forwarding_rule_id, **kwargs):  # noqa: E501
        """Delete NLB forwarding rules  # noqa: E501

        Delete the specified Network Load Balancer forwarding rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_delete(datacenter_id, network_load_balancer_id, forwarding_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        return self.datacenters_networkloadbalancers_forwardingrules_delete_with_http_info(datacenter_id, network_load_balancer_id, forwarding_rule_id, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_forwardingrules_delete_with_http_info(self, datacenter_id, network_load_balancer_id, forwarding_rule_id, **kwargs):  # noqa: E501
        """Delete NLB forwarding rules  # noqa: E501

        Delete the specified Network Load Balancer forwarding rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_delete_with_http_info(datacenter_id, network_load_balancer_id, forwarding_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
            'datacenter_id',
            'network_load_balancer_id',
            'forwarding_rule_id',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_forwardingrules_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_forwardingrules_delete`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_forwardingrules_delete`")  # noqa: E501
        # verify the required parameter 'forwarding_rule_id' is set
        if self.api_client.client_side_validation and ('forwarding_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['forwarding_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `forwarding_rule_id` when calling `datacenters_networkloadbalancers_forwardingrules_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501
        if 'forwarding_rule_id' in local_var_params:
            path_params['forwardingRuleId'] = local_var_params['forwarding_rule_id']  # noqa: E501

        query_params = []
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
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId}', 'DELETE',
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

    def datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id(self, datacenter_id, network_load_balancer_id, forwarding_rule_id, **kwargs):  # noqa: E501
        """Retrieve NLB forwarding rules  # noqa: E501

        Retrieve the specified Network Load Balance forwarding rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, network_load_balancer_id, forwarding_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: NetworkLoadBalancerForwardingRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id_with_http_info(datacenter_id, network_load_balancer_id, forwarding_rule_id, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id_with_http_info(self, datacenter_id, network_load_balancer_id, forwarding_rule_id, **kwargs):  # noqa: E501
        """Retrieve NLB forwarding rules  # noqa: E501

        Retrieve the specified Network Load Balance forwarding rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id_with_http_info(datacenter_id, network_load_balancer_id, forwarding_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(NetworkLoadBalancerForwardingRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
            'forwarding_rule_id',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id`")  # noqa: E501
        # verify the required parameter 'forwarding_rule_id' is set
        if self.api_client.client_side_validation and ('forwarding_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['forwarding_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `forwarding_rule_id` when calling `datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_find_by_forwarding_rule_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501
        if 'forwarding_rule_id' in local_var_params:
            path_params['forwardingRuleId'] = local_var_params['forwarding_rule_id']  # noqa: E501

        query_params = []
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
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NetworkLoadBalancerForwardingRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId}', 'GET',
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

    def datacenters_networkloadbalancers_forwardingrules_get(self, datacenter_id, network_load_balancer_id, **kwargs):  # noqa: E501
        """List NLB forwarding rules  # noqa: E501

        List the forwarding rules for the specified Network Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_get(datacenter_id, network_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: NetworkLoadBalancerForwardingRules
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_forwardingrules_get_with_http_info(datacenter_id, network_load_balancer_id, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_forwardingrules_get_with_http_info(self, datacenter_id, network_load_balancer_id, **kwargs):  # noqa: E501
        """List NLB forwarding rules  # noqa: E501

        List the forwarding rules for the specified Network Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_get_with_http_info(datacenter_id, network_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(NetworkLoadBalancerForwardingRules, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_forwardingrules_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_forwardingrules_get`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_forwardingrules_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501

        query_params = []
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
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NetworkLoadBalancerForwardingRules'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules', 'GET',
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

    def datacenters_networkloadbalancers_forwardingrules_patch(self, datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule_properties, **kwargs):  # noqa: E501
        """Partially modify NLB forwarding rules  # noqa: E501

        Update the properties of the specified Network Load Balancer forwarding rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_patch(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param network_load_balancer_forwarding_rule_properties: The properties of the forwarding rule to be updated. (required)
        :type network_load_balancer_forwarding_rule_properties: NetworkLoadBalancerForwardingRuleProperties
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: NetworkLoadBalancerForwardingRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_forwardingrules_patch_with_http_info(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule_properties, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_forwardingrules_patch_with_http_info(self, datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule_properties, **kwargs):  # noqa: E501
        """Partially modify NLB forwarding rules  # noqa: E501

        Update the properties of the specified Network Load Balancer forwarding rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_patch_with_http_info(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param network_load_balancer_forwarding_rule_properties: The properties of the forwarding rule to be updated. (required)
        :type network_load_balancer_forwarding_rule_properties: NetworkLoadBalancerForwardingRuleProperties
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(NetworkLoadBalancerForwardingRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
            'forwarding_rule_id',
            'network_load_balancer_forwarding_rule_properties',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_forwardingrules_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_forwardingrules_patch`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_forwardingrules_patch`")  # noqa: E501
        # verify the required parameter 'forwarding_rule_id' is set
        if self.api_client.client_side_validation and ('forwarding_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['forwarding_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `forwarding_rule_id` when calling `datacenters_networkloadbalancers_forwardingrules_patch`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_forwarding_rule_properties' is set
        if self.api_client.client_side_validation and ('network_load_balancer_forwarding_rule_properties' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_forwarding_rule_properties'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_forwarding_rule_properties` when calling `datacenters_networkloadbalancers_forwardingrules_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501
        if 'forwarding_rule_id' in local_var_params:
            path_params['forwardingRuleId'] = local_var_params['forwarding_rule_id']  # noqa: E501

        query_params = []
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
        if 'network_load_balancer_forwarding_rule_properties' in local_var_params:
            body_params = local_var_params['network_load_balancer_forwarding_rule_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NetworkLoadBalancerForwardingRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId}', 'PATCH',
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

    def datacenters_networkloadbalancers_forwardingrules_post(self, datacenter_id, network_load_balancer_id, network_load_balancer_forwarding_rule, **kwargs):  # noqa: E501
        """Create NLB forwarding rules  # noqa: E501

        Create a forwarding rule for the specified Network Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_post(datacenter_id, network_load_balancer_id, network_load_balancer_forwarding_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param network_load_balancer_forwarding_rule: The forwarding rule to create. (required)
        :type network_load_balancer_forwarding_rule: NetworkLoadBalancerForwardingRule
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: NetworkLoadBalancerForwardingRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_forwardingrules_post_with_http_info(datacenter_id, network_load_balancer_id, network_load_balancer_forwarding_rule, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_forwardingrules_post_with_http_info(self, datacenter_id, network_load_balancer_id, network_load_balancer_forwarding_rule, **kwargs):  # noqa: E501
        """Create NLB forwarding rules  # noqa: E501

        Create a forwarding rule for the specified Network Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_post_with_http_info(datacenter_id, network_load_balancer_id, network_load_balancer_forwarding_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param network_load_balancer_forwarding_rule: The forwarding rule to create. (required)
        :type network_load_balancer_forwarding_rule: NetworkLoadBalancerForwardingRule
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(NetworkLoadBalancerForwardingRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
            'network_load_balancer_forwarding_rule',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_forwardingrules_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_forwardingrules_post`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_forwardingrules_post`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_forwarding_rule' is set
        if self.api_client.client_side_validation and ('network_load_balancer_forwarding_rule' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_forwarding_rule'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_forwarding_rule` when calling `datacenters_networkloadbalancers_forwardingrules_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501

        query_params = []
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
        if 'network_load_balancer_forwarding_rule' in local_var_params:
            body_params = local_var_params['network_load_balancer_forwarding_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NetworkLoadBalancerForwardingRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules', 'POST',
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

    def datacenters_networkloadbalancers_forwardingrules_put(self, datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule, **kwargs):  # noqa: E501
        """Modify NLB forwarding rules  # noqa: E501

        Modify the specified Network Load Balancer forwarding rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_put(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param network_load_balancer_forwarding_rule: The modified NLB forwarding rule. (required)
        :type network_load_balancer_forwarding_rule: NetworkLoadBalancerForwardingRulePut
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: NetworkLoadBalancerForwardingRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_forwardingrules_put_with_http_info(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_forwardingrules_put_with_http_info(self, datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule, **kwargs):  # noqa: E501
        """Modify NLB forwarding rules  # noqa: E501

        Modify the specified Network Load Balancer forwarding rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_forwardingrules_put_with_http_info(datacenter_id, network_load_balancer_id, forwarding_rule_id, network_load_balancer_forwarding_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param network_load_balancer_forwarding_rule: The modified NLB forwarding rule. (required)
        :type network_load_balancer_forwarding_rule: NetworkLoadBalancerForwardingRulePut
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(NetworkLoadBalancerForwardingRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
            'forwarding_rule_id',
            'network_load_balancer_forwarding_rule',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_forwardingrules_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_forwardingrules_put`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_forwardingrules_put`")  # noqa: E501
        # verify the required parameter 'forwarding_rule_id' is set
        if self.api_client.client_side_validation and ('forwarding_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['forwarding_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `forwarding_rule_id` when calling `datacenters_networkloadbalancers_forwardingrules_put`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_forwarding_rule' is set
        if self.api_client.client_side_validation and ('network_load_balancer_forwarding_rule' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_forwarding_rule'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_forwarding_rule` when calling `datacenters_networkloadbalancers_forwardingrules_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_forwardingrules_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501
        if 'forwarding_rule_id' in local_var_params:
            path_params['forwardingRuleId'] = local_var_params['forwarding_rule_id']  # noqa: E501

        query_params = []
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
        if 'network_load_balancer_forwarding_rule' in local_var_params:
            body_params = local_var_params['network_load_balancer_forwarding_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NetworkLoadBalancerForwardingRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}/forwardingrules/{forwardingRuleId}', 'PUT',
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

    def datacenters_networkloadbalancers_get(self, datacenter_id, **kwargs):  # noqa: E501
        """List Network Load Balancers  # noqa: E501

        List all the Network Load Balancers within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_get(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
        :type x_contract_number: int
        :param offset: The first element (from the complete list of the elements) to include in the response (use together with limit for pagination).
        :type offset: int
        :param limit: The maximum number of elements to return (use together with offset for pagination).
        :type limit: int
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
        :rtype: NetworkLoadBalancers
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_get_with_http_info(datacenter_id, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_get_with_http_info(self, datacenter_id, **kwargs):  # noqa: E501
        """List Network Load Balancers  # noqa: E501

        List all the Network Load Balancers within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_get_with_http_info(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
        :type x_contract_number: int
        :param offset: The first element (from the complete list of the elements) to include in the response (use together with limit for pagination).
        :type offset: int
        :param limit: The maximum number of elements to return (use together with offset for pagination).
        :type limit: int
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
        :rtype: tuple(NetworkLoadBalancers, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'pretty',
            'depth',
            'x_contract_number',
            'offset',
            'limit'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_networkloadbalancers_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_networkloadbalancers_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_networkloadbalancers_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

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
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NetworkLoadBalancers'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers', 'GET',
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

    def datacenters_networkloadbalancers_patch(self, datacenter_id, network_load_balancer_id, network_load_balancer_properties, **kwargs):  # noqa: E501
        """Partially modify Network Load Balancers  # noqa: E501

        Update the properties of the specified Network Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_patch(datacenter_id, network_load_balancer_id, network_load_balancer_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param network_load_balancer_properties: The properties of the Network Load Balancer to be updated. (required)
        :type network_load_balancer_properties: NetworkLoadBalancerProperties
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: NetworkLoadBalancer
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_patch_with_http_info(datacenter_id, network_load_balancer_id, network_load_balancer_properties, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_patch_with_http_info(self, datacenter_id, network_load_balancer_id, network_load_balancer_properties, **kwargs):  # noqa: E501
        """Partially modify Network Load Balancers  # noqa: E501

        Update the properties of the specified Network Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_patch_with_http_info(datacenter_id, network_load_balancer_id, network_load_balancer_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param network_load_balancer_properties: The properties of the Network Load Balancer to be updated. (required)
        :type network_load_balancer_properties: NetworkLoadBalancerProperties
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(NetworkLoadBalancer, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
            'network_load_balancer_properties',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_patch`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_patch`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_properties' is set
        if self.api_client.client_side_validation and ('network_load_balancer_properties' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_properties'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_properties` when calling `datacenters_networkloadbalancers_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501

        query_params = []
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
        if 'network_load_balancer_properties' in local_var_params:
            body_params = local_var_params['network_load_balancer_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NetworkLoadBalancer'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}', 'PATCH',
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

    def datacenters_networkloadbalancers_post(self, datacenter_id, network_load_balancer, **kwargs):  # noqa: E501
        """Create Network Load Balancers  # noqa: E501

        Create a Network Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_post(datacenter_id, network_load_balancer, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer: The Network Load Balancer to create. (required)
        :type network_load_balancer: NetworkLoadBalancer
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: NetworkLoadBalancer
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_post_with_http_info(datacenter_id, network_load_balancer, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_post_with_http_info(self, datacenter_id, network_load_balancer, **kwargs):  # noqa: E501
        """Create Network Load Balancers  # noqa: E501

        Create a Network Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_post_with_http_info(datacenter_id, network_load_balancer, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer: The Network Load Balancer to create. (required)
        :type network_load_balancer: NetworkLoadBalancer
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(NetworkLoadBalancer, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_post`")  # noqa: E501
        # verify the required parameter 'network_load_balancer' is set
        if self.api_client.client_side_validation and ('network_load_balancer' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer` when calling `datacenters_networkloadbalancers_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501

        query_params = []
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
        if 'network_load_balancer' in local_var_params:
            body_params = local_var_params['network_load_balancer']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NetworkLoadBalancer'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers', 'POST',
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

    def datacenters_networkloadbalancers_put(self, datacenter_id, network_load_balancer_id, network_load_balancer, **kwargs):  # noqa: E501
        """Modify Network Load Balancers  # noqa: E501

        Modify the properties of the specified Network Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_put(datacenter_id, network_load_balancer_id, network_load_balancer, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param network_load_balancer: The modified Network Load Balancer. (required)
        :type network_load_balancer: NetworkLoadBalancerPut
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: NetworkLoadBalancer
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_networkloadbalancers_put_with_http_info(datacenter_id, network_load_balancer_id, network_load_balancer, **kwargs)  # noqa: E501

    def datacenters_networkloadbalancers_put_with_http_info(self, datacenter_id, network_load_balancer_id, network_load_balancer, **kwargs):  # noqa: E501
        """Modify Network Load Balancers  # noqa: E501

        Modify the properties of the specified Network Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_networkloadbalancers_put_with_http_info(datacenter_id, network_load_balancer_id, network_load_balancer, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param network_load_balancer_id: The unique ID of the Network Load Balancer. (required)
        :type network_load_balancer_id: str
        :param network_load_balancer: The modified Network Load Balancer. (required)
        :type network_load_balancer: NetworkLoadBalancerPut
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, against which all API requests are to be executed.
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
        :rtype: tuple(NetworkLoadBalancer, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'network_load_balancer_id',
            'network_load_balancer',
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
                'response_type'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_networkloadbalancers_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_networkloadbalancers_put`")  # noqa: E501
        # verify the required parameter 'network_load_balancer_id' is set
        if self.api_client.client_side_validation and ('network_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer_id` when calling `datacenters_networkloadbalancers_put`")  # noqa: E501
        # verify the required parameter 'network_load_balancer' is set
        if self.api_client.client_side_validation and ('network_load_balancer' not in local_var_params or  # noqa: E501
                                                        local_var_params['network_load_balancer'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `network_load_balancer` when calling `datacenters_networkloadbalancers_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_networkloadbalancers_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'network_load_balancer_id' in local_var_params:
            path_params['networkLoadBalancerId'] = local_var_params['network_load_balancer_id']  # noqa: E501

        query_params = []
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
        if 'network_load_balancer' in local_var_params:
            body_params = local_var_params['network_load_balancer']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'NetworkLoadBalancer'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/networkloadbalancers/{networkLoadBalancerId}', 'PUT',
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
