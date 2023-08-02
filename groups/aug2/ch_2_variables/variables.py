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

