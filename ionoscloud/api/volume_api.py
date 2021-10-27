from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud.api_client import ApiClient
from ionoscloud.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class VolumeApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def datacenters_volumes_create_snapshot_post(self, datacenter_id, volume_id, **kwargs):  # noqa: E501
        """Create Volume Snapshot  # noqa: E501

        Creates a snapshot of a volume within the datacenter. You can use a snapshot to create a new storage volume or to restore a storage volume.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_create_snapshot_post(datacenter_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param name: The name of the snapshot
        :type name: str
        :param description: The description of the snapshot
        :type description: str
        :param sec_auth_protection: Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc.
        :type sec_auth_protection: bool
        :param licence_type: The OS type of this Snapshot
        :type licence_type: str
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
        :rtype: Snapshot
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_volumes_create_snapshot_post_with_http_info(datacenter_id, volume_id, **kwargs)  # noqa: E501

    def datacenters_volumes_create_snapshot_post_with_http_info(self, datacenter_id, volume_id, **kwargs):  # noqa: E501
        """Create Volume Snapshot  # noqa: E501

        Creates a snapshot of a volume within the datacenter. You can use a snapshot to create a new storage volume or to restore a storage volume.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_create_snapshot_post_with_http_info(datacenter_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param name: The name of the snapshot
        :type name: str
        :param description: The description of the snapshot
        :type description: str
        :param sec_auth_protection: Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc.
        :type sec_auth_protection: bool
        :param licence_type: The OS type of this Snapshot
        :type licence_type: str
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
        :rtype: tuple(Snapshot, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'datacenter_id',
            'volume_id',
            'pretty',
            'depth',
            'x_contract_number',
            'name',
            'description',
            'sec_auth_protection',
            'licence_type'
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
                    " to method datacenters_volumes_create_snapshot_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_volumes_create_snapshot_post`")  # noqa: E501
        # verify the required parameter 'volume_id' is set
        if self.api_client.client_side_validation and ('volume_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume_id` when calling `datacenters_volumes_create_snapshot_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_create_snapshot_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_create_snapshot_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
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
        if 'name' in local_var_params:
            form_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'description' in local_var_params:
            form_params.append(('description', local_var_params['description']))  # noqa: E501
        if 'sec_auth_protection' in local_var_params:
            form_params.append(('secAuthProtection', local_var_params['sec_auth_protection']))  # noqa: E501
        if 'licence_type' in local_var_params:
            form_params.append(('licenceType', local_var_params['licence_type']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Snapshot'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/volumes/{volumeId}/create-snapshot', 'POST',
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

    def datacenters_volumes_delete(self, datacenter_id, volume_id, **kwargs):  # noqa: E501
        """Delete a Volume  # noqa: E501

        Deletes the specified volume. This will result in the volume being removed from your datacenter. Use this with caution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_delete(datacenter_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
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
        return self.datacenters_volumes_delete_with_http_info(datacenter_id, volume_id, **kwargs)  # noqa: E501

    def datacenters_volumes_delete_with_http_info(self, datacenter_id, volume_id, **kwargs):  # noqa: E501
        """Delete a Volume  # noqa: E501

        Deletes the specified volume. This will result in the volume being removed from your datacenter. Use this with caution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_delete_with_http_info(datacenter_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
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
                    " to method datacenters_volumes_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_volumes_delete`")  # noqa: E501
        # verify the required parameter 'volume_id' is set
        if self.api_client.client_side_validation and ('volume_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume_id` when calling `datacenters_volumes_delete`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_delete`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_delete`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
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
            '/datacenters/{datacenterId}/volumes/{volumeId}', 'DELETE',
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

    def datacenters_volumes_find_by_id(self, datacenter_id, volume_id, **kwargs):  # noqa: E501
        """Retrieve a Volume  # noqa: E501

        Retrieves the attributes of a given Volume  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_find_by_id(datacenter_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
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
        return self.datacenters_volumes_find_by_id_with_http_info(datacenter_id, volume_id, **kwargs)  # noqa: E501

    def datacenters_volumes_find_by_id_with_http_info(self, datacenter_id, volume_id, **kwargs):  # noqa: E501
        """Retrieve a Volume  # noqa: E501

        Retrieves the attributes of a given Volume  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_find_by_id_with_http_info(datacenter_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
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
                    " to method datacenters_volumes_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_volumes_find_by_id`")  # noqa: E501
        # verify the required parameter 'volume_id' is set
        if self.api_client.client_side_validation and ('volume_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume_id` when calling `datacenters_volumes_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_find_by_id`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_find_by_id`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
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
            '/datacenters/{datacenterId}/volumes/{volumeId}', 'GET',
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

    def datacenters_volumes_get(self, datacenter_id, **kwargs):  # noqa: E501
        """List Volumes   # noqa: E501

        Retrieves a list of Volumes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_get(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
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
        :rtype: Volumes
        """
        kwargs['_return_http_data_only'] = True
        return self.datacenters_volumes_get_with_http_info(datacenter_id, **kwargs)  # noqa: E501

    def datacenters_volumes_get_with_http_info(self, datacenter_id, **kwargs):  # noqa: E501
        """List Volumes   # noqa: E501

        Retrieves a list of Volumes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_get_with_http_info(datacenter_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
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
        :rtype: tuple(Volumes, status_code(int), headers(HTTPHeaderDict))
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
                    " to method datacenters_volumes_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_volumes_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_get`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `datacenters_volumes_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_volumes_get`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `datacenters_volumes_get`, must be a value greater than or equal to `1`")  # noqa: E501
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

        response_type = 'Volumes'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/volumes', 'GET',
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

    def datacenters_volumes_patch(self, datacenter_id, volume_id, volume, **kwargs):  # noqa: E501
        """Partially modify a Volume  # noqa: E501

        You can use update attributes of a Volume  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_patch(datacenter_id, volume_id, volume, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param volume: Modified properties of Volume (required)
        :type volume: VolumeProperties
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
        return self.datacenters_volumes_patch_with_http_info(datacenter_id, volume_id, volume, **kwargs)  # noqa: E501

    def datacenters_volumes_patch_with_http_info(self, datacenter_id, volume_id, volume, **kwargs):  # noqa: E501
        """Partially modify a Volume  # noqa: E501

        You can use update attributes of a Volume  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_patch_with_http_info(datacenter_id, volume_id, volume, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param volume: Modified properties of Volume (required)
        :type volume: VolumeProperties
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
            'volume_id',
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
                    " to method datacenters_volumes_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_volumes_patch`")  # noqa: E501
        # verify the required parameter 'volume_id' is set
        if self.api_client.client_side_validation and ('volume_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume_id` when calling `datacenters_volumes_patch`")  # noqa: E501
        # verify the required parameter 'volume' is set
        if self.api_client.client_side_validation and ('volume' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume` when calling `datacenters_volumes_patch`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_patch`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_patch`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
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
        if 'volume' in local_var_params:
            body_params = local_var_params['volume']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Volume'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/volumes/{volumeId}', 'PATCH',
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

    def datacenters_volumes_post(self, datacenter_id, volume, **kwargs):  # noqa: E501
        """Create a Volume  # noqa: E501

        Creates a volume within the datacenter. This will not attach the volume to a server. Please see the Servers section for details on how to attach storage volumes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_post(datacenter_id, volume, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param volume: Volume to be created (required)
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
        return self.datacenters_volumes_post_with_http_info(datacenter_id, volume, **kwargs)  # noqa: E501

    def datacenters_volumes_post_with_http_info(self, datacenter_id, volume, **kwargs):  # noqa: E501
        """Create a Volume  # noqa: E501

        Creates a volume within the datacenter. This will not attach the volume to a server. Please see the Servers section for details on how to attach storage volumes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_post_with_http_info(datacenter_id, volume, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param volume: Volume to be created (required)
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
                    " to method datacenters_volumes_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_volumes_post`")  # noqa: E501
        # verify the required parameter 'volume' is set
        if self.api_client.client_side_validation and ('volume' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume` when calling `datacenters_volumes_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_post`, must be a value greater than or equal to `0`")  # noqa: E501
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
        if 'volume' in local_var_params:
            body_params = local_var_params['volume']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Volume'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/volumes', 'POST',
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

    def datacenters_volumes_put(self, datacenter_id, volume_id, volume, **kwargs):  # noqa: E501
        """Modify a Volume  # noqa: E501

        You can use update attributes of a Volume  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_put(datacenter_id, volume_id, volume, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param volume: Modified Volume (required)
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
        return self.datacenters_volumes_put_with_http_info(datacenter_id, volume_id, volume, **kwargs)  # noqa: E501

    def datacenters_volumes_put_with_http_info(self, datacenter_id, volume_id, volume, **kwargs):  # noqa: E501
        """Modify a Volume  # noqa: E501

        You can use update attributes of a Volume  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_put_with_http_info(datacenter_id, volume_id, volume, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param volume: Modified Volume (required)
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
            'volume_id',
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
                    " to method datacenters_volumes_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_volumes_put`")  # noqa: E501
        # verify the required parameter 'volume_id' is set
        if self.api_client.client_side_validation and ('volume_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume_id` when calling `datacenters_volumes_put`")  # noqa: E501
        # verify the required parameter 'volume' is set
        if self.api_client.client_side_validation and ('volume' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume` when calling `datacenters_volumes_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_put`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_put`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
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
        if 'volume' in local_var_params:
            body_params = local_var_params['volume']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'Volume'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/volumes/{volumeId}', 'PUT',
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

    def datacenters_volumes_restore_snapshot_post(self, datacenter_id, volume_id, **kwargs):  # noqa: E501
        """Restore Volume Snapshot  # noqa: E501

        This will restore a snapshot onto a volume. A snapshot is created as just another image that can be used to create subsequent volumes if you want or to restore an existing volume.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_restore_snapshot_post(datacenter_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param snapshot_id: This is the ID of the snapshot
        :type snapshot_id: str
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
        return self.datacenters_volumes_restore_snapshot_post_with_http_info(datacenter_id, volume_id, **kwargs)  # noqa: E501

    def datacenters_volumes_restore_snapshot_post_with_http_info(self, datacenter_id, volume_id, **kwargs):  # noqa: E501
        """Restore Volume Snapshot  # noqa: E501

        This will restore a snapshot onto a volume. A snapshot is created as just another image that can be used to create subsequent volumes if you want or to restore an existing volume.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.datacenters_volumes_restore_snapshot_post_with_http_info(datacenter_id, volume_id, async_req=True)
        >>> result = thread.get()

        :param datacenter_id: The unique ID of the datacenter (required)
        :type datacenter_id: str
        :param volume_id: The unique ID of the Volume (required)
        :type volume_id: str
        :param pretty: Controls whether response is pretty-printed (with indentation and new lines)
        :type pretty: bool
        :param depth: Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on
        :type depth: int
        :param x_contract_number: Users having more than 1 contract need to provide contract number, against which all API requests should be executed
        :type x_contract_number: int
        :param snapshot_id: This is the ID of the snapshot
        :type snapshot_id: str
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
            'volume_id',
            'pretty',
            'depth',
            'x_contract_number',
            'snapshot_id'
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
                    " to method datacenters_volumes_restore_snapshot_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'datacenter_id' is set
        if self.api_client.client_side_validation and ('datacenter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['datacenter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `datacenter_id` when calling `datacenters_volumes_restore_snapshot_post`")  # noqa: E501
        # verify the required parameter 'volume_id' is set
        if self.api_client.client_side_validation and ('volume_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['volume_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `volume_id` when calling `datacenters_volumes_restore_snapshot_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] > 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_restore_snapshot_post`, must be a value less than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'depth' in local_var_params and local_var_params['depth'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `depth` when calling `datacenters_volumes_restore_snapshot_post`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'datacenter_id' in local_var_params:
            path_params['datacenterId'] = local_var_params['datacenter_id']  # noqa: E501
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
        if 'snapshot_id' in local_var_params:
            form_params.append(('snapshotId', local_var_params['snapshot_id']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic Authentication', 'Token Authentication']  # noqa: E501

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/datacenters/{datacenterId}/volumes/{volumeId}/restore-snapshot', 'POST',
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
