from items_api.resources.items_resource import ITEMS, ITEMS_ENDPOINT

def test_get_all_items(client):
  response = client.get(f"{ITEMS_ENDPOINT}")
  assert response.status_code == 200
  assert len(response.json) == 3