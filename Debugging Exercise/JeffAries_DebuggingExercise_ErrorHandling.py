"""
Validates inputs so bad values do not crash the program.
"""

from __future__ import annotations


def parse_price(raw_price):
    """Return price, non-negative float."""
    if isinstance(raw_price, bool):
        raise TypeError("Price cannot be a boolean.")

    if isinstance(raw_price, (int, float)):
        price = float(raw_price)

    elif isinstance(raw_price, str):
        text = raw_price.strip()
        if text == "":
            raise ValueError("Price cannot be blank.")
        try:
            price = float(text)
        except ValueError as exc:
            raise ValueError(f"Price must be numeric. Got {raw_price!r}.") from exc

    else:
        raise TypeError(f"Unsupported price type: {type(raw_price).__name__}")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    return price


def validate_discount_rate(raw_rate):
    """Return discount in float from 0 to 1."""
    if isinstance(raw_rate, bool):
        raise TypeError("Discount rate cannot be a boolean.")

    if isinstance(raw_rate, (int, float)):
        rate = float(raw_rate)

    elif isinstance(raw_rate, str):
        text = raw_rate.strip()
        if text == "":
            raise ValueError("Discount rate cannot be blank.")
        try:
            rate = float(text)
        except ValueError as exc:
            raise ValueError(f"Discount rate must be numeric. Got {raw_rate!r}.") from exc

    else:
        raise TypeError(f"Unsupported discount rate type: {type(raw_rate).__name__}")

    if not 0 <= rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1 (ex: 0.15).")

    return rate


def calculate_discount(price, discount_rate):
    """Return discount amount."""
    return price * discount_rate


def apply_discount(price, discount_amount):
    """Return final price, discount applied."""
    return price - discount_amount


def format_money(value):
    """Format $ number"""
    return f"${value:,.2f}"


def run_products(products):
    """Print discounted results."""
    for product in products:
        name = product.get("name", "<missing name>")

        try:
            price = parse_price(product.get("price"))
            discount_rate = validate_discount_rate(product.get("discount_rate"))

            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {name}")
            print(f"Original Price: {format_money(price)}")
            print(f"Discount Amount: {format_money(discount_amount)}")
            print(f"Final Price: {format_money(final_price)}")
            print()

        except (TypeError, ValueError) as err:
            print(f"Product: {name}")
            print("ERROR: Cannot calculate discount.")
            print(f"Reason: {err}")
            print(f"Raw data: {product}")
            print()


def run_tests():
    """Bad-input test."""
    test_products = [
        {"name": "BadPriceText", "price": "five hundred", "discount_rate": 0.2},
        {"name": "BadPriceBlank", "price": "   ", "discount_rate": 0.2},
        {"name": "BadRateHigh", "price": 100, "discount_rate": 1.5},
        {"name": "BadRateText", "price": 100, "discount_rate": "ten percent"},
        {"name": "NegativePrice", "price": -10, "discount_rate": 0.1},
        {"name": "OKStringPrice", "price": "500", "discount_rate": 0.2},
    ]
    run_products(test_products)


def main():
    """Run program."""
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05},
    ]

    print("=== Product Discounts ===\n")
    run_products(products)

    print("=== Test Cases (Bad Inputs) ===\n")
    run_tests()


if __name__ == "__main__":
    main()