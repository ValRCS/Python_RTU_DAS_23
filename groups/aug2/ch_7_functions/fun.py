# let's talk about functions in Python

# what is a function - a named sequence of statements that performs a computation
# functions let us break down programs into smaller chunks
# functions can be reused
# ideally functions should be short and do one thing
# in practice functions can be long and do many things

# advantages of functions
# 1. Reusability - we can reuse functions in other programs
# 2. Decomposition - we can break down complex problems into smaller chunks
# 3. Readability - we can give meaningful names to functions
# 4. Testing and Debugging - we can test functions separately from the rest of the program
# 5. Maintainability - we can modify functions without affecting other parts of the program


# we have already used some functions
# print() is a function - print("Hello")
# input() is a function - input("Please enter your name")
# len() is a function - len("Valdis")
# range() is a function - range(10)
# type() is a function - type(10)
# sorted() is a function - sorted([5, 2, 3, 1, 4])
# we did not check too much a few other functions
# built-in functions https://docs.python.org/3/library/functions.html
# reminder on min, max, and sum functions
number_list = list(range(10))
print(number_list)
print(f"Min is {min(number_list)}")
print(f"Max is {max(number_list)}")
print(f"Sum is {sum(number_list)}")

# let's create our own functions

# let's create a function that does nothing
# could be useful for stubbing out functions - stub means a placeholder
def do_nothing():
    # TODO implement this function
    pass # empty instruction, not needed if we do anything in the function

# let's create a function to drink a beer

def drink_beer(): # notice the colon
    print("Drinking beer")
    print("Burp")
    print("Feeling good")

# nothing happens unless we call the function
drink_beer() # notice the parentheses
# i can do this multiple times
for _ in range(3): # note use of _ to indicate I do not care about the value
    drink_beer()

# a more useful would be a generic function to drink anything
# 
def drink(liquid): # liquid is a parameter - local to the function
    print(f"Drinking {liquid}")
    print(f"Ahh, {liquid} was good")
    print("I am done drinking")

# now I can pass any liquid to drink function
drink("Beer")
drink("Water")
# my function does not check if I am passing a string
# i could drink numbers in this case
drink(10)

# let's create a list of drinks
drinks = ["Beer", "Water", "Milk", "Juice", "Wine", "Tea", "Coffee"]
# we can loop over the list and drink each drink
for drink_item in drinks:
    drink(drink_item) # we are passing a string drink_item to drink function


# we can make a function that takes a list and drinks each item
def drink_from_list(drink_list):
    # let's print how much I need to drink
    print(f"I have {len(drink_list)} drinks to drink")
    for drink_item in drink_list:
        drink(drink_item)

# let's drink first 3 drinks from our list
drink_from_list(drinks[:3]) # we are passing a list to drink_from_list function

# functions generally should have verb names - perform_action etc.

# let's create a function that returns a value
# we can return a value from a function

def add_two_numbers(a, b):
    # i could add some checks here
    return a + b

my_result = add_two_numbers(10, 20)
print(my_result)
print(add_two_numbers(100, 200))
# common mistake is to forget to use return statement
not_result = print(add_two_numbers(100, 200)) # print returns None
# print is a classical example of a procedure - it does not return anything
# Python does not have procedures, but we can create functions that do not return anything
# if we do not use return statement, then function returns None
print(not_result) # None

# compare with display adding two numbers
def display_add_two_numbers(a, b):
    print(a + b)
    # returns None so we can not save the result

not_result = display_add_two_numbers(100, 200)
print(not_result) # None - None is special value in Python representing nothing
print(5+10)
print() # empty print newline

# let's make a function with default parameters
def multiply(a, b=2, debug=False):
    if debug:
        print(f"Multiplying {a} and {b}")
    return a * b

print(multiply(10, 20)) # works normally
print(multiply(10)) # uses default value for b
print(multiply(10, debug=True)) # uses default value for b, using named parameter debug
# technically I could mix named parameters 
print(multiply(10, debug=True, b=20)) # uses default value for b, using named parameter debug
# above is not recommended, but it is possible

# i could make a function with ALL default parameters
def multiply_default(a=1, b=2, debug=False):
    if debug:
        print(f"Multiplying {a} and {b}")
    return a * b

print(multiply_default()) # uses default values for a and b
print(multiply_default(debug=True)) # uses default values for a,b

# I can make a function that takes unlimited number of parameters
# i use * notation to indicate that I will be passing multiple parameters
def multiply_all(*numbers):
    print(numbers)
    result = 1
    for number in numbers:
        result *= number # same as result = result * number
    return result

print(multiply_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# no arguments
print(multiply_all())

# i can make a funtion with multiple parameters and then named parameters
def multiply_all_with_debug(*numbers, start = 1, debug=False):
    if debug:
        print(numbers)
    result = start
    for number in numbers:
        result *= number # same as result = result * number
    return result

print(multiply_all_with_debug(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# with debug
print(multiply_all_with_debug(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, debug=True))
print(multiply_all_with_debug(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, start = 5_000, debug=True))

# compare with a function that takes a list
def multiply_all_with_debug_list(number_list, start = 1, debug=False):
    if debug:
        print(number_list)
    result = start
    for number in number_list:
        result *= number # same as result = result * number
    return result

import math
print(math.factorial(10)*5_000)

# functions can have docstrings that describe what the function does
def subtract(a, b):
    """Subtracts b from a"""
    # so any text with triple quotes is a docstring right after the function definition
    return a - b

print(subtract(10, 5))

# in a docstring we would describe what the function does
# talk about parameters and return values
# we can use docstrings to generate documentation for our code

def format_name(first_name, last_name):
    """Formats first and last name into a string
    Parameters:
    first_name - first name
    last_name - last name
    Returns:
    formatted string"""
    # here we can see that good parameter names are self-documenting
    return f"{last_name}, {first_name}"

# compare function with a,b,c parameters with no docstring
def format_name2(a, b, c):
    return f"{c}, {a}, {b}" # this is a bad function!!!
# should refactor with better parameter names
# also provide a docstring
# explain why we need this function to format names

# so parameters vs arguments
# parameters are defined in the function definition
# arguments are passed to the function when we call it
# in practice we use these terms interchangeably