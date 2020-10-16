# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ionossdk
from ionossdk.models.no_state_meta_data import NoStateMetaData  # noqa: E501
from ionossdk.rest import ApiException

class TestNoStateMetaData(unittest.TestCase):
    """NoStateMetaData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NoStateMetaData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionossdk.models.no_state_meta_data.NoStateMetaData()  # noqa: E501
        if include_optional :
            return NoStateMetaData(
                etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                created_date = '2015-12-04T14:34:09.809Z', 
                created_by = 'user@example.com', 
                created_by_user_id = 'user@example.com', 
                last_modified_date = '2015-12-04T14:34:09.809Z', 
                last_modified_by = 'user@example.com', 
                last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90'
            )
        else :
            return NoStateMetaData(
        )

    def testNoStateMetaData(self):
        """Test NoStateMetaData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
