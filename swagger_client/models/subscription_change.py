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


class SubscriptionChange(object):
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
        'plan': 'str',
        'amount': 'int',
        'quantity': 'int',
        'pending': 'bool',
        'applied': 'datetime',
        'updated': 'datetime',
        'created': 'datetime',
        'amount_incl_vat': 'bool',
        'subscription_add_ons': 'list[SubscriptionAddOn]',
        'remove_add_ons': 'list[str]'
    }

    attribute_map = {
        'plan': 'plan',
        'amount': 'amount',
        'quantity': 'quantity',
        'pending': 'pending',
        'applied': 'applied',
        'updated': 'updated',
        'created': 'created',
        'amount_incl_vat': 'amount_incl_vat',
        'subscription_add_ons': 'subscription_add_ons',
        'remove_add_ons': 'remove_add_ons'
    }

    def __init__(self, plan=None, amount=None, quantity=None, pending=None, applied=None, updated=None, created=None, amount_incl_vat=None, subscription_add_ons=None, remove_add_ons=None):  # noqa: E501
        """SubscriptionChange - a model defined in Swagger"""  # noqa: E501

        self._plan = None
        self._amount = None
        self._quantity = None
        self._pending = None
        self._applied = None
        self._updated = None
        self._created = None
        self._amount_incl_vat = None
        self._subscription_add_ons = None
        self._remove_add_ons = None
        self.discriminator = None

        if plan is not None:
            self.plan = plan
        if amount is not None:
            self.amount = amount
        if quantity is not None:
            self.quantity = quantity
        self.pending = pending
        if applied is not None:
            self.applied = applied
        if updated is not None:
            self.updated = updated
        self.created = created
        if amount_incl_vat is not None:
            self.amount_incl_vat = amount_incl_vat
        if subscription_add_ons is not None:
            self.subscription_add_ons = subscription_add_ons
        if remove_add_ons is not None:
            self.remove_add_ons = remove_add_ons

    @property
    def plan(self):
        """Gets the plan of this SubscriptionChange.  # noqa: E501

        The handle of the plan to change to  # noqa: E501

        :return: The plan of this SubscriptionChange.  # noqa: E501
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this SubscriptionChange.

        The handle of the plan to change to  # noqa: E501

        :param plan: The plan of this SubscriptionChange.  # noqa: E501
        :type: str
        """

        self._plan = plan

    @property
    def amount(self):
        """Gets the amount of this SubscriptionChange.  # noqa: E501

        Optional custom per quantity plan price. If provided the plan price billed for each billing period will be overridden by this price.  # noqa: E501

        :return: The amount of this SubscriptionChange.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SubscriptionChange.

        Optional custom per quantity plan price. If provided the plan price billed for each billing period will be overridden by this price.  # noqa: E501

        :param amount: The amount of this SubscriptionChange.  # noqa: E501
        :type: int
        """
        if amount is not None and amount < 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0`")  # noqa: E501

        self._amount = amount

    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionChange.  # noqa: E501

        Optional quantity of the plan product for this subscription. If not provided the default is the default plan quantity defined for the plan.  # noqa: E501

        :return: The quantity of this SubscriptionChange.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionChange.

        Optional quantity of the plan product for this subscription. If not provided the default is the default plan quantity defined for the plan.  # noqa: E501

        :param quantity: The quantity of this SubscriptionChange.  # noqa: E501
        :type: int
        """
        if quantity is not None and quantity < 1:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")  # noqa: E501

        self._quantity = quantity

    @property
    def pending(self):
        """Gets the pending of this SubscriptionChange.  # noqa: E501

        Whether this is a pending change at next renewal, or it has been applied  # noqa: E501

        :return: The pending of this SubscriptionChange.  # noqa: E501
        :rtype: bool
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this SubscriptionChange.

        Whether this is a pending change at next renewal, or it has been applied  # noqa: E501

        :param pending: The pending of this SubscriptionChange.  # noqa: E501
        :type: bool
        """
        if pending is None:
            raise ValueError("Invalid value for `pending`, must not be `None`")  # noqa: E501

        self._pending = pending

    @property
    def applied(self):
        """Gets the applied of this SubscriptionChange.  # noqa: E501

        If defined the change was applied on this date and time  # noqa: E501

        :return: The applied of this SubscriptionChange.  # noqa: E501
        :rtype: datetime
        """
        return self._applied

    @applied.setter
    def applied(self, applied):
        """Sets the applied of this SubscriptionChange.

        If defined the change was applied on this date and time  # noqa: E501

        :param applied: The applied of this SubscriptionChange.  # noqa: E501
        :type: datetime
        """

        self._applied = applied

    @property
    def updated(self):
        """Gets the updated of this SubscriptionChange.  # noqa: E501

        Date and time of update of pending change  # noqa: E501

        :return: The updated of this SubscriptionChange.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this SubscriptionChange.

        Date and time of update of pending change  # noqa: E501

        :param updated: The updated of this SubscriptionChange.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this SubscriptionChange.  # noqa: E501

        Date when the change was created. In [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :return: The created of this SubscriptionChange.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SubscriptionChange.

        Date when the change was created. In [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :param created: The created of this SubscriptionChange.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def amount_incl_vat(self):
        """Gets the amount_incl_vat of this SubscriptionChange.  # noqa: E501

        Whether the optional amount is including VAT. Defaults to true.  # noqa: E501

        :return: The amount_incl_vat of this SubscriptionChange.  # noqa: E501
        :rtype: bool
        """
        return self._amount_incl_vat

    @amount_incl_vat.setter
    def amount_incl_vat(self, amount_incl_vat):
        """Sets the amount_incl_vat of this SubscriptionChange.

        Whether the optional amount is including VAT. Defaults to true.  # noqa: E501

        :param amount_incl_vat: The amount_incl_vat of this SubscriptionChange.  # noqa: E501
        :type: bool
        """

        self._amount_incl_vat = amount_incl_vat

    @property
    def subscription_add_ons(self):
        """Gets the subscription_add_ons of this SubscriptionChange.  # noqa: E501

        List of subscription add-ons to create in change  # noqa: E501

        :return: The subscription_add_ons of this SubscriptionChange.  # noqa: E501
        :rtype: list[SubscriptionAddOn]
        """
        return self._subscription_add_ons

    @subscription_add_ons.setter
    def subscription_add_ons(self, subscription_add_ons):
        """Sets the subscription_add_ons of this SubscriptionChange.

        List of subscription add-ons to create in change  # noqa: E501

        :param subscription_add_ons: The subscription_add_ons of this SubscriptionChange.  # noqa: E501
        :type: list[SubscriptionAddOn]
        """

        self._subscription_add_ons = subscription_add_ons

    @property
    def remove_add_ons(self):
        """Gets the remove_add_ons of this SubscriptionChange.  # noqa: E501

        Subscription add-ons to remove from subscription by subscription add-on handle  # noqa: E501

        :return: The remove_add_ons of this SubscriptionChange.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_add_ons

    @remove_add_ons.setter
    def remove_add_ons(self, remove_add_ons):
        """Sets the remove_add_ons of this SubscriptionChange.

        Subscription add-ons to remove from subscription by subscription add-on handle  # noqa: E501

        :param remove_add_ons: The remove_add_ons of this SubscriptionChange.  # noqa: E501
        :type: list[str]
        """

        self._remove_add_ons = remove_add_ons

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
        if issubclass(SubscriptionChange, dict):
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
        if not isinstance(other, SubscriptionChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other