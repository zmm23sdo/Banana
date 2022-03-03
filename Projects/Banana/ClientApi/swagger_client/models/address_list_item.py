# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AddressListItem(object):
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
        'id': 'int',
        'full_name': 'str',
        'phone_number': 'str',
        'state': 'str',
        'city': 'str',
        'zipcode': 'str',
        'detail': 'str',
        'is_default': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'full_name': 'full_name',
        'phone_number': 'phone_number',
        'state': 'state',
        'city': 'city',
        'zipcode': 'zipcode',
        'detail': 'detail',
        'is_default': 'is_default'
    }

    def __init__(self, id=None, full_name=None, phone_number=None, state=None, city=None, zipcode=None, detail=None, is_default=None):  # noqa: E501
        """AddressListItem - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._full_name = None
        self._phone_number = None
        self._state = None
        self._city = None
        self._zipcode = None
        self._detail = None
        self._is_default = None
        self.discriminator = None
        self.id = id
        self.full_name = full_name
        self.phone_number = phone_number
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.detail = detail
        self.is_default = is_default

    @property
    def id(self):
        """Gets the id of this AddressListItem.  # noqa: E501

         id  # noqa: E501

        :return: The id of this AddressListItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddressListItem.

         id  # noqa: E501

        :param id: The id of this AddressListItem.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def full_name(self):
        """Gets the full_name of this AddressListItem.  # noqa: E501

         全名  # noqa: E501

        :return: The full_name of this AddressListItem.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this AddressListItem.

         全名  # noqa: E501

        :param full_name: The full_name of this AddressListItem.  # noqa: E501
        :type: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def phone_number(self):
        """Gets the phone_number of this AddressListItem.  # noqa: E501

         电话号码  # noqa: E501

        :return: The phone_number of this AddressListItem.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this AddressListItem.

         电话号码  # noqa: E501

        :param phone_number: The phone_number of this AddressListItem.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def state(self):
        """Gets the state of this AddressListItem.  # noqa: E501

         state  # noqa: E501

        :return: The state of this AddressListItem.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AddressListItem.

         state  # noqa: E501

        :param state: The state of this AddressListItem.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def city(self):
        """Gets the city of this AddressListItem.  # noqa: E501

         city  # noqa: E501

        :return: The city of this AddressListItem.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AddressListItem.

         city  # noqa: E501

        :param city: The city of this AddressListItem.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def zipcode(self):
        """Gets the zipcode of this AddressListItem.  # noqa: E501

         邮政编码  # noqa: E501

        :return: The zipcode of this AddressListItem.  # noqa: E501
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this AddressListItem.

         邮政编码  # noqa: E501

        :param zipcode: The zipcode of this AddressListItem.  # noqa: E501
        :type: str
        """
        if zipcode is None:
            raise ValueError("Invalid value for `zipcode`, must not be `None`")  # noqa: E501

        self._zipcode = zipcode

    @property
    def detail(self):
        """Gets the detail of this AddressListItem.  # noqa: E501

         detail  # noqa: E501

        :return: The detail of this AddressListItem.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this AddressListItem.

         detail  # noqa: E501

        :param detail: The detail of this AddressListItem.  # noqa: E501
        :type: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

    @property
    def is_default(self):
        """Gets the is_default of this AddressListItem.  # noqa: E501

         是否默认地址  # noqa: E501

        :return: The is_default of this AddressListItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this AddressListItem.

         是否默认地址  # noqa: E501

        :param is_default: The is_default of this AddressListItem.  # noqa: E501
        :type: bool
        """
        if is_default is None:
            raise ValueError("Invalid value for `is_default`, must not be `None`")  # noqa: E501

        self._is_default = is_default

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
        if issubclass(AddressListItem, dict):
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
        if not isinstance(other, AddressListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
