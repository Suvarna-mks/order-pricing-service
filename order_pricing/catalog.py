# sku -> (name, unit price in rupees, GST category)
PRODUCTS = {
    "BOOK-001": ("Python Testing Handbook", 450.0, "books"),
    "PEN-010": ("Gel Pen Pack", 120.0, "stationery"),
    "MUG-100": ("Ceramic Mug", 299.0, "home"),
    "HDP-500": ("Wired Headphones", 1499.0, "electronics"),
    "TEA-020": ("Green Tea 100g", 210.0, "food"),
}


def get_product(sku):
    if sku not in PRODUCTS:
        raise KeyError(f"unknown sku: {sku}")
    name, price, category = PRODUCTS[sku]
    return {"sku": sku, "name": name, "price": price, "category": category}
