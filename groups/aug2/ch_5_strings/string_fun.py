print("Let's talk about strings!")
# What is a string after all?

# A string is a sequence of characters
# Python does not have a character data type
# Even a single character is a string

# strings are immutable
# once we make a string, we cannot change it
# we can only make new strings or possiblye overwrite the old one

# let's make some strings
food = "pizza"
print(food)
print(type(food))
drink = "water"
print(drink)
# i can change it to say kefir
drink = "kefir"
print(drink)

# we can concatenate strings
# we can use the + operator to concatenate strings
food_drink = food + " goes well with " + drink
print(food_drink)
# we can use the * operator to repeat strings
print(food * 3)

# we also have f-string formatting
food_and_drink = f"{food} goes well with {drink}"
print(food_and_drink)

# strings can be used with double or single quotes
# in Python there is no difference between the two
# but you can use one or the other to make it easier to use quotes in your strings

# for example
# this is a string with double quotes
print("I'm a string with double quotes") # note single quote in string
# how about single quotes?
print('There is a "quote" in this string')
# with single quotes I'd need to escape the single quote
print('\'m a string with single quotes for double "quotes" i do not need escaping')

# so we use \ for escaping special characters

# common escape characters
# \n - newline
# \t - tab
# \\ - backslash - represents a single backslash
# \' - single quote
# \" - double quote
# docs with full list: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals

# we can also use triple quotes to make multi-line strings
# or just to make a string with single or double quotes in it
# for example
multi_line_string = """This is a multi-line string
I can write whatever I want in it such as "quotes" or 'quotes'
I can use \t or i can just use tab directly or newline\n
This will have two newlines after it\n\n
"""
print(multi_line_string)

# i can use triple quotes with f-strings
# for example
food = "potatoes"
recipe = f"""{food} goes well with {drink}
I can also use {food} to make a {food} pie
And so on and so forth
"""
print(recipe)

# finally we have raw strings
# raw strings are prefixed with r
# raw strings ignore escape characters
raw_string = r"This is a raw string\n no newlines" # \n will be printed as is
print(raw_string)
# raw strings are useful for regular expressions which use a lot of backslashes
# otherwise we'd have to write \\\\ instead of \\ to represent a single backslash
# also useful for windows file paths