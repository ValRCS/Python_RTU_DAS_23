# Boolean data type and comparison operators
# Boolean data type is the simplest data type of all
# represents 1 or 0 (yes or no, red or black, etc etc), no Maybe :)
# it is convention to prefix boolean variables with is (or are)
is_sunny = False # note we use Capitalize False and True
is_warm = True
is_summer = True
is_raining = False

print(is_sunny, is_warm, is_summer, is_raining) # hard to say which one is which

# for debugging Python 3.8 lets us use = inside f-string {}
# = lets us print both name of variable and value
print(f"Debugging: {is_sunny=} and {is_summer=}")
# before i would have to do this
print(f"Debug: is_warm={is_warm} and is_raining={is_raining}")

# so how do we get booleans?
# one of the most common ways is to use comparision operators

print(2*2 == 4) # note == not single = !!
print(2*2 == 5)
print(f"2*2==4? Answer: {2*2==4}")
print(f"2*2==5? Answer: {2*2==5}")

# we can store the result of our comparison in a variable
a = 2
b = 3
c = 6
is_math_sane = a*b == c # assignment will be last
# so = is assignment
# == is equality operator
# we could use ( ) if we are afraid of order
print(f"So {a}*{b} == {c} ? Answer: {is_math_sane}")

# we also have inequality
print("2+2 != 10 ?", 2+2 != 10) # True
# compare with equality
print("2+2 == 10 ?", 2+2 == 10) # False

print(f"So {a}*{b} != {c} ? Answer: {a*b != c}")

# we also have greater than >
print(f"So {a}*{b} > {c} ? Answer: {a*b > c}")
print(f"So {a}+{b} > {c} ? Answer: {a+b > c}")

# however we also have less than <
print(f"So {a}+{b} < {c} ? Answer: {a+b < c}")
print(3 < 1) # False

# we also have greater or equal >= (write exactly >= NOT =>....)
print(f"So {a}*{b} >= {c} ? Answer: {a*b >= c}")
print(f"So {a}+{b} >= {c} ? Answer: {a+b >= c}")

# finally we have less or equal
print(f"So {a}*{b} <= {c} ? Answer: {a*b <= c}")
print(f"So {a}+{b} <= {c} ? Answer: {a+b <= c}")

# we also have way of chaining multiple operators
print(f" {a} < {b} < {c} ? {a < b <c}")
# in above we compared a < b AND b < c only if both are true result is True
# we can chain more
d = 100
print(a < b < c < d)
# one bad apple will ruin the whole chain..
print(a < b < c < d < a)
# chaining works on other comparisions too

# we can compare strings
name = "Valdis"
other_name = "Voldemārs"
print(name < other_name) # True but why?
# a bit of red herring the length
# answer: lexicographical values
# V is equal for both variables
# but a < o
# for ASCII values ( and thus also Unicode values )
print(ord("a"), ord("o"))
# for non English letters the ord values will be higher
print(ord("ā"), ord("Ā"))

# so we can compare similar data types
# any numeric types can be compared
# or strings
# or any other objects which have comparison operator methods implemented


