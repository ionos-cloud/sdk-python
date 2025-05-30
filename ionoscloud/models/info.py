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


class Info(object):
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

        'href': 'str',

        'name': 'str',

        'version': 'str',
    }

    attribute_map = {

        'href': 'href',

        'name': 'name',

        'version': 'version',
    }

    def __init__(self, href=None, name=None, version=None, local_vars_configuration=None):  # noqa: E501
        """Info - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._name = None
        self._version = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version


    @property
    def href(self):
        """Gets the href of this Info.  # noqa: E501

        The API entry point.  # noqa: E501

        :return: The href of this Info.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Info.

        The API entry point.  # noqa: E501

        :param href: The href of this Info.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this Info.  # noqa: E501

        The API name.  # noqa: E501

        :return: The name of this Info.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Info.

        The API name.  # noqa: E501

        :param name: The name of this Info.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this Info.  # noqa: E501

        The API version.  # noqa: E501

        :return: The version of this Info.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Info.

        The API version.  # noqa: E501

        :param version: The version of this Info.  # noqa: E501
        :type version: str
        """

        self._version = version
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
        if not isinstance(other, Info):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Info):
            return True

        return self.to_dict() != other.to_dict()
