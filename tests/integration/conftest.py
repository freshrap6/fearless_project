import pytest
from items_api.api import create_app

@pytest.fixture
def client():
  app = create_app()
  app.config["TESTING"] = True

  with app.test_client() as client:
    yield client