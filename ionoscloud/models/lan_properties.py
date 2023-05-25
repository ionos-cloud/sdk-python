# coding: utf-8

"""
    CLOUD API

    IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.  # noqa: E501

    The version of the OpenAPI document: 6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class LanProperties(object):
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

        'ip_failover': 'list[IPFailover]',

        'name': 'str',

        'pcc': 'str',

        'public': 'bool',
    }

    attribute_map = {

        'ip_failover': 'ipFailover',

        'name': 'name',

        'pcc': 'pcc',

        'public': 'public',
    }

    def __init__(self, ip_failover=None, name=None, pcc=None, public=None, local_vars_configuration=None):  # noqa: E501
        """LanProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ip_failover = None
        self._name = None
        self._pcc = None
        self._public = None
        self.discriminator = None

        if ip_failover is not None:
            self.ip_failover = ip_failover
        if name is not None:
            self.name = name
        if pcc is not None:
            self.pcc = pcc
        if public is not None:
            self.public = public


    @property
    def ip_failover(self):
        """Gets the ip_failover of this LanProperties.  # noqa: E501

        IP failover configurations for lan  # noqa: E501

        :return: The ip_failover of this LanProperties.  # noqa: E501
        :rtype: list[IPFailover]
        """
        return self._ip_failover

    @ip_failover.setter
    def ip_failover(self, ip_failover):
        """Sets the ip_failover of this LanProperties.

        IP failover configurations for lan  # noqa: E501

        :param ip_failover: The ip_failover of this LanProperties.  # noqa: E501
        :type ip_failover: list[IPFailover]
        """

        self._ip_failover = ip_failover

    @property
    def name(self):
        """Gets the name of this LanProperties.  # noqa: E501

        The name of the  resource.  # noqa: E501

        :return: The name of this LanProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LanProperties.

        The name of the  resource.  # noqa: E501

        :param name: The name of this LanProperties.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def pcc(self):
        """Gets the pcc of this LanProperties.  # noqa: E501

        The unique identifier of the private Cross-Connect the LAN is connected to, if any.  # noqa: E501

        :return: The pcc of this LanProperties.  # noqa: E501
        :rtype: str
        """
        return self._pcc

    @pcc.setter
    def pcc(self, pcc):
        """Sets the pcc of this LanProperties.

        The unique identifier of the private Cross-Connect the LAN is connected to, if any.  # noqa: E501

        :param pcc: The pcc of this LanProperties.  # noqa: E501
        :type pcc: str
        """

        self._pcc = pcc

    @property
    def public(self):
        """Gets the public of this LanProperties.  # noqa: E501

        This LAN faces the public Internet.  # noqa: E501

        :return: The public of this LanProperties.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this LanProperties.

        This LAN faces the public Internet.  # noqa: E501

        :param public: The public of this LanProperties.  # noqa: E501
        :type public: bool
        """

        self._public = public
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
        if not isinstance(other, LanProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LanProperties):
            return True

        return self.to_dict() != other.to_dict()
