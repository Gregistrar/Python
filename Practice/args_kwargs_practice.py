"""
*args are arguments
    - args collect extra positional arguments as a tuple
**kwargs are keyword arguments
    - kwargs collect the extra keyword arguments as a dictionary

The * and ** are operators while args and kwargs are just the nicknames.

https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
"""


def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

# Will print the required and the *args
foo('hello', 1 , 2 , 3)

# Will print the required, *args and **kwargs
foo('hello', 1 , 2 , 3 , 4 , key1='value', key2=999)


# First Technique: Write a wrapper function that does something to arguments and passes them on
# This changes the args and kwargs by adding more data
def foo(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra,' )
    bar(x, *new_args, **kwargs)



# Extend the behavior
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

# Takes data that was there
class AlwaysBlueCar(Car):
    def __intit__(self, *args, **kwargs):
        super().__init__(*awgrs, **kwargs)
        self.color = 'blue'


def test_var_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg:", arg

test_var_args(1, "two", 3)



def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call(1, **kwargs)
