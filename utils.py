from geojson import Feature, FeatureCollection


def format_query(args):
    query_params = {}
    for arg, value in args.iteritems():
        if not 'price' in arg:
            arg += 'rooms'
        if arg.startswith('min_'):
            arg = arg.lstrip('min_') + "__gte"
        elif arg.startswith('max_'):
            arg = arg.lstrip('max_') + "__lte"
        else:
            continue
        query_params[arg] = value
    return query_params


def create_listing_geojson(listings):
    features = []
    for listing in listings:
        feature = Feature(geometry=listing.location, properties=listing.to_properties())
        features.append(feature)
    return FeatureCollection(features)