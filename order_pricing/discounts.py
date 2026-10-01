from order_pricing.catalog import get_product

# code -> (type, value, min order subtotal)
COUPONS = {
    "SAVE10": ("percent", 10, 500),
    "FLAT100": ("flat", 100, 999),
    "BOGO-MUG": ("bogo", "MUG-100", 0),
}

MAX_PERCENT_DISCOUNT = 300  # cap for percent coupons, in rupees


def coupon_discount(code, items, subtotal):
    if code not in COUPONS:
        return 0.0
    kind, value, min_subtotal = COUPONS[code]
    if subtotal < min_subtotal:
        return 0.0
    if kind == "percent":
        return min(subtotal * value / 100, MAX_PERCENT_DISCOUNT)
    if kind == "flat":
        return float(value)
    if kind == "bogo":
        qty = sum(i.qty for i in items if i.sku == value)
        return (qty // 2) * get_product(value)["price"]
    return 0.0


def bulk_discount(items):
    # 5% off any line with 10 or more units
    total = 0.0
    for item in items:
        if item.qty >= 10:
            total += item.qty * get_product(item.sku)["price"] * 0.05
    return total


def best_discount(order, subtotal):
    """Coupons and bulk discount don't stack - the customer gets the bigger one."""
    return max(coupon_discount(order.coupon, order.items, subtotal), bulk_discount(order.items))
