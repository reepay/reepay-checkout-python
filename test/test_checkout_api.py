# coding: utf-8

"""
    Reepay Checkout API

    Reepay Checkout REST API  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.checkout_api import CheckoutApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCheckoutApi(unittest.TestCase):
    """CheckoutApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.checkout_api.CheckoutApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_charge_checkout_session(self):
        """Test case for charge_checkout_session

        Finish charge using source  # noqa: E501
        """
        pass

    def test_create_applepay_session(self):
        """Test case for create_applepay_session

        Create Apple Pay session  # noqa: E501
        """
        pass

    def test_create_googlepay_session(self):
        """Test case for create_googlepay_session

        Create Google Pay session  # noqa: E501
        """
        pass

    def test_create_mpo_session(self):
        """Test case for create_mpo_session

        Create MobilePay Online session  # noqa: E501
        """
        pass

    def test_create_paypal_session(self):
        """Test case for create_paypal_session

        Create PayPal session  # noqa: E501
        """
        pass

    def test_create_pgw_session(self):
        """Test case for create_pgw_session

        Create pgw session  # noqa: E501
        """
        pass

    def test_create_resurs_session(self):
        """Test case for create_resurs_session

        Create Resurs session  # noqa: E501
        """
        pass

    def test_create_viabill_session(self):
        """Test case for create_viabill_session

        Create ViaBill session  # noqa: E501
        """
        pass

    def test_get_checkout_session(self):
        """Test case for get_checkout_session

        Get checkout session data  # noqa: E501
        """
        pass

    def test_get_resurs_payment_method_cost(self):
        """Test case for get_resurs_payment_method_cost

        Get HTML with cost of Resurs payment method  # noqa: E501
        """
        pass

    def test_get_resurs_payment_methods(self):
        """Test case for get_resurs_payment_methods

        Get Resurs payment methods  # noqa: E501
        """
        pass

    def test_get_terms(self):
        """Test case for get_terms

        Get account terms template  # noqa: E501
        """
        pass

    def test_recurring_checkout_session(self):
        """Test case for recurring_checkout_session

        Save recurring customer payment method  # noqa: E501
        """
        pass

    def test_subscription_checkout_session(self):
        """Test case for subscription_checkout_session

        Set payment method on subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
