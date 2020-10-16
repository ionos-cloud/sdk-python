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
from ionossdk.models.lan_properties import LanProperties  # noqa: E501
from ionossdk.rest import ApiException

class TestLanProperties(unittest.TestCase):
    """LanProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LanProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionossdk.models.lan_properties.LanProperties()  # noqa: E501
        if include_optional :
            return LanProperties(
                name = 'My resource', 
                ip_failover = { "ipFailover": [ { "ip": "192.18.2.231", "nicUuid": "3c11273c-b3e1-4ca3-8134-84fd2dd4ebec"} ] }, 
                pcc = '3c11273c-b3e1-4ca3-8134-84fd2dd4ebec', 
                public = True
            )
        else :
            return LanProperties(
        )

    def testLanProperties(self):
        """Test LanProperties"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
