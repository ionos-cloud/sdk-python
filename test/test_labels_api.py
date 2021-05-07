# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ionoscloud
from ionoscloud.api.labels_api import LabelsApi  # noqa: E501
from ionoscloud.rest import ApiException


class TestLabelsApi(unittest.TestCase):
    """LabelsApi unit test stubs"""

    def setUp(self):
        self.api = ionoscloud.api.labels_api.LabelsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_datacenters_labels_delete(self):
        """Test case for datacenters_labels_delete

        Delete a Label from Data Center  # noqa: E501
        """
        pass

    def test_datacenters_labels_find_by_key(self):
        """Test case for datacenters_labels_find_by_key

        Retrieve a Label of Data Center  # noqa: E501
        """
        pass

    def test_datacenters_labels_get(self):
        """Test case for datacenters_labels_get

        List all Data Center Labels  # noqa: E501
        """
        pass

    def test_datacenters_labels_post(self):
        """Test case for datacenters_labels_post

        Add a Label to Data Center  # noqa: E501
        """
        pass

    def test_datacenters_labels_put(self):
        """Test case for datacenters_labels_put

        Modify a Label of Data Center  # noqa: E501
        """
        pass

    def test_datacenters_servers_labels_delete(self):
        """Test case for datacenters_servers_labels_delete

        Delete a Label from Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_labels_find_by_key(self):
        """Test case for datacenters_servers_labels_find_by_key

        Retrieve a Label of Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_labels_get(self):
        """Test case for datacenters_servers_labels_get

        List all Server Labels  # noqa: E501
        """
        pass

    def test_datacenters_servers_labels_post(self):
        """Test case for datacenters_servers_labels_post

        Add a Label to Server  # noqa: E501
        """
        pass

    def test_datacenters_servers_labels_put(self):
        """Test case for datacenters_servers_labels_put

        Modify a Label of Server  # noqa: E501
        """
        pass

    def test_datacenters_volumes_labels_delete(self):
        """Test case for datacenters_volumes_labels_delete

        Delete a Label from Volume  # noqa: E501
        """
        pass

    def test_datacenters_volumes_labels_find_by_key(self):
        """Test case for datacenters_volumes_labels_find_by_key

        Retrieve a Label of Volume  # noqa: E501
        """
        pass

    def test_datacenters_volumes_labels_get(self):
        """Test case for datacenters_volumes_labels_get

        List all Volume Labels  # noqa: E501
        """
        pass

    def test_datacenters_volumes_labels_post(self):
        """Test case for datacenters_volumes_labels_post

        Add a Label to Volume  # noqa: E501
        """
        pass

    def test_datacenters_volumes_labels_put(self):
        """Test case for datacenters_volumes_labels_put

        Modify a Label of Volume  # noqa: E501
        """
        pass

    def test_ipblocks_labels_delete(self):
        """Test case for ipblocks_labels_delete

        Delete a Label from IP Block  # noqa: E501
        """
        pass

    def test_ipblocks_labels_find_by_key(self):
        """Test case for ipblocks_labels_find_by_key

        Retrieve a Label of IP Block  # noqa: E501
        """
        pass

    def test_ipblocks_labels_get(self):
        """Test case for ipblocks_labels_get

        List all Ip Block Labels  # noqa: E501
        """
        pass

    def test_ipblocks_labels_post(self):
        """Test case for ipblocks_labels_post

        Add a Label to IP Block  # noqa: E501
        """
        pass

    def test_ipblocks_labels_put(self):
        """Test case for ipblocks_labels_put

        Modify a Label of IP Block  # noqa: E501
        """
        pass

    def test_labels_find_by_urn(self):
        """Test case for labels_find_by_urn

        Returns the label by its URN.  # noqa: E501
        """
        pass

    def test_labels_get(self):
        """Test case for labels_get

        List Labels   # noqa: E501
        """
        pass

    def test_snapshots_labels_delete(self):
        """Test case for snapshots_labels_delete

        Delete a Label from Snapshot  # noqa: E501
        """
        pass

    def test_snapshots_labels_find_by_key(self):
        """Test case for snapshots_labels_find_by_key

        Retrieve a Label of Snapshot  # noqa: E501
        """
        pass

    def test_snapshots_labels_get(self):
        """Test case for snapshots_labels_get

        List all Snapshot Labels  # noqa: E501
        """
        pass

    def test_snapshots_labels_post(self):
        """Test case for snapshots_labels_post

        Add a Label to Snapshot  # noqa: E501
        """
        pass

    def test_snapshots_labels_put(self):
        """Test case for snapshots_labels_put

        Modify a Label of Snapshot  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()