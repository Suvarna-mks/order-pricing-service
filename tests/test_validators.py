import pytest

from order_pricing.models import LineItem, Order
from order_pricing.orders.validator import Validator as OrderValidator
from order_pricing.payments.validator import Validator as PaymentValidator


@pytest.mark.parametrize("items,msg", [
    ([], "no items"),
    ([LineItem("XYZ-999", 1)], "unknown sku"),
    ([LineItem("PEN-010", 0)], "bad qty"),
    ([LineItem("PEN-010", 51)], "bad qty"),
    ([LineItem("PEN-010", 1), LineItem("PEN-010", 2)], "duplicate"),
])
def test_order_validator_rejects(items, msg):
    with pytest.raises(ValueError, match=msg):
        OrderValidator().validate(Order(items))


def test_order_validator_accepts_good_order():
    assert OrderValidator().validate(Order([LineItem("PEN-010", 50)]))


@pytest.mark.parametrize("number,ok", [
    ("4111 1111 1111 1111", True),
    ("4111111111111112", False),
    ("4111-1111-1111-1111", False),
    ("411111", False),
])
def test_card_luhn(number, ok):
    assert PaymentValidator().validate("card", number) is ok


@pytest.mark.parametrize("upi,ok", [("suvarna@okaxis", True), ("bad@", False), ("@upi", False)])
def test_upi_format(upi, ok):
    assert PaymentValidator().validate("upi", upi) is ok


def test_unsupported_payment_method():
    with pytest.raises(ValueError, match="unsupported"):
        PaymentValidator().validate("cash", "100")
