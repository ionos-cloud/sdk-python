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
from ionoscloud.models.kubernetes_node_pool_for_post import KubernetesNodePoolForPost  # noqa: E501
from ionoscloud.rest import ApiException

class TestKubernetesNodePoolForPost(unittest.TestCase):
    """KubernetesNodePoolForPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubernetesNodePoolForPost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.kubernetes_node_pool_for_post.KubernetesNodePoolForPost()  # noqa: E501
        if include_optional :
            return KubernetesNodePoolForPost(
                id = '1e072e52-2ed3-492f-b6b6-c6b116907527',
                type = 'nodepool',
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
                properties = ionoscloud.models.kubernetes_node_pool_properties_for_post.KubernetesNodePoolPropertiesForPost(
                    name = 'k8s-node-pool', 
                    datacenter_id = '1e072e52-2ed3-492f-b6b6-c6b116907521', 
                    node_count = 2, 
                    cpu_family = 'AMD_OPTERON', 
                    cores_count = 4, 
                    ram_size = 2048, 
                    availability_zone = 'AUTO', 
                    storage_type = 'HDD', 
                    storage_size = 100, 
                    k8s_version = '1.15.4', 
                    maintenance_window = ionoscloud.models.kubernetes_maintenance_window.KubernetesMaintenanceWindow(
                        day_of_the_week = 'Monday', 
                        time = '13:00:00', ), 
                    auto_scaling = ionoscloud.models.kubernetes_auto_scaling.KubernetesAutoScaling(
                        min_node_count = 1, 
                        max_node_count = 1, ), 
                    lans = [
                        ionoscloud.models.kubernetes_node_pool_lan.KubernetesNodePoolLan(
                            id = 3, 
                            dhcp = True, 
                            routes = [
                                ionoscloud.models.kubernetes_node_pool_lan_routes.KubernetesNodePoolLanRoutes(
                                    network = '1.2.3.4/24', 
                                    gateway_ip = '10.1.5.16', )
                                ], )
                        ], 
                    labels = {
                        'key' : ''
                        }, 
                    annotations = {
                        'key' : ''
                        }, 
                    public_ips = [81.173.1.2, 82.231.2.5, 92.221.2.4], )
            )
        else :
            return KubernetesNodePoolForPost(
                properties = ionoscloud.models.kubernetes_node_pool_properties_for_post.KubernetesNodePoolPropertiesForPost(
                    name = 'k8s-node-pool', 
                    datacenter_id = '1e072e52-2ed3-492f-b6b6-c6b116907521', 
                    node_count = 2, 
                    cpu_family = 'AMD_OPTERON', 
                    cores_count = 4, 
                    ram_size = 2048, 
                    availability_zone = 'AUTO', 
                    storage_type = 'HDD', 
                    storage_size = 100, 
                    k8s_version = '1.15.4', 
                    maintenance_window = ionoscloud.models.kubernetes_maintenance_window.KubernetesMaintenanceWindow(
                        day_of_the_week = 'Monday', 
                        time = '13:00:00', ), 
                    auto_scaling = ionoscloud.models.kubernetes_auto_scaling.KubernetesAutoScaling(
                        min_node_count = 1, 
                        max_node_count = 1, ), 
                    lans = [
                        ionoscloud.models.kubernetes_node_pool_lan.KubernetesNodePoolLan(
                            id = 3, 
                            dhcp = True, 
                            routes = [
                                ionoscloud.models.kubernetes_node_pool_lan_routes.KubernetesNodePoolLanRoutes(
                                    network = '1.2.3.4/24', 
                                    gateway_ip = '10.1.5.16', )
                                ], )
                        ], 
                    labels = {
                        'key' : ''
                        }, 
                    annotations = {
                        'key' : ''
                        }, 
                    public_ips = [81.173.1.2, 82.231.2.5, 92.221.2.4], ),
        )

    def testKubernetesNodePoolForPost(self):
        """Test KubernetesNodePoolForPost"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
