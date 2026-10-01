from order_pricing.catalog import PRODUCTS

MAX_QTY_PER_LINE = 50


class Validator:
    """Checks an order before pricing it."""

    def validate(self, order):
        if not order.items:
            raise ValueError("order has no items")
        seen = set()
        for item in order.items:
            if item.sku not in PRODUCTS:
                raise ValueError(f"unknown sku: {item.sku}")
            if item.qty <= 0 or item.qty > MAX_QTY_PER_LINE:
                raise ValueError(f"bad qty {item.qty} for {item.sku}")
            if item.sku in seen:
                raise ValueError(f"duplicate line for {item.sku}")
            seen.add(item.sku)
        return True
