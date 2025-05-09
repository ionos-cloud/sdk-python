from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud.api_client import ApiClient
from ionoscloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SecurityGroupsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def datacenters_securitygroups_delete(self, datacenter_id, security_group_id, **kwargs):  # noqa: E501
        """Delete a Security Group  # noqa: E501

        Deletes the specified Security Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_delete(datacenter_id, security_group_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the Security Group. (required)
        :type security_group_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
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
        return self.datacenters_securitygroups_delete_with_http_info(datacenter_id, security_group_id, **kwargs)  # noqa: E501

    def datacenters_securitygroups_delete_with_http_info(self, datacenter_id, security_group_id, **kwargs):  # noqa: E501
        """Delete a Security Group  # noqa: E501

        Deletes the specified Security Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_delete_with_http_info(datacenter_id, security_group_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the Security Group. (required)
        :type security_group_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
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
            'security_group_id',
            'pretty'
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
                    " to method datacenters_securitygroups_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_delete`")  # noqa: E501
        # verify the required parameter 'security_group_id' is set
        if self.api_client.client_side_validation and ('security_group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group_id` when calling `datacenters_securitygroups_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'security_group_id' in local_var_params:
            path_params['securityGroupId'] = local_var_params['security_group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501

        header_params = {}

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
            '/datacenters/{datacenterId}/securitygroups/{securityGroupId}', 'DELETE',
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

    def datacenters_securitygroups_find_by_id(self, datacenter_id, security_group_id, **kwargs):  # noqa: E501
        """Retrieve a Security Group  # noqa: E501

        Retrieves the attributes of a given Security Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_find_by_id(datacenter_id, security_group_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: SecurityGroup
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_securitygroups_find_by_id_with_http_info(datacenter_id, security_group_id, **kwargs)  # noqa: E501

    def datacenters_securitygroups_find_by_id_with_http_info(self, datacenter_id, security_group_id, **kwargs):  # noqa: E501
        """Retrieve a Security Group  # noqa: E501

        Retrieves the attributes of a given Security Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_find_by_id_with_http_info(datacenter_id, security_group_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(SecurityGroup, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'security_group_id',
            'pretty',
            'depth'
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
                    " to method datacenters_securitygroups_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_find_by_id`")  # noqa: E501
        # verify the required parameter 'security_group_id' is set
        if self.api_client.client_side_validation and ('security_group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group_id` when calling `datacenters_securitygroups_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'security_group_id' in local_var_params:
            path_params['securityGroupId'] = local_var_params['security_group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'SecurityGroup'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups/{securityGroupId}', 'GET',
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

    def datacenters_securitygroups_firewallrules_delete(self, datacenter_id, security_group_id, rule_id, **kwargs):  # noqa: E501
        """Remove a Firewall Rule from a Security Group  # noqa: E501

        Removes the specific Firewall Rule from the Security Group and delete the Firewall rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_firewallrules_delete(datacenter_id, security_group_id, rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param rule_id: The unique ID of the firewall rule. (required)
        :type rule_id: str
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
        return self.datacenters_securitygroups_firewallrules_delete_with_http_info(datacenter_id, security_group_id, rule_id, **kwargs)  # noqa: E501

    def datacenters_securitygroups_firewallrules_delete_with_http_info(self, datacenter_id, security_group_id, rule_id, **kwargs):  # noqa: E501
        """Remove a Firewall Rule from a Security Group  # noqa: E501

        Removes the specific Firewall Rule from the Security Group and delete the Firewall rule  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_firewallrules_delete_with_http_info(datacenter_id, security_group_id, rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param rule_id: The unique ID of the firewall rule. (required)
        :type rule_id: str
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
            'security_group_id',
            'rule_id'
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
                    " to method datacenters_securitygroups_firewallrules_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_firewallrules_delete`")  # noqa: E501
        # verify the required parameter 'security_group_id' is set
        if self.api_client.client_side_validation and ('security_group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group_id` when calling `datacenters_securitygroups_firewallrules_delete`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if self.api_client.client_side_validation and ('rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rule_id` when calling `datacenters_securitygroups_firewallrules_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'security_group_id' in local_var_params:
            path_params['securityGroupId'] = local_var_params['security_group_id']  # noqa: E501
        if 'rule_id' in local_var_params:
            path_params['ruleId'] = local_var_params['rule_id']  # noqa: E501

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

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId}', 'DELETE',
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

    def datacenters_securitygroups_firewallrules_post(self, datacenter_id, security_group_id, firewall_rule, **kwargs):  # noqa: E501
        """Create Firewall rule to a Security Group  # noqa: E501

        Create one firewall rule and attach it to the existing security group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_firewallrules_post(datacenter_id, security_group_id, firewall_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param firewall_rule: The firewall to be attached (or created and attached). (required)
        :type firewall_rule: FirewallRule
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
        :rtype: FirewallRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_securitygroups_firewallrules_post_with_http_info(datacenter_id, security_group_id, firewall_rule, **kwargs)  # noqa: E501

    def datacenters_securitygroups_firewallrules_post_with_http_info(self, datacenter_id, security_group_id, firewall_rule, **kwargs):  # noqa: E501
        """Create Firewall rule to a Security Group  # noqa: E501

        Create one firewall rule and attach it to the existing security group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_firewallrules_post_with_http_info(datacenter_id, security_group_id, firewall_rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param firewall_rule: The firewall to be attached (or created and attached). (required)
        :type firewall_rule: FirewallRule
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
        :rtype: tuple(FirewallRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'security_group_id',
            'firewall_rule'
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
                    " to method datacenters_securitygroups_firewallrules_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_firewallrules_post`")  # noqa: E501
        # verify the required parameter 'security_group_id' is set
        if self.api_client.client_side_validation and ('security_group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group_id` when calling `datacenters_securitygroups_firewallrules_post`")  # noqa: E501
        # verify the required parameter 'firewall_rule' is set
        if self.api_client.client_side_validation and ('firewall_rule' not in local_var_params or  # noqa: E501
                                                        local_var_params['firewall_rule'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `firewall_rule` when calling `datacenters_securitygroups_firewallrules_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'security_group_id' in local_var_params:
            path_params['securityGroupId'] = local_var_params['security_group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'firewall_rule' in local_var_params:
            body_params = local_var_params['firewall_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'FirewallRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules', 'POST',
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

    def datacenters_securitygroups_get(self, datacenter_id, **kwargs):  # noqa: E501
        """List Security Groups  # noqa: E501

        Retrieve a list of available security groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_get(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: SecurityGroups
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_securitygroups_get_with_http_info(datacenter_id, **kwargs)  # noqa: E501

    def datacenters_securitygroups_get_with_http_info(self, datacenter_id, **kwargs):  # noqa: E501
        """List Security Groups  # noqa: E501

        Retrieve a list of available security groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_get_with_http_info(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(SecurityGroups, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'pretty',
            'depth',
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
                    " to method datacenters_securitygroups_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_securitygroups_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_securitygroups_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_securitygroups_get`, must be a value greater than or equal to `1`")  # noqa: E501
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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'SecurityGroups'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups', 'GET',
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

    def datacenters_securitygroups_patch(self, datacenter_id, security_group_id, security_group, **kwargs):  # noqa: E501
        """Partially modify Security Group  # noqa: E501

        Modify the properties of the specified Security Group within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_patch(datacenter_id, security_group_id, security_group, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the Security Group. (required)
        :type security_group_id: str
        :param security_group: The modified Security Group (required)
        :type security_group: SecurityGroupProperties
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: SecurityGroup
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_securitygroups_patch_with_http_info(datacenter_id, security_group_id, security_group, **kwargs)  # noqa: E501

    def datacenters_securitygroups_patch_with_http_info(self, datacenter_id, security_group_id, security_group, **kwargs):  # noqa: E501
        """Partially modify Security Group  # noqa: E501

        Modify the properties of the specified Security Group within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_patch_with_http_info(datacenter_id, security_group_id, security_group, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the Security Group. (required)
        :type security_group_id: str
        :param security_group: The modified Security Group (required)
        :type security_group: SecurityGroupProperties
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(SecurityGroup, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'security_group_id',
            'security_group',
            'pretty',
            'depth'
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
                    " to method datacenters_securitygroups_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_patch`")  # noqa: E501
        # verify the required parameter 'security_group_id' is set
        if self.api_client.client_side_validation and ('security_group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group_id` when calling `datacenters_securitygroups_patch`")  # noqa: E501
        # verify the required parameter 'security_group' is set
        if self.api_client.client_side_validation and ('security_group' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group` when calling `datacenters_securitygroups_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'security_group_id' in local_var_params:
            path_params['securityGroupId'] = local_var_params['security_group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'security_group' in local_var_params:
            body_params = local_var_params['security_group']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'SecurityGroup'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups/{securityGroupId}', 'PATCH',
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

    def datacenters_securitygroups_post(self, datacenter_id, security_group, **kwargs):  # noqa: E501
        """Create a Security Group  # noqa: E501

        Creates a security group within the data center. This will allow you to define which IP addresses and networks have access to your servers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_post(datacenter_id, security_group, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group: The security group to be created (required)
        :type security_group: SecurityGroupRequest
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: SecurityGroup
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_securitygroups_post_with_http_info(datacenter_id, security_group, **kwargs)  # noqa: E501

    def datacenters_securitygroups_post_with_http_info(self, datacenter_id, security_group, **kwargs):  # noqa: E501
        """Create a Security Group  # noqa: E501

        Creates a security group within the data center. This will allow you to define which IP addresses and networks have access to your servers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_post_with_http_info(datacenter_id, security_group, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group: The security group to be created (required)
        :type security_group: SecurityGroupRequest
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(SecurityGroup, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'security_group',
            'pretty',
            'depth'
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
                    " to method datacenters_securitygroups_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_post`")  # noqa: E501
        # verify the required parameter 'security_group' is set
        if self.api_client.client_side_validation and ('security_group' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group` when calling `datacenters_securitygroups_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_post`, must be a value greater than or equal to `0`")  # noqa: E501
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

        form_params = []
        local_var_files = {}

        body_params = None
        if 'security_group' in local_var_params:
            body_params = local_var_params['security_group']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'SecurityGroup'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups', 'POST',
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

    def datacenters_securitygroups_put(self, datacenter_id, security_group_id, security_group, **kwargs):  # noqa: E501
        """Modify Security Group  # noqa: E501

        Modify the properties of the specified Security Group within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_put(datacenter_id, security_group_id, security_group, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the Security Group. (required)
        :type security_group_id: str
        :param security_group: The modified Security Group (required)
        :type security_group: SecurityGroupRequest
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: SecurityGroup
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_securitygroups_put_with_http_info(datacenter_id, security_group_id, security_group, **kwargs)  # noqa: E501

    def datacenters_securitygroups_put_with_http_info(self, datacenter_id, security_group_id, security_group, **kwargs):  # noqa: E501
        """Modify Security Group  # noqa: E501

        Modify the properties of the specified Security Group within the data center.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_put_with_http_info(datacenter_id, security_group_id, security_group, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the Security Group. (required)
        :type security_group_id: str
        :param security_group: The modified Security Group (required)
        :type security_group: SecurityGroupRequest
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(SecurityGroup, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'security_group_id',
            'security_group',
            'pretty',
            'depth'
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
                    " to method datacenters_securitygroups_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_put`")  # noqa: E501
        # verify the required parameter 'security_group_id' is set
        if self.api_client.client_side_validation and ('security_group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group_id` when calling `datacenters_securitygroups_put`")  # noqa: E501
        # verify the required parameter 'security_group' is set
        if self.api_client.client_side_validation and ('security_group' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group` when calling `datacenters_securitygroups_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'security_group_id' in local_var_params:
            path_params['securityGroupId'] = local_var_params['security_group_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'security_group' in local_var_params:
            body_params = local_var_params['security_group']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'SecurityGroup'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups/{securityGroupId}', 'PUT',
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

    def datacenters_securitygroups_rules_find_by_id(self, datacenter_id, security_group_id, rule_id, **kwargs):  # noqa: E501
        """Retrieve security group rule by id  # noqa: E501

        Retrieve the properties of the specified Security Group rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_rules_find_by_id(datacenter_id, security_group_id, rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the Security Group. (required)
        :type security_group_id: str
        :param rule_id: The unique ID of the Security Group rule. (required)
        :type rule_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: FirewallRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_securitygroups_rules_find_by_id_with_http_info(datacenter_id, security_group_id, rule_id, **kwargs)  # noqa: E501

    def datacenters_securitygroups_rules_find_by_id_with_http_info(self, datacenter_id, security_group_id, rule_id, **kwargs):  # noqa: E501
        """Retrieve security group rule by id  # noqa: E501

        Retrieve the properties of the specified Security Group rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_rules_find_by_id_with_http_info(datacenter_id, security_group_id, rule_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the Security Group. (required)
        :type security_group_id: str
        :param rule_id: The unique ID of the Security Group rule. (required)
        :type rule_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(FirewallRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'security_group_id',
            'rule_id',
            'pretty',
            'depth'
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
                    " to method datacenters_securitygroups_rules_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_rules_find_by_id`")  # noqa: E501
        # verify the required parameter 'security_group_id' is set
        if self.api_client.client_side_validation and ('security_group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group_id` when calling `datacenters_securitygroups_rules_find_by_id`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if self.api_client.client_side_validation and ('rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rule_id` when calling `datacenters_securitygroups_rules_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_rules_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_rules_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'security_group_id' in local_var_params:
            path_params['securityGroupId'] = local_var_params['security_group_id']  # noqa: E501
        if 'rule_id' in local_var_params:
            path_params['ruleId'] = local_var_params['rule_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'FirewallRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId}', 'GET',
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

    def datacenters_securitygroups_rules_get(self, datacenter_id, security_group_id, **kwargs):  # noqa: E501
        """List Security Group rules  # noqa: E501

        List all rules for the specified Security Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_rules_get(datacenter_id, security_group_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: FirewallRules
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_securitygroups_rules_get_with_http_info(datacenter_id, security_group_id, **kwargs)  # noqa: E501

    def datacenters_securitygroups_rules_get_with_http_info(self, datacenter_id, security_group_id, **kwargs):  # noqa: E501
        """List Security Group rules  # noqa: E501

        List all rules for the specified Security Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_rules_get_with_http_info(datacenter_id, security_group_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(FirewallRules, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'security_group_id',
            'pretty',
            'depth',
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
                    " to method datacenters_securitygroups_rules_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_rules_get`")  # noqa: E501
        # verify the required parameter 'security_group_id' is set
        if self.api_client.client_side_validation and ('security_group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group_id` when calling `datacenters_securitygroups_rules_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_rules_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_rules_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_securitygroups_rules_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_securitygroups_rules_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_securitygroups_rules_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'security_group_id' in local_var_params:
            path_params['securityGroupId'] = local_var_params['security_group_id']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'FirewallRules'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules', 'GET',
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

    def datacenters_securitygroups_rules_patch(self, datacenter_id, security_group_id, rule_id, rule, **kwargs):  # noqa: E501
        """Partially modify Security Group Rules  # noqa: E501

        Update the properties of the specified Security Group rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_rules_patch(datacenter_id, security_group_id, rule_id, rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param rule_id: The unique ID of the Security Group Rule. (required)
        :type rule_id: str
        :param rule: The properties of the Security Group Rule to be updated. (required)
        :type rule: FirewallruleProperties
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: FirewallRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_securitygroups_rules_patch_with_http_info(datacenter_id, security_group_id, rule_id, rule, **kwargs)  # noqa: E501

    def datacenters_securitygroups_rules_patch_with_http_info(self, datacenter_id, security_group_id, rule_id, rule, **kwargs):  # noqa: E501
        """Partially modify Security Group Rules  # noqa: E501

        Update the properties of the specified Security Group rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_rules_patch_with_http_info(datacenter_id, security_group_id, rule_id, rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param rule_id: The unique ID of the Security Group Rule. (required)
        :type rule_id: str
        :param rule: The properties of the Security Group Rule to be updated. (required)
        :type rule: FirewallruleProperties
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(FirewallRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'security_group_id',
            'rule_id',
            'rule',
            'pretty',
            'depth'
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
                    " to method datacenters_securitygroups_rules_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_rules_patch`")  # noqa: E501
        # verify the required parameter 'security_group_id' is set
        if self.api_client.client_side_validation and ('security_group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group_id` when calling `datacenters_securitygroups_rules_patch`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if self.api_client.client_side_validation and ('rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rule_id` when calling `datacenters_securitygroups_rules_patch`")  # noqa: E501
        # verify the required parameter 'rule' is set
        if self.api_client.client_side_validation and ('rule' not in local_var_params or  # noqa: E501
                                                        local_var_params['rule'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rule` when calling `datacenters_securitygroups_rules_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_rules_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_rules_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'security_group_id' in local_var_params:
            path_params['securityGroupId'] = local_var_params['security_group_id']  # noqa: E501
        if 'rule_id' in local_var_params:
            path_params['ruleId'] = local_var_params['rule_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rule' in local_var_params:
            body_params = local_var_params['rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'FirewallRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId}', 'PATCH',
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

    def datacenters_securitygroups_rules_put(self, datacenter_id, security_group_id, rule_id, rule, **kwargs):  # noqa: E501
        """Modify a Security Group Rule  # noqa: E501

        Modifies the properties of the specified Security Group Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_rules_put(datacenter_id, security_group_id, rule_id, rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param rule_id: The unique ID of the Security Group Rule. (required)
        :type rule_id: str
        :param rule: The modified Security Group Rule. (required)
        :type rule: FirewallRule
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: FirewallRule
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_securitygroups_rules_put_with_http_info(datacenter_id, security_group_id, rule_id, rule, **kwargs)  # noqa: E501

    def datacenters_securitygroups_rules_put_with_http_info(self, datacenter_id, security_group_id, rule_id, rule, **kwargs):  # noqa: E501
        """Modify a Security Group Rule  # noqa: E501

        Modifies the properties of the specified Security Group Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_securitygroups_rules_put_with_http_info(datacenter_id, security_group_id, rule_id, rule, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param security_group_id: The unique ID of the security group. (required)
        :type security_group_id: str
        :param rule_id: The unique ID of the Security Group Rule. (required)
        :type rule_id: str
        :param rule: The modified Security Group Rule. (required)
        :type rule: FirewallRule
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(FirewallRule, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'security_group_id',
            'rule_id',
            'rule',
            'pretty',
            'depth'
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
                    " to method datacenters_securitygroups_rules_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_securitygroups_rules_put`")  # noqa: E501
        # verify the required parameter 'security_group_id' is set
        if self.api_client.client_side_validation and ('security_group_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_group_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_group_id` when calling `datacenters_securitygroups_rules_put`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if self.api_client.client_side_validation and ('rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rule_id` when calling `datacenters_securitygroups_rules_put`")  # noqa: E501
        # verify the required parameter 'rule' is set
        if self.api_client.client_side_validation and ('rule' not in local_var_params or  # noqa: E501
                                                        local_var_params['rule'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rule` when calling `datacenters_securitygroups_rules_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_rules_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_securitygroups_rules_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'security_group_id' in local_var_params:
            path_params['securityGroupId'] = local_var_params['security_group_id']  # noqa: E501
        if 'rule_id' in local_var_params:
            path_params['ruleId'] = local_var_params['rule_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rule' in local_var_params:
            body_params = local_var_params['rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'FirewallRule'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/securitygroups/{securityGroupId}/rules/{ruleId}', 'PUT',
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

    def datacenters_servers_nics_securitygroups_put(self, datacenter_id, server_id, nic_id, securitygroups, **kwargs):  # noqa: E501
        """Attach a list of Security Groups to a NIC  # noqa: E501

        Updating the list of Security Groups attached to an existing NIC specified by its ID.  Security Groups should already exist as part of the datacenter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_securitygroups_put(datacenter_id, server_id, nic_id, securitygroups, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic_id: The unique ID of the server. (required)
        :type nic_id: str
        :param securitygroups: The list of NIC attached Security Groups IDs. (required)
        :type securitygroups: ListOfIds
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: SecurityGroups
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_nics_securitygroups_put_with_http_info(datacenter_id, server_id, nic_id, securitygroups, **kwargs)  # noqa: E501

    def datacenters_servers_nics_securitygroups_put_with_http_info(self, datacenter_id, server_id, nic_id, securitygroups, **kwargs):  # noqa: E501
        """Attach a list of Security Groups to a NIC  # noqa: E501

        Updating the list of Security Groups attached to an existing NIC specified by its ID.  Security Groups should already exist as part of the datacenter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_nics_securitygroups_put_with_http_info(datacenter_id, server_id, nic_id, securitygroups, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param nic_id: The unique ID of the server. (required)
        :type nic_id: str
        :param securitygroups: The list of NIC attached Security Groups IDs. (required)
        :type securitygroups: ListOfIds
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(SecurityGroups, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'nic_id',
            'securitygroups',
            'pretty',
            'depth'
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
                    " to method datacenters_servers_nics_securitygroups_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_nics_securitygroups_put`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_nics_securitygroups_put`")  # noqa: E501
        # verify the required parameter 'nic_id' is set
        if self.api_client.client_side_validation and ('nic_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nic_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nic_id` when calling `datacenters_servers_nics_securitygroups_put`")  # noqa: E501
        # verify the required parameter 'securitygroups' is set
        if self.api_client.client_side_validation and ('securitygroups' not in local_var_params or  # noqa: E501
                                                        local_var_params['securitygroups'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `securitygroups` when calling `datacenters_servers_nics_securitygroups_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_securitygroups_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_nics_securitygroups_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501
        if 'nic_id' in local_var_params:
            path_params['nicId'] = local_var_params['nic_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'securitygroups' in local_var_params:
            body_params = local_var_params['securitygroups']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'SecurityGroups'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/nics/{nicId}/securitygroups', 'PUT',
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

    def datacenters_servers_securitygroups_put(self, datacenter_id, server_id, securitygroups, **kwargs):  # noqa: E501
        """Attach a list of Security Groups to a Server  # noqa: E501

        Updating the list of Security Groups attached to an existing server specified by its ID.  Security Groups should already exist as part of the datacenter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_securitygroups_put(datacenter_id, server_id, securitygroups, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param securitygroups: The list of server attached Security Groups IDs. (required)
        :type securitygroups: ListOfIds
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: SecurityGroups
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_servers_securitygroups_put_with_http_info(datacenter_id, server_id, securitygroups, **kwargs)  # noqa: E501

    def datacenters_servers_securitygroups_put_with_http_info(self, datacenter_id, server_id, securitygroups, **kwargs):  # noqa: E501
        """Attach a list of Security Groups to a Server  # noqa: E501

        Updating the list of Security Groups attached to an existing server specified by its ID.  Security Groups should already exist as part of the datacenter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_servers_securitygroups_put_with_http_info(datacenter_id, server_id, securitygroups, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the data center. (required)
        :type datacenter_id: str
        :param server_id: The unique ID of the server. (required)
        :type server_id: str
        :param securitygroups: The list of server attached Security Groups IDs. (required)
        :type securitygroups: ListOfIds
        :param pretty: Controls whether the response is pretty-printed (with indentations and new lines).
        :type pretty: bool
        :param depth: Controls the detail depth of the response objects. GET /datacenters/[ID]   - depth=0: Only direct properties are included;              children (servers and other elements) are not included.   - depth=1: Direct properties and children references are included.   - depth=2: Direct properties and children properties are included.   - depth=3: Direct properties and children properties and children's children are included.   - depth=... and so on
        :type depth: int
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
        :rtype: tuple(SecurityGroups, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'server_id',
            'securitygroups',
            'pretty',
            'depth'
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
                    " to method datacenters_servers_securitygroups_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_servers_securitygroups_put`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if self.api_client.client_side_validation and ('server_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['server_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `server_id` when calling `datacenters_servers_securitygroups_put`")  # noqa: E501
        # verify the required parameter 'securitygroups' is set
        if self.api_client.client_side_validation and ('securitygroups' not in local_var_params or  # noqa: E501
                                                        local_var_params['securitygroups'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `securitygroups` when calling `datacenters_servers_securitygroups_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_securitygroups_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_servers_securitygroups_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
        if 'server_id' in local_var_params:
            path_params['serverId'] = local_var_params['server_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'depth' in local_var_params and local_var_params['depth'] is not None:  # noqa: E501
            query_params.append(('depth', local_var_params['depth']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'securitygroups' in local_var_params:
            body_params = local_var_params['securitygroups']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuthentication', 'TokenAuthentication']  # noqa: E501

        response_type = 'SecurityGroups'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/servers/{serverId}/securitygroups', 'PUT',
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
