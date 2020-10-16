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
from ionossdk.api.image_api import ImageApi  # noqa: E501
from ionossdk.rest import ApiException


class TestImageApi(unittest.TestCase):
    """ImageApi unit test stubs"""

    def setUp(self):
        self.api = ionossdk.api.image_api.ImageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_images_delete(self):
        """Test case for images_delete

        Delete an Image  # noqa: E501
        """
        pass

    def test_images_find_by_id(self):
        """Test case for images_find_by_id

        Retrieve an Image  # noqa: E501
        """
        pass

    def test_images_get(self):
        """Test case for images_get

        List Images   # noqa: E501
        """
        pass

    def test_images_patch(self):
        """Test case for images_patch

        Partially modify an Image  # noqa: E501
        """
        pass

    def test_images_put(self):
        """Test case for images_put

        Modify an Image  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
