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


class SessionChargeDto(object):
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
        'source': 'str',
        'tamper': 'str',
        'fail_on_error': 'bool'
    }

    attribute_map = {
        'source': 'source',
        'tamper': 'tamper',
        'fail_on_error': 'fail_on_error'
    }

    def __init__(self, source=None, tamper=None, fail_on_error=None):  # noqa: E501
        """SessionChargeDto - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self._tamper = None
        self._fail_on_error = None
        self.discriminator = None

        self.source = source
        self.tamper = tamper
        if fail_on_error is not None:
            self.fail_on_error = fail_on_error

    @property
    def source(self):
        """Gets the source of this SessionChargeDto.  # noqa: E501

        The source for the charge  # noqa: E501

        :return: The source of this SessionChargeDto.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SessionChargeDto.

        The source for the charge  # noqa: E501

        :param source: The source of this SessionChargeDto.  # noqa: E501
        :type: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def tamper(self):
        """Gets the tamper of this SessionChargeDto.  # noqa: E501

        Anti-tamper token  # noqa: E501

        :return: The tamper of this SessionChargeDto.  # noqa: E501
        :rtype: str
        """
        return self._tamper

    @tamper.setter
    def tamper(self, tamper):
        """Sets the tamper of this SessionChargeDto.

        Anti-tamper token  # noqa: E501

        :param tamper: The tamper of this SessionChargeDto.  # noqa: E501
        :type: str
        """
        if tamper is None:
            raise ValueError("Invalid value for `tamper`, must not be `None`")  # noqa: E501

        self._tamper = tamper

    @property
    def fail_on_error(self):
        """Gets the fail_on_error of this SessionChargeDto.  # noqa: E501

        Whether to fail invoice on failed attempt  # noqa: E501

        :return: The fail_on_error of this SessionChargeDto.  # noqa: E501
        :rtype: bool
        """
        return self._fail_on_error

    @fail_on_error.setter
    def fail_on_error(self, fail_on_error):
        """Sets the fail_on_error of this SessionChargeDto.

        Whether to fail invoice on failed attempt  # noqa: E501

        :param fail_on_error: The fail_on_error of this SessionChargeDto.  # noqa: E501
        :type: bool
        """

        self._fail_on_error = fail_on_error

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
        if issubclass(SessionChargeDto, dict):
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
        if not isinstance(other, SessionChargeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other