# let's talk about Python dictionaries
# Documentation: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Dictionaries are a data structure that stores key-value pairs
# other programming languages call them maps, associative arrays, hashes, hashmaps, etc.

# core idea is that if we know the key we can get the value very quickly
# this works even if we have millions of key-value pairs or even billions

# so called one way lookup
# value to key is not going to be fast and also it will be unambiguous potentially

# main properties:
# - unordered - technically Python dictionaries are ordered by insertion order since Python 3.7
# - mutable - we can change the contents of some value for some key of the dictionary
# - dynamic - we can add/remove new key-value pairs to the dictionary at any time
# - keys have to be unique
# - keys have to be hashable(means strings, numbers, tuples, etc.)
# - values can be anything (strings, numbers, lists, dictionaries, etc.) so nesting is possible
# - dictionaries are not sequences, so we can't use indexing or slicing
# we can however iterate/loop over them

# so we will use dictionaries whenever we have a key and we want to get a value
# so real life analogy would be a dictionary book where we have a word and we want to get the definition

# let's create a dictionary
# let's start with an empty one
my_dict = {} # so curly braces are used to create dictionaries
# alternative would be to use the dict() function
also_empty_dict = dict()

# length of a dictionary
print("Length of my dictionary:", len(my_dict))
# other dictionary is also empty
print("Length of also empty dictionary:", len(also_empty_dict))

# I can add some key-value pairs
my_dict["key1"] = "value1" # so string key and string value
my_dict["key2"] = "value2"
my_dict["name"] = "Valdis"
my_dict["age"] = 99 # string key and integer value

# let's check the length again
print("Length of my dictionary:", len(my_dict))
# i can get individual values by using the key
print("My name is:", my_dict["name"]) # Will be fast even for large dictionaries

# let's print out the whole dictionary
print(my_dict)

# let's make a phone book as a dictionary
# i am adding a few key-value pairs to start with
phone_book = {
    "Valdis": 12345678,
    "Līga": 87654321,
    "Maija": 12344321,
    "Rūta": 11111111, # last comma is optional
}

# print my phone book first
print(phone_book)

# let's Līga's phone number
print("Līga's phone number is:", phone_book["Līga"])
# let's add a phone number for another Līga
phone_book["Līga"] = 99999999 # turns out it will overwrite the previous value
print("Līga's phone number is:", phone_book["Līga"])

# so there can be only one Līga - like Highlander

# so if we have multiple Līgas we would use Līga with last name or Līga with address, etc.
# so
phone_book["Līga K"] = 88888888
phone_book["Līga P"] = 77777777
print("Full phone book", phone_book)

# i can check if Līga is in my phone book
print("Is Līga in my phone book?", "Līga" in phone_book) # so in is a keyword
# this check is very fast in dictionaries even if we have millions of entries
# this check would be very slow in lists if we had millions of entries
# note this is for exact match
# i can check for any key
print("Is Valdis in my phone book?", "Valdis" in phone_book)
print("Is Voldemort in my phone book?", "Voldemort" in phone_book)

# I will get an error if I get an unknown key
try:
    print("Voldemort's phone number is:", phone_book["Voldemort"])
except KeyError as e:
    print("Sorry I do not know this key", e)

# I can use get() method to get a value for a key
print("Voldemort's phone number is:", phone_book.get("Voldemort")) # so this will return None
# I can provide a default value if key is not found
print("Voldemort's phone number is:", phone_book.get("Voldemort", "DO NOT CALL ME"))

# so essentially get works as if we had a default value for all keys
key = "Voldemort"
if key in phone_book:
    print(f"{key}'s phone number is:", phone_book[key])
else:
    print(f"Sorry I do not know {key}")

# so get method saves us from writing above if-else block

# get is slightly slower than direct access but it is safer

# iterating over ALL the keys in a dictionary
# key is just a variable name, we could use any name we want, k, entry, key, etc.
for key in phone_book: # syntactic sugar for for key in phone_book.keys():
    print(key, phone_book[key]) # no need to use get here, since I am guaranteed to have a key

print("*" * 40)
# i can iteratoe over both keys and values
for key, value in phone_book.items(): # often we use k,v as variable names
    print(key, value) # i could use phone_book[key] here as well which is same as value


# let's create a dictionary with only Līgas	
ligas_dict = {}
for key, value in phone_book.items():
    if key.startswith("Līga"):
        ligas_dict[key] = value # add new value to our new dictionary

print("Līgas dictionary", ligas_dict)

# if Valdis has many phone numbers I can store them in a list
phone_book["Valdis"] = [12345678, 87654321, 11111111] # overwrite old phone number
# print my phone book first
print(phone_book)

# let's get last phone number for Valdis
# first all phone number for Valdis
print("All phone numbers for Valdis:", phone_book["Valdis"])
# last phone number for Valdis
print("Last phone number for Valdis:", phone_book["Valdis"][-1]) # so we are using list indexing here
# let me go back to single phone number for Valdis
phone_book["Valdis"] = 12345678
# print whole dictionary
print(phone_book)
# so how about removing individual key-value pairs
# first lets backup our phone book
phone_book_backup = phone_book.copy() # so we are making a copy of our dictionary

# let's remove Līga P
del phone_book["Līga P"] # we need to know the key and that key has to exist
# print whole dictionary
print(phone_book)
# 2nd attempt would fail
try:
    del phone_book["Līga P"]
except KeyError as e:
    print("Sorry I do not know this key", e)

# let's remove Līga K using pop method
saved_value = phone_book.pop("Līga K") # pop will return the value for the key
print("Saved value:", saved_value)
# full dictionary
print(phone_book)
# i could  now supply a default value for pop and then there would be no key error
saved_value = phone_book.pop("Līga K", "DO NOT CALL ME") # could be anything or even empty string
print("Saved value:", saved_value)
# full dictionary
print(phone_book)

# similarly to lists when we iterate we should not change size of the dictionary 
# so no removing or deleting keys while iterating

# one option is to iterate over a copy of the keys
# following will remove all Līgas from our phone book
for key in phone_book.copy(): # note copy first
    if key.startswith("Līga"):
        del phone_book[key]

print("Phone book without Līgas", phone_book)