l = ['eggs', 'eggs', 'bacon', 'eggs', 'bacon']
set(l)
list(set(l))


# Set Comprehensions
from unicodedata import name

{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}





