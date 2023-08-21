# tuples in Python are basically immutable lists

# some properties of tuples
# tuples are immutable - size can not be changed
# tuples are ordered - we can access elements by index
# slicing works on tuples
# tuples can contain any type of object
# tuples can contain duplicates
# tuples can be nested inside other tuples, lists, dictionaries
# tuples are faster than lists
# tuples use less memory than lists - slightly less
# tuples can be used as keys in dictionaries - fixed size

# philosophically tuples are for fixed size collections
# also for heterogeneous collections - meaning all kinds of different objects, different types
# lists are better for homogeneous collections - meaning all objects are of same type, ints, strings, etc.

new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9) # parentheses are optional
print(new_tuple)
also_tuple = 3, "Valdis", True, 3.1415 # parentheses are optional
print(also_tuple)

# some uses of tuples
# return as values from functions
def min_max(numbers):
    return min(numbers), max(numbers) # we return a tuple (size 2)

print(min_max([3,2,6,1,1,2,-111,5]))

# tuple packing and unpacking
# we can assign multiple variables at once
a, b, c = 1, 2, 3 # so we are packing 1,2,3 into a tuple and then unpacking into a,b,c
print(a, b, c)
# we can swap variables - without temp variable
a, b = b, a # right eval first, we are packing b,a into a tuple and then unpacking into a,b
print(a, b, c)
# works on larger tuples as well

# we can use tuples as keys in dictionaries
person = "Valdis", 45, "brown" # tuple packing of 3 values
print(person)
# i can use this as key in dictionary
people = {person: "programmer, very dangerous"}
print(people)
# of course we can add more persons to our dictionary
people["John", 33, "blonde"] = "programmer, nice guy"
# so key is tuple and value is string in this case
print(people)
# so whole tuple is key


# partial unpacking
# we can use * to capture the rest of the values
long_tuple = tuple(range(20))
print(long_tuple)
first, second, *middle, last = long_tuple # *middle will capture all values in the middle as a list
print(first, second, middle, last)

# of course I could have use regular slicing
first, second, middle, last = long_tuple[0], long_tuple[1], long_tuple[2:-1], long_tuple[-1]
print(first, second, middle, last) # slight difference we get a tuple in the middle

# we get tuples from dictionary items
tuple_list = list(people.items())
print(tuple_list)
# so here we have a list of tuples, and those tuples have 2 values of key and value
# here key also happens to be a tuple
# so getting blonde 
print(tuple_list[1])
print(tuple_list[1][0])
print(tuple_list[1][0][2]) # we get the second tuple, then first value of that tuple, then third value of that tuple

# tuples have only two methods count and index, which are similar to list methods
print(person.count("brown")) # 1
print(person.index("brown")) # 2 # 3rd item in tuple
try:
    print(person.index("blonde")) # will fail
except ValueError:
    print("blonde not found")

# for extra credit:
# if we have mutable values in our tuple we can change contents of those values but not the tuple itself

# finally we can have an tuple with 1 element
single_tuple = (1,) # note the comma
print(single_tuple)
# where to use this, when you need to pass a tuple to a function
# or when you need to unpack a tuple with 1 element
# empty tuple exists as well
empty_tuple = ()
print(empty_tuple)
# not much you can do with empty tuple, just pass it or convert to list and add values