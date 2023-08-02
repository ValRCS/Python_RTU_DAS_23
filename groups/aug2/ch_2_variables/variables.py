# we need variables to hold information in all programming languages
name = "Valdis" # so name is a variable identifier
# in Python variables we get automatically
# when we assign something to them
print(name)
# compare with
print("name")

# what are valid names for variables?
# starts with alphanumeric,can have numbers and _ in variable
my_name = "Valdis"
my_age = 49
print("My name is", my_name, " and my age is", my_age)
my_age = my_age - 5 # I found fountain of youth
# so right side is evaluated first!
print("My name is", my_name, " and my age is", my_age)
# what type of data is my_name?
print("my_name is of type", type(my_name)) # so text
print("my_age is of type", type(my_age))
# new_result = my_name + my_age # + does not work for str and int
new_result = my_name + " " + str(my_age) # + does not work for str and int
print(new_result)
# i can use f-strings - so called string interpolation
# introduces in Python 3.6
another_result = f"I am {my_name} and I am {my_age} years old.."
# notice I did not need to use str(my_age) using f-strings
print(another_result)

# so all variables have specific data type
# in Python it can change dynamically
name = 7 # i can do this, not good practice but okay
print(name, type(name))

# name is just a identifier
# here name does not make sense semenatically
# is name allowed to be 7 in some sense?

# similarly
my_age = "Prefer not to answer" # now it will be str
print(my_age, type(my_age))

# better practice is not to change data types for variables
# if you can help it

# naming variables is the is one of the hardest things in programming

# small code fragments can use
# short variables such as a,b,c
# generally you want variables to mean something

# c could be character
# Python has no character data type
c = "A" # still string with one letter
# s could be string for short term use
s = "quick throwaway string"

# generally you want variable names to be correct English

# kaķis = "Vinnijs" # very bad variable name
# print(kaķis) # would work but make life hell for non Latvians

my_cat = "kaķis Vinnijs" # completely okay
print(my_cat)

# there is style guide for variable names in Python
# https://peps.python.org/pep-0008/

# so genrally one or two word variable names
this_very_long_variable_name_is_too_much = "too long"

# for short variables
# x,y,z for coordinates
# f for file objects/streams
# i for looping/iterators
# t for temporary
# other short ones could be okay if they make sense in context

# bad names would be a1, a2, a3 if they do not refer to paper sizes :)

# so we could change any data type to string with str(my_data)
name_str = str(name) # if name was str nothing would happen
print(name_str)
my_text = "9001"
my_number = int(my_text) # so if text is an actual number
print(my_number)
# what happens if we give regular text to int?
# we get error
# i_am_not_a_number = int(my_name) # will not work

# there is floating point for numbers with  comma( . in english)
my_float = 10/4
print(my_float, "is of type", type(my_float))





