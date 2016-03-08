import geojson
import pytest

from app import create_app
from models.listing import Listing
from tests.unit.fixtures import fake_listings, get_listing_json


@pytest.fixture
def test_client():
    application = create_app()
    return application.test_client()


def test_get_listings_value_error(test_client):
    resp = test_client.get('/listings?max_price=not_number')
    assert resp.status_code == 400


def test_get_listings_correct(test_client, mocker):
    mock_db = mocker.patch("routes.Listing")
    mock_db.objects.return_value = fake_listings()
    resp = test_client.get('/listings')
    assert resp.status_code == 200
    assert resp.data == get_listing_json()
