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
from ionossdk.api.server_api import ServerApi  # noqa: E501
from ionossdk.rest import ApiException


class TestServerApi(unittest.TestCase):
    """ServerApi unit test stubs"""

    def setUp(self):
        self.api = ionossdk.api.server_api.ServerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_datacenters_servers_cdroms_delete(self):
        """Test case for datacenters_servers_cdroms_delete

        Detach a CD-ROM  # noqa: E501
        """
        pass

    def test_datacenters_servers_cdroms_find_by_id(self):
        """Test case for datacenters_servers_cdroms_find_by_id

        Retrieve an attached CD-ROM  # noqa: E501
        """
        pass

    def test_datacenters_servers_cdroms_get(self):
        """Test case for datacenters_servers_cdroms_get

        List attached CD-ROMs   # noqa: E501
        """
        pass

    def test_datacenters_servers_cdroms_post(self):
        """Test case for datacenters_servers_cdroms_post

        Attach a CD-ROM  # noqa: E501
        """
        pass

    def test_datacenters_servers_delete(self):
        """Test case for datacenters_servers_delete

        Delete a Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_find_by_id(self):
        """Test case for datacenters_servers_find_by_id

        Retrieve a Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_get(self):
        """Test case for datacenters_servers_get

        List Servers   # noqa: E501
        """
        pass

    def test_datacenters_servers_patch(self):
        """Test case for datacenters_servers_patch

        Partially modify a Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_post(self):
        """Test case for datacenters_servers_post

        Create a Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_put(self):
        """Test case for datacenters_servers_put

        Modify a Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_reboot_post(self):
        """Test case for datacenters_servers_reboot_post

        Reboot a Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_start_post(self):
        """Test case for datacenters_servers_start_post

        Start a Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_stop_post(self):
        """Test case for datacenters_servers_stop_post

        Stop a Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_upgrade_post(self):
        """Test case for datacenters_servers_upgrade_post

        Upgrade a Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_volumes_delete(self):
        """Test case for datacenters_servers_volumes_delete

        Detach a volume  # noqa: E501
        """
        pass

    def test_datacenters_servers_volumes_find_by_id(self):
        """Test case for datacenters_servers_volumes_find_by_id

        Retrieve an attached volume  # noqa: E501
        """
        pass

    def test_datacenters_servers_volumes_get(self):
        """Test case for datacenters_servers_volumes_get

        List Attached Volumes  # noqa: E501
        """
        pass

    def test_datacenters_servers_volumes_post(self):
        """Test case for datacenters_servers_volumes_post

        Attach a volume  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
