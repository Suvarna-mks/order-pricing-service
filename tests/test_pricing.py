from order_pricing.models import LineItem, Order
from order_pricing.pricing import price_order, subtotal


def test_subtotal_sums_lines():
    assert subtotal([LineItem("BOOK-001", 1), LineItem("MUG-100", 2)]) == 1048.0


def test_example_order_total():
    order = Order([LineItem("BOOK-001", 1), LineItem("MUG-100", 2)], coupon="SAVE10")
    result = price_order(order)
    assert result == {"subtotal": 1048.0, "discount": 104.8, "tax": 96.88, "shipping": 49, "total": 1089.08}


def test_no_coupon_big_order_ships_free():
    result = price_order(Order([LineItem("HDP-500", 1)]))
    assert result["discount"] == 0
    assert result["shipping"] == 0
    assert result["total"] == 1499 + 269.82
