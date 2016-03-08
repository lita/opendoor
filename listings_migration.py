import csv

from models.listing import Listing


def run():
    with open('./listing-details.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        count = 0
        for row in reader:
            row['location'] = [float(row['lng']), float(row['lat'])]
            row.pop("lng", None)
            row.pop("lat", None)
            listing = Listing(**row)
            listing.save()
            count += 1
            print "saved %d items" % (count)