class Customer:
    """Represent a customer with validated contact details."""

    def __init__(self, name: str, email: str, phone_number: str):
        """Create a customer and validate its name, email, and phone number."""
        self.name = name
        self.email = email
        self.phone_number = phone_number
        if not self.email or "@" not in self.email:
            raise ValueError("Invalid email address")
        if not self.phone_number or not self.phone_number.isdigit():
            raise ValueError("Invalid phone number")
        if not self.name or not self.name.strip():
            raise ValueError("Invalid name")

    def __repr__(self):
        """Return a developer-friendly representation of the customer."""
        return f"Customer(name={self.name}, email={self.email}, phone_number={self.phone_number})"

    def __str__(self):
        """Return a readable summary of the customer's contact details."""
        return f"{self.name} ({self.email}, {self.phone_number})"
