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


class Contract(object):
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

        'properties': 'ContractProperties',

        'type': 'Type',
    }

    attribute_map = {

        'properties': 'properties',

        'type': 'type',
    }

    def __init__(self, properties=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Contract - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._properties = None
        self._type = None
        self.discriminator = None

        self.properties = properties
        if type is not None:
            self.type = type


    @property
    def properties(self):
        """Gets the properties of this Contract.  # noqa: E501


        :return: The properties of this Contract.  # noqa: E501
        :rtype: ContractProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Contract.


        :param properties: The properties of this Contract.  # noqa: E501
        :type properties: ContractProperties
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this Contract.  # noqa: E501

        The type of the resource.  # noqa: E501

        :return: The type of this Contract.  # noqa: E501
        :rtype: Type
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Contract.

        The type of the resource.  # noqa: E501

        :param type: The type of this Contract.  # noqa: E501
        :type type: Type
        """

        self._type = type
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
        if not isinstance(other, Contract):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Contract):
            return True

        return self.to_dict() != other.to_dict()
