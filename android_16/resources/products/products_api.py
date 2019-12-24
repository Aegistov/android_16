from flask.views import MethodView
from typing import Dict

from android_16.resources.products.products_api_actor import ProductsApiActor


class ProductsApi(MethodView):
    @staticmethod
    def get() -> Dict:
        return {
            'response': ProductsApiActor.get_products()
        }