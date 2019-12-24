from typing import Dict, List

from android_16.resources.products.product import Product
from android_16.resources.products.product_reader import ProductReader


class ProductsApiActor:
    @staticmethod
    def get_products() -> List[Dict]:
        return [Product.serialize(item) for item in ProductReader.get_products()]