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


class ApplicationLoadBalancerHttpRule(object):
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

        'name': 'str',

        'type': 'str',

        'target_group': 'str',

        'drop_query': 'bool',

        'location': 'str',

        'status_code': 'int',

        'response_message': 'str',

        'content_type': 'str',

        'conditions': 'list[ApplicationLoadBalancerHttpRuleCondition]',
    }

    attribute_map = {

        'name': 'name',

        'type': 'type',

        'target_group': 'targetGroup',

        'drop_query': 'dropQuery',

        'location': 'location',

        'status_code': 'statusCode',

        'response_message': 'responseMessage',

        'content_type': 'contentType',

        'conditions': 'conditions',
    }

    def __init__(self, name=None, type=None, target_group=None, drop_query=None, location=None, status_code=None, response_message=None, content_type=None, conditions=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationLoadBalancerHttpRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self._target_group = None
        self._drop_query = None
        self._location = None
        self._status_code = None
        self._response_message = None
        self._content_type = None
        self._conditions = None
        self.discriminator = None

        self.name = name
        self.type = type
        if target_group is not None:
            self.target_group = target_group
        if drop_query is not None:
            self.drop_query = drop_query
        if location is not None:
            self.location = location
        if status_code is not None:
            self.status_code = status_code
        if response_message is not None:
            self.response_message = response_message
        if content_type is not None:
            self.content_type = content_type
        if conditions is not None:
            self.conditions = conditions


    @property
    def name(self):
        """Gets the name of this ApplicationLoadBalancerHttpRule.  # noqa: E501

        The unique name of the Application Load Balancer HTTP rule.  # noqa: E501

        :return: The name of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationLoadBalancerHttpRule.

        The unique name of the Application Load Balancer HTTP rule.  # noqa: E501

        :param name: The name of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this ApplicationLoadBalancerHttpRule.  # noqa: E501

        Type of the HTTP rule.  # noqa: E501

        :return: The type of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApplicationLoadBalancerHttpRule.

        Type of the HTTP rule.  # noqa: E501

        :param type: The type of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["FORWARD", "STATIC", "REDIRECT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def target_group(self):
        """Gets the target_group of this ApplicationLoadBalancerHttpRule.  # noqa: E501

        The ID of the target group; mandatory and only valid for FORWARD actions.  # noqa: E501

        :return: The target_group of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :rtype: str
        """
        return self._target_group

    @target_group.setter
    def target_group(self, target_group):
        """Sets the target_group of this ApplicationLoadBalancerHttpRule.

        The ID of the target group; mandatory and only valid for FORWARD actions.  # noqa: E501

        :param target_group: The target_group of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :type target_group: str
        """

        self._target_group = target_group

    @property
    def drop_query(self):
        """Gets the drop_query of this ApplicationLoadBalancerHttpRule.  # noqa: E501

        Default is false; valid only for REDIRECT actions.  # noqa: E501

        :return: The drop_query of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :rtype: bool
        """
        return self._drop_query

    @drop_query.setter
    def drop_query(self, drop_query):
        """Sets the drop_query of this ApplicationLoadBalancerHttpRule.

        Default is false; valid only for REDIRECT actions.  # noqa: E501

        :param drop_query: The drop_query of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :type drop_query: bool
        """

        self._drop_query = drop_query

    @property
    def location(self):
        """Gets the location of this ApplicationLoadBalancerHttpRule.  # noqa: E501

        The location for redirecting; mandatory and valid only for REDIRECT actions.  # noqa: E501

        :return: The location of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ApplicationLoadBalancerHttpRule.

        The location for redirecting; mandatory and valid only for REDIRECT actions.  # noqa: E501

        :param location: The location of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :type location: str
        """

        self._location = location

    @property
    def status_code(self):
        """Gets the status_code of this ApplicationLoadBalancerHttpRule.  # noqa: E501

        Valid only for REDIRECT and STATIC actions. For REDIRECT actions, default is 301 and possible values are 301, 302, 303, 307, and 308. For STATIC actions, default is 503 and valid range is 200 to 599.  # noqa: E501

        :return: The status_code of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ApplicationLoadBalancerHttpRule.

        Valid only for REDIRECT and STATIC actions. For REDIRECT actions, default is 301 and possible values are 301, 302, 303, 307, and 308. For STATIC actions, default is 503 and valid range is 200 to 599.  # noqa: E501

        :param status_code: The status_code of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :type status_code: int
        """
        allowed_values = [301, 302, 303, 307, 308, 200, 503, 599]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status_code` ({0}), must be one of {1}"  # noqa: E501
                .format(status_code, allowed_values)
            )

        self._status_code = status_code

    @property
    def response_message(self):
        """Gets the response_message of this ApplicationLoadBalancerHttpRule.  # noqa: E501

        The response message of the request; mandatory for STATIC actions.  # noqa: E501

        :return: The response_message of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :rtype: str
        """
        return self._response_message

    @response_message.setter
    def response_message(self, response_message):
        """Sets the response_message of this ApplicationLoadBalancerHttpRule.

        The response message of the request; mandatory for STATIC actions.  # noqa: E501

        :param response_message: The response_message of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :type response_message: str
        """

        self._response_message = response_message

    @property
    def content_type(self):
        """Gets the content_type of this ApplicationLoadBalancerHttpRule.  # noqa: E501

        Valid only for STATIC actions.  # noqa: E501

        :return: The content_type of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ApplicationLoadBalancerHttpRule.

        Valid only for STATIC actions.  # noqa: E501

        :param content_type: The content_type of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :type content_type: str
        """

        self._content_type = content_type

    @property
    def conditions(self):
        """Gets the conditions of this ApplicationLoadBalancerHttpRule.  # noqa: E501

        An array of items in the collection.The action is only performed if each and every condition is met; if no conditions are set, the rule will always be performed.  # noqa: E501

        :return: The conditions of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :rtype: list[ApplicationLoadBalancerHttpRuleCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ApplicationLoadBalancerHttpRule.

        An array of items in the collection.The action is only performed if each and every condition is met; if no conditions are set, the rule will always be performed.  # noqa: E501

        :param conditions: The conditions of this ApplicationLoadBalancerHttpRule.  # noqa: E501
        :type conditions: list[ApplicationLoadBalancerHttpRuleCondition]
        """

        self._conditions = conditions
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
        if not isinstance(other, ApplicationLoadBalancerHttpRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationLoadBalancerHttpRule):
            return True

        return self.to_dict() != other.to_dict()