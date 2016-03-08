from models import db


class Listing(db.Document):
    listing_id = db.IntField(primary_key=True, unique=True, required=True)
    street_address = db.StringField()
    status = db.StringField()
    price = db.IntField()
    bedrooms = db.IntField()
    bathrooms = db.IntField()
    square_feet = db.IntField()
    location = db.PointField()
    meta = {
        'indexes': [
            'bedrooms',
            'bathrooms',
            'price'
        ]
    }

    def to_properties(self):
        """
        Return a dictionary with just the properties. This is to help generate
        the Feature of the GeoJSON.
        :return dict:
        """
        return {
            "id": self.listing_id,
            "price": self.price,
            "street": self.street_address,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "sq_ft": self.square_feet
        }