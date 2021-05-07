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
from ionoscloud.models.loadbalancer import Loadbalancer  # noqa: E501
from ionoscloud.rest import ApiException

class TestLoadbalancer(unittest.TestCase):
    """Loadbalancer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Loadbalancer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.loadbalancer.Loadbalancer()  # noqa: E501
        if include_optional :
            return Loadbalancer(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = "loadbalancer",
                href = '<RESOURCE-URI>',
                metadata = ionoscloud.models.datacenter_element_metadata.DatacenterElementMetadata(
                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                    created_date = '2015-12-04T14:34:09.809Z', 
                    created_by = 'user@example.com', 
                    created_by_user_id = 'user@example.com', 
                    last_modified_date = '2015-12-04T14:34:09.809Z', 
                    last_modified_by = 'user@example.com', 
                    last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                    state = 'AVAILABLE', ),
                properties = ionoscloud.models.loadbalancer_properties.LoadbalancerProperties(
                    name = 'My resource', 
                    ip = '22.231.113.64', 
                    dhcp = True, ),
                entities = ionoscloud.models.loadbalancer_entities.LoadbalancerEntities(
                    balancednics = ionoscloud.models.balanced_nics.BalancedNics(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "collection", 
                        href = '<RESOURCE-URI>', 
                        items = [
                            ionoscloud.models.nic.Nic(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "nic", 
                                href = '<RESOURCE-URI>', 
                                metadata = ionoscloud.models.datacenter_element_metadata.DatacenterElementMetadata(
                                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                                    created_date = '2015-12-04T14:34:09.809Z', 
                                    created_by = 'user@example.com', 
                                    created_by_user_id = 'user@example.com', 
                                    last_modified_date = '2015-12-04T14:34:09.809Z', 
                                    last_modified_by = 'user@example.com', 
                                    last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                                    state = 'AVAILABLE', ), 
                                properties = ionoscloud.models.nic_properties.NicProperties(
                                    name = 'My resource', 
                                    mac = '00:0a:95:9d:68:16', 
                                    ips = [
                                        ''
                                        ], 
                                    dhcp = True, 
                                    lan = 2, 
                                    firewall_active = False, 
                                    firewall_type = 'INGRESS', 
                                    device_number = 3, 
                                    pci_slot = 7, ), )
                            ], 
                        offset = 0, 
                        limit = 1000, 
                        _links = ionoscloud.models.pagination_links.PaginationLinks(
                            prev = '<PREVIOUS-PAGE-URI>', 
                            self = '<THIS-PAGE-URI>', 
                            next = '<NEXT-PAGE-URI>', ), ), )
            )
        else :
            return Loadbalancer(
                properties = ionoscloud.models.loadbalancer_properties.LoadbalancerProperties(
                    name = 'My resource', 
                    ip = '22.231.113.64', 
                    dhcp = True, ),
        )

    def testLoadbalancer(self):
        """Test Loadbalancer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
