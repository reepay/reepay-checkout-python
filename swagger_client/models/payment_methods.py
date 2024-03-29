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


class PaymentMethods(object):
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
        'cards': 'list[Card]'
    }

    attribute_map = {
        'cards': 'cards'
    }

    def __init__(self, cards=None):  # noqa: E501
        """PaymentMethods - a model defined in Swagger"""  # noqa: E501

        self._cards = None
        self.discriminator = None

        if cards is not None:
            self.cards = cards

    @property
    def cards(self):
        """Gets the cards of this PaymentMethods.  # noqa: E501

        List of cards  # noqa: E501

        :return: The cards of this PaymentMethods.  # noqa: E501
        :rtype: list[Card]
        """
        return self._cards

    @cards.setter
    def cards(self, cards):
        """Sets the cards of this PaymentMethods.

        List of cards  # noqa: E501

        :param cards: The cards of this PaymentMethods.  # noqa: E501
        :type: list[Card]
        """

        self._cards = cards

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
        if issubclass(PaymentMethods, dict):
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
        if not isinstance(other, PaymentMethods):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
