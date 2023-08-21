# Sets in Python
# official docs: https://docs.python.org/3/tutorial/datastructures.html#sets

# so sets are unordered collections of unique elements
# Latvian: kopas

# properties of sets
# sets are mutable - we can add and remove elements
# sets are unordered - we can not access elements by index
# sets are unindexed - we can not access elements by index

# primary uses of sets
# membership testing - is element in set or not - very fast - unlike lists/tuples
# removing duplicates from a sequence
# computing mathematical operations such as intersection, union, difference, and symmetric difference

# creating sets
unique_letters = set("abracadabra maģija mana")
print(unique_letters) # note no order
# i could pass a list to set
unique_numbers = set([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,1,3,5])
print(unique_numbers) # it looks ordered but it is not!

# we have membership testing
print(f"Is 3 in {unique_numbers}? {3 in unique_numbers}")
print(f"Is 10 in {unique_numbers}? {10 in unique_numbers}")
# membership testing for sets is fast O(1) constant time operation, just like testing for keys in dictionaries
# membership testing for lists is O(n) linear time operation, we have to go through all elements

# we run out of parenthesis so we use curly braces as well just like in dictionaries
new_set = {1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,1,3,5} # note no : between key and value 
# if i used [] i would get a list
# if i used () i would get a tuple
# if i used nothing i would get a tuple as well

# we can add elements to sets
new_set.add(10)
print(new_set)
new_set.add(10) # we can not add duplicates, nothing happens, NOT an error
print(new_set)

# so let's say I have a list which potentially has duplicates
# i want a new list with no duplicates
# workflow would be:
# create a set from original list
# create a new list from set
# profit!

original_list = [1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,1,3,5]
print(original_list)
unique_set = set(original_list)
print(unique_set)
unique_list = list(unique_set)
# i could have done it in one line as well
# unique_list = list(set(original_list))
print(unique_list)

# my list could have been a list of strings
foods = ["kartupelis", "citrons", "banāns", "kāposti", "kartupelis", "citrons", "banāns", "kāposti", "arbūzs"]
print(foods)
unique_foods = list(set(foods)) # not guaranteed to be in order

print(unique_foods)
# i could have sorted as well
sorted_unique_foods = sorted(set(foods)) # sorted returns a list - guaranteed to be in order
print(sorted_unique_foods)

# now let's do some set operations
numbers = set(range(12))
print(numbers)
# we can update
numbers.update([12,13,14,15,5,1,1]) # IN PLACE update - changes the original set
print(numbers)

# we can remove
numbers.remove(13) # we can remove by value
print(numbers)
# removing again will be an error
try:
    numbers.remove(13)
except KeyError as e:
    print(f"Error {e} happened no such element in set")

# lets make some number sets
num_3_7 = set(range(3,8))
num_5_9 = set(range(5,10))
print(num_3_7)
print(num_5_9)

# lets do set operations
# check if one set is subset of another
print(f"Is {num_3_7} subset of {num_5_9}? {num_3_7.issubset(num_5_9)}")
# how about numbers?
print(f"Is {numbers} subset of {num_5_9}? {numbers.issubset(num_5_9)}")
# reverse
print(f"Is {num_5_9} subset of {numbers}? {num_5_9.issubset(numbers)}")
# we have a shortcut
print(f"Is {num_5_9} subset of {numbers}? {num_5_9 <= numbers}")
# we have a strict subset
print(f"Is {num_5_9} strict subset of {numbers}? {num_5_9 < numbers}")
# strict subset will be False if sets are equal
print(f"Is {num_5_9} strict subset of {num_5_9}? {num_5_9 < num_5_9}")

# we also superset - the other way around
print(f"Is {num_5_9} superset of {num_3_7}? {num_5_9.issuperset(num_3_7)}")
# we have a shortcut
print(f"Is {num_5_9} superset of {num_3_7}? {num_5_9 >= num_3_7}")
# numbers?
print(f"Is {numbers} superset of {num_3_7}? {numbers.issuperset(num_3_7)}")

# we can check for intersection
# so we keep elements that are in both sets 
# Latviski - šķēlums
print(f"Intersection of {num_5_9} and {num_3_7} is {num_5_9.intersection(num_3_7)}")
# shortcut - & - single ampersand
# i can save result in a variable
n_5_6_7 = num_5_9 & num_3_7 # both sides need to be sets
print(n_5_6_7)
# intersection will take any iterable
n_5_6_7 = num_5_9.intersection([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # & will not work with lists
print(n_5_6_7)

# then we can create union
# Latviski - apvienojums
# so unique elements from both sets
print(f"Union of {num_5_9} and {num_3_7} is {num_5_9.union(num_3_7)}")
# again we have a shortcut - | - single pipe
n_3_9 = num_5_9 | num_3_7 # again both sides need to be sets
print(n_3_9)
# i can union with any iterable as well just need to convert to set
funky_set = n_3_9 | set("Valdis")
print(funky_set)

# we can find difference
# difference is what is in one set but not in the other
# Latviski - starpība
print(f"Difference of {num_5_9} and {num_3_7} is {num_5_9.difference(num_3_7)}")
# note difference is not symmetric!!
print(f"Difference of {num_3_7} and {num_5_9} is {num_3_7.difference(num_5_9)}")
# shortcut - -
print(f"Difference of {num_3_7} and {num_5_9} is {num_3_7 - num_5_9}")
# again i can use any iterable
print(f"Difference of {num_3_7} and 5,...,19 is {num_3_7 - set(range(5,20))}")

# finally we have symmetric difference
# Latviski - simetriskā starpība
# so what is in one set or the other but not in both
print(f"Symmetric difference of {num_5_9} and {num_3_7} is {num_5_9.symmetric_difference(num_3_7)}")

# we can check if two sets are disjoint
# Latviski - disjunkti - pilnīgi neatkarīgi
# so if they have no common elements
print(f"Are {num_5_9} and {num_3_7} disjoint? {num_5_9.isdisjoint(num_3_7)}")

# finally we can iterate over sets (order is not guaranteed)
for number in num_5_9:
    print(number)

# if i want to iterate in order i can sort first
for number in sorted(num_5_9): # in effect i am iterating over a list
    print(number)