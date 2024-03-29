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


class ChargeSource(object):
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
        'type': 'str',
        'card': 'str',
        'fingerprint': 'str',
        'provider': 'str',
        'auth_transaction': 'str',
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
        'type': 'type',
        'card': 'card',
        'fingerprint': 'fingerprint',
        'provider': 'provider',
        'auth_transaction': 'auth_transaction',
        'card_type': 'card_type',
        'exp_date': 'exp_date',
        'masked_card': 'masked_card',
        'strong_authentication_status': 'strong_authentication_status',
        'acquirer_code': 'acquirer_code',
        'acquirer_message': 'acquirer_message',
        'acquirer_reference': 'acquirer_reference',
        'text_on_statement': 'text_on_statement'
    }

    def __init__(self, type=None, card=None, fingerprint=None, provider=None, auth_transaction=None, card_type=None, exp_date=None, masked_card=None, strong_authentication_status=None, acquirer_code=None, acquirer_message=None, acquirer_reference=None, text_on_statement=None):  # noqa: E501
        """ChargeSource - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._card = None
        self._fingerprint = None
        self._provider = None
        self._auth_transaction = None
        self._card_type = None
        self._exp_date = None
        self._masked_card = None
        self._strong_authentication_status = None
        self._acquirer_code = None
        self._acquirer_message = None
        self._acquirer_reference = None
        self._text_on_statement = None
        self.discriminator = None

        self.type = type
        if card is not None:
            self.card = card
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if provider is not None:
            self.provider = provider
        if auth_transaction is not None:
            self.auth_transaction = auth_transaction
        if card_type is not None:
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
    def type(self):
        """Gets the type of this ChargeSource.  # noqa: E501

        Type of charge source: `card` - existing customer card, `card_token` - card token, `mpo` - MobilePay Online or `viabill`  # noqa: E501

        :return: The type of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChargeSource.

        Type of charge source: `card` - existing customer card, `card_token` - card token, `mpo` - MobilePay Online or `viabill`  # noqa: E501

        :param type: The type of this ChargeSource.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["card", "card_token", "mpo", "viabill"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def card(self):
        """Gets the card of this ChargeSource.  # noqa: E501

        Reference to customer card if source type `card`  # noqa: E501

        :return: The card of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this ChargeSource.

        Reference to customer card if source type `card`  # noqa: E501

        :param card: The card of this ChargeSource.  # noqa: E501
        :type: str
        """

        self._card = card

    @property
    def fingerprint(self):
        """Gets the fingerprint of this ChargeSource.  # noqa: E501

        Uniquely identifies this particular card number if credit card source  # noqa: E501

        :return: The fingerprint of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this ChargeSource.

        Uniquely identifies this particular card number if credit card source  # noqa: E501

        :param fingerprint: The fingerprint of this ChargeSource.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def provider(self):
        """Gets the provider of this ChargeSource.  # noqa: E501

        Card acquirer or card payment gateway used if card source: `reepay`, `clearhaus`, `nets`, `dibs`, `stripe`, `quickpay`, `epay`, `test`  # noqa: E501

        :return: The provider of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ChargeSource.

        Card acquirer or card payment gateway used if card source: `reepay`, `clearhaus`, `nets`, `dibs`, `stripe`, `quickpay`, `epay`, `test`  # noqa: E501

        :param provider: The provider of this ChargeSource.  # noqa: E501
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
    def auth_transaction(self):
        """Gets the auth_transaction of this ChargeSource.  # noqa: E501

        Reference to authorization transaction if charge is settled after authorization  # noqa: E501

        :return: The auth_transaction of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._auth_transaction

    @auth_transaction.setter
    def auth_transaction(self, auth_transaction):
        """Sets the auth_transaction of this ChargeSource.

        Reference to authorization transaction if charge is settled after authorization  # noqa: E501

        :param auth_transaction: The auth_transaction of this ChargeSource.  # noqa: E501
        :type: str
        """

        self._auth_transaction = auth_transaction

    @property
    def card_type(self):
        """Gets the card_type of this ChargeSource.  # noqa: E501

        Card type if credit card source: `unknown`, `visa`, `mc`, `dankort`, `visa_dk`, `ffk`, `visa_elec`, `maestro`, `laser`, `amex`, `diners`, `discover` or `jcb`  # noqa: E501

        :return: The card_type of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this ChargeSource.

        Card type if credit card source: `unknown`, `visa`, `mc`, `dankort`, `visa_dk`, `ffk`, `visa_elec`, `maestro`, `laser`, `amex`, `diners`, `discover` or `jcb`  # noqa: E501

        :param card_type: The card_type of this ChargeSource.  # noqa: E501
        :type: str
        """
        allowed_values = ["unknown", "visa", "mc", "dankort", "visa_dk", "ffk", "visa_elec", "maestro", "laser", "amex", "diners", "discover", "jcb"]  # noqa: E501
        if card_type not in allowed_values:
            raise ValueError(
                "Invalid value for `card_type` ({0}), must be one of {1}"  # noqa: E501
                .format(card_type, allowed_values)
            )

        self._card_type = card_type

    @property
    def exp_date(self):
        """Gets the exp_date of this ChargeSource.  # noqa: E501

        Card expire date on form MM-YY if credit card source  # noqa: E501

        :return: The exp_date of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._exp_date

    @exp_date.setter
    def exp_date(self, exp_date):
        """Sets the exp_date of this ChargeSource.

        Card expire date on form MM-YY if credit card source  # noqa: E501

        :param exp_date: The exp_date of this ChargeSource.  # noqa: E501
        :type: str
        """

        self._exp_date = exp_date

    @property
    def masked_card(self):
        """Gets the masked_card of this ChargeSource.  # noqa: E501

        Masked card number if credit card source  # noqa: E501

        :return: The masked_card of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._masked_card

    @masked_card.setter
    def masked_card(self, masked_card):
        """Sets the masked_card of this ChargeSource.

        Masked card number if credit card source  # noqa: E501

        :param masked_card: The masked_card of this ChargeSource.  # noqa: E501
        :type: str
        """

        self._masked_card = masked_card

    @property
    def strong_authentication_status(self):
        """Gets the strong_authentication_status of this ChargeSource.  # noqa: E501

        Status for strong customer authentication: `threed_secure`, `threed_secure_not_enrolled, `threed_secure_local_only`, `secured_by_nets`  # noqa: E501

        :return: The strong_authentication_status of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._strong_authentication_status

    @strong_authentication_status.setter
    def strong_authentication_status(self, strong_authentication_status):
        """Sets the strong_authentication_status of this ChargeSource.

        Status for strong customer authentication: `threed_secure`, `threed_secure_not_enrolled, `threed_secure_local_only`, `secured_by_nets`  # noqa: E501

        :param strong_authentication_status: The strong_authentication_status of this ChargeSource.  # noqa: E501
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
        """Gets the acquirer_code of this ChargeSource.  # noqa: E501

        Card acquirer error code in case of card error  # noqa: E501

        :return: The acquirer_code of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._acquirer_code

    @acquirer_code.setter
    def acquirer_code(self, acquirer_code):
        """Sets the acquirer_code of this ChargeSource.

        Card acquirer error code in case of card error  # noqa: E501

        :param acquirer_code: The acquirer_code of this ChargeSource.  # noqa: E501
        :type: str
        """

        self._acquirer_code = acquirer_code

    @property
    def acquirer_message(self):
        """Gets the acquirer_message of this ChargeSource.  # noqa: E501

        Card acquirer message in case of card error  # noqa: E501

        :return: The acquirer_message of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._acquirer_message

    @acquirer_message.setter
    def acquirer_message(self, acquirer_message):
        """Sets the acquirer_message of this ChargeSource.

        Card acquirer message in case of card error  # noqa: E501

        :param acquirer_message: The acquirer_message of this ChargeSource.  # noqa: E501
        :type: str
        """

        self._acquirer_message = acquirer_message

    @property
    def acquirer_reference(self):
        """Gets the acquirer_reference of this ChargeSource.  # noqa: E501

        Card acquirer reference to transaction in case of card source. E.g. Nets order id or Clearhaus reference.  # noqa: E501

        :return: The acquirer_reference of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._acquirer_reference

    @acquirer_reference.setter
    def acquirer_reference(self, acquirer_reference):
        """Sets the acquirer_reference of this ChargeSource.

        Card acquirer reference to transaction in case of card source. E.g. Nets order id or Clearhaus reference.  # noqa: E501

        :param acquirer_reference: The acquirer_reference of this ChargeSource.  # noqa: E501
        :type: str
        """

        self._acquirer_reference = acquirer_reference

    @property
    def text_on_statement(self):
        """Gets the text_on_statement of this ChargeSource.  # noqa: E501

        Resulting text on bank statement if known  # noqa: E501

        :return: The text_on_statement of this ChargeSource.  # noqa: E501
        :rtype: str
        """
        return self._text_on_statement

    @text_on_statement.setter
    def text_on_statement(self, text_on_statement):
        """Sets the text_on_statement of this ChargeSource.

        Resulting text on bank statement if known  # noqa: E501

        :param text_on_statement: The text_on_statement of this ChargeSource.  # noqa: E501
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
        if issubclass(ChargeSource, dict):
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
        if not isinstance(other, ChargeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
