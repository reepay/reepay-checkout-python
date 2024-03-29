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


class OrderLine(object):
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
        'id': 'str',
        'ordertext': 'str',
        'amount': 'int',
        'vat': 'float',
        'quantity': 'int',
        'origin': 'str',
        'timestamp': 'datetime',
        'discounted_amount': 'int',
        'amount_vat': 'int',
        'amount_ex_vat': 'int',
        'unit_amount': 'int',
        'unit_amount_vat': 'int',
        'unit_amount_ex_vat': 'int',
        'amount_defined_incl_vat': 'bool',
        'origin_handle': 'str',
        'period_from': 'datetime',
        'period_to': 'datetime',
        'discount_percentage': 'int',
        'discounted_order_line': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ordertext': 'ordertext',
        'amount': 'amount',
        'vat': 'vat',
        'quantity': 'quantity',
        'origin': 'origin',
        'timestamp': 'timestamp',
        'discounted_amount': 'discounted_amount',
        'amount_vat': 'amount_vat',
        'amount_ex_vat': 'amount_ex_vat',
        'unit_amount': 'unit_amount',
        'unit_amount_vat': 'unit_amount_vat',
        'unit_amount_ex_vat': 'unit_amount_ex_vat',
        'amount_defined_incl_vat': 'amount_defined_incl_vat',
        'origin_handle': 'origin_handle',
        'period_from': 'period_from',
        'period_to': 'period_to',
        'discount_percentage': 'discount_percentage',
        'discounted_order_line': 'discounted_order_line'
    }

    def __init__(self, id=None, ordertext=None, amount=None, vat=None, quantity=None, origin=None, timestamp=None, discounted_amount=None, amount_vat=None, amount_ex_vat=None, unit_amount=None, unit_amount_vat=None, unit_amount_ex_vat=None, amount_defined_incl_vat=None, origin_handle=None, period_from=None, period_to=None, discount_percentage=None, discounted_order_line=None):  # noqa: E501
        """OrderLine - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._ordertext = None
        self._amount = None
        self._vat = None
        self._quantity = None
        self._origin = None
        self._timestamp = None
        self._discounted_amount = None
        self._amount_vat = None
        self._amount_ex_vat = None
        self._unit_amount = None
        self._unit_amount_vat = None
        self._unit_amount_ex_vat = None
        self._amount_defined_incl_vat = None
        self._origin_handle = None
        self._period_from = None
        self._period_to = None
        self._discount_percentage = None
        self._discounted_order_line = None
        self.discriminator = None

        self.id = id
        self.ordertext = ordertext
        self.amount = amount
        self.vat = vat
        self.quantity = quantity
        self.origin = origin
        self.timestamp = timestamp
        if discounted_amount is not None:
            self.discounted_amount = discounted_amount
        self.amount_vat = amount_vat
        self.amount_ex_vat = amount_ex_vat
        self.unit_amount = unit_amount
        self.unit_amount_vat = unit_amount_vat
        self.unit_amount_ex_vat = unit_amount_ex_vat
        self.amount_defined_incl_vat = amount_defined_incl_vat
        if origin_handle is not None:
            self.origin_handle = origin_handle
        if period_from is not None:
            self.period_from = period_from
        if period_to is not None:
            self.period_to = period_to
        if discount_percentage is not None:
            self.discount_percentage = discount_percentage
        if discounted_order_line is not None:
            self.discounted_order_line = discounted_order_line

    @property
    def id(self):
        """Gets the id of this OrderLine.  # noqa: E501

        Per account unique order line id  # noqa: E501

        :return: The id of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderLine.

        Per account unique order line id  # noqa: E501

        :param id: The id of this OrderLine.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ordertext(self):
        """Gets the ordertext of this OrderLine.  # noqa: E501

        Order line text  # noqa: E501

        :return: The ordertext of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._ordertext

    @ordertext.setter
    def ordertext(self, ordertext):
        """Sets the ordertext of this OrderLine.

        Order line text  # noqa: E501

        :param ordertext: The ordertext of this OrderLine.  # noqa: E501
        :type: str
        """
        if ordertext is None:
            raise ValueError("Invalid value for `ordertext`, must not be `None`")  # noqa: E501

        self._ordertext = ordertext

    @property
    def amount(self):
        """Gets the amount of this OrderLine.  # noqa: E501

        Order line total amount including vat  # noqa: E501

        :return: The amount of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OrderLine.

        Order line total amount including vat  # noqa: E501

        :param amount: The amount of this OrderLine.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def vat(self):
        """Gets the vat of this OrderLine.  # noqa: E501

        Order line vat percent  # noqa: E501

        :return: The vat of this OrderLine.  # noqa: E501
        :rtype: float
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this OrderLine.

        Order line vat percent  # noqa: E501

        :param vat: The vat of this OrderLine.  # noqa: E501
        :type: float
        """
        if vat is None:
            raise ValueError("Invalid value for `vat`, must not be `None`")  # noqa: E501

        self._vat = vat

    @property
    def quantity(self):
        """Gets the quantity of this OrderLine.  # noqa: E501

        Order line quantity  # noqa: E501

        :return: The quantity of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderLine.

        Order line quantity  # noqa: E501

        :param quantity: The quantity of this OrderLine.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501
        if quantity is not None and quantity < 1:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")  # noqa: E501

        self._quantity = quantity

    @property
    def origin(self):
        """Gets the origin of this OrderLine.  # noqa: E501

        Order line origin, one of the following: `plan`, `add_on`, `ondemand`, `additional_cost`, `credit`, `discount`, `setup_fee`  # noqa: E501

        :return: The origin of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this OrderLine.

        Order line origin, one of the following: `plan`, `add_on`, `ondemand`, `additional_cost`, `credit`, `discount`, `setup_fee`  # noqa: E501

        :param origin: The origin of this OrderLine.  # noqa: E501
        :type: str
        """
        if origin is None:
            raise ValueError("Invalid value for `origin`, must not be `None`")  # noqa: E501
        allowed_values = ["plan", "add_on", "ondemand", "additional_cost", "credit", "discount", "setup_fee"]  # noqa: E501
        if origin not in allowed_values:
            raise ValueError(
                "Invalid value for `origin` ({0}), must be one of {1}"  # noqa: E501
                .format(origin, allowed_values)
            )

        self._origin = origin

    @property
    def timestamp(self):
        """Gets the timestamp of this OrderLine.  # noqa: E501

        Timestamp from order line origin, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :return: The timestamp of this OrderLine.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this OrderLine.

        Timestamp from order line origin, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :param timestamp: The timestamp of this OrderLine.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def discounted_amount(self):
        """Gets the discounted_amount of this OrderLine.  # noqa: E501

        Order line amount after potential discount has been deducted  # noqa: E501

        :return: The discounted_amount of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._discounted_amount

    @discounted_amount.setter
    def discounted_amount(self, discounted_amount):
        """Sets the discounted_amount of this OrderLine.

        Order line amount after potential discount has been deducted  # noqa: E501

        :param discounted_amount: The discounted_amount of this OrderLine.  # noqa: E501
        :type: int
        """

        self._discounted_amount = discounted_amount

    @property
    def amount_vat(self):
        """Gets the amount_vat of this OrderLine.  # noqa: E501

        Order line total vat amount  # noqa: E501

        :return: The amount_vat of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._amount_vat

    @amount_vat.setter
    def amount_vat(self, amount_vat):
        """Sets the amount_vat of this OrderLine.

        Order line total vat amount  # noqa: E501

        :param amount_vat: The amount_vat of this OrderLine.  # noqa: E501
        :type: int
        """
        if amount_vat is None:
            raise ValueError("Invalid value for `amount_vat`, must not be `None`")  # noqa: E501

        self._amount_vat = amount_vat

    @property
    def amount_ex_vat(self):
        """Gets the amount_ex_vat of this OrderLine.  # noqa: E501

        Order line total amount without vat  # noqa: E501

        :return: The amount_ex_vat of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._amount_ex_vat

    @amount_ex_vat.setter
    def amount_ex_vat(self, amount_ex_vat):
        """Sets the amount_ex_vat of this OrderLine.

        Order line total amount without vat  # noqa: E501

        :param amount_ex_vat: The amount_ex_vat of this OrderLine.  # noqa: E501
        :type: int
        """
        if amount_ex_vat is None:
            raise ValueError("Invalid value for `amount_ex_vat`, must not be `None`")  # noqa: E501

        self._amount_ex_vat = amount_ex_vat

    @property
    def unit_amount(self):
        """Gets the unit_amount of this OrderLine.  # noqa: E501

        Order line unit amount including vat  # noqa: E501

        :return: The unit_amount of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, unit_amount):
        """Sets the unit_amount of this OrderLine.

        Order line unit amount including vat  # noqa: E501

        :param unit_amount: The unit_amount of this OrderLine.  # noqa: E501
        :type: int
        """
        if unit_amount is None:
            raise ValueError("Invalid value for `unit_amount`, must not be `None`")  # noqa: E501

        self._unit_amount = unit_amount

    @property
    def unit_amount_vat(self):
        """Gets the unit_amount_vat of this OrderLine.  # noqa: E501

        Order line unit vat amount  # noqa: E501

        :return: The unit_amount_vat of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._unit_amount_vat

    @unit_amount_vat.setter
    def unit_amount_vat(self, unit_amount_vat):
        """Sets the unit_amount_vat of this OrderLine.

        Order line unit vat amount  # noqa: E501

        :param unit_amount_vat: The unit_amount_vat of this OrderLine.  # noqa: E501
        :type: int
        """
        if unit_amount_vat is None:
            raise ValueError("Invalid value for `unit_amount_vat`, must not be `None`")  # noqa: E501

        self._unit_amount_vat = unit_amount_vat

    @property
    def unit_amount_ex_vat(self):
        """Gets the unit_amount_ex_vat of this OrderLine.  # noqa: E501

        Order line unit amount without vat  # noqa: E501

        :return: The unit_amount_ex_vat of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._unit_amount_ex_vat

    @unit_amount_ex_vat.setter
    def unit_amount_ex_vat(self, unit_amount_ex_vat):
        """Sets the unit_amount_ex_vat of this OrderLine.

        Order line unit amount without vat  # noqa: E501

        :param unit_amount_ex_vat: The unit_amount_ex_vat of this OrderLine.  # noqa: E501
        :type: int
        """
        if unit_amount_ex_vat is None:
            raise ValueError("Invalid value for `unit_amount_ex_vat`, must not be `None`")  # noqa: E501

        self._unit_amount_ex_vat = unit_amount_ex_vat

    @property
    def amount_defined_incl_vat(self):
        """Gets the amount_defined_incl_vat of this OrderLine.  # noqa: E501

        Whether the amount was defined including VAT. E.g. plan amount defined including VAT.  # noqa: E501

        :return: The amount_defined_incl_vat of this OrderLine.  # noqa: E501
        :rtype: bool
        """
        return self._amount_defined_incl_vat

    @amount_defined_incl_vat.setter
    def amount_defined_incl_vat(self, amount_defined_incl_vat):
        """Sets the amount_defined_incl_vat of this OrderLine.

        Whether the amount was defined including VAT. E.g. plan amount defined including VAT.  # noqa: E501

        :param amount_defined_incl_vat: The amount_defined_incl_vat of this OrderLine.  # noqa: E501
        :type: bool
        """
        if amount_defined_incl_vat is None:
            raise ValueError("Invalid value for `amount_defined_incl_vat`, must not be `None`")  # noqa: E501

        self._amount_defined_incl_vat = amount_defined_incl_vat

    @property
    def origin_handle(self):
        """Gets the origin_handle of this OrderLine.  # noqa: E501

        Handle for additional cost, credit, plan or subscription discount in the case one of those are the origin  # noqa: E501

        :return: The origin_handle of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._origin_handle

    @origin_handle.setter
    def origin_handle(self, origin_handle):
        """Sets the origin_handle of this OrderLine.

        Handle for additional cost, credit, plan or subscription discount in the case one of those are the origin  # noqa: E501

        :param origin_handle: The origin_handle of this OrderLine.  # noqa: E501
        :type: str
        """

        self._origin_handle = origin_handle

    @property
    def period_from(self):
        """Gets the period_from of this OrderLine.  # noqa: E501

        The start of billing period if the order line is a plan order line for a specific billing period, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :return: The period_from of this OrderLine.  # noqa: E501
        :rtype: datetime
        """
        return self._period_from

    @period_from.setter
    def period_from(self, period_from):
        """Sets the period_from of this OrderLine.

        The start of billing period if the order line is a plan order line for a specific billing period, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :param period_from: The period_from of this OrderLine.  # noqa: E501
        :type: datetime
        """

        self._period_from = period_from

    @property
    def period_to(self):
        """Gets the period_to of this OrderLine.  # noqa: E501

        The end of billing period if the order line is a plan order line for a specific billing period, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :return: The period_to of this OrderLine.  # noqa: E501
        :rtype: datetime
        """
        return self._period_to

    @period_to.setter
    def period_to(self, period_to):
        """Sets the period_to of this OrderLine.

        The end of billing period if the order line is a plan order line for a specific billing period, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :param period_to: The period_to of this OrderLine.  # noqa: E501
        :type: datetime
        """

        self._period_to = period_to

    @property
    def discount_percentage(self):
        """Gets the discount_percentage of this OrderLine.  # noqa: E501

        The discount percentage for discount order lines that has a percentage discount  # noqa: E501

        :return: The discount_percentage of this OrderLine.  # noqa: E501
        :rtype: int
        """
        return self._discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, discount_percentage):
        """Sets the discount_percentage of this OrderLine.

        The discount percentage for discount order lines that has a percentage discount  # noqa: E501

        :param discount_percentage: The discount_percentage of this OrderLine.  # noqa: E501
        :type: int
        """

        self._discount_percentage = discount_percentage

    @property
    def discounted_order_line(self):
        """Gets the discounted_order_line of this OrderLine.  # noqa: E501

        For discount order lines a reference to the order line for which the order line is a discount  # noqa: E501

        :return: The discounted_order_line of this OrderLine.  # noqa: E501
        :rtype: str
        """
        return self._discounted_order_line

    @discounted_order_line.setter
    def discounted_order_line(self, discounted_order_line):
        """Sets the discounted_order_line of this OrderLine.

        For discount order lines a reference to the order line for which the order line is a discount  # noqa: E501

        :param discounted_order_line: The discounted_order_line of this OrderLine.  # noqa: E501
        :type: str
        """

        self._discounted_order_line = discounted_order_line

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
        if issubclass(OrderLine, dict):
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
        if not isinstance(other, OrderLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
