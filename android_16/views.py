from android_16 import app
from android_16.resources.products.products_api import ProductsApi

app.add_url_rule(
    '/v1/products', view_func=ProductsApi.get, methods=["GET"]
)


@app.route('/')
def index():
    return 'Hello World!'
