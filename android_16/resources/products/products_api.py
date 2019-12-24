from flask.views import MethodView

from android_16.resources.products.product import Product
from android_16.resources.products.product_reader import ProductReader


class ProductsApi(MethodView):
    @staticmethod
    def get():
        resp = [Product.serialize(item) for item in ProductReader.get_products()]
        print(f'MMOREL {resp}')
        return {
            'response': resp
        }