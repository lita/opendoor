import json
import logging
import traceback

import geojson
import jsonschema
from flask import Blueprint, request, jsonify

from models.listing import Listing
from utils import create_listing_geojson, format_query

blueprint = Blueprint('routes', __name__)

logger = logging.getLogger(__name__)

with open("./schema/listings.json") as f:
    listings_schema = json.loads(f.read())


def validate_messages(content):
    jsonschema.validate(content, listings_schema)


@blueprint.route('/listings', methods=['GET'])
def get_listings():
    try:
        args = {}
        for key, value in request.args.items():
            args[key] = int(value)
        validate_messages(args)
        query_params = format_query(args)
        listings = Listing.objects(**query_params)
        features = create_listing_geojson(listings)
        return geojson.dumps(features)
    except jsonschema.ValidationError as e:
        logger.exception('we got a validation error. params: %s error %s', str(args), repr(e))
        response = jsonify({"error": "invalid input"})
        response.status_code = 400
        return response
    except ValueError as e:
        logger.exception('query params were not a number. params: %s error %s', str(args), repr(e))
        response = jsonify({"error": "invalid input"})
        response.status_code = 400
        return response
    except Exception as e:
        logger.exception('We got an exception. error: %s traceback: %s', repr(e), traceback.format_exc())
        response = jsonify({"error": e.message})
        response.status_code = 500
        return response