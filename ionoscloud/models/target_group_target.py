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


class TargetGroupTarget(object):
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

        'health_check_enabled': 'bool',

        'ip': 'str',

        'maintenance_enabled': 'bool',

        'port': 'int',

        'weight': 'int',
    }

    attribute_map = {

        'health_check_enabled': 'healthCheckEnabled',

        'ip': 'ip',

        'maintenance_enabled': 'maintenanceEnabled',

        'port': 'port',

        'weight': 'weight',
    }

    def __init__(self, health_check_enabled=None, ip=None, maintenance_enabled=None, port=None, weight=None, local_vars_configuration=None):  # noqa: E501
        """TargetGroupTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._health_check_enabled = None
        self._ip = None
        self._maintenance_enabled = None
        self._port = None
        self._weight = None
        self.discriminator = None

        if health_check_enabled is not None:
            self.health_check_enabled = health_check_enabled
        self.ip = ip
        if maintenance_enabled is not None:
            self.maintenance_enabled = maintenance_enabled
        self.port = port
        self.weight = weight


    @property
    def health_check_enabled(self):
        """Gets the health_check_enabled of this TargetGroupTarget.  # noqa: E501

        When the health check is enabled, the target is available only when it accepts regular TCP or HTTP connection attempts for state checking. The state check consists of one connection attempt with the target's address and port. The default value is 'TRUE'.  # noqa: E501

        :return: The health_check_enabled of this TargetGroupTarget.  # noqa: E501
        :rtype: bool
        """
        return self._health_check_enabled

    @health_check_enabled.setter
    def health_check_enabled(self, health_check_enabled):
        """Sets the health_check_enabled of this TargetGroupTarget.

        When the health check is enabled, the target is available only when it accepts regular TCP or HTTP connection attempts for state checking. The state check consists of one connection attempt with the target's address and port. The default value is 'TRUE'.  # noqa: E501

        :param health_check_enabled: The health_check_enabled of this TargetGroupTarget.  # noqa: E501
        :type health_check_enabled: bool
        """

        self._health_check_enabled = health_check_enabled

    @property
    def ip(self):
        """Gets the ip of this TargetGroupTarget.  # noqa: E501

        The IP address of the balanced target.  # noqa: E501

        :return: The ip of this TargetGroupTarget.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this TargetGroupTarget.

        The IP address of the balanced target.  # noqa: E501

        :param ip: The ip of this TargetGroupTarget.  # noqa: E501
        :type ip: str
        """
        if self.local_vars_configuration.client_side_validation and ip is None:  # noqa: E501
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def maintenance_enabled(self):
        """Gets the maintenance_enabled of this TargetGroupTarget.  # noqa: E501

        When the maintenance mode is enabled, the target is prevented from receiving traffic; the default value is 'FALSE'.  # noqa: E501

        :return: The maintenance_enabled of this TargetGroupTarget.  # noqa: E501
        :rtype: bool
        """
        return self._maintenance_enabled

    @maintenance_enabled.setter
    def maintenance_enabled(self, maintenance_enabled):
        """Sets the maintenance_enabled of this TargetGroupTarget.

        When the maintenance mode is enabled, the target is prevented from receiving traffic; the default value is 'FALSE'.  # noqa: E501

        :param maintenance_enabled: The maintenance_enabled of this TargetGroupTarget.  # noqa: E501
        :type maintenance_enabled: bool
        """

        self._maintenance_enabled = maintenance_enabled

    @property
    def port(self):
        """Gets the port of this TargetGroupTarget.  # noqa: E501

        The port of the balanced target service; the valid range is 1 to 65535.  # noqa: E501

        :return: The port of this TargetGroupTarget.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TargetGroupTarget.

        The port of the balanced target service; the valid range is 1 to 65535.  # noqa: E501

        :param port: The port of this TargetGroupTarget.  # noqa: E501
        :type port: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def weight(self):
        """Gets the weight of this TargetGroupTarget.  # noqa: E501

        The traffic is distributed proportionally to target weight, which is the ratio of the total weight of all targets. A target with higher weight receives a larger share of traffic. The valid range is from 0 to 256; the default value is '1'. Targets with a weight of '0' do not participate in load balancing but still accept persistent connections. We recommend using values in the middle range to leave room for later adjustments.  # noqa: E501

        :return: The weight of this TargetGroupTarget.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this TargetGroupTarget.

        The traffic is distributed proportionally to target weight, which is the ratio of the total weight of all targets. A target with higher weight receives a larger share of traffic. The valid range is from 0 to 256; the default value is '1'. Targets with a weight of '0' do not participate in load balancing but still accept persistent connections. We recommend using values in the middle range to leave room for later adjustments.  # noqa: E501

        :param weight: The weight of this TargetGroupTarget.  # noqa: E501
        :type weight: int
        """
        if self.local_vars_configuration.client_side_validation and weight is None:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight
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
        if not isinstance(other, TargetGroupTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetGroupTarget):
            return True

        return self.to_dict() != other.to_dict()