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


class ApplepayPaymentRequestDto(object):
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
        'auth_url': 'str',
        'country_code': 'str',
        'supported_networks': 'list[str]',
        'merchant_capabilities': 'str',
        'currency_code': 'str',
        'total': 'AppleLineItem',
        'create_session_url': 'str'
    }

    attribute_map = {
        'auth_url': 'authUrl',
        'country_code': 'countryCode',
        'supported_networks': 'supportedNetworks',
        'merchant_capabilities': 'merchantCapabilities',
        'currency_code': 'currencyCode',
        'total': 'total',
        'create_session_url': 'createSessionUrl'
    }

    def __init__(self, auth_url=None, country_code=None, supported_networks=None, merchant_capabilities=None, currency_code=None, total=None, create_session_url=None):  # noqa: E501
        """ApplepayPaymentRequestDto - a model defined in Swagger"""  # noqa: E501

        self._auth_url = None
        self._country_code = None
        self._supported_networks = None
        self._merchant_capabilities = None
        self._currency_code = None
        self._total = None
        self._create_session_url = None
        self.discriminator = None

        if auth_url is not None:
            self.auth_url = auth_url
        if country_code is not None:
            self.country_code = country_code
        if supported_networks is not None:
            self.supported_networks = supported_networks
        if merchant_capabilities is not None:
            self.merchant_capabilities = merchant_capabilities
        if currency_code is not None:
            self.currency_code = currency_code
        if total is not None:
            self.total = total
        if create_session_url is not None:
            self.create_session_url = create_session_url

    @property
    def auth_url(self):
        """Gets the auth_url of this ApplepayPaymentRequestDto.  # noqa: E501


        :return: The auth_url of this ApplepayPaymentRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        """Sets the auth_url of this ApplepayPaymentRequestDto.


        :param auth_url: The auth_url of this ApplepayPaymentRequestDto.  # noqa: E501
        :type: str
        """

        self._auth_url = auth_url

    @property
    def country_code(self):
        """Gets the country_code of this ApplepayPaymentRequestDto.  # noqa: E501


        :return: The country_code of this ApplepayPaymentRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ApplepayPaymentRequestDto.


        :param country_code: The country_code of this ApplepayPaymentRequestDto.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def supported_networks(self):
        """Gets the supported_networks of this ApplepayPaymentRequestDto.  # noqa: E501


        :return: The supported_networks of this ApplepayPaymentRequestDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_networks

    @supported_networks.setter
    def supported_networks(self, supported_networks):
        """Sets the supported_networks of this ApplepayPaymentRequestDto.


        :param supported_networks: The supported_networks of this ApplepayPaymentRequestDto.  # noqa: E501
        :type: list[str]
        """

        self._supported_networks = supported_networks

    @property
    def merchant_capabilities(self):
        """Gets the merchant_capabilities of this ApplepayPaymentRequestDto.  # noqa: E501


        :return: The merchant_capabilities of this ApplepayPaymentRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._merchant_capabilities

    @merchant_capabilities.setter
    def merchant_capabilities(self, merchant_capabilities):
        """Sets the merchant_capabilities of this ApplepayPaymentRequestDto.


        :param merchant_capabilities: The merchant_capabilities of this ApplepayPaymentRequestDto.  # noqa: E501
        :type: str
        """

        self._merchant_capabilities = merchant_capabilities

    @property
    def currency_code(self):
        """Gets the currency_code of this ApplepayPaymentRequestDto.  # noqa: E501


        :return: The currency_code of this ApplepayPaymentRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this ApplepayPaymentRequestDto.


        :param currency_code: The currency_code of this ApplepayPaymentRequestDto.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def total(self):
        """Gets the total of this ApplepayPaymentRequestDto.  # noqa: E501


        :return: The total of this ApplepayPaymentRequestDto.  # noqa: E501
        :rtype: AppleLineItem
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ApplepayPaymentRequestDto.


        :param total: The total of this ApplepayPaymentRequestDto.  # noqa: E501
        :type: AppleLineItem
        """

        self._total = total

    @property
    def create_session_url(self):
        """Gets the create_session_url of this ApplepayPaymentRequestDto.  # noqa: E501


        :return: The create_session_url of this ApplepayPaymentRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._create_session_url

    @create_session_url.setter
    def create_session_url(self, create_session_url):
        """Sets the create_session_url of this ApplepayPaymentRequestDto.


        :param create_session_url: The create_session_url of this ApplepayPaymentRequestDto.  # noqa: E501
        :type: str
        """

        self._create_session_url = create_session_url

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
        if issubclass(ApplepayPaymentRequestDto, dict):
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
        if not isinstance(other, ApplepayPaymentRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other