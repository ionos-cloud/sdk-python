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
from ionossdk.models.volume import Volume  # noqa: E501
from ionossdk.rest import ApiException

class TestVolume(unittest.TestCase):
    """Volume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Volume
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionossdk.models.volume.Volume()  # noqa: E501
        if include_optional :
            return Volume(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                type = "volume", 
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
                properties = ionossdk.models.volume_properties.VolumeProperties(
                    name = 'My resource', 
                    type = 'HDD', 
                    size = 100.0, 
                    availability_zone = 'AUTO', 
                    image = 'd6ad1576-fde9-4696-aa41-1ebd75bdaf49', 
                    image_alias = '0', 
                    image_password = 'mypass123', 
                    ssh_keys = [ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyWh6LZ7f2wxnupVgtK2096bc69Vv9uT2A58lwN3ol0A6mxqlT0f4M1NbarVUxa+MVdxBLud5PvlkbYc9mY91OyzLGZMfVWvhAYz/tJSsDtsgRUl0GFVv332zDWk0i+mAVy0N408OORm5XqV6zvIDaiB/jopyjemUp2rnP7pXU4+98ilZw6ef9DF9y4YZ64mchL5//rcrGm1Lff3pC75X/polGONHeG6m4Vs8eIu+0epJ4PJBxO+rwRYp1zMnn90UCk21KvTcYops2cte7ouXQwkGUq3vmXxnSdvuivK/4JNoFQBsaGV974hDmloS5LOvSJjKpXs8Ed437ln712345, ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyWh6LZ7f2wxnupVgtK2096bc69Vv9uT2A58lwN3ol0A6mxqlT0f4M1NbarVUxa+MVdxBLud5PvlkbYc9mY91OyzLGZMfVWvhAYz/tJSsDtsgRUl0GFVv332zDWk0i+mAVy0N408OORm5XqV6zvIDaiB/jopyjemUp2rnP7pXU4+98ilZw6ef9DF9y4YZ64mchL5//rcrGm1Lff3pC75X/polGONHeG6m4Vs8eIu+0epJ4PJBxO+rwRYp1zMnn90UCk21KvTcYops2cte7ouXQwkGUq3vmXxnSdvuivK/asdfghjkjhyutry545tgvbn76e4rf43], 
                    bus = 'VIRTIO', 
                    licence_type = 'LINUX', 
                    cpu_hot_plug = True, 
                    ram_hot_plug = True, 
                    nic_hot_plug = True, 
                    nic_hot_unplug = True, 
                    disc_virtio_hot_plug = True, 
                    disc_virtio_hot_unplug = True, 
                    device_number = 3, 
                    backupunit_id = '25f67991-0f51-4efc-a8ad-ef1fb31a481c', )
            )
        else :
            return Volume(
                properties = ionossdk.models.volume_properties.VolumeProperties(
                    name = 'My resource', 
                    type = 'HDD', 
                    size = 100.0, 
                    availability_zone = 'AUTO', 
                    image = 'd6ad1576-fde9-4696-aa41-1ebd75bdaf49', 
                    image_alias = '0', 
                    image_password = 'mypass123', 
                    ssh_keys = [ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyWh6LZ7f2wxnupVgtK2096bc69Vv9uT2A58lwN3ol0A6mxqlT0f4M1NbarVUxa+MVdxBLud5PvlkbYc9mY91OyzLGZMfVWvhAYz/tJSsDtsgRUl0GFVv332zDWk0i+mAVy0N408OORm5XqV6zvIDaiB/jopyjemUp2rnP7pXU4+98ilZw6ef9DF9y4YZ64mchL5//rcrGm1Lff3pC75X/polGONHeG6m4Vs8eIu+0epJ4PJBxO+rwRYp1zMnn90UCk21KvTcYops2cte7ouXQwkGUq3vmXxnSdvuivK/4JNoFQBsaGV974hDmloS5LOvSJjKpXs8Ed437ln712345, ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyWh6LZ7f2wxnupVgtK2096bc69Vv9uT2A58lwN3ol0A6mxqlT0f4M1NbarVUxa+MVdxBLud5PvlkbYc9mY91OyzLGZMfVWvhAYz/tJSsDtsgRUl0GFVv332zDWk0i+mAVy0N408OORm5XqV6zvIDaiB/jopyjemUp2rnP7pXU4+98ilZw6ef9DF9y4YZ64mchL5//rcrGm1Lff3pC75X/polGONHeG6m4Vs8eIu+0epJ4PJBxO+rwRYp1zMnn90UCk21KvTcYops2cte7ouXQwkGUq3vmXxnSdvuivK/asdfghjkjhyutry545tgvbn76e4rf43], 
                    bus = 'VIRTIO', 
                    licence_type = 'LINUX', 
                    cpu_hot_plug = True, 
                    ram_hot_plug = True, 
                    nic_hot_plug = True, 
                    nic_hot_unplug = True, 
                    disc_virtio_hot_plug = True, 
                    disc_virtio_hot_unplug = True, 
                    device_number = 3, 
                    backupunit_id = '25f67991-0f51-4efc-a8ad-ef1fb31a481c', ),
        )

    def testVolume(self):
        """Test Volume"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
