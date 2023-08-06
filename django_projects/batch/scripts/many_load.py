import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        cat, created = Category.objects.get_or_create(name=row[7])
        state, created = State.objects.get_or_create(name=row[8])
        iso, created = Iso.objects.get_or_create(name=row[10])
        region, created = Region.objects.get_or_create(name=row[9])

        try:
            year = int(row[3])
        except:
            year = None

        try:
            lon = int(row[4])
        except:
            lon = None

        try:
            lat = int(row[5])
        except:
            lat = None

        try:
            area = int(row[6])
        except:
            area = None

        site = Site(name=row[0], description=row[1], justification=row[2],
                    year=year, longitude=lon, latitude=lat, area_hectares=area,
                    category=cat, region=region, iso=iso, state=state)
        site.save()