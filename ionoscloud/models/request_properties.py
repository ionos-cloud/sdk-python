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


class RequestProperties(object):
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

        'method': 'str',

        'headers': 'dict(str, str)',

        'body': 'str',

        'url': 'str',
    }

    attribute_map = {

        'method': 'method',

        'headers': 'headers',

        'body': 'body',

        'url': 'url',
    }

    def __init__(self, method=None, headers=None, body=None, url=None, local_vars_configuration=None):  # noqa: E501
        """RequestProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._method = None
        self._headers = None
        self._body = None
        self._url = None
        self.discriminator = None

        if method is not None:
            self.method = method
        if headers is not None:
            self.headers = headers
        if body is not None:
            self.body = body
        if url is not None:
            self.url = url


    @property
    def method(self):
        """Gets the method of this RequestProperties.  # noqa: E501


        :return: The method of this RequestProperties.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this RequestProperties.


        :param method: The method of this RequestProperties.  # noqa: E501
        :type method: str
        """

        self._method = method

    @property
    def headers(self):
        """Gets the headers of this RequestProperties.  # noqa: E501


        :return: The headers of this RequestProperties.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this RequestProperties.


        :param headers: The headers of this RequestProperties.  # noqa: E501
        :type headers: dict(str, str)
        """

        self._headers = headers

    @property
    def body(self):
        """Gets the body of this RequestProperties.  # noqa: E501


        :return: The body of this RequestProperties.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this RequestProperties.


        :param body: The body of this RequestProperties.  # noqa: E501
        :type body: str
        """

        self._body = body

    @property
    def url(self):
        """Gets the url of this RequestProperties.  # noqa: E501


        :return: The url of this RequestProperties.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RequestProperties.


        :param url: The url of this RequestProperties.  # noqa: E501
        :type url: str
        """

        self._url = url
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
        if not isinstance(other, RequestProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestProperties):
            return True

        return self.to_dict() != other.to_dict()
