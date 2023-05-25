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

        'k8s_version': 'str',

        'name': 'str',

        'private_ip': 'str',

        'public_ip': 'str',
    }

    attribute_map = {

        'k8s_version': 'k8sVersion',

        'name': 'name',

        'private_ip': 'privateIP',

        'public_ip': 'publicIP',
    }

    def __init__(self, k8s_version=None, name=None, private_ip=None, public_ip=None, local_vars_configuration=None):  # noqa: E501
        """KubernetesNodeProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._k8s_version = None
        self._name = None
        self._private_ip = None
        self._public_ip = None
        self.discriminator = None

        self.k8s_version = k8s_version
        self.name = name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip


    @property
    def k8s_version(self):
        """Gets the k8s_version of this KubernetesNodeProperties.  # noqa: E501

        The Kubernetes version running in the node pool. Note that this imposes restrictions on which Kubernetes versions can run in the node pools of a cluster. Also, not all Kubernetes versions are suitable upgrade targets for all earlier versions.  # noqa: E501

        :return: The k8s_version of this KubernetesNodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._k8s_version

    @k8s_version.setter
    def k8s_version(self, k8s_version):
        """Sets the k8s_version of this KubernetesNodeProperties.

        The Kubernetes version running in the node pool. Note that this imposes restrictions on which Kubernetes versions can run in the node pools of a cluster. Also, not all Kubernetes versions are suitable upgrade targets for all earlier versions.  # noqa: E501

        :param k8s_version: The k8s_version of this KubernetesNodeProperties.  # noqa: E501
        :type k8s_version: str
        """
        if self.local_vars_configuration.client_side_validation and k8s_version is None:  # noqa: E501
            raise ValueError("Invalid value for `k8s_version`, must not be `None`")  # noqa: E501

        self._k8s_version = k8s_version

    @property
    def name(self):
        """Gets the name of this KubernetesNodeProperties.  # noqa: E501

        The Kubernetes node name.  # noqa: E501

        :return: The name of this KubernetesNodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KubernetesNodeProperties.

        The Kubernetes node name.  # noqa: E501

        :param name: The name of this KubernetesNodeProperties.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def private_ip(self):
        """Gets the private_ip of this KubernetesNodeProperties.  # noqa: E501

        The private IP associated with the node.  # noqa: E501

        :return: The private_ip of this KubernetesNodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this KubernetesNodeProperties.

        The private IP associated with the node.  # noqa: E501

        :param private_ip: The private_ip of this KubernetesNodeProperties.  # noqa: E501
        :type private_ip: str
        """

        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this KubernetesNodeProperties.  # noqa: E501

        The public IP associated with the node.  # noqa: E501

        :return: The public_ip of this KubernetesNodeProperties.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this KubernetesNodeProperties.

        The public IP associated with the node.  # noqa: E501

        :param public_ip: The public_ip of this KubernetesNodeProperties.  # noqa: E501
        :type public_ip: str
        """

        self._public_ip = public_ip
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
