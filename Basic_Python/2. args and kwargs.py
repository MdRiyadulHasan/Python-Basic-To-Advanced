def print_arguments(arg1, *args):
    print("First argument:", arg1)
    print("Additional arguments:", args)

print_arguments("hello", "world", "how", "are", "you")

# Output
# First argument: hello
# Additional arguments: ('world', 'how', 'are', 'you')
def print_keyword_arguments(arg1, **kwargs):
    print("First argument:", arg1)
    print("Additional keyword arguments:", kwargs)

print_keyword_arguments("hello", name="Alice", age=30, city="Wonderland")

#output 
# First argument: hello
# Additional keyword arguments: {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
