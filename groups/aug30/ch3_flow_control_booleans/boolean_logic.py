# let's talk about Boolean logic how to combine our booleans
# https://en.wikipedia.org/wiki/Boolean_algebra

# let's start with the simplest of them all - negation
print(not True)
print(not False)
# unlike other C based languages Python uses English not
# not ! :)

# we can use negation as a toggle
is_raining = False
print("Is it raining?", is_raining)
is_raining = not is_raining
# so we overwrite whatever is_raining had with opposite
print("Is it raining?", is_raining)
# we can toggle/reverse again
is_raining = not is_raining
print("Is it raining?", is_raining)

# logical conjunction - both sides have to be True
# in Python we use English and (not && as in other languages)
print("True and True", True and True)
print("True and False", True and False)
print("False and True", False and True)
print("False and False", False and False)

# Python uses short-circuit evaluation for logic
# for and this means immediately one False statement will make everything
# False and Python stops evaluating the rest
is_long_chain_correct = True and 2*2 == 4 and 3+3 == 6
print(is_long_chain_correct)
divisor = 0
# short circuit can sometimes be useful
# here the last 10 / divisor is not evaluated because 2nd part is false
is_long_chain_correct = 2*2 == 4 and divisor != 0 and 10 / divisor
print(is_long_chain_correct)
# again we can chain many and expressions but as soon as one is False
# the whole chain is False
# so one drop of black tar in honey jar ruins the whole jar...

# finally we have logical disjunction
# this means only ONE of potentially many sides in or chain have to be correct
# again we use English or (not || in many other languages)
print("True or True", True or True)
print("True or False", True or False)
print("False or True", False or True)
print("False or False", False or False)

# so with or , as soon as we get ONE True  then the whole or chain is True
statement = "Something else"
print(True or 2*2 == 4 or 1/0 == 3333 or "Pigs fly" == statement)
# again short-circuit means the first part makes the whole expression
# True so no need to check the rest

# there are secondary operators
# such as XOR - Exclusive OR
# those are not built into Python
# we can create the logic ourselves
# so exclusive or means True when ONLY one side is True
is_sunny = True
my_xor = (is_raining and not is_sunny) or (not is_raining and is_sunny)
print("Is it raining or exclusively sunny?", my_xor)
# so if both sides are True it will be False xor
is_raining = True
my_xor = (is_raining and not is_sunny) or (not is_raining and is_sunny)
print("Is it raining or exclusively sunny?", my_xor)



