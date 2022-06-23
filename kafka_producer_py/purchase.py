
from dataclasses import dataclass, field
import json
import random

from faker import Faker


@dataclass
class Purchase:
    fake = Faker()
    username: str = field(default_factory=fake.user_name)
    currency: str = field(default_factory=fake.currency_code)
    amount: int = field(default_factory=lambda: random.randint(100, 200000))

    def serialize(self):
        """Serializes the object in JSON string format"""
        return json.dumps(
            {
                "username": self.username,
                "currency": self.currency,
                "amount": self.amount,
            }
        )
