from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud.api_client import ApiClient
from ionoscloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ServerApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def datacenters_servers_cdroms_delete(self, datacenter_id, server_id, cdrom_id, **kwargs):  # noqa: E501
        """Detach a CD-ROM  # noqa: E501

        This will detach a CD-ROM from the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_cdroms_delete(datacenter_id, server_id, cdrom_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param cdrom_id: The unique ID of the CD-ROM (required)
        :type cdrom_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_cdroms_delete_with_http_info(datacenter_id, server_id, cdrom_id, **kwargs)  # noqa: E501

    def datacenters_servers_cdroms_delete_with_http_info(self, datacenter_id, server_id, cdrom_id, **kwargs):  # noqa: E501
        """Detach a CD-ROM  # noqa: E501

        This will detach a CD-ROM from the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_cdroms_delete_with_http_info(datacenter_id, server_id, cdrom_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param cdrom_id: The unique ID of the CD-ROM (required)
        :type cdrom_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'cdrom_id',
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
                    " to method datacenters_servers_cdroms_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_cdroms_delete`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_cdroms_delete`")  # noqa: E501
        # verify the required parameter 'cdrom_id' is set
        if self.api_client.client_side_validation and ('cdrom_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cdrom_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cdrom_id` when calling `datacenters_servers_cdroms_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_cdroms_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_cdroms_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501
        if 'cdrom_id' in local_var_params:
            path_params['cdromId'] = local_var_params['cdrom_id']  # noqa: E501

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

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/cdroms/{cdromId}', 'DELETE',
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

    def datacenters_servers_cdroms_find_by_id(self, datacenter_id, server_id, cdrom_id, **kwargs):  # noqa: E501
        """Retrieve an attached CD-ROM  # noqa: E501

        You can retrieve a specific CD-ROM attached to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_cdroms_find_by_id(datacenter_id, server_id, cdrom_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param cdrom_id: The unique ID of the CD-ROM (required)
        :type cdrom_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: Image
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_cdroms_find_by_id_with_http_info(datacenter_id, server_id, cdrom_id, **kwargs)  # noqa: E501

    def datacenters_servers_cdroms_find_by_id_with_http_info(self, datacenter_id, server_id, cdrom_id, **kwargs):  # noqa: E501
        """Retrieve an attached CD-ROM  # noqa: E501

        You can retrieve a specific CD-ROM attached to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_cdroms_find_by_id_with_http_info(datacenter_id, server_id, cdrom_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param cdrom_id: The unique ID of the CD-ROM (required)
        :type cdrom_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(Image, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'cdrom_id',
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
                    " to method datacenters_servers_cdroms_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_cdroms_find_by_id`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_cdroms_find_by_id`")  # noqa: E501
        # verify the required parameter 'cdrom_id' is set
        if self.api_client.client_side_validation and ('cdrom_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cdrom_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cdrom_id` when calling `datacenters_servers_cdroms_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_cdroms_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_cdroms_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501
        if 'cdrom_id' in local_var_params:
            path_params['cdromId'] = local_var_params['cdrom_id']  # noqa: E501

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

        response_type = 'Image'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/cdroms/{cdromId}', 'GET',
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

    def datacenters_servers_cdroms_get(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """List attached CD-ROMs   # noqa: E501

        You can retrieve a list of CD-ROMs attached to the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_cdroms_get(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param offset: the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination)
        :type offset: int
        :param limit: the maximum number of elements to return (use together with <code>offset</code> for pagination)
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
        :rtype: Cdroms
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_cdroms_get_with_http_info(datacenter_id, server_id, **kwargs)  # noqa: E501

    def datacenters_servers_cdroms_get_with_http_info(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """List attached CD-ROMs   # noqa: E501

        You can retrieve a list of CD-ROMs attached to the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_cdroms_get_with_http_info(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param offset: the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination)
        :type offset: int
        :param limit: the maximum number of elements to return (use together with <code>offset</code> for pagination)
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
        :rtype: tuple(Cdroms, status_code(int), headers(HTTPHeaderDict))
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
                    " to method datacenters_servers_cdroms_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_cdroms_get`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_cdroms_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_cdroms_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_cdroms_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_servers_cdroms_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_servers_cdroms_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_servers_cdroms_get`, must be a value greater than or equal to `1`")  # noqa: E501
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

        response_type = 'Cdroms'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/cdroms', 'GET',
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

    def datacenters_servers_cdroms_post(self, datacenter_id, server_id, cdrom, **kwargs):  # noqa: E501
        """Attach a CD-ROM  # noqa: E501

        You can attach a CD-ROM to an existing server. You can attach up to 2 CD-ROMs to one server.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_cdroms_post(datacenter_id, server_id, cdrom, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param cdrom: CD-ROM to be attached (required)
        :type cdrom: Image
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: Image
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_cdroms_post_with_http_info(datacenter_id, server_id, cdrom, **kwargs)  # noqa: E501

    def datacenters_servers_cdroms_post_with_http_info(self, datacenter_id, server_id, cdrom, **kwargs):  # noqa: E501
        """Attach a CD-ROM  # noqa: E501

        You can attach a CD-ROM to an existing server. You can attach up to 2 CD-ROMs to one server.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_cdroms_post_with_http_info(datacenter_id, server_id, cdrom, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param cdrom: CD-ROM to be attached (required)
        :type cdrom: Image
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(Image, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'cdrom',
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
                    " to method datacenters_servers_cdroms_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_cdroms_post`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_cdroms_post`")  # noqa: E501
        # verify the required parameter 'cdrom' is set
        if self.api_client.client_side_validation and ('cdrom' not in local_var_params or  # noqa: E501
                                                        local_var_params['cdrom'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cdrom` when calling `datacenters_servers_cdroms_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_cdroms_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_cdroms_post`, must be a value greater than or equal to `0`")  # noqa: E501
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
        if 'cdrom' in local_var_params:
            body_params = local_var_params['cdrom']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Image'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/cdroms', 'POST',
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

    def datacenters_servers_delete(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Delete a Server  # noqa: E501

        This will remove a server from your datacenter; however, it will not remove the storage volumes attached to the server. You will need to make a separate API call to perform that action  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_delete(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_delete_with_http_info(datacenter_id, server_id, **kwargs)  # noqa: E501

    def datacenters_servers_delete_with_http_info(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Delete a Server  # noqa: E501

        This will remove a server from your datacenter; however, it will not remove the storage volumes attached to the server. You will need to make a separate API call to perform that action  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_delete_with_http_info(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
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
                    " to method datacenters_servers_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_delete`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_delete`, must be a value greater than or equal to `0`")  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}', 'DELETE',
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

    def datacenters_servers_find_by_id(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Retrieve a Server  # noqa: E501

        Returns information about a server such as its configuration, provisioning status, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_find_by_id(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: Server
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_find_by_id_with_http_info(datacenter_id, server_id, **kwargs)  # noqa: E501

    def datacenters_servers_find_by_id_with_http_info(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Retrieve a Server  # noqa: E501

        Returns information about a server such as its configuration, provisioning status, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_find_by_id_with_http_info(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(Server, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
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
                    " to method datacenters_servers_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_find_by_id`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Server'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}', 'GET',
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

    def datacenters_servers_get(self, datacenter_id, **kwargs):  # noqa: E501
        """List Servers   # noqa: E501

        You can retrieve a list of servers within a datacenter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_get(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param upgrade_needed: It can be used to filter which servers can be upgraded which can not be upgraded.
        :type upgrade_needed: bool
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param offset: the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination)
        :type offset: int
        :param limit: the maximum number of elements to return (use together with <code>offset</code> for pagination)
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
        :rtype: Servers
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_get_with_http_info(datacenter_id, **kwargs)  # noqa: E501

    def datacenters_servers_get_with_http_info(self, datacenter_id, **kwargs):  # noqa: E501
        """List Servers   # noqa: E501

        You can retrieve a list of servers within a datacenter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_get_with_http_info(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param upgrade_needed: It can be used to filter which servers can be upgraded which can not be upgraded.
        :type upgrade_needed: bool
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param offset: the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination)
        :type offset: int
        :param limit: the maximum number of elements to return (use together with <code>offset</code> for pagination)
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
        :rtype: tuple(Servers, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'pretty',
            'depth',
            'upgrade_needed',
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
                    " to method datacenters_servers_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_servers_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_servers_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_servers_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501
        if 'upgrade_needed' in local_var_params and local_var_params['upgrade_needed'] is not None:  # noqa: E501
            query_params.append(('upgradeNeeded', local_var_params['upgrade_needed']))  # noqa: E501
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

        response_type = 'Servers'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers', 'GET',
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

    def datacenters_servers_patch(self, datacenter_id, server_id, server, **kwargs):  # noqa: E501
        """Partially modify a Server  # noqa: E501

        You can use update attributes of a server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_patch(datacenter_id, server_id, server, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server (required)
        :type server_id: str
        :param server: Modified properties of Server (required)
        :type server: ServerProperties
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: Server
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_patch_with_http_info(datacenter_id, server_id, server, **kwargs)  # noqa: E501

    def datacenters_servers_patch_with_http_info(self, datacenter_id, server_id, server, **kwargs):  # noqa: E501
        """Partially modify a Server  # noqa: E501

        You can use update attributes of a server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_patch_with_http_info(datacenter_id, server_id, server, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server (required)
        :type server_id: str
        :param server: Modified properties of Server (required)
        :type server: ServerProperties
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(Server, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'server',
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
                    " to method datacenters_servers_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_patch`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_patch`")  # noqa: E501
        # verify the required parameter 'server' is set
        if self.api_client.client_side_validation and ('server' not in local_var_params or  # noqa: E501
                                                        local_var_params['server'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server` when calling `datacenters_servers_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_patch`, must be a value greater than or equal to `0`")  # noqa: E501
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
        if 'server' in local_var_params:
            body_params = local_var_params['server']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Server'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}', 'PATCH',
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

    def datacenters_servers_post(self, datacenter_id, server, **kwargs):  # noqa: E501
        """Create a Server  # noqa: E501

        Creates a server within an existing datacenter. You can configure the boot volume and connect the server to an existing LAN.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_post(datacenter_id, server, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server: Server to be created (required)
        :type server: Server
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: Server
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_post_with_http_info(datacenter_id, server, **kwargs)  # noqa: E501

    def datacenters_servers_post_with_http_info(self, datacenter_id, server, **kwargs):  # noqa: E501
        """Create a Server  # noqa: E501

        Creates a server within an existing datacenter. You can configure the boot volume and connect the server to an existing LAN.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_post_with_http_info(datacenter_id, server, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server: Server to be created (required)
        :type server: Server
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(Server, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server',
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
                    " to method datacenters_servers_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_post`")  # noqa: E501
        # verify the required parameter 'server' is set
        if self.api_client.client_side_validation and ('server' not in local_var_params or  # noqa: E501
                                                        local_var_params['server'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server` when calling `datacenters_servers_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_post`, must be a value greater than or equal to `0`")  # noqa: E501
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
        if 'server' in local_var_params:
            body_params = local_var_params['server']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Server'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers', 'POST',
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

    def datacenters_servers_put(self, datacenter_id, server_id, server, **kwargs):  # noqa: E501
        """Modify a Server  # noqa: E501

        Allows to modify the attributes of a Server. From v5 onwards 'allowReboot' attribute will no longer be available. For certain server property change it was earlier forced to be provided. Now this behaviour is implicit and backend will do this automatically e.g. in earlier versions, when CPU family changes, the 'allowReboot' property was required to be set to true which will no longer be the case and the server will be rebooted automatically  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_put(datacenter_id, server_id, server, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server (required)
        :type server_id: str
        :param server: Modified Server (required)
        :type server: Server
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: Server
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_put_with_http_info(datacenter_id, server_id, server, **kwargs)  # noqa: E501

    def datacenters_servers_put_with_http_info(self, datacenter_id, server_id, server, **kwargs):  # noqa: E501
        """Modify a Server  # noqa: E501

        Allows to modify the attributes of a Server. From v5 onwards 'allowReboot' attribute will no longer be available. For certain server property change it was earlier forced to be provided. Now this behaviour is implicit and backend will do this automatically e.g. in earlier versions, when CPU family changes, the 'allowReboot' property was required to be set to true which will no longer be the case and the server will be rebooted automatically  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_put_with_http_info(datacenter_id, server_id, server, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server (required)
        :type server_id: str
        :param server: Modified Server (required)
        :type server: Server
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(Server, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'server',
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
                    " to method datacenters_servers_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_put`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_put`")  # noqa: E501
        # verify the required parameter 'server' is set
        if self.api_client.client_side_validation and ('server' not in local_var_params or  # noqa: E501
                                                        local_var_params['server'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server` when calling `datacenters_servers_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_put`, must be a value greater than or equal to `0`")  # noqa: E501
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
        if 'server' in local_var_params:
            body_params = local_var_params['server']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Server'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}', 'PUT',
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

    def datacenters_servers_reboot_post(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Reboot a Server  # noqa: E501

        This will force a hard reboot of the server. Do not use this method if you want to gracefully reboot the machine. This is the equivalent of powering off the machine and turning it back on.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_reboot_post(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_reboot_post_with_http_info(datacenter_id, server_id, **kwargs)  # noqa: E501

    def datacenters_servers_reboot_post_with_http_info(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Reboot a Server  # noqa: E501

        This will force a hard reboot of the server. Do not use this method if you want to gracefully reboot the machine. This is the equivalent of powering off the machine and turning it back on.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_reboot_post_with_http_info(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
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
                    " to method datacenters_servers_reboot_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_reboot_post`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_reboot_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_reboot_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_reboot_post`, must be a value greater than or equal to `0`")  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/reboot', 'POST',
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

    def datacenters_servers_start_post(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Start a Server  # noqa: E501

        This will start a server. If the server's public IP was deallocated then a new IP will be assigned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_start_post(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_start_post_with_http_info(datacenter_id, server_id, **kwargs)  # noqa: E501

    def datacenters_servers_start_post_with_http_info(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Start a Server  # noqa: E501

        This will start a server. If the server's public IP was deallocated then a new IP will be assigned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_start_post_with_http_info(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
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
                    " to method datacenters_servers_start_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_start_post`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_start_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_start_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_start_post`, must be a value greater than or equal to `0`")  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/start', 'POST',
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

    def datacenters_servers_stop_post(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Stop a Server  # noqa: E501

        This will stop a server. The machine will be forcefully powered off, billing will cease, and the public IP, if one is allocated, will be deallocated. The operation is not supported for Cube servers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_stop_post(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_stop_post_with_http_info(datacenter_id, server_id, **kwargs)  # noqa: E501

    def datacenters_servers_stop_post_with_http_info(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Stop a Server  # noqa: E501

        This will stop a server. The machine will be forcefully powered off, billing will cease, and the public IP, if one is allocated, will be deallocated. The operation is not supported for Cube servers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_stop_post_with_http_info(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
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
                    " to method datacenters_servers_stop_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_stop_post`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_stop_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_stop_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_stop_post`, must be a value greater than or equal to `0`")  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/stop', 'POST',
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

    def datacenters_servers_upgrade_post(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Upgrade a Server  # noqa: E501

        This will upgrade the version of the server, if needed. To verify if there is an upgrade available for a server, call '/datacenters/{datacenterId}/servers?upgradeNeeded=true'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_upgrade_post(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_upgrade_post_with_http_info(datacenter_id, server_id, **kwargs)  # noqa: E501

    def datacenters_servers_upgrade_post_with_http_info(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """Upgrade a Server  # noqa: E501

        This will upgrade the version of the server, if needed. To verify if there is an upgrade available for a server, call '/datacenters/{datacenterId}/servers?upgradeNeeded=true'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_upgrade_post_with_http_info(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
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
                    " to method datacenters_servers_upgrade_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_upgrade_post`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_upgrade_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_upgrade_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_upgrade_post`, must be a value greater than or equal to `0`")  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/upgrade', 'POST',
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

    def datacenters_servers_volumes_delete(self, datacenter_id, server_id, volume_id, **kwargs):  # noqa: E501
        """Detach a volume  # noqa: E501

        This will detach the volume from the server. This will not delete the volume from your datacenter. You will need to make a separate request to perform a deletion  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_volumes_delete(datacenter_id, server_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_volumes_delete_with_http_info(datacenter_id, server_id, volume_id, **kwargs)  # noqa: E501

    def datacenters_servers_volumes_delete_with_http_info(self, datacenter_id, server_id, volume_id, **kwargs):  # noqa: E501
        """Detach a volume  # noqa: E501

        This will detach the volume from the server. This will not delete the volume from your datacenter. You will need to make a separate request to perform a deletion  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_volumes_delete_with_http_info(datacenter_id, server_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'volume_id',
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
                    " to method datacenters_servers_volumes_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_volumes_delete`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_volumes_delete`")  # noqa: E501
        # verify the required parameter 'volume_id' is set
        if self.api_client.client_side_validation and ('volume_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume_id` when calling `datacenters_servers_volumes_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_volumes_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_volumes_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501
        if 'volume_id' in local_var_params:
            path_params['volumeId'] = local_var_params['volume_id']  # noqa: E501

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

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/volumes/{volumeId}', 'DELETE',
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

    def datacenters_servers_volumes_find_by_id(self, datacenter_id, server_id, volume_id, **kwargs):  # noqa: E501
        """Retrieve an attached volume  # noqa: E501

        This will retrieve the properties of an attached volume.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_volumes_find_by_id(datacenter_id, server_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: Volume
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_volumes_find_by_id_with_http_info(datacenter_id, server_id, volume_id, **kwargs)  # noqa: E501

    def datacenters_servers_volumes_find_by_id_with_http_info(self, datacenter_id, server_id, volume_id, **kwargs):  # noqa: E501
        """Retrieve an attached volume  # noqa: E501

        This will retrieve the properties of an attached volume.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_volumes_find_by_id_with_http_info(datacenter_id, server_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(Volume, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'volume_id',
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
                    " to method datacenters_servers_volumes_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_volumes_find_by_id`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_volumes_find_by_id`")  # noqa: E501
        # verify the required parameter 'volume_id' is set
        if self.api_client.client_side_validation and ('volume_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume_id` when calling `datacenters_servers_volumes_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_volumes_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_volumes_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501
        if 'volume_id' in local_var_params:
            path_params['volumeId'] = local_var_params['volume_id']  # noqa: E501

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

        response_type = 'Volume'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/volumes/{volumeId}', 'GET',
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

    def datacenters_servers_volumes_get(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """List Attached Volumes  # noqa: E501

        You can retrieve a list of volumes attached to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_volumes_get(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param offset: the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination)
        :type offset: int
        :param limit: the maximum number of elements to return (use together with <code>offset</code> for pagination)
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
        :rtype: AttachedVolumes
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_volumes_get_with_http_info(datacenter_id, server_id, **kwargs)  # noqa: E501

    def datacenters_servers_volumes_get_with_http_info(self, datacenter_id, server_id, **kwargs):  # noqa: E501
        """List Attached Volumes  # noqa: E501

        You can retrieve a list of volumes attached to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_volumes_get_with_http_info(datacenter_id, server_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param offset: the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination)
        :type offset: int
        :param limit: the maximum number of elements to return (use together with <code>offset</code> for pagination)
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
        :rtype: tuple(AttachedVolumes, status_code(int), headers(HTTPHeaderDict))
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
                    " to method datacenters_servers_volumes_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_volumes_get`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_volumes_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_volumes_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_volumes_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_servers_volumes_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_servers_volumes_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_servers_volumes_get`, must be a value greater than or equal to `1`")  # noqa: E501
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
        auth_settings = ['Basic Authentication']  # noqa: E501

        response_type = 'AttachedVolumes'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/volumes', 'GET',
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

    def datacenters_servers_volumes_post(self, datacenter_id, server_id, volume, **kwargs):  # noqa: E501
        """Attach a volume  # noqa: E501

        This will attach a pre-existing storage volume to the server. It is also possible to create and attach a volume in one step just by providing a new volume description as payload. Combine count of Nics and volumes attached to the server should not exceed size 24.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_volumes_post(datacenter_id, server_id, volume, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param volume: Volume to be attached (created and attached) (required)
        :type volume: Volume
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: Volume
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_volumes_post_with_http_info(datacenter_id, server_id, volume, **kwargs)  # noqa: E501

    def datacenters_servers_volumes_post_with_http_info(self, datacenter_id, server_id, volume, **kwargs):  # noqa: E501
        """Attach a volume  # noqa: E501

        This will attach a pre-existing storage volume to the server. It is also possible to create and attach a volume in one step just by providing a new volume description as payload. Combine count of Nics and volumes attached to the server should not exceed size 24.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_volumes_post_with_http_info(datacenter_id, server_id, volume, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the Datacenter (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the Server (required)
        :type server_id: str
        :param volume: Volume to be attached (created and attached) (required)
        :type volume: Volume
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
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
        :rtype: tuple(Volume, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'volume',
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
                    " to method datacenters_servers_volumes_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_volumes_post`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_volumes_post`")  # noqa: E501
        # verify the required parameter 'volume' is set
        if self.api_client.client_side_validation and ('volume' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume` when calling `datacenters_servers_volumes_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_volumes_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_volumes_post`, must be a value greater than or equal to `0`")  # noqa: E501
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
        if 'volume' in local_var_params:
            body_params = local_var_params['volume']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication']  # noqa: E501

        response_type = 'Volume'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/volumes', 'POST',
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
