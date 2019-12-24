import os

from csv import writer

from android_16.resources.cart.cart import Cart
from android_16.resources.cart.cart_reader import CartReader


class CartWriter:
    CSV_NAME = f'{os.getcwd()}/android_16/data_store/cart.csv'

    @staticmethod
    def insert_item(cart_sid: str, product_sid: str, quantity: int) -> Cart:
        with open(CartWriter.CSV_NAME, 'a', newline='') as cart_table:
            cart_writer = writer(cart_table)
            uid = CartReader.get_table_size()
            cart_writer.writerow([uid, cart_sid, product_sid, quantity])
        return Cart(uid, cart_sid, product_sid, quantity)