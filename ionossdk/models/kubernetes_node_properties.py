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

from ionossdk.configuration import Configuration


class KubernetesNodeProperties(object):
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
        'public_ip': 'str',
        'k8s_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'public_ip': 'publicIP',
        'k8s_version': 'k8sVersion'
    }

    def __init__(self, name=None, public_ip=None, k8s_version=None, local_vars_configuration=None):  # noqa: E501
        """KubernetesNodeProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._public_ip = None
        self._k8s_version = None
        self.discriminator = None

        self.name = name
        self.public_ip = public_ip
        self.k8s_version = k8s_version

    @property
    def name(self):
        """Gets the name of this KubernetesNodeProperties.  # noqa: E501

        A Kubernetes Node Name.  # noqa: E501

        :return: The name of this KubernetesNodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KubernetesNodeProperties.

        A Kubernetes Node Name.  # noqa: E501

        :param name: The name of this KubernetesNodeProperties.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def public_ip(self):
        """Gets the public_ip of this KubernetesNodeProperties.  # noqa: E501

        A valid public IP.  # noqa: E501

        :return: The public_ip of this KubernetesNodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this KubernetesNodeProperties.

        A valid public IP.  # noqa: E501

        :param public_ip: The public_ip of this KubernetesNodeProperties.  # noqa: E501
        :type public_ip: str
        """
        if self.local_vars_configuration.client_side_validation and public_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `public_ip`, must not be `None`")  # noqa: E501

        self._public_ip = public_ip

    @property
    def k8s_version(self):
        """Gets the k8s_version of this KubernetesNodeProperties.  # noqa: E501

        The kubernetes version in which a nodepool is running. This imposes restrictions on what kubernetes versions can be run in a cluster's nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions.  # noqa: E501

        :return: The k8s_version of this KubernetesNodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._k8s_version

    @k8s_version.setter
    def k8s_version(self, k8s_version):
        """Sets the k8s_version of this KubernetesNodeProperties.

        The kubernetes version in which a nodepool is running. This imposes restrictions on what kubernetes versions can be run in a cluster's nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions.  # noqa: E501

        :param k8s_version: The k8s_version of this KubernetesNodeProperties.  # noqa: E501
        :type k8s_version: str
        """
        if self.local_vars_configuration.client_side_validation and k8s_version is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_version`, must not be `None`")  # noqa: E501

        self._k8s_version = k8s_version

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
        if not isinstance(other, KubernetesNodeProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubernetesNodeProperties):
            return True

        return self.to_dict() != other.to_dict()