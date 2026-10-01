"""Price an order from a JSON file:  python -m order_pricing.cli examples/order.json"""
import json
import sys

from order_pricing.models import LineItem, Order
from order_pricing.pricing import price_order


def load_order(path):
    with open(path) as f:
        data = json.load(f)
    items = [LineItem(i["sku"], i["qty"]) for i in data["items"]]
    return Order(items, data.get("coupon"), data.get("express", False), data.get("state", "KA"))


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        return 1
    print(json.dumps(price_order(load_order(argv[0])), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
