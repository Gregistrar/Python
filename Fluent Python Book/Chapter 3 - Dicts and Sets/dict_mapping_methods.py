test_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

test_dict.keys()
test_dict.clear()
test_dict.__len__()
test_dict.pop('one')
test_dict.items()
test_dict.__delitem__('two')
test_dict.values()


# Various ways to implement a dictionary
A = dict(one=1, two=2, three=3)
B = {'one': 1, 'two': 2, 'three': 3}
C = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
D = dict([('one', 1), ('two', 2), ('three', 3)])

D['five']
D.get('five')


# defaultdict example
from collections import defaultdict

def def_value():
    return "Not Present"

d = defaultdict(def_value)
d['a'] = 1
d['c']
'b' in d
