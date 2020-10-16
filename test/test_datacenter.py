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
from ionossdk.models.datacenter import Datacenter  # noqa: E501
from ionossdk.rest import ApiException

class TestDatacenter(unittest.TestCase):
    """Datacenter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Datacenter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionossdk.models.datacenter.Datacenter()  # noqa: E501
        if include_optional :
            return Datacenter(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                type = "datacenter", 
                href = '<RESOURCE-URI>', 
                metadata = ionossdk.models.datacenter_element_metadata.DatacenterElementMetadata(
                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                    created_date = '2015-12-04T14:34:09.809Z', 
                    created_by = 'user@example.com', 
                    created_by_user_id = 'user@example.com', 
                    last_modified_date = '2015-12-04T14:34:09.809Z', 
                    last_modified_by = 'user@example.com', 
                    last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                    state = 'AVAILABLE', ), 
                properties = ionossdk.models.datacenter_properties.DatacenterProperties(
                    name = 'My resource', 
                    description = 'My Production Datacenter', 
                    location = 'us/las', 
                    version = 8, 
                    features = [SSD], 
                    sec_auth_protection = True, ), 
                entities = ionossdk.models.datacenter_entities.DatacenterEntities(
                    servers = ionossdk.models.servers.Servers(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "collection", 
                        href = '<RESOURCE-URI>', 
                        items = [
                            ionossdk.models.server.Server(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "server", 
                                href = '<RESOURCE-URI>', 
                                metadata = ionossdk.models.datacenter_element_metadata.DatacenterElementMetadata(
                                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                                    created_date = '2015-12-04T14:34:09.809Z', 
                                    created_by = 'user@example.com', 
                                    created_by_user_id = 'user@example.com', 
                                    last_modified_date = '2015-12-04T14:34:09.809Z', 
                                    last_modified_by = 'user@example.com', 
                                    last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                                    state = 'AVAILABLE', ), 
                                properties = ionossdk.models.server_properties.ServerProperties(
                                    name = 'My resource', 
                                    cores = 4, 
                                    ram = 4096, 
                                    availability_zone = 'AUTO', 
                                    vm_state = 'RUNNING', 
                                    boot_cdrom = ionossdk.models.resource_reference.ResourceReference(
                                        id = '0', 
                                        type = "resource", 
                                        href = '<RESOURCE-URI>', ), 
                                    boot_volume = ionossdk.models.resource_reference.ResourceReference(
                                        id = '0', 
                                        type = "resource", 
                                        href = '<RESOURCE-URI>', ), 
                                    cpu_family = 'AMD_OPTERON', ), 
                                entities = ionossdk.models.server_entities.ServerEntities(
                                    cdroms = ionossdk.models.cdroms.Cdroms(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = "collection", 
                                        href = '<RESOURCE-URI>', ), 
                                    volumes = ionossdk.models.attached_volumes.AttachedVolumes(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = "collection", 
                                        href = '<RESOURCE-URI>', ), 
                                    nics = ionossdk.models.nics.Nics(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = "collection", 
                                        href = '<RESOURCE-URI>', ), ), )
                            ], ), 
                    volumes = ionossdk.models.volumes.Volumes(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "collection", 
                        href = '<RESOURCE-URI>', ), 
                    loadbalancers = ionossdk.models.loadbalancers.Loadbalancers(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "collection", 
                        href = '<RESOURCE-URI>', ), 
                    lans = ionossdk.models.lans.Lans(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "collection", 
                        href = '<RESOURCE-URI>', ), )
            )
        else :
            return Datacenter(
                properties = ionossdk.models.datacenter_properties.DatacenterProperties(
                    name = 'My resource', 
                    description = 'My Production Datacenter', 
                    location = 'us/las', 
                    version = 8, 
                    features = [SSD], 
                    sec_auth_protection = True, ),
        )

    def testDatacenter(self):
        """Test Datacenter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
