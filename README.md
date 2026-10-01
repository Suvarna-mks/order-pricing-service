# order-pricing-service

A small Python service that prices a shopping order: subtotal, coupons, bulk discount, GST per product category and shipping. I wrote it as a practice codebase for testing pricing logic, where most real bugs hide in boundaries and rounding.

## Why I built this
In checkout testing the bugs I find are rarely "the page is broken". They are things like a coupon applied below its minimum, free shipping at exactly ₹999, or tax calculated before the discount instead of after. I wanted a small codebase where I could write those rules down and test every edge on purpose.

## What it does
- `pricing.py` – `price_order()` validates the order, then works out subtotal → discount → GST → shipping → total
- `discounts.py` – percent (capped at ₹300), flat and buy-one-get-one coupons, plus 5% bulk discount on 10+ units. Coupon and bulk don't stack; you get the bigger one
- `tax.py` – GST by category (books 0%, food 5%, stationery 12%, home/electronics 18%), with the discount split across lines by value
- `shipping.py` – free above ₹999, express +₹99, remote states +₹150
- `orders/validator.py` and `payments/validator.py` – two classes both called `Validator`: one checks the order, the other checks a card (Luhn) or UPI id

## Run it
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pytest
pytest
python -m order_pricing.cli examples/order.json
```

## What I learned
- Splitting a discount across lines before applying different GST rates changes the tax total – the order of operations matters
- Boundary values (₹999 vs ₹999.01, qty 9 vs 10, qty 50 vs 51) catch more bugs than random inputs
- Rounding each line vs rounding the total can differ by a paisa, so I round per line and say so

## Known limitations / TODO
- Prices are floats; should move to `Decimal` for money
- No inter-state IGST vs CGST/SGST split yet
- Coupons are hard-coded; next step is loading them from a JSON file
- Add GitHub Actions to run the tests on every push
