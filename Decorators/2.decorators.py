# Decorator function
def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        # Log the function name and its arguments
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log the result of the function
        print(f"{func.__name__} returned: {result}")
        
        return result
    
    return wrapper

# Applying the decorator to a function
@log_args_and_result
def add(a, b):
    return a + b

# Applying the decorator to another function
@log_args_and_result
def multiply(a, b):
    return a * b

# Using the decorated functions
result1 = add(3, 5)
result2 = multiply(4, 6)

print("Addition", result1)
print("Multiplying", result2)

