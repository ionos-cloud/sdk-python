# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class S3KeyProperties(object):
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

        'secret_key': 'str',

        'active': 'bool',
    }

    attribute_map = {

        'secret_key': 'secretKey',

        'active': 'active',
    }

    def __init__(self, secret_key=None, active=None, local_vars_configuration=None):  # noqa: E501
        """S3KeyProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._secret_key = None
        self._active = None
        self.discriminator = None

        if secret_key is not None:
            self.secret_key = secret_key
        if active is not None:
            self.active = active


    @property
    def secret_key(self):
        """Gets the secret_key of this S3KeyProperties.  # noqa: E501

        secret of the S3 key  # noqa: E501

        :return: The secret_key of this S3KeyProperties.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this S3KeyProperties.

        secret of the S3 key  # noqa: E501

        :param secret_key: The secret_key of this S3KeyProperties.  # noqa: E501
        :type secret_key: str
        """

        self._secret_key = secret_key

    @property
    def active(self):
        """Gets the active of this S3KeyProperties.  # noqa: E501

        denotes if the S3 key is active or not  # noqa: E501

        :return: The active of this S3KeyProperties.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this S3KeyProperties.

        denotes if the S3 key is active or not  # noqa: E501

        :param active: The active of this S3KeyProperties.  # noqa: E501
        :type active: bool
        """

        self._active = active
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
        if not isinstance(other, S3KeyProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, S3KeyProperties):
            return True

        return self.to_dict() != other.to_dict()
