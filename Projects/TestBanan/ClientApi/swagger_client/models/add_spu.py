# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AddSpu(object):
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
        'category_id': 'str',
        'brand_id': 'str',
        'name': 'str',
        'sold': 'int'
    }

    attribute_map = {
        'category_id': 'categoryId',
        'brand_id': 'brandId',
        'name': 'name',
        'sold': 'sold'
    }

    def __init__(self, category_id=None, brand_id=None, name=None, sold=None):  # noqa: E501
        """AddSpu - a model defined in Swagger"""  # noqa: E501
        self._category_id = None
        self._brand_id = None
        self._name = None
        self._sold = None
        self.discriminator = None
        self.category_id = category_id
        self.brand_id = brand_id
        self.name = name
        self.sold = sold

    @property
    def category_id(self):
        """Gets the category_id of this AddSpu.  # noqa: E501

        类别id  # noqa: E501

        :return: The category_id of this AddSpu.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this AddSpu.

        类别id  # noqa: E501

        :param category_id: The category_id of this AddSpu.  # noqa: E501
        :type: str
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

    @property
    def brand_id(self):
        """Gets the brand_id of this AddSpu.  # noqa: E501

        品牌id  # noqa: E501

        :return: The brand_id of this AddSpu.  # noqa: E501
        :rtype: str
        """
        return self._brand_id

    @brand_id.setter
    def brand_id(self, brand_id):
        """Sets the brand_id of this AddSpu.

        品牌id  # noqa: E501

        :param brand_id: The brand_id of this AddSpu.  # noqa: E501
        :type: str
        """
        if brand_id is None:
            raise ValueError("Invalid value for `brand_id`, must not be `None`")  # noqa: E501

        self._brand_id = brand_id

    @property
    def name(self):
        """Gets the name of this AddSpu.  # noqa: E501

        名称  # noqa: E501

        :return: The name of this AddSpu.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddSpu.

        名称  # noqa: E501

        :param name: The name of this AddSpu.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sold(self):
        """Gets the sold of this AddSpu.  # noqa: E501

        售价  # noqa: E501

        :return: The sold of this AddSpu.  # noqa: E501
        :rtype: int
        """
        return self._sold

    @sold.setter
    def sold(self, sold):
        """Sets the sold of this AddSpu.

        售价  # noqa: E501

        :param sold: The sold of this AddSpu.  # noqa: E501
        :type: int
        """
        if sold is None:
            raise ValueError("Invalid value for `sold`, must not be `None`")  # noqa: E501

        self._sold = sold

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
        if issubclass(AddSpu, dict):
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
        if not isinstance(other, AddSpu):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
