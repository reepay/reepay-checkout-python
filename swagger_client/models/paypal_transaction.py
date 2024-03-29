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


class PaypalTransaction(object):
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
        'error': 'str',
        'ref_transaction': 'str',
        'paypal_id': 'str',
        'error_state': 'str',
        'acquirer_message': 'str'
    }

    attribute_map = {
        'error': 'error',
        'ref_transaction': 'ref_transaction',
        'paypal_id': 'paypal_id',
        'error_state': 'error_state',
        'acquirer_message': 'acquirer_message'
    }

    def __init__(self, error=None, ref_transaction=None, paypal_id=None, error_state=None, acquirer_message=None):  # noqa: E501
        """PaypalTransaction - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._ref_transaction = None
        self._paypal_id = None
        self._error_state = None
        self._acquirer_message = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if ref_transaction is not None:
            self.ref_transaction = ref_transaction
        if paypal_id is not None:
            self.paypal_id = paypal_id
        if error_state is not None:
            self.error_state = error_state
        if acquirer_message is not None:
            self.acquirer_message = acquirer_message

    @property
    def error(self):
        """Gets the error of this PaypalTransaction.  # noqa: E501

        Error code if failed. See [transaction errors](https://reference.reepay.com/api/#transaction-errors).  # noqa: E501

        :return: The error of this PaypalTransaction.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PaypalTransaction.

        Error code if failed. See [transaction errors](https://reference.reepay.com/api/#transaction-errors).  # noqa: E501

        :param error: The error of this PaypalTransaction.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def ref_transaction(self):
        """Gets the ref_transaction of this PaypalTransaction.  # noqa: E501

        Id of a possible referenced transaction  # noqa: E501

        :return: The ref_transaction of this PaypalTransaction.  # noqa: E501
        :rtype: str
        """
        return self._ref_transaction

    @ref_transaction.setter
    def ref_transaction(self, ref_transaction):
        """Sets the ref_transaction of this PaypalTransaction.

        Id of a possible referenced transaction  # noqa: E501

        :param ref_transaction: The ref_transaction of this PaypalTransaction.  # noqa: E501
        :type: str
        """

        self._ref_transaction = ref_transaction

    @property
    def paypal_id(self):
        """Gets the paypal_id of this PaypalTransaction.  # noqa: E501

        PayPal id  # noqa: E501

        :return: The paypal_id of this PaypalTransaction.  # noqa: E501
        :rtype: str
        """
        return self._paypal_id

    @paypal_id.setter
    def paypal_id(self, paypal_id):
        """Sets the paypal_id of this PaypalTransaction.

        PayPal id  # noqa: E501

        :param paypal_id: The paypal_id of this PaypalTransaction.  # noqa: E501
        :type: str
        """

        self._paypal_id = paypal_id

    @property
    def error_state(self):
        """Gets the error_state of this PaypalTransaction.  # noqa: E501

        Error state if failed: `pending`, `soft_declined`, `hard_declined` or `processing_error`  # noqa: E501

        :return: The error_state of this PaypalTransaction.  # noqa: E501
        :rtype: str
        """
        return self._error_state

    @error_state.setter
    def error_state(self, error_state):
        """Sets the error_state of this PaypalTransaction.

        Error state if failed: `pending`, `soft_declined`, `hard_declined` or `processing_error`  # noqa: E501

        :param error_state: The error_state of this PaypalTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "soft_declined", "hard_declined", "processing_error"]  # noqa: E501
        if error_state not in allowed_values:
            raise ValueError(
                "Invalid value for `error_state` ({0}), must be one of {1}"  # noqa: E501
                .format(error_state, allowed_values)
            )

        self._error_state = error_state

    @property
    def acquirer_message(self):
        """Gets the acquirer_message of this PaypalTransaction.  # noqa: E501

        Acquirer message in case of error  # noqa: E501

        :return: The acquirer_message of this PaypalTransaction.  # noqa: E501
        :rtype: str
        """
        return self._acquirer_message

    @acquirer_message.setter
    def acquirer_message(self, acquirer_message):
        """Sets the acquirer_message of this PaypalTransaction.

        Acquirer message in case of error  # noqa: E501

        :param acquirer_message: The acquirer_message of this PaypalTransaction.  # noqa: E501
        :type: str
        """

        self._acquirer_message = acquirer_message

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
        if issubclass(PaypalTransaction, dict):
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
        if not isinstance(other, PaypalTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
