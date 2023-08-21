# let's talk about Python dictionaries
# docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# why would we need a dictionary if we have a list?
# let's say we have a list of students
students = ["Jānis", "Janīna", "Bruno", "Alise"]
# and we want to store their grades
# we could do it like this
grades = [10, 8, 9, 7]
# then we would get grades and names using indexes
# so first student name and grade
print(students[0], grades[0])

# so dictionaries allow us to store data in key-value pairs
# this let us access data using keys instead of indexes
# lookup by key is constant time O(1) even in a large dictionary

# so let's create a dictionary
grade_dict = {"Jānis": 10, "Janīna": 8, "Bruno": 9, "Alise": 7} # note curly braces
# so we can access data using keys
print(grade_dict["Jānis"]) # prints 10 - very fast even in a large dictionary

# dictionary is called associative array in other languages, hash map, hash table

# main properties of a dictionary
# 1. unordered - items are not stored in any particular order
# 1.b - in Python 3.7+ dictionaries keep insertion order
# 2. mutable - we can change the values of keys, we change values not keys
# 3. keys must be unique - we can't have two keys with the same name
# 4. keys must be immutable - we can't use lists as keys, but we can use tuples
# 4.b - typically keys are strings, numbers, tuples
# 5. values can be anything - strings, numbers, lists, dictionaries, etc.
# 6. dynamic - we can add and remove items(key-value pairs) from a dictionary, means change size
# 7. dictionaries are iterable - we can use for loop to iterate over a dictionary
# 8. no slicing - we can't use slicing to get a subset of a dictionary
# 9. no sorting - we can't sort a dictionary, but we can sort keys or values and create a new dictionary
# 10. we can have nested dictionaries - dictionaries inside dictionaries, lists inside dictionaries, etc.

# so very flexible data structure

# let's make a blank dictionary
my_dict = {}
print(my_dict)
# size of a dictionary
print(f"Size of empty_dict is {len(my_dict)}")

# so I can add key-value pairs to a dictionary
my_dict["name"] = "Valdis" # so key name has value Valdis
my_dict["age"] = 42
my_dict["city"] = "Rīga"
my_dict["country"] = "Latvia"
my_dict["food"] = "potatoes"
print(my_dict)
# print size of my_dict
print(f"Size of my_dict is {len(my_dict)}")

# let's get some values from my_dict
print(f"My name is {my_dict['name']}")

# if i get a key that does not exist I get an error
try:
    print(my_dict["surname"])
except KeyError as e:
    print(f"Key surname does not exist in my_dict, error {e}")

needle = "surname"
# we can check if a key exists in a dictionary
if needle in my_dict: # very fast even in a large dictionary
    print("key surname exists in my_dict")
    print(my_dict[needle])
else:
    print(f"key {needle} does not exist in my_dict")

# since this is a common operation we can use get method
print(my_dict.get("name")) # returns value if key exists
print(my_dict.get("surname")) # returns None if key does not exist
print(my_dict.get("surname", "Bērziņš - default")) # returns default value if key does not exist

# so when to use get and when to use regular access?
# if we expect that key might not exist then use get
# if we expect that key should exist then use regular access

# for example when I am looping over a dictionary I expect that keys exist

for key in my_dict: # same as for key in my_dict.keys(): # so we loop through keys, key is arbitrary name, could be k, key, x, etc.
    # so we loop through keys, key is arbitrary name, could be k, key, x, etc.
    print(f"key {key} has value {my_dict[key]}") # no need for get here
    # get would work but it slightly slower
    print(f"key {key} has value {my_dict.get(key)}")  

# we can also loop through values - slightly less common
for value in my_dict.values(): # so we loop through values, value is arbitrary name, could be v, value, x, etc.
    print(f"value {value}") # we do not get keys here  

# we can loop through both keys and values
for key, value in my_dict.items(): # so we loop through key-value pairs, key and value are arbitrary names, could be k, v, key, value, x, y, etc.
    print(f"key {key} has value {value} same as {my_dict[key]}") # no need for get here

# let's make a phone book dictionary

phone_book = {"Valdis": "29495849", 
              "Jānis": "29495848", 
              "Līga": "29495847", 
              "Dace": "29495846"}
