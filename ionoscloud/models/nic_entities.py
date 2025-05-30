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


class NicEntities(object):
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

        'flowlogs': 'FlowLogs',

        'firewallrules': 'FirewallRules',

        'securitygroups': 'SecurityGroups',
    }

    attribute_map = {

        'flowlogs': 'flowlogs',

        'firewallrules': 'firewallrules',

        'securitygroups': 'securitygroups',
    }

    def __init__(self, flowlogs=None, firewallrules=None, securitygroups=None, local_vars_configuration=None):  # noqa: E501
        """NicEntities - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._flowlogs = None
        self._firewallrules = None
        self._securitygroups = None
        self.discriminator = None

        if flowlogs is not None:
            self.flowlogs = flowlogs
        if firewallrules is not None:
            self.firewallrules = firewallrules
        if securitygroups is not None:
            self.securitygroups = securitygroups


    @property
    def flowlogs(self):
        """Gets the flowlogs of this NicEntities.  # noqa: E501


        :return: The flowlogs of this NicEntities.  # noqa: E501
        :rtype: FlowLogs
        """
        return self._flowlogs

    @flowlogs.setter
    def flowlogs(self, flowlogs):
        """Sets the flowlogs of this NicEntities.


        :param flowlogs: The flowlogs of this NicEntities.  # noqa: E501
        :type flowlogs: FlowLogs
        """

        self._flowlogs = flowlogs

    @property
    def firewallrules(self):
        """Gets the firewallrules of this NicEntities.  # noqa: E501


        :return: The firewallrules of this NicEntities.  # noqa: E501
        :rtype: FirewallRules
        """
        return self._firewallrules

    @firewallrules.setter
    def firewallrules(self, firewallrules):
        """Sets the firewallrules of this NicEntities.


        :param firewallrules: The firewallrules of this NicEntities.  # noqa: E501
        :type firewallrules: FirewallRules
        """

        self._firewallrules = firewallrules

    @property
    def securitygroups(self):
        """Gets the securitygroups of this NicEntities.  # noqa: E501


        :return: The securitygroups of this NicEntities.  # noqa: E501
        :rtype: SecurityGroups
        """
        return self._securitygroups

    @securitygroups.setter
    def securitygroups(self, securitygroups):
        """Sets the securitygroups of this NicEntities.


        :param securitygroups: The securitygroups of this NicEntities.  # noqa: E501
        :type securitygroups: SecurityGroups
        """

        self._securitygroups = securitygroups
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
        if not isinstance(other, NicEntities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NicEntities):
            return True

        return self.to_dict() != other.to_dict()
