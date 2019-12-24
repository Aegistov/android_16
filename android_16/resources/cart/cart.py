from typing import Dict


class Cart:
    def __init__(
        self,
        uid: int,
        sid: str,
        product_sid: str,
        quantity: int,
    ):
        self.uid = uid
        self.sid = sid
        self.product_sid = product_sid
        self.quantity = quantity

    def serialize(self) -> Dict:
        return {
            "sid": self.sid,
            "product_sid": self.product_sid,
            "quantity": self.quantity,
        }