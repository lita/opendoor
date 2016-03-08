import json

import geojson
import pytest

from models.listing import Listing

@pytest.fixture
def fake_listings():
    params = {
        "listing_id": 1,
        "street_address": "123 Fake St",
        "status": "pending",
        "bedrooms": 4,
        "bathrooms": 3,
        "square_feet": 3125,
        "location": geojson.Point([112, 33])
    }
    return [Listing(**params)]

@pytest.fixture
def get_listing_json():
     return json.dumps({
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {"type": "Point", "coordinates": [112, 33]},
                "type": "Feature",
                "properties": {
                    "bathrooms": 3,
                    "sq_ft": 3125,
                    "price": None,
                    "bedrooms": 4,
                    "street": "123 Fake St",
                    "id": 1
                }
            }
        ]
    })