# again size
print(f"Size of phone_book is {len(phone_book)}")

# so if i change Valdis number
phone_book["Valdis"] = "22112211" # either I add a new key-value pair or I change an existing one
print(phone_book) # notice order stays the same
# if I have more than one phone number I can use a list
phone_book["Valdis"] = ["22112211", "22112212", "22112213"]
print(phone_book) # notice order stays the same
# so let's get Valdis number
print(f"Valdis number is {phone_book['Valdis']}") # so we get a list back
# so let's get the first number
print(f"Valdis first number is {phone_book['Valdis'][0]}") # so we get a list back
# of course I'd have to know that Valdis has more than one number and it is stored in a list
# how to check if value is a list?
if type(phone_book["Valdis"]) == list: # will work for other types, too: tuple, set, dict, int, float, etc.
    print("Valdis has more than one number")
    # let's get first two numbers - slicing works on lists no matter the size
    print(f"Valdis first two numbers are {phone_book['Valdis'][:2]}")
else:
    print("Valdis has only one number")
    # print that number
    print(f"Valdis number is {phone_book['Valdis']}")

# how about another key Valdis? - it is not possible to have two keys with the same name
# we will need to add another key so we could use last name
phone_book["Valdis Zatlers"] = "22112211"
print(phone_book)
# also note that we can have duplicate values in a dictionary
# let me overwrite my phone number list with single number
phone_book["Valdis"] = "22112211"
print(phone_book)

# let's get all the keys from phone_book
key_list = list(phone_book.keys()) # so we get a list of keys
print(key_list) # separate from phone_book
# let's get all the values from phone_book
value_list = list(phone_book.values()) # so we get a list of values
print(value_list) # separate from phone_book

# i can combine two lists into a dictionary
same_dict = dict(zip(key_list, value_list)) #same contents but different object
print(same_dict)
# check if same contents
print(f"Are phone_book and same_dict the same? {phone_book == same_dict}")
# check if same object
print(f"Are phone_book and same_dict the same object? {phone_book is same_dict}")
# reverse is also possible
reverse_dict = dict(zip(value_list, key_list))
print(reverse_dict)

# we can create a reversed dictionary using in a loop
reversed_phone_book = {}
for key, value in phone_book.items():
    # we could use loop for extra logic
    # if key already exists we could add to a list!
    if value in reversed_phone_book:
        reversed_phone_book[value].append(key)
    else:
        reversed_phone_book[value] = [key] # initialize a list with one element
print(reversed_phone_book)

# we also have a dictionary comprehension - later

# let's look at some more dictionary methods
# we can remove a key-value pair
print(phone_book)
del phone_book["Valdis"]
print(phone_book)
# we can also use pop method
phone_book["Valdis"] = "22112211"
print(phone_book)
my_old_phone = phone_book.pop("Valdis") # pop returns the value, so we can store if need be
print(f"my_old_phone is {my_old_phone}")
print(phone_book)

# there is also setdefault method
# idea is to set a default value if key does not exist otherwise do nothing
# so let's add a phone number for Rūta
phone_book.setdefault("Rūta", "22112211")
print(phone_book)
# now let's use it again
phone_book.setdefault("Rūta", "9999") # does nothing since key already exists
print(phone_book)

# again = will give you alias
phone_book_alias = phone_book # just another name for the same object
print(f"Are phone_book and phone_book_alias the same object? {phone_book is phone_book_alias}")
# let's change something in phone_book
phone_book["Valdis"] = "55555555"
print(phone_book)
print(phone_book_alias) # notice that phone_book_alias also changed

# but if we use copy method we get a new object
phone_book_copy = phone_book.copy()
print(f"Are phone_book and phone_book_copy the same object? {phone_book is phone_book_copy}")
# then changing phone_book does not affect phone_book_copy
phone_book["Valdis"] = "22112211"
print(phone_book)
print(phone_book_copy) # keeps the old value

# last warning: when looping through a dictionary we should not change size of the dictionary(add/remove keys)
# so if we need to remove or add keys we should loop over a copy of the dictionary
for key, value in phone_book_copy.items():
    if key == "Valdis":
        del phone_book[key] # no error if we go over copy

print(phone_book_copy) # still has Valdis
print(phone_book) # Valdis is gone
