import os
from csv import reader

from android_16.resources.products.product import Product


class ProductReader:
    CSV_NAME = f'{os.getcwd()}/android_16/data_store/products.csv'

    @staticmethod
    def get_products():
        with open(ProductReader.CSV_NAME, newline='') as products_table:
            product_reader = reader(products_table)
            return [Product(*item) for item in product_reader]
