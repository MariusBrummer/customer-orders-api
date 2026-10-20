class Product:
    """Represent a product with a non-negative price."""

    def __init__(self, name: str, price: float):
        """Create a product and reject negative prices."""
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.name = name
        self.price = price

    def discounted_price(self, discount_percent: float) -> float:
        """Return the price after applying a discount from 0 to 100 percent."""
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount must be betwee 0 and 100")

        return self.price * (1 - discount_percent / 100)
