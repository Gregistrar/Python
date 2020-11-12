# Tuples as records
lax_coords = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

# Tuple unpacking
lax_coords = (33.9425, -118.408056)
lat, long = lax_coords
lat, long = long, lat


# Named Tuples
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.98, (35.65555, 139.4566))
tokyo  # equals City(name='Tokyo', country='JP', population=36.98, coordinates=(35.65555, 139.4566))
tokyo.country  # equals 'JP'
City._fields  # equals ('name', 'country', 'population', 'coordinates')


test_tuple = ('one', 'two')
lax_coords.__add__(test_tuple)



