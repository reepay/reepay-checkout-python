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


class AddOn(object):
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
        'amount': 'int',
        'vat': 'float',
        'handle': 'str',
        'type': 'str',
        'state': 'str',
        'deleted': 'datetime',
        'created': 'datetime',
        'amount_incl_vat': 'bool',
        'all_plans': 'bool',
        'eligible_plans': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'amount': 'amount',
        'vat': 'vat',
        'handle': 'handle',
        'type': 'type',
        'state': 'state',
        'deleted': 'deleted',
        'created': 'created',
        'amount_incl_vat': 'amount_incl_vat',
        'all_plans': 'all_plans',
        'eligible_plans': 'eligible_plans'
    }

    def __init__(self, name=None, description=None, amount=None, vat=None, handle=None, type=None, state=None, deleted=None, created=None, amount_incl_vat=None, all_plans=None, eligible_plans=None):  # noqa: E501
        """AddOn - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._amount = None
        self._vat = None
        self._handle = None
        self._type = None
        self._state = None
        self._deleted = None
        self._created = None
        self._amount_incl_vat = None
        self._all_plans = None
        self._eligible_plans = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.amount = amount
        if vat is not None:
            self.vat = vat
        self.handle = handle
        self.type = type
        self.state = state
        if deleted is not None:
            self.deleted = deleted
        self.created = created
        if amount_incl_vat is not None:
            self.amount_incl_vat = amount_incl_vat
        if all_plans is not None:
            self.all_plans = all_plans
        if eligible_plans is not None:
            self.eligible_plans = eligible_plans

    @property
    def name(self):
        """Gets the name of this AddOn.  # noqa: E501

        Name of add-on. Will be used as order line text.  # noqa: E501

        :return: The name of this AddOn.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddOn.

        Name of add-on. Will be used as order line text.  # noqa: E501

        :param name: The name of this AddOn.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this AddOn.  # noqa: E501

        Optional description of add-on  # noqa: E501

        :return: The description of this AddOn.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddOn.

        Optional description of add-on  # noqa: E501

        :param description: The description of this AddOn.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def amount(self):
        """Gets the amount of this AddOn.  # noqa: E501

        Add-on amount  # noqa: E501

        :return: The amount of this AddOn.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AddOn.

        Add-on amount  # noqa: E501

        :param amount: The amount of this AddOn.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if amount is not None and amount < 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0`")  # noqa: E501

        self._amount = amount

    @property
    def vat(self):
        """Gets the vat of this AddOn.  # noqa: E501

        Optional vat for add-on. Account default is used if none given.  # noqa: E501

        :return: The vat of this AddOn.  # noqa: E501
        :rtype: float
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this AddOn.

        Optional vat for add-on. Account default is used if none given.  # noqa: E501

        :param vat: The vat of this AddOn.  # noqa: E501
        :type: float
        """
        if vat is not None and vat > 1:  # noqa: E501
            raise ValueError("Invalid value for `vat`, must be a value less than or equal to `1`")  # noqa: E501
        if vat is not None and vat < 0:  # noqa: E501
            raise ValueError("Invalid value for `vat`, must be a value greater than or equal to `0`")  # noqa: E501

        self._vat = vat

    @property
    def handle(self):
        """Gets the handle of this AddOn.  # noqa: E501

        Per account unique handle for the add-on  # noqa: E501

        :return: The handle of this AddOn.  # noqa: E501
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this AddOn.

        Per account unique handle for the add-on  # noqa: E501

        :param handle: The handle of this AddOn.  # noqa: E501
        :type: str
        """
        if handle is None:
            raise ValueError("Invalid value for `handle`, must not be `None`")  # noqa: E501

        self._handle = handle

    @property
    def type(self):
        """Gets the type of this AddOn.  # noqa: E501

        Add-on type `on_off` or `quantity`. An `on_off` type cannot be given a quantity when attached to subscription. For `quantity` type it is possible.  # noqa: E501

        :return: The type of this AddOn.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddOn.

        Add-on type `on_off` or `quantity`. An `on_off` type cannot be given a quantity when attached to subscription. For `quantity` type it is possible.  # noqa: E501

        :param type: The type of this AddOn.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["on_off", "quantity"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def state(self):
        """Gets the state of this AddOn.  # noqa: E501

        Add-on state `active` or `deleted`.  # noqa: E501

        :return: The state of this AddOn.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AddOn.

        Add-on state `active` or `deleted`.  # noqa: E501

        :param state: The state of this AddOn.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["active", "deleted"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def deleted(self):
        """Gets the deleted of this AddOn.  # noqa: E501

        Date when the add-on was deleted if deleted. In ISO-8601 extended offset date-time format.  # noqa: E501

        :return: The deleted of this AddOn.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this AddOn.

        Date when the add-on was deleted if deleted. In ISO-8601 extended offset date-time format.  # noqa: E501

        :param deleted: The deleted of this AddOn.  # noqa: E501
        :type: datetime
        """

        self._deleted = deleted

    @property
    def created(self):
        """Gets the created of this AddOn.  # noqa: E501

        Date when the add-on was created. In ISO-8601 extended offset date-time format.  # noqa: E501

        :return: The created of this AddOn.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AddOn.

        Date when the add-on was created. In ISO-8601 extended offset date-time format.  # noqa: E501

        :param created: The created of this AddOn.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def amount_incl_vat(self):
        """Gets the amount_incl_vat of this AddOn.  # noqa: E501

        Whether the amount is including VAT. Default true.  # noqa: E501

        :return: The amount_incl_vat of this AddOn.  # noqa: E501
        :rtype: bool
        """
        return self._amount_incl_vat

    @amount_incl_vat.setter
    def amount_incl_vat(self, amount_incl_vat):
        """Sets the amount_incl_vat of this AddOn.

        Whether the amount is including VAT. Default true.  # noqa: E501

        :param amount_incl_vat: The amount_incl_vat of this AddOn.  # noqa: E501
        :type: bool
        """

        self._amount_incl_vat = amount_incl_vat

    @property
    def all_plans(self):
        """Gets the all_plans of this AddOn.  # noqa: E501

        Whether all plans are eligible for this add-on. Defaults to false.  # noqa: E501

        :return: The all_plans of this AddOn.  # noqa: E501
        :rtype: bool
        """
        return self._all_plans

    @all_plans.setter
    def all_plans(self, all_plans):
        """Sets the all_plans of this AddOn.

        Whether all plans are eligible for this add-on. Defaults to false.  # noqa: E501

        :param all_plans: The all_plans of this AddOn.  # noqa: E501
        :type: bool
        """

        self._all_plans = all_plans

    @property
    def eligible_plans(self):
        """Gets the eligible_plans of this AddOn.  # noqa: E501

        If not `all_plans` are set to true, then the set of eligible plan handles must be defined.  # noqa: E501

        :return: The eligible_plans of this AddOn.  # noqa: E501
        :rtype: list[str]
        """
        return self._eligible_plans

    @eligible_plans.setter
    def eligible_plans(self, eligible_plans):
        """Sets the eligible_plans of this AddOn.

        If not `all_plans` are set to true, then the set of eligible plan handles must be defined.  # noqa: E501

        :param eligible_plans: The eligible_plans of this AddOn.  # noqa: E501
        :type: list[str]
        """

        self._eligible_plans = eligible_plans

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
        if issubclass(AddOn, dict):
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
        if not isinstance(other, AddOn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
