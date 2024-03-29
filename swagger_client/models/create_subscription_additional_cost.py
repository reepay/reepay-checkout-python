# coding: utf-8

"""
    Reepay Checkout API

    Reepay Checkout REST API  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateSubscriptionAdditionalCost(object):
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
        'handle': 'str',
        'ordertext': 'str',
        'quantity': 'int',
        'amount': 'int',
        'vat': 'float',
        'amount_incl_vat': 'bool'
    }

    attribute_map = {
        'handle': 'handle',
        'ordertext': 'ordertext',
        'quantity': 'quantity',
        'amount': 'amount',
        'vat': 'vat',
        'amount_incl_vat': 'amount_incl_vat'
    }

    def __init__(self, handle=None, ordertext=None, quantity=None, amount=None, vat=None, amount_incl_vat=None):  # noqa: E501
        """CreateSubscriptionAdditionalCost - a model defined in Swagger"""  # noqa: E501

        self._handle = None
        self._ordertext = None
        self._quantity = None
        self._amount = None
        self._vat = None
        self._amount_incl_vat = None
        self.discriminator = None

        self.handle = handle
        self.ordertext = ordertext
        if quantity is not None:
            self.quantity = quantity
        self.amount = amount
        if vat is not None:
            self.vat = vat
        if amount_incl_vat is not None:
            self.amount_incl_vat = amount_incl_vat

    @property
    def handle(self):
        """Gets the handle of this CreateSubscriptionAdditionalCost.  # noqa: E501

        Per account unique handle for the additional cost  # noqa: E501

        :return: The handle of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this CreateSubscriptionAdditionalCost.

        Per account unique handle for the additional cost  # noqa: E501

        :param handle: The handle of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :type: str
        """
        if handle is None:
            raise ValueError("Invalid value for `handle`, must not be `None`")  # noqa: E501

        self._handle = handle

    @property
    def ordertext(self):
        """Gets the ordertext of this CreateSubscriptionAdditionalCost.  # noqa: E501

        Order text for the additional cost. Will be on affected invoices.  # noqa: E501

        :return: The ordertext of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :rtype: str
        """
        return self._ordertext

    @ordertext.setter
    def ordertext(self, ordertext):
        """Sets the ordertext of this CreateSubscriptionAdditionalCost.

        Order text for the additional cost. Will be on affected invoices.  # noqa: E501

        :param ordertext: The ordertext of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :type: str
        """
        if ordertext is None:
            raise ValueError("Invalid value for `ordertext`, must not be `None`")  # noqa: E501

        self._ordertext = ordertext

    @property
    def quantity(self):
        """Gets the quantity of this CreateSubscriptionAdditionalCost.  # noqa: E501

        Quantity for the additional cost. Default 1.  # noqa: E501

        :return: The quantity of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CreateSubscriptionAdditionalCost.

        Quantity for the additional cost. Default 1.  # noqa: E501

        :param quantity: The quantity of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :type: int
        """
        if quantity is not None and quantity < 1:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")  # noqa: E501

        self._quantity = quantity

    @property
    def amount(self):
        """Gets the amount of this CreateSubscriptionAdditionalCost.  # noqa: E501

        Per quantity amount in the smallest unit for the account currency  # noqa: E501

        :return: The amount of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateSubscriptionAdditionalCost.

        Per quantity amount in the smallest unit for the account currency  # noqa: E501

        :param amount: The amount of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if amount is not None and amount < 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0`")  # noqa: E501

        self._amount = amount

    @property
    def vat(self):
        """Gets the vat of this CreateSubscriptionAdditionalCost.  # noqa: E501

        Optional vat for additional cost. Account default is used if none given.  # noqa: E501

        :return: The vat of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :rtype: float
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this CreateSubscriptionAdditionalCost.

        Optional vat for additional cost. Account default is used if none given.  # noqa: E501

        :param vat: The vat of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :type: float
        """
        if vat is not None and vat > 1:  # noqa: E501
            raise ValueError("Invalid value for `vat`, must be a value less than or equal to `1`")  # noqa: E501
        if vat is not None and vat < 0:  # noqa: E501
            raise ValueError("Invalid value for `vat`, must be a value greater than or equal to `0`")  # noqa: E501

        self._vat = vat

    @property
    def amount_incl_vat(self):
        """Gets the amount_incl_vat of this CreateSubscriptionAdditionalCost.  # noqa: E501

        Whether the per quantity amount is including VAT. Defaults to true.  # noqa: E501

        :return: The amount_incl_vat of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :rtype: bool
        """
        return self._amount_incl_vat

    @amount_incl_vat.setter
    def amount_incl_vat(self, amount_incl_vat):
        """Sets the amount_incl_vat of this CreateSubscriptionAdditionalCost.

        Whether the per quantity amount is including VAT. Defaults to true.  # noqa: E501

        :param amount_incl_vat: The amount_incl_vat of this CreateSubscriptionAdditionalCost.  # noqa: E501
        :type: bool
        """

        self._amount_incl_vat = amount_incl_vat

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
        if issubclass(CreateSubscriptionAdditionalCost, dict):
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
        if not isinstance(other, CreateSubscriptionAdditionalCost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
