from decimal import Decimal

from typing import Dict


class Product:
    def __init__(
         self,
         uid: int,
         sid: str,
         name: str,
         price: Decimal
    ):
        self.uid = uid
        self.sid = sid
        self.name = name
        self.price = price

    def serialize(self) -> Dict:
        return {
            "sid": self.sid,
            "name": self.name,
            "price": self.price,
        }
