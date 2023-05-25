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


class ApplicationLoadBalancerHttpRuleCondition(object):
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

        'condition': 'str',

        'key': 'str',

        'negate': 'bool',

        'type': 'str',

        'value': 'str',
    }

    attribute_map = {

        'condition': 'condition',

        'key': 'key',

        'negate': 'negate',

        'type': 'type',

        'value': 'value',
    }

    def __init__(self, condition=None, key=None, negate=None, type=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationLoadBalancerHttpRuleCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._condition = None
        self._key = None
        self._negate = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.condition = condition
        if key is not None:
            self.key = key
        if negate is not None:
            self.negate = negate
        self.type = type
        if value is not None:
            self.value = value


    @property
    def condition(self):
        """Gets the condition of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501

        The matching rule for the HTTP rule condition attribute; this parameter is mandatory for 'HEADER', 'PATH', 'QUERY', 'METHOD', 'HOST', and 'COOKIE' types. It must be 'null' if the type is 'SOURCE_IP'.  # noqa: E501

        :return: The condition of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ApplicationLoadBalancerHttpRuleCondition.

        The matching rule for the HTTP rule condition attribute; this parameter is mandatory for 'HEADER', 'PATH', 'QUERY', 'METHOD', 'HOST', and 'COOKIE' types. It must be 'null' if the type is 'SOURCE_IP'.  # noqa: E501

        :param condition: The condition of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501
        :type condition: str
        """
        if self.local_vars_configuration.client_side_validation and condition is None:  # noqa: E501
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501
        allowed_values = ["EXISTS", "CONTAINS", "EQUALS", "MATCHES", "STARTS_WITH", "ENDS_WITH"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and condition not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def key(self):
        """Gets the key of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501

        The key can only be set when the HTTP rule condition type is 'COOKIES', 'HEADER', or 'QUERY'. For the type 'PATH', 'METHOD', 'HOST', or 'SOURCE_IP' the value must be 'null'.  # noqa: E501

        :return: The key of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ApplicationLoadBalancerHttpRuleCondition.

        The key can only be set when the HTTP rule condition type is 'COOKIES', 'HEADER', or 'QUERY'. For the type 'PATH', 'METHOD', 'HOST', or 'SOURCE_IP' the value must be 'null'.  # noqa: E501

        :param key: The key of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501
        :type key: str
        """

        self._key = key

    @property
    def negate(self):
        """Gets the negate of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501

        Specifies whether the condition should be negated; the default value is 'FALSE'.  # noqa: E501

        :return: The negate of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501
        :rtype: bool
        """
        return self._negate

    @negate.setter
    def negate(self, negate):
        """Sets the negate of this ApplicationLoadBalancerHttpRuleCondition.

        Specifies whether the condition should be negated; the default value is 'FALSE'.  # noqa: E501

        :param negate: The negate of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501
        :type negate: bool
        """

        self._negate = negate

    @property
    def type(self):
        """Gets the type of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501

        The HTTP rule condition type.  # noqa: E501

        :return: The type of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApplicationLoadBalancerHttpRuleCondition.

        The HTTP rule condition type.  # noqa: E501

        :param type: The type of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["HEADER", "PATH", "QUERY", "METHOD", "HOST", "COOKIE", "SOURCE_IP"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501

        This parameter is mandatory for the conditions 'CONTAINS', 'EQUALS', 'MATCHES', 'STARTS_WITH', 'ENDS_WITH', or if the type is 'SOURCE_IP'. Specify a valid CIDR. If the condition is 'EXISTS', the value must be 'null'.  # noqa: E501

        :return: The value of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ApplicationLoadBalancerHttpRuleCondition.

        This parameter is mandatory for the conditions 'CONTAINS', 'EQUALS', 'MATCHES', 'STARTS_WITH', 'ENDS_WITH', or if the type is 'SOURCE_IP'. Specify a valid CIDR. If the condition is 'EXISTS', the value must be 'null'.  # noqa: E501

        :param value: The value of this ApplicationLoadBalancerHttpRuleCondition.  # noqa: E501
        :type value: str
        """

        self._value = value
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
        if not isinstance(other, ApplicationLoadBalancerHttpRuleCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationLoadBalancerHttpRuleCondition):
            return True

        return self.to_dict() != other.to_dict()
