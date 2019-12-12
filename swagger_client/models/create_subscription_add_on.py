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


class CreateSubscriptionAddOn(object):
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
        'quantity': 'int',
        'amount': 'int',
        'name': 'str',
        'description': 'str',
        'add_on': 'str',
        'fixed_amount': 'bool',
        'amount_incl_vat': 'bool'
    }

    attribute_map = {
        'handle': 'handle',
        'quantity': 'quantity',
        'amount': 'amount',
        'name': 'name',
        'description': 'description',
        'add_on': 'add_on',
        'fixed_amount': 'fixed_amount',
        'amount_incl_vat': 'amount_incl_vat'
    }

    def __init__(self, handle=None, quantity=None, amount=None, name=None, description=None, add_on=None, fixed_amount=None, amount_incl_vat=None):  # noqa: E501
        """CreateSubscriptionAddOn - a model defined in Swagger"""  # noqa: E501

        self._handle = None
        self._quantity = None
        self._amount = None
        self._name = None
        self._description = None
        self._add_on = None
        self._fixed_amount = None
        self._amount_incl_vat = None
        self.discriminator = None

        self.handle = handle
        if quantity is not None:
            self.quantity = quantity
        if amount is not None:
            self.amount = amount
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.add_on = add_on
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if amount_incl_vat is not None:
            self.amount_incl_vat = amount_incl_vat

    @property
    def handle(self):
        """Gets the handle of this CreateSubscriptionAddOn.  # noqa: E501

        Optional per subscription unique handle for the subscription add-on. If not defined the handle will default to the add-on handle, this means that by default an add-on can only be attached once to each subscription. The handle can be used to link the subscription add-on to an entity like computer serial number or vehicle license plate.  # noqa: E501

        :return: The handle of this CreateSubscriptionAddOn.  # noqa: E501
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this CreateSubscriptionAddOn.

        Optional per subscription unique handle for the subscription add-on. If not defined the handle will default to the add-on handle, this means that by default an add-on can only be attached once to each subscription. The handle can be used to link the subscription add-on to an entity like computer serial number or vehicle license plate.  # noqa: E501

        :param handle: The handle of this CreateSubscriptionAddOn.  # noqa: E501
        :type: str
        """
        if handle is None:
            raise ValueError("Invalid value for `handle`, must not be `None`")  # noqa: E501

        self._handle = handle

    @property
    def quantity(self):
        """Gets the quantity of this CreateSubscriptionAddOn.  # noqa: E501

        Optional quantity of the of the add-on for this subscription. Defaults to 1. May only be provided for add-on with type `quantity`.  # noqa: E501

        :return: The quantity of this CreateSubscriptionAddOn.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CreateSubscriptionAddOn.

        Optional quantity of the of the add-on for this subscription. Defaults to 1. May only be provided for add-on with type `quantity`.  # noqa: E501

        :param quantity: The quantity of this CreateSubscriptionAddOn.  # noqa: E501
        :type: int
        """
        if quantity is not None and quantity < 1:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")  # noqa: E501

        self._quantity = quantity

    @property
    def amount(self):
        """Gets the amount of this CreateSubscriptionAddOn.  # noqa: E501

        Optional custom fixed per quantity add-on price. If provided the add-on price billed for each billing period will be overridden by this price. Implicitly defines `fixed_amount` as true. Cannot be provided with `fixed_amount` false.  # noqa: E501

        :return: The amount of this CreateSubscriptionAddOn.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateSubscriptionAddOn.

        Optional custom fixed per quantity add-on price. If provided the add-on price billed for each billing period will be overridden by this price. Implicitly defines `fixed_amount` as true. Cannot be provided with `fixed_amount` false.  # noqa: E501

        :param amount: The amount of this CreateSubscriptionAddOn.  # noqa: E501
        :type: int
        """
        if amount is not None and amount < 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0`")  # noqa: E501

        self._amount = amount

    @property
    def name(self):
        """Gets the name of this CreateSubscriptionAddOn.  # noqa: E501

        Optional name overriding the add-on name. If not defined the add-on name will be used as order line text.  # noqa: E501

        :return: The name of this CreateSubscriptionAddOn.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSubscriptionAddOn.

        Optional name overriding the add-on name. If not defined the add-on name will be used as order line text.  # noqa: E501

        :param name: The name of this CreateSubscriptionAddOn.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateSubscriptionAddOn.  # noqa: E501

        Optional description overriding the add-on description. If not defined the add-on description will be used.  # noqa: E501

        :return: The description of this CreateSubscriptionAddOn.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSubscriptionAddOn.

        Optional description overriding the add-on description. If not defined the add-on description will be used.  # noqa: E501

        :param description: The description of this CreateSubscriptionAddOn.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def add_on(self):
        """Gets the add_on of this CreateSubscriptionAddOn.  # noqa: E501

        Add-on for subscription add-on  # noqa: E501

        :return: The add_on of this CreateSubscriptionAddOn.  # noqa: E501
        :rtype: str
        """
        return self._add_on

    @add_on.setter
    def add_on(self, add_on):
        """Sets the add_on of this CreateSubscriptionAddOn.

        Add-on for subscription add-on  # noqa: E501

        :param add_on: The add_on of this CreateSubscriptionAddOn.  # noqa: E501
        :type: str
        """
        if add_on is None:
            raise ValueError("Invalid value for `add_on`, must not be `None`")  # noqa: E501

        self._add_on = add_on

    @property
    def fixed_amount(self):
        """Gets the fixed_amount of this CreateSubscriptionAddOn.  # noqa: E501

        Whether the price of the subscription add-on should be fixed to the current price of add-on, or the price should follow the add-on price. Defaults to true. If set to false the price of the add-on will be determined by the add-on price at the time of subscription billing.  # noqa: E501

        :return: The fixed_amount of this CreateSubscriptionAddOn.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        """Sets the fixed_amount of this CreateSubscriptionAddOn.

        Whether the price of the subscription add-on should be fixed to the current price of add-on, or the price should follow the add-on price. Defaults to true. If set to false the price of the add-on will be determined by the add-on price at the time of subscription billing.  # noqa: E501

        :param fixed_amount: The fixed_amount of this CreateSubscriptionAddOn.  # noqa: E501
        :type: bool
        """

        self._fixed_amount = fixed_amount

    @property
    def amount_incl_vat(self):
        """Gets the amount_incl_vat of this CreateSubscriptionAddOn.  # noqa: E501

        Whether the optional amount is including VAT. Defaults to true.  # noqa: E501

        :return: The amount_incl_vat of this CreateSubscriptionAddOn.  # noqa: E501
        :rtype: bool
        """
        return self._amount_incl_vat

    @amount_incl_vat.setter
    def amount_incl_vat(self, amount_incl_vat):
        """Sets the amount_incl_vat of this CreateSubscriptionAddOn.

        Whether the optional amount is including VAT. Defaults to true.  # noqa: E501

        :param amount_incl_vat: The amount_incl_vat of this CreateSubscriptionAddOn.  # noqa: E501
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
        if issubclass(CreateSubscriptionAddOn, dict):
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
        if not isinstance(other, CreateSubscriptionAddOn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other