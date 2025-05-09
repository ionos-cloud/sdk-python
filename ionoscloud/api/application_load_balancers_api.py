from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud.api_client import ApiClient
from ionoscloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ApplicationLoadBalancersApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def datacenters_applicationloadbalancers_delete(self, datacenter_id, application_load_balancer_id, **kwargs):  # noqa: E501
        """Delete an Application Load Balancer by ID  # noqa: E501

        Removes the specified Application Load Balancer from the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_delete(datacenter_id, application_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
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
        return self.datacenters_applicationloadbalancers_delete_with_http_info(datacenter_id, application_load_balancer_id, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_delete_with_http_info(self, datacenter_id, application_load_balancer_id, **kwargs):  # noqa: E501
        """Delete an Application Load Balancer by ID  # noqa: E501

        Removes the specified Application Load Balancer from the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_delete_with_http_info(datacenter_id, application_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
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
            'datacenter_id',
            'application_load_balancer_id',
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
                    " to method datacenters_applicationloadbalancers_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_delete`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501

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
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}', 'DELETE',
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

    def datacenters_applicationloadbalancers_find_by_application_load_balancer_id(self, datacenter_id, application_load_balancer_id, **kwargs):  # noqa: E501
        """Get an Application Load Balancer by ID  # noqa: E501

        Retrieves the properties of the specified Application Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_find_by_application_load_balancer_id(datacenter_id, application_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
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
        :rtype: ApplicationLoadBalancer
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_find_by_application_load_balancer_id_with_http_info(datacenter_id, application_load_balancer_id, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_find_by_application_load_balancer_id_with_http_info(self, datacenter_id, application_load_balancer_id, **kwargs):  # noqa: E501
        """Get an Application Load Balancer by ID  # noqa: E501

        Retrieves the properties of the specified Application Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_find_by_application_load_balancer_id_with_http_info(datacenter_id, application_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
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
        :rtype: tuple(ApplicationLoadBalancer, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
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
                    " to method datacenters_applicationloadbalancers_find_by_application_load_balancer_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_find_by_application_load_balancer_id`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_find_by_application_load_balancer_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_find_by_application_load_balancer_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_find_by_application_load_balancer_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501

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

        response_type = 'ApplicationLoadBalancer'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}', 'GET',
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

    def datacenters_applicationloadbalancers_flowlogs_delete(self, datacenter_id, application_load_balancer_id, flow_log_id, **kwargs):  # noqa: E501
        """Delete an ALB Flow Log by ID  # noqa: E501

        Deletes the Application Load Balancer flow log specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_delete(datacenter_id, application_load_balancer_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param flow_log_id: The unique ID of the flow log. (required)
        :type flow_log_id: str
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
        return self.datacenters_applicationloadbalancers_flowlogs_delete_with_http_info(datacenter_id, application_load_balancer_id, flow_log_id, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_flowlogs_delete_with_http_info(self, datacenter_id, application_load_balancer_id, flow_log_id, **kwargs):  # noqa: E501
        """Delete an ALB Flow Log by ID  # noqa: E501

        Deletes the Application Load Balancer flow log specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_delete_with_http_info(datacenter_id, application_load_balancer_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param flow_log_id: The unique ID of the flow log. (required)
        :type flow_log_id: str
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
            'datacenter_id',
            'application_load_balancer_id',
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
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_applicationloadbalancers_flowlogs_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_flowlogs_delete`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_flowlogs_delete`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_applicationloadbalancers_flowlogs_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

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
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId}', 'DELETE',
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

    def datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id(self, datacenter_id, application_load_balancer_id, flow_log_id, **kwargs):  # noqa: E501
        """Get an ALB Flow Log by ID  # noqa: E501

        Retrieves the Application Load Balancer flow log specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id(datacenter_id, application_load_balancer_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param flow_log_id: The unique ID of the flow log. (required)
        :type flow_log_id: str
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
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id_with_http_info(datacenter_id, application_load_balancer_id, flow_log_id, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id_with_http_info(self, datacenter_id, application_load_balancer_id, flow_log_id, **kwargs):  # noqa: E501
        """Get an ALB Flow Log by ID  # noqa: E501

        Retrieves the Application Load Balancer flow log specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id_with_http_info(datacenter_id, application_load_balancer_id, flow_log_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param flow_log_id: The unique ID of the flow log. (required)
        :type flow_log_id: str
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
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
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
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_find_by_flow_log_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

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

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId}', 'GET',
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

    def datacenters_applicationloadbalancers_flowlogs_get(self, datacenter_id, application_load_balancer_id, **kwargs):  # noqa: E501
        """Get ALB Flow Logs  # noqa: E501

        Retrieves the flow logs for the specified Application Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_get(datacenter_id, application_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
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
        :rtype: FlowLogs
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_flowlogs_get_with_http_info(datacenter_id, application_load_balancer_id, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_flowlogs_get_with_http_info(self, datacenter_id, application_load_balancer_id, **kwargs):  # noqa: E501
        """Get ALB Flow Logs  # noqa: E501

        Retrieves the flow logs for the specified Application Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_get_with_http_info(datacenter_id, application_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
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
        :rtype: tuple(FlowLogs, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
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
                    " to method datacenters_applicationloadbalancers_flowlogs_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_flowlogs_get`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_flowlogs_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501

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

        response_type = 'FlowLogs'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs', 'GET',
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

    def datacenters_applicationloadbalancers_flowlogs_patch(self, datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log_properties, **kwargs):  # noqa: E501
        """Partially Modify an ALB Flow Log by ID  # noqa: E501

        Updates the properties of the Application Load Balancer flow log specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_patch(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param flow_log_id: The unique ID of the flow log. (required)
        :type flow_log_id: str
        :param application_load_balancer_flow_log_properties: The properties of the ALB flow log to be updated. (required)
        :type application_load_balancer_flow_log_properties: FlowLogProperties
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
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_flowlogs_patch_with_http_info(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log_properties, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_flowlogs_patch_with_http_info(self, datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log_properties, **kwargs):  # noqa: E501
        """Partially Modify an ALB Flow Log by ID  # noqa: E501

        Updates the properties of the Application Load Balancer flow log specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_patch_with_http_info(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param flow_log_id: The unique ID of the flow log. (required)
        :type flow_log_id: str
        :param application_load_balancer_flow_log_properties: The properties of the ALB flow log to be updated. (required)
        :type application_load_balancer_flow_log_properties: FlowLogProperties
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
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
            'flow_log_id',
            'application_load_balancer_flow_log_properties',
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
                    " to method datacenters_applicationloadbalancers_flowlogs_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_flowlogs_patch`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_flowlogs_patch`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_applicationloadbalancers_flowlogs_patch`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_flow_log_properties' is set
        if self.api_client.client_side_validation and ('application_load_balancer_flow_log_properties' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_flow_log_properties'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_flow_log_properties` when calling `datacenters_applicationloadbalancers_flowlogs_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

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
        if 'application_load_balancer_flow_log_properties' in local_var_params:
            body_params = local_var_params['application_load_balancer_flow_log_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId}', 'PATCH',
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

    def datacenters_applicationloadbalancers_flowlogs_post(self, datacenter_id, application_load_balancer_id, application_load_balancer_flow_log, **kwargs):  # noqa: E501
        """Create an ALB Flow Log  # noqa: E501

        Creates a flow log for the Application Load Balancer specified by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_post(datacenter_id, application_load_balancer_id, application_load_balancer_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param application_load_balancer_flow_log: The flow log to create. (required)
        :type application_load_balancer_flow_log: FlowLog
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
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_flowlogs_post_with_http_info(datacenter_id, application_load_balancer_id, application_load_balancer_flow_log, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_flowlogs_post_with_http_info(self, datacenter_id, application_load_balancer_id, application_load_balancer_flow_log, **kwargs):  # noqa: E501
        """Create an ALB Flow Log  # noqa: E501

        Creates a flow log for the Application Load Balancer specified by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_post_with_http_info(datacenter_id, application_load_balancer_id, application_load_balancer_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param application_load_balancer_flow_log: The flow log to create. (required)
        :type application_load_balancer_flow_log: FlowLog
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
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
            'application_load_balancer_flow_log',
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
                    " to method datacenters_applicationloadbalancers_flowlogs_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_flowlogs_post`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_flowlogs_post`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_flow_log' is set
        if self.api_client.client_side_validation and ('application_load_balancer_flow_log' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_flow_log'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_flow_log` when calling `datacenters_applicationloadbalancers_flowlogs_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501

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
        if 'application_load_balancer_flow_log' in local_var_params:
            body_params = local_var_params['application_load_balancer_flow_log']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs', 'POST',
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

    def datacenters_applicationloadbalancers_flowlogs_put(self, datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log, **kwargs):  # noqa: E501
        """Modify an ALB Flow Log by ID  # noqa: E501

        Modifies the Application Load Balancer flow log specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_put(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param flow_log_id: The unique ID of the flow log. (required)
        :type flow_log_id: str
        :param application_load_balancer_flow_log: The modified ALB flow log. (required)
        :type application_load_balancer_flow_log: FlowLogPut
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
        :rtype: FlowLog
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_flowlogs_put_with_http_info(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_flowlogs_put_with_http_info(self, datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log, **kwargs):  # noqa: E501
        """Modify an ALB Flow Log by ID  # noqa: E501

        Modifies the Application Load Balancer flow log specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_flowlogs_put_with_http_info(datacenter_id, application_load_balancer_id, flow_log_id, application_load_balancer_flow_log, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param flow_log_id: The unique ID of the flow log. (required)
        :type flow_log_id: str
        :param application_load_balancer_flow_log: The modified ALB flow log. (required)
        :type application_load_balancer_flow_log: FlowLogPut
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
        :rtype: tuple(FlowLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
            'flow_log_id',
            'application_load_balancer_flow_log',
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
                    " to method datacenters_applicationloadbalancers_flowlogs_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_flowlogs_put`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_flowlogs_put`")  # noqa: E501
        # verify the required parameter 'flow_log_id' is set
        if self.api_client.client_side_validation and ('flow_log_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['flow_log_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `flow_log_id` when calling `datacenters_applicationloadbalancers_flowlogs_put`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_flow_log' is set
        if self.api_client.client_side_validation and ('application_load_balancer_flow_log' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_flow_log'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_flow_log` when calling `datacenters_applicationloadbalancers_flowlogs_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_flowlogs_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501
        if 'flow_log_id' in local_var_params:
            path_params['flowLogId'] = local_var_params['flow_log_id']  # noqa: E501

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
        if 'application_load_balancer_flow_log' in local_var_params:
            body_params = local_var_params['application_load_balancer_flow_log']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'FlowLog'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/flowlogs/{flowLogId}', 'PUT',
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

    def datacenters_applicationloadbalancers_forwardingrules_delete(self, datacenter_id, application_load_balancer_id, forwarding_rule_id, **kwargs):  # noqa: E501
        """Delete an ALB Forwarding Rule by ID  # noqa: E501

        Deletes the Application Load Balancer forwarding rule specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_delete(datacenter_id, application_load_balancer_id, forwarding_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
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
        return self.datacenters_applicationloadbalancers_forwardingrules_delete_with_http_info(datacenter_id, application_load_balancer_id, forwarding_rule_id, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_forwardingrules_delete_with_http_info(self, datacenter_id, application_load_balancer_id, forwarding_rule_id, **kwargs):  # noqa: E501
        """Delete an ALB Forwarding Rule by ID  # noqa: E501

        Deletes the Application Load Balancer forwarding rule specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_delete_with_http_info(datacenter_id, application_load_balancer_id, forwarding_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
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
            'datacenter_id',
            'application_load_balancer_id',
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
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_applicationloadbalancers_forwardingrules_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_forwardingrules_delete`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_forwardingrules_delete`")  # noqa: E501
        # verify the required parameter 'forwarding_rule_id' is set
        if self.api_client.client_side_validation and ('forwarding_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['forwarding_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `forwarding_rule_id` when calling `datacenters_applicationloadbalancers_forwardingrules_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501
        if 'forwarding_rule_id' in local_var_params:
            path_params['forwardingRuleId'] = local_var_params['forwarding_rule_id']  # noqa: E501

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
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId}', 'DELETE',
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

    def datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id(self, datacenter_id, application_load_balancer_id, forwarding_rule_id, **kwargs):  # noqa: E501
        """Get an ALB Forwarding Rule by ID  # noqa: E501

        Retrieves the Application Load Balancer forwarding rule specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id(datacenter_id, application_load_balancer_id, forwarding_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
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
        :rtype: ApplicationLoadBalancerForwardingRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id_with_http_info(datacenter_id, application_load_balancer_id, forwarding_rule_id, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id_with_http_info(self, datacenter_id, application_load_balancer_id, forwarding_rule_id, **kwargs):  # noqa: E501
        """Get an ALB Forwarding Rule by ID  # noqa: E501

        Retrieves the Application Load Balancer forwarding rule specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id_with_http_info(datacenter_id, application_load_balancer_id, forwarding_rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
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
        :rtype: tuple(ApplicationLoadBalancerForwardingRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
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
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id`")  # noqa: E501
        # verify the required parameter 'forwarding_rule_id' is set
        if self.api_client.client_side_validation and ('forwarding_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['forwarding_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `forwarding_rule_id` when calling `datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_find_by_forwarding_rule_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501
        if 'forwarding_rule_id' in local_var_params:
            path_params['forwardingRuleId'] = local_var_params['forwarding_rule_id']  # noqa: E501

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

        response_type = 'ApplicationLoadBalancerForwardingRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId}', 'GET',
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

    def datacenters_applicationloadbalancers_forwardingrules_get(self, datacenter_id, application_load_balancer_id, **kwargs):  # noqa: E501
        """Get ALB Forwarding Rules  # noqa: E501

        Lists the forwarding rules of the specified Application Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_get(datacenter_id, application_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
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
        :rtype: ApplicationLoadBalancerForwardingRules
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_forwardingrules_get_with_http_info(datacenter_id, application_load_balancer_id, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_forwardingrules_get_with_http_info(self, datacenter_id, application_load_balancer_id, **kwargs):  # noqa: E501
        """Get ALB Forwarding Rules  # noqa: E501

        Lists the forwarding rules of the specified Application Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_get_with_http_info(datacenter_id, application_load_balancer_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
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
        :rtype: tuple(ApplicationLoadBalancerForwardingRules, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
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
                    " to method datacenters_applicationloadbalancers_forwardingrules_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_forwardingrules_get`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_forwardingrules_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501

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

        response_type = 'ApplicationLoadBalancerForwardingRules'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules', 'GET',
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

    def datacenters_applicationloadbalancers_forwardingrules_patch(self, datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule_properties, **kwargs):  # noqa: E501
        """Partially modify an ALB Forwarding Rule by ID  # noqa: E501

        Updates the properties of the Application Load Balancer forwarding rule specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_patch(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param application_load_balancer_forwarding_rule_properties: The properties of the forwarding rule to be updated. (required)
        :type application_load_balancer_forwarding_rule_properties: ApplicationLoadBalancerForwardingRuleProperties
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
        :rtype: ApplicationLoadBalancerForwardingRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_forwardingrules_patch_with_http_info(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule_properties, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_forwardingrules_patch_with_http_info(self, datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule_properties, **kwargs):  # noqa: E501
        """Partially modify an ALB Forwarding Rule by ID  # noqa: E501

        Updates the properties of the Application Load Balancer forwarding rule specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_patch_with_http_info(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param application_load_balancer_forwarding_rule_properties: The properties of the forwarding rule to be updated. (required)
        :type application_load_balancer_forwarding_rule_properties: ApplicationLoadBalancerForwardingRuleProperties
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
        :rtype: tuple(ApplicationLoadBalancerForwardingRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
            'forwarding_rule_id',
            'application_load_balancer_forwarding_rule_properties',
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
                    " to method datacenters_applicationloadbalancers_forwardingrules_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_forwardingrules_patch`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_forwardingrules_patch`")  # noqa: E501
        # verify the required parameter 'forwarding_rule_id' is set
        if self.api_client.client_side_validation and ('forwarding_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['forwarding_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `forwarding_rule_id` when calling `datacenters_applicationloadbalancers_forwardingrules_patch`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_forwarding_rule_properties' is set
        if self.api_client.client_side_validation and ('application_load_balancer_forwarding_rule_properties' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_forwarding_rule_properties'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_forwarding_rule_properties` when calling `datacenters_applicationloadbalancers_forwardingrules_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501
        if 'forwarding_rule_id' in local_var_params:
            path_params['forwardingRuleId'] = local_var_params['forwarding_rule_id']  # noqa: E501

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
        if 'application_load_balancer_forwarding_rule_properties' in local_var_params:
            body_params = local_var_params['application_load_balancer_forwarding_rule_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'ApplicationLoadBalancerForwardingRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId}', 'PATCH',
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

    def datacenters_applicationloadbalancers_forwardingrules_post(self, datacenter_id, application_load_balancer_id, application_load_balancer_forwarding_rule, **kwargs):  # noqa: E501
        """Create an ALB Forwarding Rule  # noqa: E501

        Creates a forwarding rule for the specified Application Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_post(datacenter_id, application_load_balancer_id, application_load_balancer_forwarding_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param application_load_balancer_forwarding_rule: The forwarding rule to create. (required)
        :type application_load_balancer_forwarding_rule: ApplicationLoadBalancerForwardingRule
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
        :rtype: ApplicationLoadBalancerForwardingRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_forwardingrules_post_with_http_info(datacenter_id, application_load_balancer_id, application_load_balancer_forwarding_rule, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_forwardingrules_post_with_http_info(self, datacenter_id, application_load_balancer_id, application_load_balancer_forwarding_rule, **kwargs):  # noqa: E501
        """Create an ALB Forwarding Rule  # noqa: E501

        Creates a forwarding rule for the specified Application Load Balancer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_post_with_http_info(datacenter_id, application_load_balancer_id, application_load_balancer_forwarding_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param application_load_balancer_forwarding_rule: The forwarding rule to create. (required)
        :type application_load_balancer_forwarding_rule: ApplicationLoadBalancerForwardingRule
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
        :rtype: tuple(ApplicationLoadBalancerForwardingRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
            'application_load_balancer_forwarding_rule',
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
                    " to method datacenters_applicationloadbalancers_forwardingrules_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_forwardingrules_post`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_forwardingrules_post`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_forwarding_rule' is set
        if self.api_client.client_side_validation and ('application_load_balancer_forwarding_rule' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_forwarding_rule'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_forwarding_rule` when calling `datacenters_applicationloadbalancers_forwardingrules_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501

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
        if 'application_load_balancer_forwarding_rule' in local_var_params:
            body_params = local_var_params['application_load_balancer_forwarding_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'ApplicationLoadBalancerForwardingRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules', 'POST',
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

    def datacenters_applicationloadbalancers_forwardingrules_put(self, datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule, **kwargs):  # noqa: E501
        """Modify an ALB Forwarding Rule by ID  # noqa: E501

        Modifies the Application Load Balancer forwarding rule specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_put(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param application_load_balancer_forwarding_rule: The modified ALB forwarding rule. (required)
        :type application_load_balancer_forwarding_rule: ApplicationLoadBalancerForwardingRulePut
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
        :rtype: ApplicationLoadBalancerForwardingRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_forwardingrules_put_with_http_info(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_forwardingrules_put_with_http_info(self, datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule, **kwargs):  # noqa: E501
        """Modify an ALB Forwarding Rule by ID  # noqa: E501

        Modifies the Application Load Balancer forwarding rule specified by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_forwardingrules_put_with_http_info(datacenter_id, application_load_balancer_id, forwarding_rule_id, application_load_balancer_forwarding_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param forwarding_rule_id: The unique ID of the forwarding rule. (required)
        :type forwarding_rule_id: str
        :param application_load_balancer_forwarding_rule: The modified ALB forwarding rule. (required)
        :type application_load_balancer_forwarding_rule: ApplicationLoadBalancerForwardingRulePut
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
        :rtype: tuple(ApplicationLoadBalancerForwardingRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
            'forwarding_rule_id',
            'application_load_balancer_forwarding_rule',
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
                    " to method datacenters_applicationloadbalancers_forwardingrules_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_forwardingrules_put`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_forwardingrules_put`")  # noqa: E501
        # verify the required parameter 'forwarding_rule_id' is set
        if self.api_client.client_side_validation and ('forwarding_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['forwarding_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `forwarding_rule_id` when calling `datacenters_applicationloadbalancers_forwardingrules_put`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_forwarding_rule' is set
        if self.api_client.client_side_validation and ('application_load_balancer_forwarding_rule' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_forwarding_rule'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_forwarding_rule` when calling `datacenters_applicationloadbalancers_forwardingrules_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_forwardingrules_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501
        if 'forwarding_rule_id' in local_var_params:
            path_params['forwardingRuleId'] = local_var_params['forwarding_rule_id']  # noqa: E501

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
        if 'application_load_balancer_forwarding_rule' in local_var_params:
            body_params = local_var_params['application_load_balancer_forwarding_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'ApplicationLoadBalancerForwardingRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}/forwardingrules/{forwardingRuleId}', 'PUT',
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

    def datacenters_applicationloadbalancers_get(self, datacenter_id, **kwargs):  # noqa: E501
        """Get Application Load Balancers  # noqa: E501

        Lists all Application Load Balancers within a data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_get(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param offset: The first element (from the complete list of the elements) to include in the response (used together with <b><i>limit</i></b> for pagination).
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
        :rtype: ApplicationLoadBalancers
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_get_with_http_info(datacenter_id, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_get_with_http_info(self, datacenter_id, **kwargs):  # noqa: E501
        """Get Application Load Balancers  # noqa: E501

        Lists all Application Load Balancers within a data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_get_with_http_info(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects.  GET /datacenters/[ID]  - depth=0: Only direct properties are included; children (servers and other elements) are not included.  - depth=1: Direct properties and children references are included.  - depth=2: Direct properties and children properties are included.  - depth=3: Direct properties and children properties and children's children are included.  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users with multiple contracts must provide the contract number, for which all API requests are to be executed.
        :type x_contract_number: int
        :param offset: The first element (from the complete list of the elements) to include in the response (used together with <b><i>limit</i></b> for pagination).
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
        :rtype: tuple(ApplicationLoadBalancers, status_code(int), headers(HTTPHeaderDict))
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
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method datacenters_applicationloadbalancers_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_applicationloadbalancers_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_applicationloadbalancers_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_applicationloadbalancers_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
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
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'ApplicationLoadBalancers'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers', 'GET',
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

    def datacenters_applicationloadbalancers_patch(self, datacenter_id, application_load_balancer_id, application_load_balancer_properties, **kwargs):  # noqa: E501
        """Partially Modify an Application Load Balancer by ID  # noqa: E501

        Updates the properties of the specified Application Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_patch(datacenter_id, application_load_balancer_id, application_load_balancer_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param application_load_balancer_properties: The Application Load Balancer properties to be updated. (required)
        :type application_load_balancer_properties: ApplicationLoadBalancerProperties
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
        :rtype: ApplicationLoadBalancer
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_patch_with_http_info(datacenter_id, application_load_balancer_id, application_load_balancer_properties, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_patch_with_http_info(self, datacenter_id, application_load_balancer_id, application_load_balancer_properties, **kwargs):  # noqa: E501
        """Partially Modify an Application Load Balancer by ID  # noqa: E501

        Updates the properties of the specified Application Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_patch_with_http_info(datacenter_id, application_load_balancer_id, application_load_balancer_properties, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param application_load_balancer_properties: The Application Load Balancer properties to be updated. (required)
        :type application_load_balancer_properties: ApplicationLoadBalancerProperties
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
        :rtype: tuple(ApplicationLoadBalancer, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
            'application_load_balancer_properties',
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
                    " to method datacenters_applicationloadbalancers_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_patch`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_patch`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_properties' is set
        if self.api_client.client_side_validation and ('application_load_balancer_properties' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_properties'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_properties` when calling `datacenters_applicationloadbalancers_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501

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
        if 'application_load_balancer_properties' in local_var_params:
            body_params = local_var_params['application_load_balancer_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'ApplicationLoadBalancer'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}', 'PATCH',
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

    def datacenters_applicationloadbalancers_post(self, datacenter_id, application_load_balancer, **kwargs):  # noqa: E501
        """Create an Application Load Balancer  # noqa: E501

        Creates an Application Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_post(datacenter_id, application_load_balancer, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer: The Application Load Balancer to create. (required)
        :type application_load_balancer: ApplicationLoadBalancer
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
        :rtype: ApplicationLoadBalancer
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_post_with_http_info(datacenter_id, application_load_balancer, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_post_with_http_info(self, datacenter_id, application_load_balancer, **kwargs):  # noqa: E501
        """Create an Application Load Balancer  # noqa: E501

        Creates an Application Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_post_with_http_info(datacenter_id, application_load_balancer, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer: The Application Load Balancer to create. (required)
        :type application_load_balancer: ApplicationLoadBalancer
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
        :rtype: tuple(ApplicationLoadBalancer, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer',
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
                    " to method datacenters_applicationloadbalancers_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_post`")  # noqa: E501
        # verify the required parameter 'application_load_balancer' is set
        if self.api_client.client_side_validation and ('application_load_balancer' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer` when calling `datacenters_applicationloadbalancers_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501

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
        if 'application_load_balancer' in local_var_params:
            body_params = local_var_params['application_load_balancer']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'ApplicationLoadBalancer'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers', 'POST',
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

    def datacenters_applicationloadbalancers_put(self, datacenter_id, application_load_balancer_id, application_load_balancer, **kwargs):  # noqa: E501
        """Modify an Application Load Balancer by ID  # noqa: E501

        Modifies the properties of the specified Application Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_put(datacenter_id, application_load_balancer_id, application_load_balancer, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param application_load_balancer: The modified Application Load Balancer. (required)
        :type application_load_balancer: ApplicationLoadBalancerPut
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
        :rtype: ApplicationLoadBalancer
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_applicationloadbalancers_put_with_http_info(datacenter_id, application_load_balancer_id, application_load_balancer, **kwargs)  # noqa: E501

    def datacenters_applicationloadbalancers_put_with_http_info(self, datacenter_id, application_load_balancer_id, application_load_balancer, **kwargs):  # noqa: E501
        """Modify an Application Load Balancer by ID  # noqa: E501

        Modifies the properties of the specified Application Load Balancer within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_applicationloadbalancers_put_with_http_info(datacenter_id, application_load_balancer_id, application_load_balancer, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param application_load_balancer_id: The unique ID of the Application Load Balancer. (required)
        :type application_load_balancer_id: str
        :param application_load_balancer: The modified Application Load Balancer. (required)
        :type application_load_balancer: ApplicationLoadBalancerPut
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
        :rtype: tuple(ApplicationLoadBalancer, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'application_load_balancer_id',
            'application_load_balancer',
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
                    " to method datacenters_applicationloadbalancers_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_applicationloadbalancers_put`")  # noqa: E501
        # verify the required parameter 'application_load_balancer_id' is set
        if self.api_client.client_side_validation and ('application_load_balancer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer_id` when calling `datacenters_applicationloadbalancers_put`")  # noqa: E501
        # verify the required parameter 'application_load_balancer' is set
        if self.api_client.client_side_validation and ('application_load_balancer' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_load_balancer'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_load_balancer` when calling `datacenters_applicationloadbalancers_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_applicationloadbalancers_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'application_load_balancer_id' in local_var_params:
            path_params['applicationLoadBalancerId'] = local_var_params['application_load_balancer_id']  # noqa: E501

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
        if 'application_load_balancer' in local_var_params:
            body_params = local_var_params['application_load_balancer']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'ApplicationLoadBalancer'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/applicationloadbalancers/{applicationLoadBalancerId}', 'PUT',
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
