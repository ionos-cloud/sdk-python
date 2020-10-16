# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ionossdk
from ionossdk.api.load_balancer_api import LoadBalancerApi  # noqa: E501
from ionossdk.rest import ApiException


class TestLoadBalancerApi(unittest.TestCase):
    """LoadBalancerApi unit test stubs"""

    def setUp(self):
        self.api = ionossdk.api.load_balancer_api.LoadBalancerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_datacenters_loadbalancers_balancednics_delete(self):
        """Test case for datacenters_loadbalancers_balancednics_delete

        Detach a nic from loadbalancer  # noqa: E501
        """
        pass

    def test_datacenters_loadbalancers_balancednics_find_by_nic(self):
        """Test case for datacenters_loadbalancers_balancednics_find_by_nic

        Retrieve a nic attached to Load Balancer  # noqa: E501
        """
        pass

    def test_datacenters_loadbalancers_balancednics_get(self):
        """Test case for datacenters_loadbalancers_balancednics_get

        List Load Balancer Members   # noqa: E501
        """
        pass

    def test_datacenters_loadbalancers_balancednics_post(self):
        """Test case for datacenters_loadbalancers_balancednics_post

        Attach a nic to Load Balancer  # noqa: E501
        """
        pass

    def test_datacenters_loadbalancers_delete(self):
        """Test case for datacenters_loadbalancers_delete

        Delete a Loadbalancer.  # noqa: E501
        """
        pass

    def test_datacenters_loadbalancers_find_by_id(self):
        """Test case for datacenters_loadbalancers_find_by_id

        Retrieve a loadbalancer  # noqa: E501
        """
        pass

    def test_datacenters_loadbalancers_get(self):
        """Test case for datacenters_loadbalancers_get

        List Load Balancers  # noqa: E501
        """
        pass

    def test_datacenters_loadbalancers_patch(self):
        """Test case for datacenters_loadbalancers_patch

        Partially modify a Loadbalancer  # noqa: E501
        """
        pass

    def test_datacenters_loadbalancers_post(self):
        """Test case for datacenters_loadbalancers_post

        Create a Load Balancer  # noqa: E501
        """
        pass

    def test_datacenters_loadbalancers_put(self):
        """Test case for datacenters_loadbalancers_put

        Modify a Load Balancer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
