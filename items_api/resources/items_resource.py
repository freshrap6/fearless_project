import logging
import sqlite3

from flask import request, jsonify
from flask_restful import Resource, abort

ITEMS_ENDPOINT = "/api/items"
logger = logging.getLogger(__name__)

class ItemsResource(Resource):

  def get(self, id=None):
    if not id:
      return self._get_all_items(), 200
    
    try:
      return self._get_item_by_id(id), 200
    except:
      abort(404, message="Item not found")

  def _get_all_items(self):
    logging.info("Getting all items")
    with sqlite3.connect('items.db') as connection:
      cursor = connection.cursor()
      cursor.execute("SELECT * FROM items ORDER BY id desc")
      all_items = cursor.fetchall()
      return all_items

  def _get_item_by_id(self, item_id):
    logging.info(f"Getting item {item_id}")
    with sqlite3.connect('items.db') as connection:
      cursor = connection.cursor()
      cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
      item = cursor.fetchone()
      if not item:
        raise Exception("No Result Found")
    return item

  def delete(self, id=None):
    logging.info(f"Deleting all items")
    with sqlite3.connect('items.db') as connection:
      cursor = connection.cursor()
      cursor.execute("DELETE FROM items")
    return 200

  def put(self, id=None):
    logging.info(f"Updating all items")
    with sqlite3.connect('items.db') as connection:
      cursor = connection.cursor()
      cursor.execute("DELETE FROM items")
      for item in request.json['data']:
        logging.info(f"Adding item: {item}")
        cursor.execute("""INSERT INTO items (name) values(?);""", (item["name"],))
    return "", 200
