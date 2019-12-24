import os
from csv import reader

from typing import List

from android_16.resources.products.product import Product


class ProductReader:
    CSV_NAME = f'{os.getcwd()}/android_16/data_store/products.csv'

    @staticmethod
    def get_products() -> List[Product]:
        with open(ProductReader.CSV_NAME, newline='') as products_table:
            product_reader = reader(products_table)
            # We skip the first item because that one contains the column names
            next(product_reader)
            return [Product(*item) for item in product_reader]
