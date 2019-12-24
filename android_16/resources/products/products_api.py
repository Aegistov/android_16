from flask.views import MethodView

from android_16.resources.products.products_api_actor import ProductsApiActor


class ProductsApi(MethodView):
    @staticmethod
    def get():
        return {
            'response': ProductsApiActor.get_products()
        }