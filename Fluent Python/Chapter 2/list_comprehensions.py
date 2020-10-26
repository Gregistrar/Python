
# First method to generate the list of codes for the symbols
symbols = '$¢£¥'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
codes  # equals [36, 162, 163, 165]


# Second method, a faster way to generate code symbols
codes = [ord(symbol) for symbol in symbols]
codes  # equals [36, 162, 163, 165]


# Listcomps no longer leak their variables
x = 'ABC'
test = [ord(x) for x in x]
x  # equals 'ABC'


# Listcomps vs filter
ascii_key = [ord(s) for s in symbols if ord(s) > 127]
ascii_key = list(filter(lambda c: c > 127, map(ord, symbols)))


# Cartesian products
colors = ['green', 'blue']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
tshirts  # [('green', 'S'), ('green', 'M'), ('green', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]




