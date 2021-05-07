# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class NatGatewayLanProperties(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'gateway_ips': 'list[str]',
    }

    attribute_map = {
        'id': 'id',
        'gateway_ips': 'gatewayIps',
    }

    def __init__(self, id=None, gateway_ips=None, local_vars_configuration=None):  # noqa: E501
        """NatGatewayLanProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._gateway_ips = None
        self.discriminator = None

        self.id = id
        if gateway_ips is not None:
            self.gateway_ips = gateway_ips

    @property
    def id(self):
        """Gets the id of this NatGatewayLanProperties.  # noqa: E501

        Id for the LAN connected to the NAT gateway  # noqa: E501

        :return: The id of this NatGatewayLanProperties.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NatGatewayLanProperties.

        Id for the LAN connected to the NAT gateway  # noqa: E501

        :param id: The id of this NatGatewayLanProperties.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def gateway_ips(self):
        """Gets the gateway_ips of this NatGatewayLanProperties.  # noqa: E501

        Collection of gateway IP addresses of the NAT gateway. Will be auto-generated if not provided. Should ideally be an IP belonging to the same subnet as the LAN  # noqa: E501

        :return: The gateway_ips of this NatGatewayLanProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._gateway_ips

    @gateway_ips.setter
    def gateway_ips(self, gateway_ips):
        """Sets the gateway_ips of this NatGatewayLanProperties.

        Collection of gateway IP addresses of the NAT gateway. Will be auto-generated if not provided. Should ideally be an IP belonging to the same subnet as the LAN  # noqa: E501

        :param gateway_ips: The gateway_ips of this NatGatewayLanProperties.  # noqa: E501
        :type gateway_ips: list[str]
        """

        self._gateway_ips = gateway_ips

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NatGatewayLanProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NatGatewayLanProperties):
            return True

        return self.to_dict() != other.to_dict()
