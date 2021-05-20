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


class KubernetesClusterPropertiesForPost(object):
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
        'k8s_version': 'str',
        'maintenance_window': 'KubernetesMaintenanceWindow',
        'public': 'bool',
        'gateway_ip': 'str',
    }

    attribute_map = {
        'name': 'name',
        'k8s_version': 'k8sVersion',
        'maintenance_window': 'maintenanceWindow',
        'public': 'public',
        'gateway_ip': 'gatewayIp',
    }

    def __init__(self, name=None, k8s_version=None, maintenance_window=None, public=True, gateway_ip=None, local_vars_configuration=None):  # noqa: E501
        """KubernetesClusterPropertiesForPost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._k8s_version = None
        self._maintenance_window = None
        self._public = None
        self._gateway_ip = None
        self.discriminator = None

        self.name = name
        if k8s_version is not None:
            self.k8s_version = k8s_version
        if maintenance_window is not None:
            self.maintenance_window = maintenance_window
        if public is not None:
            self.public = public
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip

    @property
    def name(self):
        """Gets the name of this KubernetesClusterPropertiesForPost.  # noqa: E501

        A Kubernetes Cluster Name. Valid Kubernetes Cluster name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.  # noqa: E501

        :return: The name of this KubernetesClusterPropertiesForPost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KubernetesClusterPropertiesForPost.

        A Kubernetes Cluster Name. Valid Kubernetes Cluster name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.  # noqa: E501

        :param name: The name of this KubernetesClusterPropertiesForPost.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def k8s_version(self):
        """Gets the k8s_version of this KubernetesClusterPropertiesForPost.  # noqa: E501

        The kubernetes version in which a cluster is running. This imposes restrictions on what kubernetes versions can be run in a cluster's nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions.  # noqa: E501

        :return: The k8s_version of this KubernetesClusterPropertiesForPost.  # noqa: E501
        :rtype: str
        """
        return self._k8s_version

    @k8s_version.setter
    def k8s_version(self, k8s_version):
        """Sets the k8s_version of this KubernetesClusterPropertiesForPost.

        The kubernetes version in which a cluster is running. This imposes restrictions on what kubernetes versions can be run in a cluster's nodepools. Additionally, not all kubernetes versions are viable upgrade targets for all prior versions.  # noqa: E501

        :param k8s_version: The k8s_version of this KubernetesClusterPropertiesForPost.  # noqa: E501
        :type k8s_version: str
        """

        self._k8s_version = k8s_version

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this KubernetesClusterPropertiesForPost.  # noqa: E501


        :return: The maintenance_window of this KubernetesClusterPropertiesForPost.  # noqa: E501
        :rtype: KubernetesMaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this KubernetesClusterPropertiesForPost.


        :param maintenance_window: The maintenance_window of this KubernetesClusterPropertiesForPost.  # noqa: E501
        :type maintenance_window: KubernetesMaintenanceWindow
        """

        self._maintenance_window = maintenance_window

    @property
    def public(self):
        """Gets the public of this KubernetesClusterPropertiesForPost.  # noqa: E501

        The indicator if the cluster is public or private. Be aware that setting it to false is currently in beta phase.  # noqa: E501

        :return: The public of this KubernetesClusterPropertiesForPost.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this KubernetesClusterPropertiesForPost.

        The indicator if the cluster is public or private. Be aware that setting it to false is currently in beta phase.  # noqa: E501

        :param public: The public of this KubernetesClusterPropertiesForPost.  # noqa: E501
        :type public: bool
        """

        self._public = public

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this KubernetesClusterPropertiesForPost.  # noqa: E501

        The IP address of the gateway used by the cluster. This is mandatory when `public` is set to `false` and should not be provided otherwise.  # noqa: E501

        :return: The gateway_ip of this KubernetesClusterPropertiesForPost.  # noqa: E501
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this KubernetesClusterPropertiesForPost.

        The IP address of the gateway used by the cluster. This is mandatory when `public` is set to `false` and should not be provided otherwise.  # noqa: E501

        :param gateway_ip: The gateway_ip of this KubernetesClusterPropertiesForPost.  # noqa: E501
        :type gateway_ip: str
        """

        self._gateway_ip = gateway_ip

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
        if not isinstance(other, KubernetesClusterPropertiesForPost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubernetesClusterPropertiesForPost):
            return True

        return self.to_dict() != other.to_dict()
