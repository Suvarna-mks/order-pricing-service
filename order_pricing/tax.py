from order_pricing.catalog import get_product

GST_RATES = {"books": 0.0, "food": 0.05, "stationery": 0.12, "home": 0.18, "electronics": 0.18}


def line_tax(item, discount_share=0.0):
    product = get_product(item.sku)
    taxable = item.qty * product["price"] - discount_share
    return round(max(taxable, 0) * GST_RATES[product["category"]], 2)


def calculate_tax(items, discount, subtotal):
    """Spread the discount across lines by value, then apply each line's GST rate."""
    if subtotal == 0:
        return 0.0
    tax = 0.0
    for item in items:
        line_value = item.qty * get_product(item.sku)["price"]
        tax += line_tax(item, discount * line_value / subtotal)
    return round(tax, 2)
