class Product:
    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.name = name
        self.price = price

    def discounted_price(self, discount_percent: float) -> float:
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount must be betwee 0 and 100")

        return self.price * (1 - discount_percent / 100)
