# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ionoscloud
from ionoscloud.api.requests_api import RequestsApi  # noqa: E501
from ionoscloud.rest import ApiException


class TestRequestsApi(unittest.TestCase):
    """RequestsApi unit test stubs"""

    def setUp(self):
        self.api = ionoscloud.api.requests_api.RequestsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_requests_find_by_id(self):
        """Test case for requests_find_by_id

        Retrieve a Request  # noqa: E501
        """
        pass

    def test_requests_get(self):
        """Test case for requests_get

        List Requests  # noqa: E501
        """
        pass

    def test_requests_status_get(self):
        """Test case for requests_status_get

        Retrieve Request Status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
