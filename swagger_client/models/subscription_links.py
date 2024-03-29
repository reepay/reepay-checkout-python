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


class SubscriptionLinks(object):
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
        'payment_info': 'str'
    }

    attribute_map = {
        'payment_info': 'payment_info'
    }

    def __init__(self, payment_info=None):  # noqa: E501
        """SubscriptionLinks - a model defined in Swagger"""  # noqa: E501

        self._payment_info = None
        self.discriminator = None

        self.payment_info = payment_info

    @property
    def payment_info(self):
        """Gets the payment_info of this SubscriptionLinks.  # noqa: E501

        Hosted page for setting payment information on subscription  # noqa: E501

        :return: The payment_info of this SubscriptionLinks.  # noqa: E501
        :rtype: str
        """
        return self._payment_info

    @payment_info.setter
    def payment_info(self, payment_info):
        """Sets the payment_info of this SubscriptionLinks.

        Hosted page for setting payment information on subscription  # noqa: E501

        :param payment_info: The payment_info of this SubscriptionLinks.  # noqa: E501
        :type: str
        """
        if payment_info is None:
            raise ValueError("Invalid value for `payment_info`, must not be `None`")  # noqa: E501

        self._payment_info = payment_info

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
        if issubclass(SubscriptionLinks, dict):
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
        if not isinstance(other, SubscriptionLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
