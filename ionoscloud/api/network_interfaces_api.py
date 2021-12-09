from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud.api_client import ApiClient
from ionoscloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class NetworkInterfacesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def datacenters_servers_nics_delete(self, datacenter_id, server_id, nic_id, **kwargs):  # noqa: E501
        """Delete NICs  # noqa: E501

        Remove the specified NIC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_delete(datacenter_id, server_id, nic_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic_id: The unique ID of the NIC. (required)
        :type nic_id: str
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
        return self.datacenters_servers_nics_delete_with_http_info(datacenter_id, server_id, nic_id, **kwargs)  # noqa: E501

    def datacenters_servers_nics_delete_with_http_info(self, datacenter_id, server_id, nic_id, **kwargs):  # noqa: E501
        """Delete NICs  # noqa: E501

        Remove the specified NIC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_delete_with_http_info(datacenter_id, server_id, nic_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic_id: The unique ID of the NIC. (required)
        :type nic_id: str
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
            'server_id',
            'nic_id',
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
                    " to method datacenters_servers_nics_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_nics_delete`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_nics_delete`")  # noqa: E501
        # verify the required parameter 'nic_id' is set
        if self.api_client.client_side_validation and ('nic_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nic_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nic_id` when calling `datacenters_servers_nics_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501
        if 'nic_id' in local_var_params:
            path_params['nicId'] = local_var_params['nic_id']  # noqa: E501

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
            '/datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}', 'DELETE',
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

    def datacenters_servers_nics_find_by_id(self, datacenter_id, server_id, nic_id, **kwargs):  # noqa: E501
        """Retrieve NICs  # noqa: E501

        Retrieve the properties of the specified NIC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_find_by_id(datacenter_id, server_id, nic_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic_id: The unique ID of the NIC. (required)
        :type nic_id: str
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
        :rtype: Nic
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_nics_find_by_id_with_http_info(datacenter_id, server_id, nic_id, **kwargs)  # noqa: E501

    def datacenters_servers_nics_find_by_id_with_http_info(self, datacenter_id, server_id, nic_id, **kwargs):  # noqa: E501
        """Retrieve NICs  # noqa: E501

        Retrieve the properties of the specified NIC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_find_by_id_with_http_info(datacenter_id, server_id, nic_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic_id: The unique ID of the NIC. (required)
        :type nic_id: str
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
        :rtype: tuple(Nic, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'nic_id',
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
                    " to method datacenters_servers_nics_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_nics_find_by_id`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_nics_find_by_id`")  # noqa: E501
        # verify the required parameter 'nic_id' is set
        if self.api_client.client_side_validation and ('nic_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nic_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nic_id` when calling `datacenters_servers_nics_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501
        if 'nic_id' in local_var_params:
            path_params['nicId'] = local_var_params['nic_id']  # noqa: E501

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

        response_type = 'Nic'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}', 'GET',
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

    def datacenters_servers_nics_get(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """List NICs  # noqa: E501

        List all NICs, attached to the specified server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_get(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
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
        :rtype: Nics
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_nics_get_with_http_info(datacenter_id, server_id, **kwargs)  # noqa: E501

    def datacenters_servers_nics_get_with_http_info(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """List NICs  # noqa: E501

        List all NICs, attached to the specified server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_get_with_http_info(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
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
        :rtype: tuple(Nics, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
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
                    " to method datacenters_servers_nics_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_nics_get`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_nics_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_servers_nics_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_servers_nics_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_servers_nics_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501

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

        response_type = 'Nics'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/nics', 'GET',
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

    def datacenters_servers_nics_patch(self, datacenter_id, server_id, nic_id, nic, **kwargs):  # noqa: E501
        """Partially modify NICs  # noqa: E501

        Update the properties of the specified NIC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_patch(datacenter_id, server_id, nic_id, nic, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic_id: The unique ID of the NIC. (required)
        :type nic_id: str
        :param nic: The properties of the NIC to be updated. (required)
        :type nic: NicProperties
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
        :rtype: Nic
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_nics_patch_with_http_info(datacenter_id, server_id, nic_id, nic, **kwargs)  # noqa: E501

    def datacenters_servers_nics_patch_with_http_info(self, datacenter_id, server_id, nic_id, nic, **kwargs):  # noqa: E501
        """Partially modify NICs  # noqa: E501

        Update the properties of the specified NIC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_patch_with_http_info(datacenter_id, server_id, nic_id, nic, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic_id: The unique ID of the NIC. (required)
        :type nic_id: str
        :param nic: The properties of the NIC to be updated. (required)
        :type nic: NicProperties
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
        :rtype: tuple(Nic, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'nic_id',
            'nic',
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
                    " to method datacenters_servers_nics_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_nics_patch`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_nics_patch`")  # noqa: E501
        # verify the required parameter 'nic_id' is set
        if self.api_client.client_side_validation and ('nic_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nic_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nic_id` when calling `datacenters_servers_nics_patch`")  # noqa: E501
        # verify the required parameter 'nic' is set
        if self.api_client.client_side_validation and ('nic' not in local_var_params or  # noqa: E501
                                                        local_var_params['nic'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nic` when calling `datacenters_servers_nics_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501
        if 'nic_id' in local_var_params:
            path_params['nicId'] = local_var_params['nic_id']  # noqa: E501

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
        if 'nic' in local_var_params:
            body_params = local_var_params['nic']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Nic'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}', 'PATCH',
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

    def datacenters_servers_nics_post(self, datacenter_id, server_id, nic, **kwargs):  # noqa: E501
        """Create NICs  # noqa: E501

        Add a NIC to the specified server. The combined total of NICs and attached volumes cannot exceed 24 per server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_post(datacenter_id, server_id, nic, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic: The NIC to create. (required)
        :type nic: Nic
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
        :rtype: Nic
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_nics_post_with_http_info(datacenter_id, server_id, nic, **kwargs)  # noqa: E501

    def datacenters_servers_nics_post_with_http_info(self, datacenter_id, server_id, nic, **kwargs):  # noqa: E501
        """Create NICs  # noqa: E501

        Add a NIC to the specified server. The combined total of NICs and attached volumes cannot exceed 24 per server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_post_with_http_info(datacenter_id, server_id, nic, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic: The NIC to create. (required)
        :type nic: Nic
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
        :rtype: tuple(Nic, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'nic',
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
                    " to method datacenters_servers_nics_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_nics_post`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_nics_post`")  # noqa: E501
        # verify the required parameter 'nic' is set
        if self.api_client.client_side_validation and ('nic' not in local_var_params or  # noqa: E501
                                                        local_var_params['nic'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nic` when calling `datacenters_servers_nics_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501

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
        if 'nic' in local_var_params:
            body_params = local_var_params['nic']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Nic'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/nics', 'POST',
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

    def datacenters_servers_nics_put(self, datacenter_id, server_id, nic_id, nic, **kwargs):  # noqa: E501
        """Modify NICs  # noqa: E501

        Modify the properties of the specified NIC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_put(datacenter_id, server_id, nic_id, nic, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic_id: The unique ID of the NIC. (required)
        :type nic_id: str
        :param nic: The modified NIC (required)
        :type nic: NicPut
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
        :rtype: Nic
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_nics_put_with_http_info(datacenter_id, server_id, nic_id, nic, **kwargs)  # noqa: E501

    def datacenters_servers_nics_put_with_http_info(self, datacenter_id, server_id, nic_id, nic, **kwargs):  # noqa: E501
        """Modify NICs  # noqa: E501

        Modify the properties of the specified NIC.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_put_with_http_info(datacenter_id, server_id, nic_id, nic, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic_id: The unique ID of the NIC. (required)
        :type nic_id: str
        :param nic: The modified NIC (required)
        :type nic: NicPut
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
        :rtype: tuple(Nic, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'nic_id',
            'nic',
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
                    " to method datacenters_servers_nics_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_nics_put`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_nics_put`")  # noqa: E501
        # verify the required parameter 'nic_id' is set
        if self.api_client.client_side_validation and ('nic_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nic_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nic_id` when calling `datacenters_servers_nics_put`")  # noqa: E501
        # verify the required parameter 'nic' is set
        if self.api_client.client_side_validation and ('nic' not in local_var_params or  # noqa: E501
                                                        local_var_params['nic'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nic` when calling `datacenters_servers_nics_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501
        if 'nic_id' in local_var_params:
            path_params['nicId'] = local_var_params['nic_id']  # noqa: E501

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
        if 'nic' in local_var_params:
            body_params = local_var_params['nic']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Nic'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}', 'PUT',
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
