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


class CreateChargeSession(object):
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
        'configuration': 'str',
        'locale': 'str',
        'ttl': 'str',
        'invoice': 'str',
        'settle': 'bool',
        'order': 'Order',
        'recurring': 'bool',
        'accept_url': 'str',
        'cancel_url': 'str',
        'payment_methods': 'list[str]',
        'button_text': 'str',
        'card_on_file': 'str'
    }

    attribute_map = {
        'configuration': 'configuration',
        'locale': 'locale',
        'ttl': 'ttl',
        'invoice': 'invoice',
        'settle': 'settle',
        'order': 'order',
        'recurring': 'recurring',
        'accept_url': 'accept_url',
        'cancel_url': 'cancel_url',
        'payment_methods': 'payment_methods',
        'button_text': 'button_text',
        'card_on_file': 'card_on_file'
    }

    def __init__(self, configuration=None, locale=None, ttl=None, invoice=None, settle=None, order=None, recurring=None, accept_url=None, cancel_url=None, payment_methods=None, button_text=None, card_on_file=None):  # noqa: E501
        """CreateChargeSession - a model defined in Swagger"""  # noqa: E501

        self._configuration = None
        self._locale = None
        self._ttl = None
        self._invoice = None
        self._settle = None
        self._order = None
        self._recurring = None
        self._accept_url = None
        self._cancel_url = None
        self._payment_methods = None
        self._button_text = None
        self._card_on_file = None
        self.discriminator = None

        if configuration is not None:
            self.configuration = configuration
        if locale is not None:
            self.locale = locale
        if ttl is not None:
            self.ttl = ttl
        if invoice is not None:
            self.invoice = invoice
        if settle is not None:
            self.settle = settle
        if order is not None:
            self.order = order
        if recurring is not None:
            self.recurring = recurring
        if accept_url is not None:
            self.accept_url = accept_url
        if cancel_url is not None:
            self.cancel_url = cancel_url
        if payment_methods is not None:
            self.payment_methods = payment_methods
        if button_text is not None:
            self.button_text = button_text
        if card_on_file is not None:
            self.card_on_file = card_on_file

    @property
    def configuration(self):
        """Gets the configuration of this CreateChargeSession.  # noqa: E501

        Optional handle for a configuration to use for this session  # noqa: E501

        :return: The configuration of this CreateChargeSession.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this CreateChargeSession.

        Optional handle for a configuration to use for this session  # noqa: E501

        :param configuration: The configuration of this CreateChargeSession.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def locale(self):
        """Gets the locale of this CreateChargeSession.  # noqa: E501

        Optional locale for session. E.g. `en_GB`, `da_DK`, `es_ES`. Defaults to configuration locale or account locale.   # noqa: E501

        :return: The locale of this CreateChargeSession.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CreateChargeSession.

        Optional locale for session. E.g. `en_GB`, `da_DK`, `es_ES`. Defaults to configuration locale or account locale.   # noqa: E501

        :param locale: The locale of this CreateChargeSession.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def ttl(self):
        """Gets the ttl of this CreateChargeSession.  # noqa: E501

        Optional time-to-live duration. The session will expire after the duration from creation. The duration must be given as an ISO-8601 duration. See https://en.wikipedia.org/wiki/ISO_8601#Durations. E.g. PT3H (three hours).  # noqa: E501

        :return: The ttl of this CreateChargeSession.  # noqa: E501
        :rtype: str
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this CreateChargeSession.

        Optional time-to-live duration. The session will expire after the duration from creation. The duration must be given as an ISO-8601 duration. See https://en.wikipedia.org/wiki/ISO_8601#Durations. E.g. PT3H (three hours).  # noqa: E501

        :param ttl: The ttl of this CreateChargeSession.  # noqa: E501
        :type: str
        """

        self._ttl = ttl

    @property
    def invoice(self):
        """Gets the invoice of this CreateChargeSession.  # noqa: E501

        Handle for existing invoice to charge. Either this argument must be provided or `order`.  # noqa: E501

        :return: The invoice of this CreateChargeSession.  # noqa: E501
        :rtype: str
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this CreateChargeSession.

        Handle for existing invoice to charge. Either this argument must be provided or `order`.  # noqa: E501

        :param invoice: The invoice of this CreateChargeSession.  # noqa: E501
        :type: str
        """

        self._invoice = invoice

    @property
    def settle(self):
        """Gets the settle of this CreateChargeSession.  # noqa: E501

        Whether or not to immediately settle (capture). Default is false. If not settled immediately an authorization will be performed which can be settled later. Normally this have to be done within 7 days.  # noqa: E501

        :return: The settle of this CreateChargeSession.  # noqa: E501
        :rtype: bool
        """
        return self._settle

    @settle.setter
    def settle(self, settle):
        """Sets the settle of this CreateChargeSession.

        Whether or not to immediately settle (capture). Default is false. If not settled immediately an authorization will be performed which can be settled later. Normally this have to be done within 7 days.  # noqa: E501

        :param settle: The settle of this CreateChargeSession.  # noqa: E501
        :type: bool
        """

        self._settle = settle

    @property
    def order(self):
        """Gets the order of this CreateChargeSession.  # noqa: E501

        Order object. Either this argument must be provided or `invoice`.   # noqa: E501

        :return: The order of this CreateChargeSession.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CreateChargeSession.

        Order object. Either this argument must be provided or `invoice`.   # noqa: E501

        :param order: The order of this CreateChargeSession.  # noqa: E501
        :type: Order
        """

        self._order = order

    @property
    def recurring(self):
        """Gets the recurring of this CreateChargeSession.  # noqa: E501

        If set a recurring payment method is stored for the customer and a reference returned. This parameter if set to true will limit payment methods to those that are reusable.  # noqa: E501

        :return: The recurring of this CreateChargeSession.  # noqa: E501
        :rtype: bool
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """Sets the recurring of this CreateChargeSession.

        If set a recurring payment method is stored for the customer and a reference returned. This parameter if set to true will limit payment methods to those that are reusable.  # noqa: E501

        :param recurring: The recurring of this CreateChargeSession.  # noqa: E501
        :type: bool
        """

        self._recurring = recurring

    @property
    def accept_url(self):
        """Gets the accept_url of this CreateChargeSession.  # noqa: E501

        If checkout is opened in separate window the customer will be directed to this page after success  # noqa: E501

        :return: The accept_url of this CreateChargeSession.  # noqa: E501
        :rtype: str
        """
        return self._accept_url

    @accept_url.setter
    def accept_url(self, accept_url):
        """Sets the accept_url of this CreateChargeSession.

        If checkout is opened in separate window the customer will be directed to this page after success  # noqa: E501

        :param accept_url: The accept_url of this CreateChargeSession.  # noqa: E501
        :type: str
        """

        self._accept_url = accept_url

    @property
    def cancel_url(self):
        """Gets the cancel_url of this CreateChargeSession.  # noqa: E501

        If checkout is opened in separate window the customer will be directed to this page if the customer cancels  # noqa: E501

        :return: The cancel_url of this CreateChargeSession.  # noqa: E501
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """Sets the cancel_url of this CreateChargeSession.

        If checkout is opened in separate window the customer will be directed to this page if the customer cancels  # noqa: E501

        :param cancel_url: The cancel_url of this CreateChargeSession.  # noqa: E501
        :type: str
        """

        self._cancel_url = cancel_url

    @property
    def payment_methods(self):
        """Gets the payment_methods of this CreateChargeSession.  # noqa: E501

        Optional list of payment methods to use for the checkout session. Format: `<payment_methods> = list of <payment_method>` `<payment_method>  = [sca-|scafallback-|nosca-|]<payment_name>` `<payment_name>    = The id of payment method, e.g. dankort` See https://docs.reepay.com/docs/checkout-payment-methods for full documentation  # noqa: E501

        :return: The payment_methods of this CreateChargeSession.  # noqa: E501
        :rtype: list[str]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """Sets the payment_methods of this CreateChargeSession.

        Optional list of payment methods to use for the checkout session. Format: `<payment_methods> = list of <payment_method>` `<payment_method>  = [sca-|scafallback-|nosca-|]<payment_name>` `<payment_name>    = The id of payment method, e.g. dankort` See https://docs.reepay.com/docs/checkout-payment-methods for full documentation  # noqa: E501

        :param payment_methods: The payment_methods of this CreateChargeSession.  # noqa: E501
        :type: list[str]
        """

        self._payment_methods = payment_methods

    @property
    def button_text(self):
        """Gets the button_text of this CreateChargeSession.  # noqa: E501

        Optional alternative button text. Maximum length 32 characters.  # noqa: E501

        :return: The button_text of this CreateChargeSession.  # noqa: E501
        :rtype: str
        """
        return self._button_text

    @button_text.setter
    def button_text(self, button_text):
        """Sets the button_text of this CreateChargeSession.

        Optional alternative button text. Maximum length 32 characters.  # noqa: E501

        :param button_text: The button_text of this CreateChargeSession.  # noqa: E501
        :type: str
        """

        self._button_text = button_text

    @property
    def card_on_file(self):
        """Gets the card_on_file of this CreateChargeSession.  # noqa: E501

        Reference to existing card payment method (`ca_xxx`) to perform card-on-file payment for.  # noqa: E501

        :return: The card_on_file of this CreateChargeSession.  # noqa: E501
        :rtype: str
        """
        return self._card_on_file

    @card_on_file.setter
    def card_on_file(self, card_on_file):
        """Sets the card_on_file of this CreateChargeSession.

        Reference to existing card payment method (`ca_xxx`) to perform card-on-file payment for.  # noqa: E501

        :param card_on_file: The card_on_file of this CreateChargeSession.  # noqa: E501
        :type: str
        """

        self._card_on_file = card_on_file

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
        if issubclass(CreateChargeSession, dict):
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
        if not isinstance(other, CreateChargeSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
