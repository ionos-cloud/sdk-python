# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ionoscloud
from ionoscloud.api.volume_api import VolumeApi  # noqa: E501
from ionoscloud.rest import ApiException


class TestVolumeApi(unittest.TestCase):
    """VolumeApi unit test stubs"""

    def setUp(self):
        self.api = ionoscloud.api.volume_api.VolumeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_datacenters_volumes_create_snapshot_post(self):
        """Test case for datacenters_volumes_create_snapshot_post

        Create Volume Snapshot  # noqa: E501
        """
        pass

    def test_datacenters_volumes_delete(self):
        """Test case for datacenters_volumes_delete

        Delete a Volume  # noqa: E501
        """
        pass

    def test_datacenters_volumes_find_by_id(self):
        """Test case for datacenters_volumes_find_by_id

        Retrieve a Volume  # noqa: E501
        """
        pass

    def test_datacenters_volumes_get(self):
        """Test case for datacenters_volumes_get

        List Volumes   # noqa: E501
        """
        pass

    def test_datacenters_volumes_patch(self):
        """Test case for datacenters_volumes_patch

        Partially modify a Volume  # noqa: E501
        """
        pass

    def test_datacenters_volumes_post(self):
        """Test case for datacenters_volumes_post

        Create a Volume  # noqa: E501
        """
        pass

    def test_datacenters_volumes_put(self):
        """Test case for datacenters_volumes_put

        Modify a Volume  # noqa: E501
        """
        pass

    def test_datacenters_volumes_restore_snapshot_post(self):
        """Test case for datacenters_volumes_restore_snapshot_post

        Restore Volume Snapshot  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
