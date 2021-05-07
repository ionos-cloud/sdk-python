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
from ionoscloud.api.backup_units_api import BackupUnitsApi  # noqa: E501
from ionoscloud.rest import ApiException


class TestBackupUnitsApi(unittest.TestCase):
    """BackupUnitsApi unit test stubs"""

    def setUp(self):
        self.api = ionoscloud.api.backup_units_api.BackupUnitsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_backupunits_delete(self):
        """Test case for backupunits_delete

        Delete a Backup Unit  # noqa: E501
        """
        pass

    def test_backupunits_find_by_id(self):
        """Test case for backupunits_find_by_id

        Returns the specified Backup Unit  # noqa: E501
        """
        pass

    def test_backupunits_get(self):
        """Test case for backupunits_get

        List Backup Units  # noqa: E501
        """
        pass

    def test_backupunits_patch(self):
        """Test case for backupunits_patch

        Partially modify a Backup Unit  # noqa: E501
        """
        pass

    def test_backupunits_post(self):
        """Test case for backupunits_post

        Create a Backup Unit  # noqa: E501
        """
        pass

    def test_backupunits_put(self):
        """Test case for backupunits_put

        Modify a Backup Unit  # noqa: E501
        """
        pass

    def test_backupunits_ssourl_get(self):
        """Test case for backupunits_ssourl_get

        Returns a single signon URL for the specified Backup Unit  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
