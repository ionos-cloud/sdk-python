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


class TargetPortRange(object):
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

        'start': 'int',

        'end': 'int',
    }

    attribute_map = {

        'start': 'start',

        'end': 'end',
    }

    def __init__(self, start=None, end=None, local_vars_configuration=None):  # noqa: E501
        """TargetPortRange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start = None
        self._end = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if end is not None:
            self.end = end


    @property
    def start(self):
        """Gets the start of this TargetPortRange.  # noqa: E501

        Target port range start associated with the NAT Gateway rule.  # noqa: E501

        :return: The start of this TargetPortRange.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TargetPortRange.

        Target port range start associated with the NAT Gateway rule.  # noqa: E501

        :param start: The start of this TargetPortRange.  # noqa: E501
        :type start: int
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this TargetPortRange.  # noqa: E501

        Target port range end associated with the NAT Gateway rule.  # noqa: E501

        :return: The end of this TargetPortRange.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this TargetPortRange.

        Target port range end associated with the NAT Gateway rule.  # noqa: E501

        :param end: The end of this TargetPortRange.  # noqa: E501
        :type end: int
        """

        self._end = end
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
        if not isinstance(other, TargetPortRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetPortRange):
            return True

        return self.to_dict() != other.to_dict()
