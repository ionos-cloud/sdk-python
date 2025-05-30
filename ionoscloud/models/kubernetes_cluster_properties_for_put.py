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


class KubernetesClusterPropertiesForPut(object):
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

        'api_subnet_allow_list': 'list[str]',

        's3_buckets': 'list[S3Bucket]',
    }

    attribute_map = {

        'name': 'name',

        'k8s_version': 'k8sVersion',

        'maintenance_window': 'maintenanceWindow',

        'api_subnet_allow_list': 'apiSubnetAllowList',

        's3_buckets': 's3Buckets',
    }

    def __init__(self, name=None, k8s_version=None, maintenance_window=None, api_subnet_allow_list=None, s3_buckets=None, local_vars_configuration=None):  # noqa: E501
        """KubernetesClusterPropertiesForPut - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._k8s_version = None
        self._maintenance_window = None
        self._api_subnet_allow_list = None
        self._s3_buckets = None
        self.discriminator = None

        self.name = name
        if k8s_version is not None:
            self.k8s_version = k8s_version
        if maintenance_window is not None:
            self.maintenance_window = maintenance_window
        if api_subnet_allow_list is not None:
            self.api_subnet_allow_list = api_subnet_allow_list
        if s3_buckets is not None:
            self.s3_buckets = s3_buckets


    @property
    def name(self):
        """Gets the name of this KubernetesClusterPropertiesForPut.  # noqa: E501

        A Kubernetes cluster name. Valid Kubernetes cluster name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.  # noqa: E501

        :return: The name of this KubernetesClusterPropertiesForPut.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KubernetesClusterPropertiesForPut.

        A Kubernetes cluster name. Valid Kubernetes cluster name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.  # noqa: E501

        :param name: The name of this KubernetesClusterPropertiesForPut.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def k8s_version(self):
        """Gets the k8s_version of this KubernetesClusterPropertiesForPut.  # noqa: E501

        The Kubernetes version that the cluster is running. This limits which Kubernetes versions can run in a cluster's node pools. Also, not all Kubernetes versions are suitable upgrade targets for all earlier versions.  # noqa: E501

        :return: The k8s_version of this KubernetesClusterPropertiesForPut.  # noqa: E501
        :rtype: str
        """
        return self._k8s_version

    @k8s_version.setter
    def k8s_version(self, k8s_version):
        """Sets the k8s_version of this KubernetesClusterPropertiesForPut.

        The Kubernetes version that the cluster is running. This limits which Kubernetes versions can run in a cluster's node pools. Also, not all Kubernetes versions are suitable upgrade targets for all earlier versions.  # noqa: E501

        :param k8s_version: The k8s_version of this KubernetesClusterPropertiesForPut.  # noqa: E501
        :type k8s_version: str
        """

        self._k8s_version = k8s_version

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this KubernetesClusterPropertiesForPut.  # noqa: E501


        :return: The maintenance_window of this KubernetesClusterPropertiesForPut.  # noqa: E501
        :rtype: KubernetesMaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this KubernetesClusterPropertiesForPut.


        :param maintenance_window: The maintenance_window of this KubernetesClusterPropertiesForPut.  # noqa: E501
        :type maintenance_window: KubernetesMaintenanceWindow
        """

        self._maintenance_window = maintenance_window

    @property
    def api_subnet_allow_list(self):
        """Gets the api_subnet_allow_list of this KubernetesClusterPropertiesForPut.  # noqa: E501

        Access to the K8s API server is restricted to these CIDRs. Intra-cluster traffic is not affected by this restriction. If no AllowList is specified, access is not limited. If an IP is specified without a subnet mask, the default value is 32 for IPv4 and 128 for IPv6.  # noqa: E501

        :return: The api_subnet_allow_list of this KubernetesClusterPropertiesForPut.  # noqa: E501
        :rtype: list[str]
        """
        return self._api_subnet_allow_list

    @api_subnet_allow_list.setter
    def api_subnet_allow_list(self, api_subnet_allow_list):
        """Sets the api_subnet_allow_list of this KubernetesClusterPropertiesForPut.

        Access to the K8s API server is restricted to these CIDRs. Intra-cluster traffic is not affected by this restriction. If no AllowList is specified, access is not limited. If an IP is specified without a subnet mask, the default value is 32 for IPv4 and 128 for IPv6.  # noqa: E501

        :param api_subnet_allow_list: The api_subnet_allow_list of this KubernetesClusterPropertiesForPut.  # noqa: E501
        :type api_subnet_allow_list: list[str]
        """

        self._api_subnet_allow_list = api_subnet_allow_list

    @property
    def s3_buckets(self):
        """Gets the s3_buckets of this KubernetesClusterPropertiesForPut.  # noqa: E501

        List of Object storage buckets configured for K8s usage. At the moment, it contains only one bucket that is used to store K8s API audit logs.  # noqa: E501

        :return: The s3_buckets of this KubernetesClusterPropertiesForPut.  # noqa: E501
        :rtype: list[S3Bucket]
        """
        return self._s3_buckets

    @s3_buckets.setter
    def s3_buckets(self, s3_buckets):
        """Sets the s3_buckets of this KubernetesClusterPropertiesForPut.

        List of Object storage buckets configured for K8s usage. At the moment, it contains only one bucket that is used to store K8s API audit logs.  # noqa: E501

        :param s3_buckets: The s3_buckets of this KubernetesClusterPropertiesForPut.  # noqa: E501
        :type s3_buckets: list[S3Bucket]
        """

        self._s3_buckets = s3_buckets
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
        if not isinstance(other, KubernetesClusterPropertiesForPut):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubernetesClusterPropertiesForPut):
            return True

        return self.to_dict() != other.to_dict()
