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


class CreateSnapshotProperties(object):
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

        'description': 'str',

        'sec_auth_protection': 'bool',

        'licence_type': 'str',

        'application_type': 'str',
    }

    attribute_map = {

        'name': 'name',

        'description': 'description',

        'sec_auth_protection': 'secAuthProtection',

        'licence_type': 'licenceType',

        'application_type': 'applicationType',
    }

    def __init__(self, name=None, description=None, sec_auth_protection=None, licence_type=None, application_type='UNKNOWN', local_vars_configuration=None):  # noqa: E501
        """CreateSnapshotProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._sec_auth_protection = None
        self._licence_type = None
        self._application_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if sec_auth_protection is not None:
            self.sec_auth_protection = sec_auth_protection
        if licence_type is not None:
            self.licence_type = licence_type
        if application_type is not None:
            self.application_type = application_type


    @property
    def name(self):
        """Gets the name of this CreateSnapshotProperties.  # noqa: E501

        The name of the snapshot  # noqa: E501

        :return: The name of this CreateSnapshotProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSnapshotProperties.

        The name of the snapshot  # noqa: E501

        :param name: The name of this CreateSnapshotProperties.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateSnapshotProperties.  # noqa: E501

        The description of the snapshot  # noqa: E501

        :return: The description of this CreateSnapshotProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSnapshotProperties.

        The description of the snapshot  # noqa: E501

        :param description: The description of this CreateSnapshotProperties.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def sec_auth_protection(self):
        """Gets the sec_auth_protection of this CreateSnapshotProperties.  # noqa: E501

        Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc.  # noqa: E501

        :return: The sec_auth_protection of this CreateSnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._sec_auth_protection

    @sec_auth_protection.setter
    def sec_auth_protection(self, sec_auth_protection):
        """Sets the sec_auth_protection of this CreateSnapshotProperties.

        Flag representing if extra protection is enabled on snapshot e.g. Two Factor protection etc.  # noqa: E501

        :param sec_auth_protection: The sec_auth_protection of this CreateSnapshotProperties.  # noqa: E501
        :type sec_auth_protection: bool
        """

        self._sec_auth_protection = sec_auth_protection

    @property
    def licence_type(self):
        """Gets the licence_type of this CreateSnapshotProperties.  # noqa: E501

        OS type of this Snapshot  # noqa: E501

        :return: The licence_type of this CreateSnapshotProperties.  # noqa: E501
        :rtype: str
        """
        return self._licence_type

    @licence_type.setter
    def licence_type(self, licence_type):
        """Sets the licence_type of this CreateSnapshotProperties.

        OS type of this Snapshot  # noqa: E501

        :param licence_type: The licence_type of this CreateSnapshotProperties.  # noqa: E501
        :type licence_type: str
        """
        allowed_values = ["UNKNOWN", "WINDOWS", "WINDOWS2016", "WINDOWS2019", "WINDOWS2022", "WINDOWS2025", "RHEL", "LINUX", "OTHER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and licence_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `licence_type` ({0}), must be one of {1}"  # noqa: E501
                .format(licence_type, allowed_values)
            )

        self._licence_type = licence_type

    @property
    def application_type(self):
        """Gets the application_type of this CreateSnapshotProperties.  # noqa: E501

        The type of application that is hosted on this resource.  Only public images can have an Application type different than UNKNOWN.  # noqa: E501

        :return: The application_type of this CreateSnapshotProperties.  # noqa: E501
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """Sets the application_type of this CreateSnapshotProperties.

        The type of application that is hosted on this resource.  Only public images can have an Application type different than UNKNOWN.  # noqa: E501

        :param application_type: The application_type of this CreateSnapshotProperties.  # noqa: E501
        :type application_type: str
        """

        self._application_type = application_type
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
        if not isinstance(other, CreateSnapshotProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSnapshotProperties):
            return True

        return self.to_dict() != other.to_dict()
