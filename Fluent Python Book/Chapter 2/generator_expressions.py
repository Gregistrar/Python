import array

symbols = '$¢£¥'
tuple(ord(symbol) for symbol in symbols)

# Initializing a tuple and array from a genexp
array.array('I', (ord(symbol) for symbol in symbols))

# Cartesian product genexp
colors = ['green', 'blue']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)




