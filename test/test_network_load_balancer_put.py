# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ionoscloud
from ionoscloud.models.network_load_balancer_put import NetworkLoadBalancerPut  # noqa: E501
from ionoscloud.rest import ApiException

class TestNetworkLoadBalancerPut(unittest.TestCase):
    """NetworkLoadBalancerPut unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NetworkLoadBalancerPut
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.network_load_balancer_put.NetworkLoadBalancerPut()  # noqa: E501
        if include_optional :
            return NetworkLoadBalancerPut(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = "networkloadbalancer",
                href = '<RESOURCE-URI>',
                properties = ionoscloud.models.network_load_balancer_properties.NetworkLoadBalancerProperties(
                    name = 'My Network Load Balancer', 
                    listener_lan = 1, 
                    ips = [81.173.1.2, 22.231.2.2, 22.231.2.3], 
                    target_lan = 2, 
                    lb_private_ips = [81.173.1.5/24, 22.231.2.5/24], )
            )
        else :
            return NetworkLoadBalancerPut(
                properties = ionoscloud.models.network_load_balancer_properties.NetworkLoadBalancerProperties(
                    name = 'My Network Load Balancer', 
                    listener_lan = 1, 
                    ips = [81.173.1.2, 22.231.2.2, 22.231.2.3], 
                    target_lan = 2, 
                    lb_private_ips = [81.173.1.5/24, 22.231.2.5/24], ),
        )

    def testNetworkLoadBalancerPut(self):
        """Test NetworkLoadBalancerPut"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
