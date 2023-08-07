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


class TargetGroupProperties(object):
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

        'algorithm': 'str',

        'health_check': 'TargetGroupHealthCheck',

        'http_health_check': 'TargetGroupHttpHealthCheck',

        'name': 'str',

        'protocol': 'str',

        'targets': 'list[TargetGroupTarget]',
    }

    attribute_map = {

        'algorithm': 'algorithm',

        'health_check': 'healthCheck',

        'http_health_check': 'httpHealthCheck',

        'name': 'name',

        'protocol': 'protocol',

        'targets': 'targets',
    }

    def __init__(self, algorithm=None, health_check=None, http_health_check=None, name=None, protocol=None, targets=None, local_vars_configuration=None):  # noqa: E501
        """TargetGroupProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._algorithm = None
        self._health_check = None
        self._http_health_check = None
        self._name = None
        self._protocol = None
        self._targets = None
        self.discriminator = None

        self.algorithm = algorithm
        if health_check is not None:
            self.health_check = health_check
        if http_health_check is not None:
            self.http_health_check = http_health_check
        self.name = name
        self.protocol = protocol
        if targets is not None:
            self.targets = targets


    @property
    def algorithm(self):
        """Gets the algorithm of this TargetGroupProperties.  # noqa: E501

        The balancing algorithm. A balancing algorithm consists of predefined rules with the logic that a load balancer uses to distribute network traffic between servers.  - **Round Robin**: Targets are served alternately according to their weighting.  - **Least Connection**: The target with the least active connection is served.  - **Random**: The targets are served based on a consistent pseudorandom algorithm.  - **Source IP**: It is ensured that the same client IP address reaches the same target.  # noqa: E501

        :return: The algorithm of this TargetGroupProperties.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this TargetGroupProperties.

        The balancing algorithm. A balancing algorithm consists of predefined rules with the logic that a load balancer uses to distribute network traffic between servers.  - **Round Robin**: Targets are served alternately according to their weighting.  - **Least Connection**: The target with the least active connection is served.  - **Random**: The targets are served based on a consistent pseudorandom algorithm.  - **Source IP**: It is ensured that the same client IP address reaches the same target.  # noqa: E501

        :param algorithm: The algorithm of this TargetGroupProperties.  # noqa: E501
        :type algorithm: str
        """
        if self.local_vars_configuration.client_side_validation and algorithm is None:  # noqa: E501
            raise ValueError("Invalid value for `algorithm`, must not be `None`")  # noqa: E501
        allowed_values = ["ROUND_ROBIN", "LEAST_CONNECTION", "RANDOM", "SOURCE_IP"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and algorithm not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(algorithm, allowed_values)
            )

        self._algorithm = algorithm

    @property
    def health_check(self):
        """Gets the health_check of this TargetGroupProperties.  # noqa: E501


        :return: The health_check of this TargetGroupProperties.  # noqa: E501
        :rtype: TargetGroupHealthCheck
        """
        return self._health_check

    @health_check.setter
    def health_check(self, health_check):
        """Sets the health_check of this TargetGroupProperties.


        :param health_check: The health_check of this TargetGroupProperties.  # noqa: E501
        :type health_check: TargetGroupHealthCheck
        """

        self._health_check = health_check

    @property
    def http_health_check(self):
        """Gets the http_health_check of this TargetGroupProperties.  # noqa: E501


        :return: The http_health_check of this TargetGroupProperties.  # noqa: E501
        :rtype: TargetGroupHttpHealthCheck
        """
        return self._http_health_check

    @http_health_check.setter
    def http_health_check(self, http_health_check):
        """Sets the http_health_check of this TargetGroupProperties.


        :param http_health_check: The http_health_check of this TargetGroupProperties.  # noqa: E501
        :type http_health_check: TargetGroupHttpHealthCheck
        """

        self._http_health_check = http_health_check

    @property
    def name(self):
        """Gets the name of this TargetGroupProperties.  # noqa: E501

        The target group name.  # noqa: E501

        :return: The name of this TargetGroupProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetGroupProperties.

        The target group name.  # noqa: E501

        :param name: The name of this TargetGroupProperties.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this TargetGroupProperties.  # noqa: E501

        The forwarding protocol. Only the value 'HTTP' is allowed.  # noqa: E501

        :return: The protocol of this TargetGroupProperties.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this TargetGroupProperties.

        The forwarding protocol. Only the value 'HTTP' is allowed.  # noqa: E501

        :param protocol: The protocol of this TargetGroupProperties.  # noqa: E501
        :type protocol: str
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["HTTP"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and protocol not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def targets(self):
        """Gets the targets of this TargetGroupProperties.  # noqa: E501

        Array of items in the collection.  # noqa: E501

        :return: The targets of this TargetGroupProperties.  # noqa: E501
        :rtype: list[TargetGroupTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this TargetGroupProperties.

        Array of items in the collection.  # noqa: E501

        :param targets: The targets of this TargetGroupProperties.  # noqa: E501
        :type targets: list[TargetGroupTarget]
        """

        self._targets = targets
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
        if not isinstance(other, TargetGroupProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetGroupProperties):
            return True

        return self.to_dict() != other.to_dict()