import json

import geojson

from models.listing import Listing
from utils import format_query, create_listing_geojson
from tests.unit.fixtures import fake_listings, get_listing_json

def test_format_query():
    args = {
        "min_price": 5,
        "max_price": 8,
        "min_bed": 9,
        "max_bed": 11,
        "min_bath": 1,
        "max_bath": 2
    }

    expected_args = {
        "price__gte": 5,
        "price__lte": 8,
        "bedrooms__gte": 9,
        "bedrooms__lte": 11,
        "bathrooms__gte": 1,
        "bathrooms__lte": 2
    }

    result = format_query(args)

    assert cmp(expected_args, result) == 0


def test_create_listing_geojson():
    params = {
        "listing_id": 1,
        "street_address": "123 Fake St",
        "status": "pending",
        "bedrooms": 4,
        "bathrooms": 3,
        "square_feet": 3125,
        "location": geojson.Point([112, 33])
    }

    expected_json = get_listing_json()
    listing = Listing(**params)
    assert expected_json == geojson.dumps(create_listing_geojson([listing]))