import logging 
import sys
from os import path

from flask import Flask
from flask_restful import Api

from items_api.resources.items_resource import ItemsResource, ITEMS_ENDPOINT
def create_app():
  logging.basicConfig(level=logging.DEBUG)

  app = Flask(__name__)
  api = Api(app)

  api.add_resource(ItemsResource, ITEMS_ENDPOINT, f"{ITEMS_ENDPOINT}/<id>")

  return app

if __name__ == "__main__":
  app = create_app()
  app.run(debug=True, host='0.0.0.0') #host is needed for container