"""Entry point for the customer orders application."""

from customer_orders import customer, product


def main():
    """Create sample customer and product instances."""
    customer1 = customer.Customer("Jack", "Jack@black.com", "484848484")
    product1 = product.Product("Laptop", 500.32)
    print(customer1.name)
    print(product1.name)


if __name__ == "__main__":
    main()
