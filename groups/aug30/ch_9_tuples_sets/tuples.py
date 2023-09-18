# so tuples - immutable lists
# so what is the difference between lists and tuples?

# lists are mutable - we can change them
# tuples are immutable - we can not change them
# tuples are faster than lists - slightly
# tuples use less memory than lists - slightly
# tuples can be used as keys in dictionaries - lists can not

# philosophically
# tuples are used for heterogeneous data - mixed type of data
# list for homogeneous data - same type of data
# Python does not enforce this but it is a good practice

# Latvian
# tuples - korteži

# so let's create a tuple
# we use round brackets () to create a tuple
# we can also use tuple() function to create a tuple
my_tuple = ("Valdis", "programmer", 99, "Rīga", True, 3.14159) # so we can mix types
# parentheses are optional actually for tuples
my_other_tuple = "Valdis", "programmer", 99, "Rīga", True, 3.14159 # so we can mix types
# again two different tuples have been created, just same contents

# all normal non mutable operations for lists are available for tuples
# so we can get length
print("My tuple length is", len(my_tuple))
# existance check
print("Valdis" in my_tuple)
# indexing
print(my_tuple[0])
# slicing
print(my_tuple[1:3]) # 2nd to 3rd element, 4th element(index 3)is not included

# we can iterate over tuples
for item in my_tuple:
    print(item)

# count method
print(my_tuple.count("Valdis")) # duplicates are counted
# index method
print("Rīga index is at", my_tuple.index("Rīga")) # returns first index of the element

# i can not change contents of a tuple
try:
    my_tuple[2] = "lecturer"
except TypeError as err:
    print(err)

# we could use the concatenation approach to change
new_tuple = my_tuple[:2] + ("lecturer",) + my_tuple[3:] # note the comma after lecturer
# we needed that comma to make it a tuple else it would be just a string which can not be concatenated
print(new_tuple)
# old is not changed
print(my_tuple)

# alternative we could have converted to list and back
new_list = list(my_tuple)
new_list[2] = "lecturer" # so change for list is possible
another_tuple = tuple(new_list) # back to tuple to fix immutability
print(another_tuple)

# tuples can be unpacked and packed
# so we can assign tuple contents to variables
name, job, age, city, is_tall, pi = my_tuple
print(name)
print(job)
print(pi)

# this leads to a nice way to swap variables
a = 10
b = 20
print(a, b)
a, b = b, a # so we swap values without temp variable
# eval is from right side
# we create a tuple from b,a and unpack it to a,b
print(a, b)

# so tuples as dictionary keys
person = ("Valdis", "Rīga", "programmer")
doctor = ("Valdis", "Rīga", "doctor")
phone_book = {person: "123-456", doctor: "456-789"}

print(phone_book)
# so we can not use lists as keys but tuples are fine

# so when we extract items from dictionaries we get list of tuples

my_items = list(phone_book.items())
print(my_items)

# so how would I get doctor here
print(my_items[1][0][2]) # so we get doctor
# so 2nd element of the list is a tuple
# 1st element of that tuple is a tuple
# 3rd element of that tuple is doctor string

# tuples are used to return multiple values from functions

def get_name():
    # here goes some logic
    return "Valdis", "Vītoliņš" # returns a tuple

name, surname = get_name() # so we unpack tuple to variables
full_name_tuple = get_name() # so we can get tuple
print(name, surname)