from order_pricing.models import LineItem
from order_pricing.tax import calculate_tax, line_tax


def test_books_are_zero_rated():
    assert line_tax(LineItem("BOOK-001", 2)) == 0


def test_food_gst():
    assert line_tax(LineItem("TEA-020", 2)) == 21.0


def test_discount_is_split_by_line_value():
    items = [LineItem("BOOK-001", 1), LineItem("MUG-100", 2)]
    assert calculate_tax(items, 104.8, 1048) == 96.88


def test_empty_order_has_no_tax():
    assert calculate_tax([], 0, 0) == 0
