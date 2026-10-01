from order_pricing.catalog import get_product
from order_pricing.discounts import best_discount
from order_pricing.orders.validator import Validator
from order_pricing.shipping import shipping_fee
from order_pricing.tax import calculate_tax


def subtotal(items):
    return round(sum(i.qty * get_product(i.sku)["price"] for i in items), 2)


def price_order(order):
    Validator().validate(order)
    sub = subtotal(order.items)
    discount = round(best_discount(order, sub), 2)
    after_discount = sub - discount
    tax = calculate_tax(order.items, discount, sub)
    ship = shipping_fee(after_discount, order.express, order.state)
    return {
        "subtotal": sub,
        "discount": discount,
        "tax": tax,
        "shipping": ship,
        "total": round(after_discount + tax + ship, 2),
    }
