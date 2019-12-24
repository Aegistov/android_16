import os
from csv import reader


class CartReader:
    CSV_NAME = f'{os.getcwd()}/android_16/data_store/cart.csv'

    @staticmethod
    def get_table_size() -> int:
        with open(CartReader.CSV_NAME, newline='') as cart_table:
            cart_reader = reader(cart_table)
            count = 0
            for item in cart_reader:
                count += 1
            return count
