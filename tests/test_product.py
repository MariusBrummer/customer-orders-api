import pytest

from customer_orders.product import Product


def test_product_sgtores_name_and_price():
    product = Product("Keyboard", 100.0)

    assert product.name == "Keyboard"
    assert product.price == 100.0


def test_discounted_price():
    product = Product("Keyboard", 100.0)

    assert product.discounted_price(20) == 80.0


def test_negative_price_is_rejected():
    with pytest.raises(ValueError):
        Product("Keyboard", -10.0)


def test_invalid_discount_is_rejected():
    product = Product("Keyboard", 100.0)

    with pytest.raises(ValueError):
        product.discounted_price(120)
