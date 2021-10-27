from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud.api_client import ApiClient
from ionoscloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DataCenterApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def datacenters_delete(self, datacenter_id, **kwargs):  # noqa: E501
        """Delete a Data Center  # noqa: E501

        Will remove all objects within the datacenter and remove the datacenter object itself, too. This is a highly destructive method which should be used with caution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_delete(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
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
        return self.datacenters_delete_with_http_info(datacenter_id, **kwargs)  # noqa: E501

    def datacenters_delete_with_http_info(self, datacenter_id, **kwargs):  # noqa: E501
        """Delete a Data Center  # noqa: E501

        Will remove all objects within the datacenter and remove the datacenter object itself, too. This is a highly destructive method which should be used with caution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_delete_with_http_info(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
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
                    " to method datacenters_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_delete`, must be a value greater than or equal to `0`")  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}', 'DELETE',
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

    def datacenters_find_by_id(self, datacenter_id, **kwargs):  # noqa: E501
        """Retrieve a Data Center  # noqa: E501

        You can retrieve a data center by using the resource's ID. This value can be found in the response body when a datacenter is created or when you GET a list of datacenters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_find_by_id(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
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
        :rtype: Datacenter
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_find_by_id_with_http_info(datacenter_id, **kwargs)  # noqa: E501

    def datacenters_find_by_id_with_http_info(self, datacenter_id, **kwargs):  # noqa: E501
        """Retrieve a Data Center  # noqa: E501

        You can retrieve a data center by using the resource's ID. This value can be found in the response body when a datacenter is created or when you GET a list of datacenters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_find_by_id_with_http_info(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
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
        :rtype: tuple(Datacenter, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
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
                    " to method datacenters_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Datacenter'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}', 'GET',
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

    def datacenters_get(self, **kwargs):  # noqa: E501
        """List Data Centers under your account  # noqa: E501

        You can retrieve a list of data centers provisioned under your account. Default list will contain first 100 items. For more items use pagination query parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_get(async_req=True)
        >>> result = thread.get()

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
        :rtype: Datacenters
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_get_with_http_info(**kwargs)  # noqa: E501

    def datacenters_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Data Centers under your account  # noqa: E501

        You can retrieve a list of data centers provisioned under your account. Default list will contain first 100 items. For more items use pagination query parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_get_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(Datacenters, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
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
                    " to method datacenters_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

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

        response_type = 'Datacenters'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters', 'GET',
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

    def datacenters_patch(self, datacenter_id, datacenter, **kwargs):  # noqa: E501
        """Partially modify a Data Center  # noqa: E501

        You can use update datacenter to re-name the datacenter or update its description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_patch(datacenter_id, datacenter, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param datacenter: Modified properties of Data Center (required)
        :type datacenter: DatacenterProperties
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
        :rtype: Datacenter
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_patch_with_http_info(datacenter_id, datacenter, **kwargs)  # noqa: E501

    def datacenters_patch_with_http_info(self, datacenter_id, datacenter, **kwargs):  # noqa: E501
        """Partially modify a Data Center  # noqa: E501

        You can use update datacenter to re-name the datacenter or update its description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_patch_with_http_info(datacenter_id, datacenter, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param datacenter: Modified properties of Data Center (required)
        :type datacenter: DatacenterProperties
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
        :rtype: tuple(Datacenter, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'datacenter',
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
                    " to method datacenters_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_patch`")  # noqa: E501
        # verify the required parameter 'datacenter' is set
        if self.api_client.client_side_validation and ('datacenter' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter` when calling `datacenters_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_patch`, must be a value greater than or equal to `0`")  # noqa: E501
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
        if 'datacenter' in local_var_params:
            body_params = local_var_params['datacenter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Datacenter'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}', 'PATCH',
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

    def datacenters_post(self, datacenter, **kwargs):  # noqa: E501
        """Create a Data Center  # noqa: E501

        Virtual data centers are the foundation of the platform. They act as logical containers for all other objects you will be creating, e.g. servers. You can provision as many data centers as you want. Datacenters have their own private network and are logically segmented from each other to create isolation. You can use this POST method to create a simple datacenter or to create a datacenter with multiple objects under it such as servers and storage volumes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_post(datacenter, async_req=True)
        >>> result = thread.get()

        :param datacenter: Datacenter to be created (required)
        :type datacenter: Datacenter
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
        :rtype: Datacenter
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_post_with_http_info(datacenter, **kwargs)  # noqa: E501

    def datacenters_post_with_http_info(self, datacenter, **kwargs):  # noqa: E501
        """Create a Data Center  # noqa: E501

        Virtual data centers are the foundation of the platform. They act as logical containers for all other objects you will be creating, e.g. servers. You can provision as many data centers as you want. Datacenters have their own private network and are logically segmented from each other to create isolation. You can use this POST method to create a simple datacenter or to create a datacenter with multiple objects under it such as servers and storage volumes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_post_with_http_info(datacenter, async_req=True)
        >>> result = thread.get()

        :param datacenter: Datacenter to be created (required)
        :type datacenter: Datacenter
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
        :rtype: tuple(Datacenter, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter',
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
                    " to method datacenters_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter' is set
        if self.api_client.client_side_validation and ('datacenter' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter` when calling `datacenters_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

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
        if 'datacenter' in local_var_params:
            body_params = local_var_params['datacenter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Datacenter'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters', 'POST',
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

    def datacenters_put(self, datacenter_id, datacenter, **kwargs):  # noqa: E501
        """Modify a Data Center  # noqa: E501

        You can use update datacenter to re-name the datacenter or update its description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_put(datacenter_id, datacenter, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param datacenter: Modified Data Center (required)
        :type datacenter: Datacenter
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
        :rtype: Datacenter
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_put_with_http_info(datacenter_id, datacenter, **kwargs)  # noqa: E501

    def datacenters_put_with_http_info(self, datacenter_id, datacenter, **kwargs):  # noqa: E501
        """Modify a Data Center  # noqa: E501

        You can use update datacenter to re-name the datacenter or update its description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_put_with_http_info(datacenter_id, datacenter, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param datacenter: Modified Data Center (required)
        :type datacenter: Datacenter
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
        :rtype: tuple(Datacenter, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'datacenter',
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
                    " to method datacenters_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_put`")  # noqa: E501
        # verify the required parameter 'datacenter' is set
        if self.api_client.client_side_validation and ('datacenter' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter` when calling `datacenters_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_put`, must be a value greater than or equal to `0`")  # noqa: E501
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
        if 'datacenter' in local_var_params:
            body_params = local_var_params['datacenter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Datacenter'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}', 'PUT',
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
