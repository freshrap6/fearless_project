import logging

from flask import request, jsonify
from flask_restful import Resource, abort

ITEMS = [
  { 'id': 1, 'name': 'red'},
  { 'id': 2, 'name': 'green'},
  { 'id': 3, 'name': 'orange'}
]

ITEMS_ENDPOINT = "/api/items"
logger = logging.getLogger(__name__)

class ItemsResource(Resource):
  def get(self, id=None):
    if not id:
      return self._get_all_items(), 200

  def _get_all_items(self):
    logging.info("Getting all items")
    return ITEMS
