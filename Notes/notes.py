# a decorator function will take a function as an argument
def add_sprinkles(func):
    # inner "wrapper" function that calls the original function
    def wrapper(*args, **kwargs):
        print("Adding sprinkles...")
        func(*args, **kwargs)
    return wrapper
    
def add_fudge(func):
    # wrapper function must take boths *args and **kwargs
    # to prevent type errors
    def wrapper(*args, **kwargs):
        print("Adding fudge...")
        # same with the func call
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Your ice cream ({flavor}) is here!")

get_ice_cream("vanilla")
