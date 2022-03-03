# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateRoleReq(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'detail': 'list[Detail]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'detail': 'detail'
    }

    def __init__(self, name=None, description=None, detail=None):  # noqa: E501
        """CreateRoleReq - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._detail = None
        self.discriminator = None
        self.name = name
        self.description = description
        self.detail = detail

    @property
    def name(self):
        """Gets the name of this CreateRoleReq.  # noqa: E501

         角色名称  # noqa: E501

        :return: The name of this CreateRoleReq.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRoleReq.

         角色名称  # noqa: E501

        :param name: The name of this CreateRoleReq.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateRoleReq.  # noqa: E501

         角色描述  # noqa: E501

        :return: The description of this CreateRoleReq.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRoleReq.

         角色描述  # noqa: E501

        :param description: The description of this CreateRoleReq.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def detail(self):
        """Gets the detail of this CreateRoleReq.  # noqa: E501

         角色对应的分组和权限  # noqa: E501

        :return: The detail of this CreateRoleReq.  # noqa: E501
        :rtype: list[Detail]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this CreateRoleReq.

         角色对应的分组和权限  # noqa: E501

        :param detail: The detail of this CreateRoleReq.  # noqa: E501
        :type: list[Detail]
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CreateRoleReq, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRoleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
