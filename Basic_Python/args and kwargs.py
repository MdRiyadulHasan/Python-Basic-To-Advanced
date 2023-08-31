# *args (Arbitrary Positional Arguments)
# The *args syntax in a function definition allows you to pass a variable number of positional arguments to the function
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3,4,5,6,7,8,9,10)

# **kwargs (Arbitrary Keyword Arguments)
# **kwargs is used to pass a variable number of keyword arguments to a function

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(a=1, b=2, c=3, d = 4, e=5, f=6, g=7)


def combined_function(arg1, arg2, *args, kwarg1=None, **kwargs):
    print("Regular arguments:", arg1, arg2)
    print("Additional positional arguments:", args)
    print("Keyword arguments1:", kwarg1)
    print("Additional Keyword arguments:", kwargs)
    

combined_function(1, 2, 3, 4, kwarg1="Hello", kwarg2="World", kwarg3="World1", kwarg4="World2")
