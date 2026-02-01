def calculate_discount(price, discount_rate):
    """Return the discount amount."""
    return price * discount_rate


def apply_discount(price, discount_amount):
    """Return the final price after discount."""
    return price - discount_amount


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.10},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": 500, "discount_rate": 0.20},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        price = product["price"]
        discount_rate = product["discount_rate"]

        discount_amount = calculate_discount(price, discount_rate)
        final_price = apply_discount(price, discount_amount)

        print(f"Product: {product['name']}")
        print(f"Original Price: ${price}")
        print(f"Discount Amount: ${discount_amount}")
        print(f"Final Price: ${final_price}\n")


if __name__ == "__main__":
    main()