from order_pricing.discounts import best_discount, bulk_discount, coupon_discount
from order_pricing.models import LineItem, Order


def test_unknown_coupon_gives_nothing():
    assert coupon_discount("NOPE", [], 2000) == 0


def test_coupon_below_minimum_is_ignored():
    assert coupon_discount("SAVE10", [LineItem("BOOK-001", 1)], 450) == 0


def test_percent_coupon_is_capped():
    assert coupon_discount("SAVE10", [LineItem("HDP-500", 3)], 4497) == 300


def test_flat_coupon():
    assert coupon_discount("FLAT100", [LineItem("HDP-500", 1)], 1499) == 100


def test_bogo_counts_pairs_only():
    assert coupon_discount("BOGO-MUG", [LineItem("MUG-100", 3)], 897) == 299
    assert coupon_discount("BOGO-MUG", [LineItem("MUG-100", 4)], 1196) == 598


def test_bulk_discount_starts_at_10_units():
    assert bulk_discount([LineItem("PEN-010", 9)]) == 0
    assert bulk_discount([LineItem("PEN-010", 10)]) == 60


def test_best_discount_does_not_stack():
    order = Order([LineItem("PEN-010", 10)], coupon="SAVE10")
    assert best_discount(order, 1200) == 120  # coupon 120 beats bulk 60
