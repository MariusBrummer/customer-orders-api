"""Unit tests for customer class"""

import pytest

from customer_orders.customer import Customer


def test_customer_creation():
    """Verify that a customer stores its contact details."""
    customer = Customer("Joe Soap", "joe@soap.com", "31333339495")

    assert customer.name == "Joe Soap"
    assert customer.email == "joe@soap.com"
    assert customer.phone_number == "31333339495"


def test_blank_name():
    """Verify that a blank name raises a ValueError."""

    with pytest.raises(ValueError, match="Invalid name"):
        Customer("", "joe@soap.com", "3423423423")


def test_invalid_email():
    """Verify that a blank email reaises a ValueError."""

    with pytest.raises(ValueError, match="Invalid email address"):
        Customer("Joe Soap", "", "34534534")


def test_empty_phone():
    """Verify that an empty phone nubmer raises ValueError."""

    with pytest.raises(ValueError, match="Invalid phone number"):
        Customer("Joe Soap", "joe@soap.com", "")
