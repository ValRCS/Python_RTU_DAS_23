# once we have booleans we can perform operations
# this is the only math you should know to program
# https://en.wikipedia.org/wiki/Boolean_algebra

# simplest negation
# in Python we use English not ( unlike  many other languages using !)
print(not True)
print(not False)
# we can use not for toggle (on/off/on/off etc)
is_sunny = False
print("Is it sunny?", is_sunny)
is_sunny = not is_sunny # so we reverse whatever was inside
print("Is it sunny?", is_sunny)
is_sunny = not is_sunny # so we reverse whatever was inside
print("Is it sunny?", is_sunny)
is_sunny = not is_sunny # so we reverse whatever was inside
print("Is it sunny?", is_sunny)

# then we have logical conjuction
# again in Python we use English and (not && which is other languages use)
print(True and True) # both sides have to be True for whole thing to be true
print(True and False) # thus False
print(False and True) # again False
print(False and False) # False

# Python uses lazy evaluation - short circuit evaluation
# means first False will stop evaluation of and chain
# one drop of oil spoils the honey principle
a = 4
d = 0 
print(True and 2*2 == 4 and d != 0 and a / d == 9999)
# so a/d was not evaluated because 3rd d != 0 was False
print(a > d and d * 5 == 0 and a * a  == 16)

# finally from essentials we have logical disjunction
# at least one sides should be True for the whole thing to be True
# Python uses English or (not || used by many other languages)
print("Logical Disjuction with or")
print(True or True)
print(True or False)
print(False or True)
print(False or False) # False

# again Python is lazy, short circuit one True in or chain will make whole thing True
# so Python stops
print(a == 100 or d == 0 or a / d == 555) # so last one will not be checked
# if a == 100 or d == 0

# XOR - exclusive OR is not implemented in Python
# we can implement it as follows
# meaning we want whole thing to be True if ONLY one side is True
is_sunny = False
is_summer = True
my_xor = (is_sunny and not is_summer) or (not is_sunny and is_summer)
