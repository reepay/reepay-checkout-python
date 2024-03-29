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


class ErrorResponse(object):
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
        'code': 'int',
        'error': 'str',
        'message': 'str',
        'path': 'str',
        'timestamp': 'datetime',
        'http_status': 'int',
        'http_reason': 'str',
        'request_id': 'str',
        'transaction_error': 'str'
    }

    attribute_map = {
        'code': 'code',
        'error': 'error',
        'message': 'message',
        'path': 'path',
        'timestamp': 'timestamp',
        'http_status': 'http_status',
        'http_reason': 'http_reason',
        'request_id': 'request_id',
        'transaction_error': 'transaction_error'
    }

    def __init__(self, code=None, error=None, message=None, path=None, timestamp=None, http_status=None, http_reason=None, request_id=None, transaction_error=None):  # noqa: E501
        """ErrorResponse - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._error = None
        self._message = None
        self._path = None
        self._timestamp = None
        self._http_status = None
        self._http_reason = None
        self._request_id = None
        self._transaction_error = None
        self.discriminator = None

        self.code = code
        self.error = error
        if message is not None:
            self.message = message
        self.path = path
        self.timestamp = timestamp
        self.http_status = http_status
        self.http_reason = http_reason
        self.request_id = request_id
        if transaction_error is not None:
            self.transaction_error = transaction_error

    @property
    def code(self):
        """Gets the code of this ErrorResponse.  # noqa: E501

        Reepay API [error codes](https://api.reepay.com/v1/error_codes)  # noqa: E501

        :return: The code of this ErrorResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorResponse.

        Reepay API [error codes](https://api.reepay.com/v1/error_codes)  # noqa: E501

        :param code: The code of this ErrorResponse.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def error(self):
        """Gets the error of this ErrorResponse.  # noqa: E501

        Short error message  # noqa: E501

        :return: The error of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ErrorResponse.

        Short error message  # noqa: E501

        :param error: The error of this ErrorResponse.  # noqa: E501
        :type: str
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def message(self):
        """Gets the message of this ErrorResponse.  # noqa: E501

        Optional clarifying error message  # noqa: E501

        :return: The message of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorResponse.

        Optional clarifying error message  # noqa: E501

        :param message: The message of this ErrorResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def path(self):
        """Gets the path of this ErrorResponse.  # noqa: E501

        The path generating the error response  # noqa: E501

        :return: The path of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ErrorResponse.

        The path generating the error response  # noqa: E501

        :param path: The path of this ErrorResponse.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def timestamp(self):
        """Gets the timestamp of this ErrorResponse.  # noqa: E501

        Timestamp for the error response in ISO-8601 extended offset date-time format  # noqa: E501

        :return: The timestamp of this ErrorResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ErrorResponse.

        Timestamp for the error response in ISO-8601 extended offset date-time format  # noqa: E501

        :param timestamp: The timestamp of this ErrorResponse.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def http_status(self):
        """Gets the http_status of this ErrorResponse.  # noqa: E501

        HTTP status code of the error  # noqa: E501

        :return: The http_status of this ErrorResponse.  # noqa: E501
        :rtype: int
        """
        return self._http_status

    @http_status.setter
    def http_status(self, http_status):
        """Sets the http_status of this ErrorResponse.

        HTTP status code of the error  # noqa: E501

        :param http_status: The http_status of this ErrorResponse.  # noqa: E501
        :type: int
        """
        if http_status is None:
            raise ValueError("Invalid value for `http_status`, must not be `None`")  # noqa: E501

        self._http_status = http_status

    @property
    def http_reason(self):
        """Gets the http_reason of this ErrorResponse.  # noqa: E501

        HTTP reason of the error  # noqa: E501

        :return: The http_reason of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._http_reason

    @http_reason.setter
    def http_reason(self, http_reason):
        """Sets the http_reason of this ErrorResponse.

        HTTP reason of the error  # noqa: E501

        :param http_reason: The http_reason of this ErrorResponse.  # noqa: E501
        :type: str
        """
        if http_reason is None:
            raise ValueError("Invalid value for `http_reason`, must not be `None`")  # noqa: E501

        self._http_reason = http_reason

    @property
    def request_id(self):
        """Gets the request_id of this ErrorResponse.  # noqa: E501

        Request-Id for the failed request  # noqa: E501

        :return: The request_id of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ErrorResponse.

        Request-Id for the failed request  # noqa: E501

        :param request_id: The request_id of this ErrorResponse.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def transaction_error(self):
        """Gets the transaction_error of this ErrorResponse.  # noqa: E501

        Optional transaction error in the case the request involved a transaction processing. See [transaction errors](https://reference.reepay.com/api/#transaction-errors).  # noqa: E501

        :return: The transaction_error of this ErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_error

    @transaction_error.setter
    def transaction_error(self, transaction_error):
        """Sets the transaction_error of this ErrorResponse.

        Optional transaction error in the case the request involved a transaction processing. See [transaction errors](https://reference.reepay.com/api/#transaction-errors).  # noqa: E501

        :param transaction_error: The transaction_error of this ErrorResponse.  # noqa: E501
        :type: str
        """

        self._transaction_error = transaction_error

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
        if issubclass(ErrorResponse, dict):
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
        if not isinstance(other, ErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
