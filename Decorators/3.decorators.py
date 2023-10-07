import time

# Decorator function to measure execution time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"{func.__name__} took {elapsed_time} seconds to execute.")
        return result
    return wrapper

# Apply the decorator to a function
@timing_decorator
def slow_function():
    time.sleep(2)  # Simulate a time-consuming operation

# Call the decorated function
slow_function()
