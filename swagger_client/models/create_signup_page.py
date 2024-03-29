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


class CreateSignupPage(object):
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
        'locale': 'str',
        'email': 'str',
        'phone': 'str',
        'address': 'str',
        'company': 'str',
        'city': 'str',
        'coupon': 'str',
        'accept_url': 'str',
        'cancel_url': 'str',
        'payment_methods': 'list[str]',
        'subscription_configuration': 'CreateSubscription',
        'first_name': 'str',
        'last_name': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'plan': 'plan',
        'locale': 'locale',
        'email': 'email',
        'phone': 'phone',
        'address': 'address',
        'company': 'company',
        'city': 'city',
        'coupon': 'coupon',
        'accept_url': 'accept_url',
        'cancel_url': 'cancel_url',
        'payment_methods': 'payment_methods',
        'subscription_configuration': 'subscription_configuration',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'postal_code': 'postal_code'
    }

    def __init__(self, plan=None, locale=None, email=None, phone=None, address=None, company=None, city=None, coupon=None, accept_url=None, cancel_url=None, payment_methods=None, subscription_configuration=None, first_name=None, last_name=None, postal_code=None):  # noqa: E501
        """CreateSignupPage - a model defined in Swagger"""  # noqa: E501

        self._plan = None
        self._locale = None
        self._email = None
        self._phone = None
        self._address = None
        self._company = None
        self._city = None
        self._coupon = None
        self._accept_url = None
        self._cancel_url = None
        self._payment_methods = None
        self._subscription_configuration = None
        self._first_name = None
        self._last_name = None
        self._postal_code = None
        self.discriminator = None

        self.plan = plan
        if locale is not None:
            self.locale = locale
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if address is not None:
            self.address = address
        if company is not None:
            self.company = company
        if city is not None:
            self.city = city
        if coupon is not None:
            self.coupon = coupon
        if accept_url is not None:
            self.accept_url = accept_url
        if cancel_url is not None:
            self.cancel_url = cancel_url
        if payment_methods is not None:
            self.payment_methods = payment_methods
        if subscription_configuration is not None:
            self.subscription_configuration = subscription_configuration
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if postal_code is not None:
            self.postal_code = postal_code

    @property
    def plan(self):
        """Gets the plan of this CreateSignupPage.  # noqa: E501

        Subscription plan  # noqa: E501

        :return: The plan of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this CreateSignupPage.

        Subscription plan  # noqa: E501

        :param plan: The plan of this CreateSignupPage.  # noqa: E501
        :type: str
        """
        if plan is None:
            raise ValueError("Invalid value for `plan`, must not be `None`")  # noqa: E501

        self._plan = plan

    @property
    def locale(self):
        """Gets the locale of this CreateSignupPage.  # noqa: E501

        Optional locale. E.g. `en_GB`, `da_DK`, `es_ES`. Defaults to configuration locale or account locale.   # noqa: E501

        :return: The locale of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CreateSignupPage.

        Optional locale. E.g. `en_GB`, `da_DK`, `es_ES`. Defaults to configuration locale or account locale.   # noqa: E501

        :param locale: The locale of this CreateSignupPage.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def email(self):
        """Gets the email of this CreateSignupPage.  # noqa: E501

        Field configuration  # noqa: E501

        :return: The email of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateSignupPage.

        Field configuration  # noqa: E501

        :param email: The email of this CreateSignupPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["HIDDEN", "OPTIONAL", "MANDATORY"]  # noqa: E501
        if email not in allowed_values:
            raise ValueError(
                "Invalid value for `email` ({0}), must be one of {1}"  # noqa: E501
                .format(email, allowed_values)
            )

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this CreateSignupPage.  # noqa: E501

        Field configuration  # noqa: E501

        :return: The phone of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CreateSignupPage.

        Field configuration  # noqa: E501

        :param phone: The phone of this CreateSignupPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["HIDDEN", "OPTIONAL", "MANDATORY"]  # noqa: E501
        if phone not in allowed_values:
            raise ValueError(
                "Invalid value for `phone` ({0}), must be one of {1}"  # noqa: E501
                .format(phone, allowed_values)
            )

        self._phone = phone

    @property
    def address(self):
        """Gets the address of this CreateSignupPage.  # noqa: E501

        Field configuration  # noqa: E501

        :return: The address of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreateSignupPage.

        Field configuration  # noqa: E501

        :param address: The address of this CreateSignupPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["HIDDEN", "OPTIONAL", "MANDATORY"]  # noqa: E501
        if address not in allowed_values:
            raise ValueError(
                "Invalid value for `address` ({0}), must be one of {1}"  # noqa: E501
                .format(address, allowed_values)
            )

        self._address = address

    @property
    def company(self):
        """Gets the company of this CreateSignupPage.  # noqa: E501

        Field configuration  # noqa: E501

        :return: The company of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this CreateSignupPage.

        Field configuration  # noqa: E501

        :param company: The company of this CreateSignupPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["HIDDEN", "OPTIONAL", "MANDATORY"]  # noqa: E501
        if company not in allowed_values:
            raise ValueError(
                "Invalid value for `company` ({0}), must be one of {1}"  # noqa: E501
                .format(company, allowed_values)
            )

        self._company = company

    @property
    def city(self):
        """Gets the city of this CreateSignupPage.  # noqa: E501

        Field configuration  # noqa: E501

        :return: The city of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CreateSignupPage.

        Field configuration  # noqa: E501

        :param city: The city of this CreateSignupPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["HIDDEN", "OPTIONAL", "MANDATORY"]  # noqa: E501
        if city not in allowed_values:
            raise ValueError(
                "Invalid value for `city` ({0}), must be one of {1}"  # noqa: E501
                .format(city, allowed_values)
            )

        self._city = city

    @property
    def coupon(self):
        """Gets the coupon of this CreateSignupPage.  # noqa: E501

        Field configuration  # noqa: E501

        :return: The coupon of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        """Sets the coupon of this CreateSignupPage.

        Field configuration  # noqa: E501

        :param coupon: The coupon of this CreateSignupPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["HIDDEN", "OPTIONAL", "MANDATORY"]  # noqa: E501
        if coupon not in allowed_values:
            raise ValueError(
                "Invalid value for `coupon` ({0}), must be one of {1}"  # noqa: E501
                .format(coupon, allowed_values)
            )

        self._coupon = coupon

    @property
    def accept_url(self):
        """Gets the accept_url of this CreateSignupPage.  # noqa: E501

        Redirect to this url after successful signup  # noqa: E501

        :return: The accept_url of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._accept_url

    @accept_url.setter
    def accept_url(self, accept_url):
        """Sets the accept_url of this CreateSignupPage.

        Redirect to this url after successful signup  # noqa: E501

        :param accept_url: The accept_url of this CreateSignupPage.  # noqa: E501
        :type: str
        """

        self._accept_url = accept_url

    @property
    def cancel_url(self):
        """Gets the cancel_url of this CreateSignupPage.  # noqa: E501

        Redirect to this url if the customer cancels sign-up  # noqa: E501

        :return: The cancel_url of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """Sets the cancel_url of this CreateSignupPage.

        Redirect to this url if the customer cancels sign-up  # noqa: E501

        :param cancel_url: The cancel_url of this CreateSignupPage.  # noqa: E501
        :type: str
        """

        self._cancel_url = cancel_url

    @property
    def payment_methods(self):
        """Gets the payment_methods of this CreateSignupPage.  # noqa: E501

        Optional list of payment methods to present to customer. Format: <payment_methods> = list of <payment_method> <payment_method>  = [sca-|nosca-]<payment_name> <payment_name>    = The id of payment method, e.g. dankort See https://docs.reepay.com/docs/checkout-payment-methods for full documentation  # noqa: E501

        :return: The payment_methods of this CreateSignupPage.  # noqa: E501
        :rtype: list[str]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """Sets the payment_methods of this CreateSignupPage.

        Optional list of payment methods to present to customer. Format: <payment_methods> = list of <payment_method> <payment_method>  = [sca-|nosca-]<payment_name> <payment_name>    = The id of payment method, e.g. dankort See https://docs.reepay.com/docs/checkout-payment-methods for full documentation  # noqa: E501

        :param payment_methods: The payment_methods of this CreateSignupPage.  # noqa: E501
        :type: list[str]
        """

        self._payment_methods = payment_methods

    @property
    def subscription_configuration(self):
        """Gets the subscription_configuration of this CreateSignupPage.  # noqa: E501

        Configuration configuration  # noqa: E501

        :return: The subscription_configuration of this CreateSignupPage.  # noqa: E501
        :rtype: CreateSubscription
        """
        return self._subscription_configuration

    @subscription_configuration.setter
    def subscription_configuration(self, subscription_configuration):
        """Sets the subscription_configuration of this CreateSignupPage.

        Configuration configuration  # noqa: E501

        :param subscription_configuration: The subscription_configuration of this CreateSignupPage.  # noqa: E501
        :type: CreateSubscription
        """

        self._subscription_configuration = subscription_configuration

    @property
    def first_name(self):
        """Gets the first_name of this CreateSignupPage.  # noqa: E501

        Field configuration  # noqa: E501

        :return: The first_name of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CreateSignupPage.

        Field configuration  # noqa: E501

        :param first_name: The first_name of this CreateSignupPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["HIDDEN", "OPTIONAL", "MANDATORY"]  # noqa: E501
        if first_name not in allowed_values:
            raise ValueError(
                "Invalid value for `first_name` ({0}), must be one of {1}"  # noqa: E501
                .format(first_name, allowed_values)
            )

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CreateSignupPage.  # noqa: E501

        Field configuration  # noqa: E501

        :return: The last_name of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CreateSignupPage.

        Field configuration  # noqa: E501

        :param last_name: The last_name of this CreateSignupPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["HIDDEN", "OPTIONAL", "MANDATORY"]  # noqa: E501
        if last_name not in allowed_values:
            raise ValueError(
                "Invalid value for `last_name` ({0}), must be one of {1}"  # noqa: E501
                .format(last_name, allowed_values)
            )

        self._last_name = last_name

    @property
    def postal_code(self):
        """Gets the postal_code of this CreateSignupPage.  # noqa: E501

        Field configuration  # noqa: E501

        :return: The postal_code of this CreateSignupPage.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this CreateSignupPage.

        Field configuration  # noqa: E501

        :param postal_code: The postal_code of this CreateSignupPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["HIDDEN", "OPTIONAL", "MANDATORY"]  # noqa: E501
        if postal_code not in allowed_values:
            raise ValueError(
                "Invalid value for `postal_code` ({0}), must be one of {1}"  # noqa: E501
                .format(postal_code, allowed_values)
            )

        self._postal_code = postal_code

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
        if issubclass(CreateSignupPage, dict):
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
        if not isinstance(other, CreateSignupPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
