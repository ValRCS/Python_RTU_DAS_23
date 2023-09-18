# Sets in Python

# Sets are unordered collections of unique elements
# official docs: https://docs.python.org/3/tutorial/datastructures.html#sets

# Basic uses include membership testing and eliminating duplicate entries. 

# main properties of sets:
# Sets can not have duplicates
# Sets are unordered
# Sets are mutable - can add and remove elements
# Sets can not be indexed

# Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.

# Sets can be created by using the set() function or using curly braces {} - note that empty {} will create a dictionary
# Sets can only contain unique values, so duplicates will be removed

# Let's create a set
unique_letters = set("Valdis Saulespurēns likes programming in Python")
print(unique_letters)

# very quick test for membership - so called hash table lookup - O(1) time - constant time
print("Is there an a in this set?", "a" in unique_letters)
# if we had a list of letters it would be much slower to check for membership
# so sets are great for membership checks
# of course for single membership check there is no point to make a set
# since it would take just as much time to create a set from a list

# but for multiple membership checks sets are great

# in some ways sets have similar properties to dictionary keys

# i can also create set using curly braces
my_food_set = {"potatoes", "cucumber", "tomatoes", "potatoes", "cucumber", "potatoes"}
# note no :, above is a set NOT a dictionary
print(my_food_set) # duplicates are removed # again order is not guaranteed

# we can go back to list by using list() function
# so canonical way to remove duplicates from a list is to convert to set and back
my_shopping_list = ["potatoes", "cucumber", "tomatoes", "potatoes", "cucumber", "potatoes"]
print(my_shopping_list)
my_unique_shopping_list = list(set(my_shopping_list))
print(my_unique_shopping_list)

# sets can store any hashable objects
# so we can store strings, numbers, tuples, frozensets

# we can create a set from a range
numbers = set(range(10))
print(numbers) # this order is not guaranteed!! for small numbers it is usually 0 to 9
# i can update an existing set with more elements
numbers.update([3,1,6,1,55,5,3,9,12,26]) # INC PLACE - modifies the set in place
print(numbers) # so no duplicates are added

# so for dictionaries we use {key:value, k1:v1} pairs
# for sets it is just {elem1, elem2, elem3}

# let's do some set operations
# first some number sets

num_3_7 = set(range(3,8)) # same as set([3,4,5,6,7]) or {3,4,5,6,7}
print(num_3_7)
num_5_9 = set(range(5,10)) # same as set([5,6,7,8,9]) or {5,6,7,8,9}
print(num_5_9)

# let's check if one set is subset of another
print("Is num_3_7 a subset of num_5_9?", num_3_7.issubset(num_5_9)) # so all elements of num_3_7 are in num_5_9
# how about numbers?
print("Is num_3_7 a subset of numbers?", num_3_7.issubset(numbers)) # so all elements of num_3_7 are in numbers
# we have syntactic sugar for subset check
print("Is num_3_7 a subset of numbers?", num_3_7 <= numbers) # so all elements of num_3_7 are in numbers
# so <= is subset check - include sets themselves
# < is proper subset check - does not include sets themselves
print("Is num_3_7 a proper subset of numbers?", num_3_7 < numbers) # so all elements of num_3_7 are in numbers
# finally is num_3_7 proper subset of num_3_7?
print("Is num_3_7 a proper subset of num_3_7?", num_3_7 < num_3_7) # so all elements of num_3_7 are in numbers

# we can go vice versa
print("Is num_5_9 a superset of num_3_7?", num_5_9.issuperset(num_3_7)) # so all elements of num_3_7 are in num_5_9
# again we have syntactic sugar
print("Is num_5_9 a superset of num_3_7?", num_5_9 >= num_3_7) # so all elements of num_3_7 are in num_5_9
# how about numbers?
print("Is numbers set a superset of num_3_7?", numbers >= num_3_7) # so all elements of num_3_7 are in numbers

# lets do some set operations

# union - all elements from both sets
n_3_9 = num_3_7.union(num_5_9) # so we get all elements from both sets
print(n_3_9) # no duplicates
# again we have syntactic sugar
n_3_9 = num_3_7 | num_5_9 # so we get all elements from both sets
print(n_3_9) # no duplicates

big_union = num_3_7.union(range(12)) # so we 2nd set can be any iterable like range or list or char
print(big_union)
big_union = big_union.union("abra")
print(big_union)

# intersection - only elements in both sets
# Latviski - šķēlums

n_5_7 = num_3_7.intersection(num_5_9) # so we get all elements from both sets
print(n_5_7) # no duplicates
# again syntactic sugar - intersection - &
n_5_7 = num_3_7 & num_5_9 # so we get all elements from both sets
print(n_5_7) # no duplicates

# difference - elements in one set but not in the other
# Latviski - starpība
n_3_4 = num_3_7.difference(num_5_9) # so we elements that are in num_3_7 but not in num_5_9
print(n_3_4) # no duplicates
# difference is not symmetric!
# again we have syntactic sugar -
n_8_9 = num_5_9 - num_3_7 # so only elements in num_5_9 but not in num_3_7
print(n_8_9) # no duplicates

# symmetric difference - elements in one set or the other but not both so no common elements
# Latviski - simetriskā starpība

n_3_4_8_9 = num_3_7.symmetric_difference(num_5_9) # so elements unique to one set or the other
print(n_3_4_8_9) # no duplicates
# again we have syntactic sugar ^
n_3_4_8_9 = num_3_7 ^ num_5_9 # so elements unique to one set or the other
print(n_3_4_8_9) # no duplicates

# we can compare it with union of differences
# are union of differences and symmetric difference the same?
print("Union of differences and symmetric difference are the same?", 
      n_3_4.union(n_8_9) == n_3_4_8_9)
