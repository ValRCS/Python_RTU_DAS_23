# let's talk about functions in Python

# functions are a way to group code together
# ideally functions should do one thing and do it well - Platonic ideal
# in practice functions can do multiple things
# generally if we see a function that is longer than one screen, it is doing too much

# so key advantages of functions:
# 1. Reusability - we can use the same function in multiple places
# 2. Readability - we can give a name to a block of code and use that name instead of the code
# 3. Modularity - we can change the implementation of a function without changing how we use it
# 4. Abstraction - we can hide the details of how a function works and just use it
# 5. Testing - we can test a function in isolation
# 6. Debugging - we can debug a function in isolation
# 7. Maintainability - we can change the implementation of a function without changing how we use it see 3

# DRY principle - Don't Repeat Yourself - if you find yourself copy pasting code, you should probably use a function

# first we already have been using functions
# print is a function
# input is a function
# len is a function
# range is a function
# sum is a function
# list is a function
# str is a function

# we call functions using function call syntax - function_name(arguments)

# so let's create the simplest function that does absolutely nothing

def dummy_function():
    # TODO solve climate crisis
    pass # pass is a keyword that does nothing, we need it because we can't have empty functions

# we might want to write empty functions when we do not know what we want to do yet

# let's createa  function to drink beer

def drink_beer(): # note the colon again we will signficant whitespace next
    # go to the fridge
    print("going to the fridge")
    print("opening the fridge")
    print("drinking beer")
    print("closing the fridge")
    # note note 100% great name since we are also going to the fridge

# we can call the function otherwse it will not run
drink_beer()
# i could do it say 3 times
for _ in range(3):
    drink_beer()

# often we want some parameters to our functions
# let's make a generic drink function
try:
    drink("beer") # i can't call function before it is defined
except NameError as e:
    print("drink function does not exist yet")
    print(e)

def drink(liquid): # so liquid is a parameter, kind of like a variable used INSIDE the function only
    print(f"drinking {liquid}")
    print("that was pretty good")
    print(f"i drank {liquid}")

drink("beer")
drink("water")
drink("coffee")
drink("tea")

# next we can create a function that drinks from a provided list of liquids/drinks

def drink_from_list(liquids):
    print(f"We have {len(liquids)} drinks")
    for liquid in liquids:
        drink(liquid)

drink_list = ["beer", "water", "coffee", "tea", "wine", "milk", "juice"]
drink_from_list(drink_list)

print("I am quite full now")

# we can creata functions with more than one parameter

def drink_n_times(liquid, n):
    for _ in range(n):
        drink(liquid)

drink_n_times("beer", 3)

# note that Python does not enforce types on parameters
# we will have hints later

# now we can have a function that returns a value

def get_drink():
    # there could be more logic here
    return "beer" # abstracting away the details of how we get the drink

my_drink = get_drink()
print(f"I got {my_drink}")

# usually we will have parameters to our functions and return a value

# mix two drinks together
def mix_drinks(drink1, drink2):
    # i could do more stuff here
    return f"{drink1} mixed with {drink2}"

# in come two drinks out comes one drink - string concatenation

mixed_drink = mix_drinks("beer", "wine")
print(f"I obtained {mixed_drink}")

# let's see how we can add 3 values together
# i can add so called type hints - just hints not enforced!
def add3(a:int, b:int, c:int) -> int:
    """Adds 3 values together
    Args:
        a (int): first value
        b (int): second value
        c (int): third value
    Returns:
        int: sum of a, b, c
    Example:
        result = add3(1,2,10)
    """	# automatically generated docstring
    # good for documentation and help
    # we could even add some example in docstring
    return a + b + c

print(add3(1, 2, 3))

# side note parameters vs arguments
# parameters are the variables in the function definition
# arguments are the values we pass to the function
# we often use interchangeably


print(add3("Valdis", " ", "is getting thirsty"))
# turns out Python Type Hints are optional
# Python itself does not use them
# only special tools so called linters use them

result = print("Something") # result will be None!!!
print(result)
# if we want to save results from our function we need to return something

# finally default values
# often we can speed up work by using sane default values for function parameters
# we can always override them later
# we need to have default values at the end of our parameter list

def multiply(a, b=2, debug=False): # debug is just a parameter name just like a and b
    result = a * b
    if debug:
        print(f"Multiplying {a} and {b} and got {result}")
    return result

# idea is that we will often multiply by 2 so we can save some typing
print(multiply(10)) # 20 because b is 2 by default
print(multiply(10, 25)) # 250 because we overrode the default value of b
# helpful if we need to modify existing functions but do not want to break existing code
# let's say i want to add debugging to function
# i can add a debug parameter with default value False

# now i can debug my function if needed
print(multiply(10, debug=True))
print(multiply(10, 25, debug=True))
# theoretically i could mix an match but that would be confusing
print(multiply(b=10, debug=True, a=33)) # please don't do this
# in practice some functions have so many parameters that we need to use keyword arguments
# for print lets say you do not need to remember if sep or end is first
print("Valdis", "is", "getting", "thirsty", sep="__", end="!!!\n")

# TODO how to handle unlimited arguments to a function - next time
