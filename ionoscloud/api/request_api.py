from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud.api_client import ApiClient
from ionoscloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RequestApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def requests_find_by_id(self, request_id, **kwargs):  # noqa: E501
        """Retrieve a Request  # noqa: E501

        Retrieves the attributes of a given request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.requests_find_by_id(request_id, async_req=True)
        >>> result = thread.get()

        :param request_id: (required)
        :type request_id: str
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
        :rtype: Request
        """
        kwargs['_return_http_data_only'] = True
        return self.requests_find_by_id_with_http_info(request_id, **kwargs)  # noqa: E501

    def requests_find_by_id_with_http_info(self, request_id, **kwargs):  # noqa: E501
        """Retrieve a Request  # noqa: E501

        Retrieves the attributes of a given request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.requests_find_by_id_with_http_info(request_id, async_req=True)
        >>> result = thread.get()

        :param request_id: (required)
        :type request_id: str
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
        :rtype: tuple(Request, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'request_id',
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
                    " to method requests_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'request_id' is set
        if self.api_client.client_side_validation and ('request_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['request_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request_id` when calling `requests_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `requests_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `requests_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'request_id' in local_var_params:
            path_params['requestId'] = local_var_params['request_id']  # noqa: E501

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

        response_type = 'Request'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/requests/{requestId}', 'GET',
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

    def requests_get(self, **kwargs):  # noqa: E501
        """List Requests  # noqa: E501

        Retrieve a list of API requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.requests_get(async_req=True)
        >>> result = thread.get()

        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param filter_status: Request filter to fetch all requests based on a particular status [QUEUED, RUNNING, DONE, FAILED]. It doesn't depend on depth query parameter
        :type filter_status: str
        :param filter_created_after: Request filter to fetch all requests created after the specified date. It doesn't depend on depth query parameter. Date format e.g. 2021-01-01+00:00:00
        :type filter_created_after: str
        :param filter_created_before: Request filter to fetch all requests created before the specified date. It doesn't depend on depth query parameter. Date format e.g. 2021-01-01+00:00:00
        :type filter_created_before: str
        :param filter_created_date: Response filter to select and display only the requests that contains the specified createdDate. The value is case insensitive and it  depends on depth query parameter that should have a value greater than 0. Date format e.g. 2020-11-16T17:42:59Z
        :type filter_created_date: str
        :param filter_created_by: Response filter to select and display only the requests that contains the specified createdBy. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_created_by: str
        :param filter_etag: Response filter to select and display only the requests that contains the specified etag. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_etag: str
        :param filter_request_status: Response filter to select and display only the requests that contains the specified requestStatus. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_request_status: str
        :param filter_method: Response filter to select and display only the requests that contains the specified method. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_method: str
        :param filter_headers: Response filter to select and display only the requests that contains the specified headers. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_headers: str
        :param filter_body: Response filter to select and display only the requests that contains the specified body. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_body: str
        :param filter_url: Response filter to select and display only the requests that contains the specified url. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_url: str
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
        :rtype: Requests
        """
        kwargs['_return_http_data_only'] = True
        return self.requests_get_with_http_info(**kwargs)  # noqa: E501

    def requests_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Requests  # noqa: E501

        Retrieve a list of API requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.requests_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param filter_status: Request filter to fetch all requests based on a particular status [QUEUED, RUNNING, DONE, FAILED]. It doesn't depend on depth query parameter
        :type filter_status: str
        :param filter_created_after: Request filter to fetch all requests created after the specified date. It doesn't depend on depth query parameter. Date format e.g. 2021-01-01+00:00:00
        :type filter_created_after: str
        :param filter_created_before: Request filter to fetch all requests created before the specified date. It doesn't depend on depth query parameter. Date format e.g. 2021-01-01+00:00:00
        :type filter_created_before: str
        :param filter_created_date: Response filter to select and display only the requests that contains the specified createdDate. The value is case insensitive and it  depends on depth query parameter that should have a value greater than 0. Date format e.g. 2020-11-16T17:42:59Z
        :type filter_created_date: str
        :param filter_created_by: Response filter to select and display only the requests that contains the specified createdBy. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_created_by: str
        :param filter_etag: Response filter to select and display only the requests that contains the specified etag. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_etag: str
        :param filter_request_status: Response filter to select and display only the requests that contains the specified requestStatus. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_request_status: str
        :param filter_method: Response filter to select and display only the requests that contains the specified method. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_method: str
        :param filter_headers: Response filter to select and display only the requests that contains the specified headers. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_headers: str
        :param filter_body: Response filter to select and display only the requests that contains the specified body. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_body: str
        :param filter_url: Response filter to select and display only the requests that contains the specified url. The value is case insensitive and it depends on depth query parameter that should have a value greater than 0. 
        :type filter_url: str
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
        :rtype: tuple(Requests, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pretty',
            'depth',
            'x_contract_number',
            'filter_status',
            'filter_created_after',
            'filter_created_before',
            'filter_created_date',
            'filter_created_by',
            'filter_etag',
            'filter_request_status',
            'filter_method',
            'filter_headers',
            'filter_body',
            'filter_url',
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
                    " to method requests_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `requests_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `requests_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `requests_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `requests_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `requests_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501
        if 'filter_status' in local_var_params and local_var_params['filter_status'] is not None:  # noqa: E501
            query_params.append(('filter.status', local_var_params['filter_status']))  # noqa: E501
        if 'filter_created_after' in local_var_params and local_var_params['filter_created_after'] is not None:  # noqa: E501
            query_params.append(('filter.createdAfter', local_var_params['filter_created_after']))  # noqa: E501
        if 'filter_created_before' in local_var_params and local_var_params['filter_created_before'] is not None:  # noqa: E501
            query_params.append(('filter.createdBefore', local_var_params['filter_created_before']))  # noqa: E501
        if 'filter_created_date' in local_var_params and local_var_params['filter_created_date'] is not None:  # noqa: E501
            query_params.append(('filter.createdDate', local_var_params['filter_created_date']))  # noqa: E501
        if 'filter_created_by' in local_var_params and local_var_params['filter_created_by'] is not None:  # noqa: E501
            query_params.append(('filter.createdBy', local_var_params['filter_created_by']))  # noqa: E501
        if 'filter_etag' in local_var_params and local_var_params['filter_etag'] is not None:  # noqa: E501
            query_params.append(('filter.etag', local_var_params['filter_etag']))  # noqa: E501
        if 'filter_request_status' in local_var_params and local_var_params['filter_request_status'] is not None:  # noqa: E501
            query_params.append(('filter.requestStatus', local_var_params['filter_request_status']))  # noqa: E501
        if 'filter_method' in local_var_params and local_var_params['filter_method'] is not None:  # noqa: E501
            query_params.append(('filter.method', local_var_params['filter_method']))  # noqa: E501
        if 'filter_headers' in local_var_params and local_var_params['filter_headers'] is not None:  # noqa: E501
            query_params.append(('filter.headers', local_var_params['filter_headers']))  # noqa: E501
        if 'filter_body' in local_var_params and local_var_params['filter_body'] is not None:  # noqa: E501
            query_params.append(('filter.body', local_var_params['filter_body']))  # noqa: E501
        if 'filter_url' in local_var_params and local_var_params['filter_url'] is not None:  # noqa: E501
            query_params.append(('filter.url', local_var_params['filter_url']))  # noqa: E501
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

        response_type = 'Requests'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/requests', 'GET',
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

    def requests_status_get(self, request_id, **kwargs):  # noqa: E501
        """Retrieve Request Status  # noqa: E501

        Retrieves the status of a given request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.requests_status_get(request_id, async_req=True)
        >>> result = thread.get()

        :param request_id: (required)
        :type request_id: str
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
        :rtype: RequestStatus
        """
        kwargs['_return_http_data_only'] = True
        return self.requests_status_get_with_http_info(request_id, **kwargs)  # noqa: E501

    def requests_status_get_with_http_info(self, request_id, **kwargs):  # noqa: E501
        """Retrieve Request Status  # noqa: E501

        Retrieves the status of a given request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.requests_status_get_with_http_info(request_id, async_req=True)
        >>> result = thread.get()

        :param request_id: (required)
        :type request_id: str
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
        :rtype: tuple(RequestStatus, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'request_id',
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
                    " to method requests_status_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'request_id' is set
        if self.api_client.client_side_validation and ('request_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['request_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request_id` when calling `requests_status_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `requests_status_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `requests_status_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'request_id' in local_var_params:
            path_params['requestId'] = local_var_params['request_id']  # noqa: E501

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

        response_type = 'RequestStatus'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/requests/{requestId}/status', 'GET',
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
