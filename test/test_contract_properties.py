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
from ionossdk.models.contract_properties import ContractProperties  # noqa: E501
from ionossdk.rest import ApiException

class TestContractProperties(unittest.TestCase):
    """ContractProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContractProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionossdk.models.contract_properties.ContractProperties()  # noqa: E501
        if include_optional :
            return ContractProperties(
                contract_number = 56, 
                owner = '0', 
                status = '0', 
                reg_domain = '0', 
                resource_limits = ionossdk.models.resource_limits.ResourceLimits(
                    cores_per_server = 56, 
                    cores_per_contract = 56, 
                    cores_provisioned = 56, 
                    ram_per_server = 56, 
                    ram_per_contract = 56, 
                    ram_provisioned = 56, 
                    hdd_limit_per_volume = 56, 
                    hdd_limit_per_contract = 56, 
                    hdd_volume_provisioned = 56, 
                    ssd_limit_per_volume = 56, 
                    ssd_limit_per_contract = 56, 
                    ssd_volume_provisioned = 56, 
                    reservable_ips = 56, 
                    reserved_ips_on_contract = 56, 
                    reserved_ips_in_use = 56, 
                    k8s_cluster_limit_total = 56, 
                    k8s_clusters_provisioned = 56, )
            )
        else :
            return ContractProperties(
        )

    def testContractProperties(self):
        """Test ContractProperties"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
