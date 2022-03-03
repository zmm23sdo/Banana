# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Cart(object):
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
        'cart_id': 'int',
        'user_id': 'str',
        'sku': 'str',
        'product_num': 'int',
        'is_selected': 'bool',
        'sku_json': 'str',
        'order_id': 'str',
        'source': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'delete_time': 'str'
    }

    attribute_map = {
        'cart_id': 'cart_id',
        'user_id': 'user_id',
        'sku': 'sku',
        'product_num': 'product_num',
        'is_selected': 'is_selected',
        'sku_json': 'sku_json',
        'order_id': 'order_id',
        'source': 'source',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'delete_time': 'delete_time'
    }

    def __init__(self, cart_id=None, user_id=None, sku=None, product_num=None, is_selected=None, sku_json=None, order_id=None, source=None, create_time=None, update_time=None, delete_time=None):  # noqa: E501
        """Cart - a model defined in Swagger"""  # noqa: E501
        self._cart_id = None
        self._user_id = None
        self._sku = None
        self._product_num = None
        self._is_selected = None
        self._sku_json = None
        self._order_id = None
        self._source = None
        self._create_time = None
        self._update_time = None
        self._delete_time = None
        self.discriminator = None
        self.cart_id = cart_id
        self.user_id = user_id
        self.sku = sku
        self.product_num = product_num
        self.is_selected = is_selected
        self.sku_json = sku_json
        self.order_id = order_id
        self.source = source
        self.create_time = create_time
        self.update_time = update_time
        self.delete_time = delete_time

    @property
    def cart_id(self):
        """Gets the cart_id of this Cart.  # noqa: E501

         购物车ID  # noqa: E501

        :return: The cart_id of this Cart.  # noqa: E501
        :rtype: int
        """
        return self._cart_id

    @cart_id.setter
    def cart_id(self, cart_id):
        """Sets the cart_id of this Cart.

         购物车ID  # noqa: E501

        :param cart_id: The cart_id of this Cart.  # noqa: E501
        :type: int
        """
        if cart_id is None:
            raise ValueError("Invalid value for `cart_id`, must not be `None`")  # noqa: E501

        self._cart_id = cart_id

    @property
    def user_id(self):
        """Gets the user_id of this Cart.  # noqa: E501

         用户ID  # noqa: E501

        :return: The user_id of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Cart.

         用户ID  # noqa: E501

        :param user_id: The user_id of this Cart.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def sku(self):
        """Gets the sku of this Cart.  # noqa: E501

         商品唯一标识Sku  # noqa: E501

        :return: The sku of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this Cart.

         商品唯一标识Sku  # noqa: E501

        :param sku: The sku of this Cart.  # noqa: E501
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")  # noqa: E501

        self._sku = sku

    @property
    def product_num(self):
        """Gets the product_num of this Cart.  # noqa: E501

         当前商品数量  # noqa: E501

        :return: The product_num of this Cart.  # noqa: E501
        :rtype: int
        """
        return self._product_num

    @product_num.setter
    def product_num(self, product_num):
        """Sets the product_num of this Cart.

         当前商品数量  # noqa: E501

        :param product_num: The product_num of this Cart.  # noqa: E501
        :type: int
        """
        if product_num is None:
            raise ValueError("Invalid value for `product_num`, must not be `None`")  # noqa: E501

        self._product_num = product_num

    @property
    def is_selected(self):
        """Gets the is_selected of this Cart.  # noqa: E501

         当前商品是否选中状态  # noqa: E501

        :return: The is_selected of this Cart.  # noqa: E501
        :rtype: bool
        """
        return self._is_selected

    @is_selected.setter
    def is_selected(self, is_selected):
        """Sets the is_selected of this Cart.

         当前商品是否选中状态  # noqa: E501

        :param is_selected: The is_selected of this Cart.  # noqa: E501
        :type: bool
        """
        if is_selected is None:
            raise ValueError("Invalid value for `is_selected`, must not be `None`")  # noqa: E501

        self._is_selected = is_selected

    @property
    def sku_json(self):
        """Gets the sku_json of this Cart.  # noqa: E501

         当前商品快照  # noqa: E501

        :return: The sku_json of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._sku_json

    @sku_json.setter
    def sku_json(self, sku_json):
        """Sets the sku_json of this Cart.

         当前商品快照  # noqa: E501

        :param sku_json: The sku_json of this Cart.  # noqa: E501
        :type: str
        """
        if sku_json is None:
            raise ValueError("Invalid value for `sku_json`, must not be `None`")  # noqa: E501

        self._sku_json = sku_json

    @property
    def order_id(self):
        """Gets the order_id of this Cart.  # noqa: E501

         当前商品生成的订单ID  # noqa: E501

        :return: The order_id of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Cart.

         当前商品生成的订单ID  # noqa: E501

        :param order_id: The order_id of this Cart.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def source(self):
        """Gets the source of this Cart.  # noqa: E501

         当前商品录入来源  # noqa: E501

        :return: The source of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Cart.

         当前商品录入来源  # noqa: E501

        :param source: The source of this Cart.  # noqa: E501
        :type: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def create_time(self):
        """Gets the create_time of this Cart.  # noqa: E501

         创建时间  # noqa: E501

        :return: The create_time of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Cart.

         创建时间  # noqa: E501

        :param create_time: The create_time of this Cart.  # noqa: E501
        :type: str
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Cart.  # noqa: E501

         更新时间  # noqa: E501

        :return: The update_time of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Cart.

         更新时间  # noqa: E501

        :param update_time: The update_time of this Cart.  # noqa: E501
        :type: str
        """
        if update_time is None:
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def delete_time(self):
        """Gets the delete_time of this Cart.  # noqa: E501

         删除时间  # noqa: E501

        :return: The delete_time of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        """Sets the delete_time of this Cart.

         删除时间  # noqa: E501

        :param delete_time: The delete_time of this Cart.  # noqa: E501
        :type: str
        """
        if delete_time is None:
            raise ValueError("Invalid value for `delete_time`, must not be `None`")  # noqa: E501

        self._delete_time = delete_time

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
        if issubclass(Cart, dict):
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
        if not isinstance(other, Cart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
