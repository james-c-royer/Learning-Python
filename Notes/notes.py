# function declaration:
def happy_Birthday(name):
    print(f"Happy birthday {name}! Happy birthday to you!")

# name is a parameter: a temporary variable used in the function
your_name = "Greg"

# calling a function
happy_Birthday(your_name)

# functions can use a "return" statement to return a value
def div(numerator, denominator):
    return numerator / denominator

num = int(div(4,2))

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

def hello(greeting, title, first, last):
    print(f"{greeting} {title}.{first} {last}")

# this is a function call with keyword arguments.
hello("Hello", title="Mr",first="James",last="Royer")

# cannot rearrange parameters - produces an error
hello(first="Bob",greeting="Hello","Mrs", "Gary")