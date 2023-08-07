# Booleans and comparison operators
# simplest data type in computer is boolean with two possible values 0 or 1
# in Python we use True or False
# for naming it is a good idea to start boolean with is_something
is_sunny = False
is_raining = True
is_summer = True
is_warm = True

print("It is sunny", is_sunny)
print("Is it raining?", is_raining)
print(f"Is it is summer? {is_summer}")
print(f"Finally, is it warm? {is_warm}")

# technically in Python there is 0 for False and 1 for True underneath
# sometimes that can be useful

# How do we get booleans?
# by using comparison operators
# simplest is == which is equality
print("is 2*2 == 4?", 2*2 == 4) # note double =, this is equality! not assignment!
# we could save result in variable
is_math_good = 3+4 == 7 # evaluation will be right side to left
print("is math good?", is_math_good)
print("Data type of variable is", type(is_math_good))
name = "Valdis"
another_name = "Valdis"
print("Are names equal?", name == another_name)

# we also have greater and lesser than operators
# > greater
a = 2
b = 4
print(f"is {a} > {b} ?", a > b)
# similarly less than
print(f"is {a} < {b} ?", a < b)

# we also have greater and equal >=
print(f"is {a} >= {b} ?", a >= b)
print(f"is {a}*{a} >= {b} ?", a*a >= b)

# similarly we have less than <=
print(f"is {a} <= {b} ?", a <= b)
print(f"is {a}*{a} <= {b} ?", a*a <= b)

# we also have inequality, != means checking for not equal
print(f"is {a} not equal to {b} ?", a != b)
print(f"is {a}*{a} not equal {b} ?", a*a != b) # False because both sides equal

# we can use chains to compare many values
c = 50
d = 100
print(a < b < c < d) # True
print(a < b < d < c) # False

# we also have is for checking memory, less used, but important for more complex structures
# used for checking booleans