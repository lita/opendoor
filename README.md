# Listings API
I createad an endpoint that returns a list of GeoJSON objects based on the filters given. The project is deployed on [Heroku](https://lita-listing-app.herokuapp.com/listings). Here is a sample url: https://lita-listing-app.herokuapp.com/listings?min_bed=3&max_bed=5&min_bath=3&max_price=200000

It took me a total of 4 hours to get everything working, with unit tests. Unfortunately, setting up Heroku took more time than expected, as I am not familar with it.

## Python files of Interest
All the endpoints are defined in [routes.py](https://github.com/lita/opendoor/blob/master/routes.py).

The model of a Listing is define in [models/listings.py](https://github.com/lita/opendoor/blob/master/models/listing.py)

## Migrating the CSV Data to MongoDB
I created a [migration script](https://github.com/lita/opendoor/blob/master/listings_migration.py) to insert all the data from the CSV file to MongoDB. This is something I have to run manually once using a one-off dyno. If you were to deploy this yourself to heroku, you will need to run the following commands:
```bash
heroku run bash
<< Once inside the Dyno>>
python manage shell
>> from listings_migration import run
>> run()
```
This will kick off the migration.

## Tests
To run the tests, enter the following command:
```bash
py.test tests/
```

## Technologies Used
I ended up using Flask with Blueprints, JSON Schema for validation, and MongoDB as my datastore. I like Flask with Blueprints, as the routing maps directly onto the function call. I also like JSON Schema, because the [json file](https://github.com/lita/opendoor/blob/master/schema/listings.json) acts like an API documentation. I ended up using MongoDB for the sake of ramp up time. I am familiar with it, and it was really quick to set up. MongoDB also has a geospatial indexes, which might be a useful feature for querying locations of the houses.

## Future Work
If I had more time, I would love to work on pagniation of the results. This would be the highest priority, as the endpoint is really slow. The server is querying and returning a lot of data and definitely not scalable at its current state.

Secondly, I would like to add a neaby feature, where you can give it a lat/lng and a radius, and it will return houses near that area.

Lastly, I would love to add a front-end portion to the API. This would be a lot more work, but I think it would be fun.
