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


class CardTransaction(object):
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
        'card': 'Card',
        'error': 'str',
        'fingerprint': 'str',
        'provider': 'str',
        'ref_transaction': 'str',
        'gw_id': 'str',
        'last_failed': 'datetime',
        'first_failed': 'datetime',
        'error_state': 'str',
        'card_type': 'str',
        'exp_date': 'str',
        'masked_card': 'str',
        'strong_authentication_status': 'str',
        'acquirer_code': 'str',
        'acquirer_message': 'str',
        'acquirer_reference': 'str',
        'text_on_statement': 'str'
    }

    attribute_map = {
        'card': 'card',
        'error': 'error',
        'fingerprint': 'fingerprint',
        'provider': 'provider',
        'ref_transaction': 'ref_transaction',
        'gw_id': 'gw_id',
        'last_failed': 'last_failed',
        'first_failed': 'first_failed',
        'error_state': 'error_state',
        'card_type': 'card_type',
        'exp_date': 'exp_date',
        'masked_card': 'masked_card',
        'strong_authentication_status': 'strong_authentication_status',
        'acquirer_code': 'acquirer_code',
        'acquirer_message': 'acquirer_message',
        'acquirer_reference': 'acquirer_reference',
        'text_on_statement': 'text_on_statement'
    }

    def __init__(self, card=None, error=None, fingerprint=None, provider=None, ref_transaction=None, gw_id=None, last_failed=None, first_failed=None, error_state=None, card_type=None, exp_date=None, masked_card=None, strong_authentication_status=None, acquirer_code=None, acquirer_message=None, acquirer_reference=None, text_on_statement=None):  # noqa: E501
        """CardTransaction - a model defined in Swagger"""  # noqa: E501

        self._card = None
        self._error = None
        self._fingerprint = None
        self._provider = None
        self._ref_transaction = None
        self._gw_id = None
        self._last_failed = None
        self._first_failed = None
        self._error_state = None
        self._card_type = None
        self._exp_date = None
        self._masked_card = None
        self._strong_authentication_status = None
        self._acquirer_code = None
        self._acquirer_message = None
        self._acquirer_reference = None
        self._text_on_statement = None
        self.discriminator = None

        if card is not None:
            self.card = card
        if error is not None:
            self.error = error
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if provider is not None:
            self.provider = provider
        if ref_transaction is not None:
            self.ref_transaction = ref_transaction
        if gw_id is not None:
            self.gw_id = gw_id
        if last_failed is not None:
            self.last_failed = last_failed
        if first_failed is not None:
            self.first_failed = first_failed
        if error_state is not None:
            self.error_state = error_state
        self.card_type = card_type
        if exp_date is not None:
            self.exp_date = exp_date
        if masked_card is not None:
            self.masked_card = masked_card
        if strong_authentication_status is not None:
            self.strong_authentication_status = strong_authentication_status
        if acquirer_code is not None:
            self.acquirer_code = acquirer_code
        if acquirer_message is not None:
            self.acquirer_message = acquirer_message
        if acquirer_reference is not None:
            self.acquirer_reference = acquirer_reference
        if text_on_statement is not None:
            self.text_on_statement = text_on_statement

    @property
    def card(self):
        """Gets the card of this CardTransaction.  # noqa: E501

        Saved card used for transaction. Only present if a saved card was used.  # noqa: E501

        :return: The card of this CardTransaction.  # noqa: E501
        :rtype: Card
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this CardTransaction.

        Saved card used for transaction. Only present if a saved card was used.  # noqa: E501

        :param card: The card of this CardTransaction.  # noqa: E501
        :type: Card
        """

        self._card = card

    @property
    def error(self):
        """Gets the error of this CardTransaction.  # noqa: E501

        Error code if failed. See [transaction errors](https://reference.reepay.com/api/#transaction-errors).  # noqa: E501

        :return: The error of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CardTransaction.

        Error code if failed. See [transaction errors](https://reference.reepay.com/api/#transaction-errors).  # noqa: E501

        :param error: The error of this CardTransaction.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def fingerprint(self):
        """Gets the fingerprint of this CardTransaction.  # noqa: E501

        Uniquely identifies this particular card number  # noqa: E501

        :return: The fingerprint of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this CardTransaction.

        Uniquely identifies this particular card number  # noqa: E501

        :param fingerprint: The fingerprint of this CardTransaction.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def provider(self):
        """Gets the provider of this CardTransaction.  # noqa: E501

        Acquirer or payment gateway used: `reepay`, `clearhaus`, `nets`, `dibs`, `stripe`, `quickpay`, `epay`, `test`  # noqa: E501

        :return: The provider of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CardTransaction.

        Acquirer or payment gateway used: `reepay`, `clearhaus`, `nets`, `dibs`, `stripe`, `quickpay`, `epay`, `test`  # noqa: E501

        :param provider: The provider of this CardTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["reepay", "clearhaus", "nets", "dibs", "stripe", "quickpay", "epay", "test"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def ref_transaction(self):
        """Gets the ref_transaction of this CardTransaction.  # noqa: E501

        Id of a possible referenced transaction  # noqa: E501

        :return: The ref_transaction of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._ref_transaction

    @ref_transaction.setter
    def ref_transaction(self, ref_transaction):
        """Sets the ref_transaction of this CardTransaction.

        Id of a possible referenced transaction  # noqa: E501

        :param ref_transaction: The ref_transaction of this CardTransaction.  # noqa: E501
        :type: str
        """

        self._ref_transaction = ref_transaction

    @property
    def gw_id(self):
        """Gets the gw_id of this CardTransaction.  # noqa: E501

        Gateway id for card  # noqa: E501

        :return: The gw_id of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._gw_id

    @gw_id.setter
    def gw_id(self, gw_id):
        """Sets the gw_id of this CardTransaction.

        Gateway id for card  # noqa: E501

        :param gw_id: The gw_id of this CardTransaction.  # noqa: E501
        :type: str
        """

        self._gw_id = gw_id

    @property
    def last_failed(self):
        """Gets the last_failed of this CardTransaction.  # noqa: E501

        When the card transaction last failed, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :return: The last_failed of this CardTransaction.  # noqa: E501
        :rtype: datetime
        """
        return self._last_failed

    @last_failed.setter
    def last_failed(self, last_failed):
        """Sets the last_failed of this CardTransaction.

        When the card transaction last failed, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :param last_failed: The last_failed of this CardTransaction.  # noqa: E501
        :type: datetime
        """

        self._last_failed = last_failed

    @property
    def first_failed(self):
        """Gets the first_failed of this CardTransaction.  # noqa: E501

        When the card transaction first failed, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :return: The first_failed of this CardTransaction.  # noqa: E501
        :rtype: datetime
        """
        return self._first_failed

    @first_failed.setter
    def first_failed(self, first_failed):
        """Sets the first_failed of this CardTransaction.

        When the card transaction first failed, in [ISO-8601](http://en.wikipedia.org/wiki/ISO_8601) extended offset date-time format.  # noqa: E501

        :param first_failed: The first_failed of this CardTransaction.  # noqa: E501
        :type: datetime
        """

        self._first_failed = first_failed

    @property
    def error_state(self):
        """Gets the error_state of this CardTransaction.  # noqa: E501

        Error state if failed: `pending`, `soft_declined`, `hard_declined` or `processing_error`  # noqa: E501

        :return: The error_state of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._error_state

    @error_state.setter
    def error_state(self, error_state):
        """Sets the error_state of this CardTransaction.

        Error state if failed: `pending`, `soft_declined`, `hard_declined` or `processing_error`  # noqa: E501

        :param error_state: The error_state of this CardTransaction.  # noqa: E501
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
    def card_type(self):
        """Gets the card_type of this CardTransaction.  # noqa: E501

        Card type: `unknown`, `visa`, `mc`, `dankort`, `visa_dk`, `ffk`, `visa_elec`, `maestro`, `laser`, `amex`, `diners`, `discover` or `jcb`  # noqa: E501

        :return: The card_type of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this CardTransaction.

        Card type: `unknown`, `visa`, `mc`, `dankort`, `visa_dk`, `ffk`, `visa_elec`, `maestro`, `laser`, `amex`, `diners`, `discover` or `jcb`  # noqa: E501

        :param card_type: The card_type of this CardTransaction.  # noqa: E501
        :type: str
        """
        if card_type is None:
            raise ValueError("Invalid value for `card_type`, must not be `None`")  # noqa: E501
        allowed_values = ["unknown", "visa", "mc", "dankort", "visa_dk", "ffk", "visa_elec", "maestro", "laser", "amex", "diners", "discover", "jcb"]  # noqa: E501
        if card_type not in allowed_values:
            raise ValueError(
                "Invalid value for `card_type` ({0}), must be one of {1}"  # noqa: E501
                .format(card_type, allowed_values)
            )

        self._card_type = card_type

    @property
    def exp_date(self):
        """Gets the exp_date of this CardTransaction.  # noqa: E501

        Card expire date on form MM-YY   # noqa: E501

        :return: The exp_date of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._exp_date

    @exp_date.setter
    def exp_date(self, exp_date):
        """Sets the exp_date of this CardTransaction.

        Card expire date on form MM-YY   # noqa: E501

        :param exp_date: The exp_date of this CardTransaction.  # noqa: E501
        :type: str
        """

        self._exp_date = exp_date

    @property
    def masked_card(self):
        """Gets the masked_card of this CardTransaction.  # noqa: E501

        Masked card number  # noqa: E501

        :return: The masked_card of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._masked_card

    @masked_card.setter
    def masked_card(self, masked_card):
        """Sets the masked_card of this CardTransaction.

        Masked card number  # noqa: E501

        :param masked_card: The masked_card of this CardTransaction.  # noqa: E501
        :type: str
        """

        self._masked_card = masked_card

    @property
    def strong_authentication_status(self):
        """Gets the strong_authentication_status of this CardTransaction.  # noqa: E501

        Status for strong customer authentication  # noqa: E501

        :return: The strong_authentication_status of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._strong_authentication_status

    @strong_authentication_status.setter
    def strong_authentication_status(self, strong_authentication_status):
        """Sets the strong_authentication_status of this CardTransaction.

        Status for strong customer authentication  # noqa: E501

        :param strong_authentication_status: The strong_authentication_status of this CardTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["threed_secure", "threed_secure_not_enrolled", "threed_secure_local_only", "secured_by_nets"]  # noqa: E501
        if strong_authentication_status not in allowed_values:
            raise ValueError(
                "Invalid value for `strong_authentication_status` ({0}), must be one of {1}"  # noqa: E501
                .format(strong_authentication_status, allowed_values)
            )

        self._strong_authentication_status = strong_authentication_status

    @property
    def acquirer_code(self):
        """Gets the acquirer_code of this CardTransaction.  # noqa: E501

        Acquirer error code in case of error  # noqa: E501

        :return: The acquirer_code of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._acquirer_code

    @acquirer_code.setter
    def acquirer_code(self, acquirer_code):
        """Sets the acquirer_code of this CardTransaction.

        Acquirer error code in case of error  # noqa: E501

        :param acquirer_code: The acquirer_code of this CardTransaction.  # noqa: E501
        :type: str
        """

        self._acquirer_code = acquirer_code

    @property
    def acquirer_message(self):
        """Gets the acquirer_message of this CardTransaction.  # noqa: E501

        Acquirer message in case of error  # noqa: E501

        :return: The acquirer_message of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._acquirer_message

    @acquirer_message.setter
    def acquirer_message(self, acquirer_message):
        """Sets the acquirer_message of this CardTransaction.

        Acquirer message in case of error  # noqa: E501

        :param acquirer_message: The acquirer_message of this CardTransaction.  # noqa: E501
        :type: str
        """

        self._acquirer_message = acquirer_message

    @property
    def acquirer_reference(self):
        """Gets the acquirer_reference of this CardTransaction.  # noqa: E501

        Acquirer reference to transaction. E.g. Nets order id or Clearhaus reference.  # noqa: E501

        :return: The acquirer_reference of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._acquirer_reference

    @acquirer_reference.setter
    def acquirer_reference(self, acquirer_reference):
        """Sets the acquirer_reference of this CardTransaction.

        Acquirer reference to transaction. E.g. Nets order id or Clearhaus reference.  # noqa: E501

        :param acquirer_reference: The acquirer_reference of this CardTransaction.  # noqa: E501
        :type: str
        """

        self._acquirer_reference = acquirer_reference

    @property
    def text_on_statement(self):
        """Gets the text_on_statement of this CardTransaction.  # noqa: E501

        Resulting text on bank statement if known  # noqa: E501

        :return: The text_on_statement of this CardTransaction.  # noqa: E501
        :rtype: str
        """
        return self._text_on_statement

    @text_on_statement.setter
    def text_on_statement(self, text_on_statement):
        """Sets the text_on_statement of this CardTransaction.

        Resulting text on bank statement if known  # noqa: E501

        :param text_on_statement: The text_on_statement of this CardTransaction.  # noqa: E501
        :type: str
        """

        self._text_on_statement = text_on_statement

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
        if issubclass(CardTransaction, dict):
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
        if not isinstance(other, CardTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other