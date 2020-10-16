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
from ionossdk.models.group_shares import GroupShares  # noqa: E501
from ionossdk.rest import ApiException

class TestGroupShares(unittest.TestCase):
    """GroupShares unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GroupShares
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionossdk.models.group_shares.GroupShares()  # noqa: E501
        if include_optional :
            return GroupShares(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                type = "shares", 
                href = 'https://<API_HOST>/cloudapi/v5/um/groups/15f67991-0f51-4efc-a8ad-ef1fb31a480c/shares', 
                items = [
                    ionossdk.models.group_share.GroupShare(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "resource", 
                        href = 'https://<API_HOST>/cloudapi/v5/um/groups/15f67991-0f51-4efc-a8ad-ef1fb31a480c/shares/17faab13-13abc-4efc-a8ad-ef1fb31a481b', 
                        properties = ionossdk.models.group_share_properties.GroupShareProperties(
                            edit_privilege = True, 
                            share_privilege = True, ), )
                    ]
            )
        else :
            return GroupShares(
        )

    def testGroupShares(self):
        """Test GroupShares"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
