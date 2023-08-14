# let's talk about string methods in Python

# so existence check 

# we can use in operator to check if a substring exists in a string
haystack = "kartupelis"
needle = "kart"
print(needle in haystack) # so we get True
needle = "art"
print(needle in haystack) # so we get True

# so we can use in inside if statement
needle = "tup"
needle = "tupi"
if needle in haystack:
    print(f"Found {needle} in {haystack}")
else:
    print(f"Did not find {needle } in {haystack}")

# i can check single letters
letter = "a"
if letter in haystack:
    print(f"Found {letter} in {haystack}")
else:
    print(f"Did not find {letter} in {haystack}")

# we can compare strings
name = "Valdis"
other_name = "Voldemars"
print(name < other_name) # so we get True, but why?
# it is not length, it is alphabetical order, so called lexicographical order
# goes back to ASCII table, but now Unicode is used same for all languages
# here ord(a) is 97 and ord(b) is 98
print(ord("a"), ord("o"))

# so if i need length comparison i need to do that explicitly
print(len(name), len(name) < len(other_name), len(other_name))

# we can find method of a substring
needle = "tup"
print(haystack.find(needle)) # so we get 3 because tup starts at index 3
# so if i want string after our needle
print(haystack[haystack.find(needle):]) # so we get tupelis
# however if we do not want to show needle
print(haystack[haystack.find(needle) + len(needle):]) # so we get elis

# alternatively we can use index method
print(haystack.index(needle)) # so we get 3 because tup starts at index 3

# difference is that index will throw an error if substring is not found
try:
    print(haystack.index("Valdis")) # there is no Valdis in kartupelis
except ValueError:
    print("Valdis not found in kartupelis")

# thus you can check for -1 using find, or use try except with index method

a_string = "aaaaa"
# we can use count method to count how many times a substring appears
print(a_string.count("a")) # so we get 5
# however it is skipped if we have overlapping substrings
print(a_string.count("aa")) # so we get 2 not 4

# we can use replace method to replace all occurrences of a substring
food = "auzu putra ar kartupeli"
# so let's replace 2nd letter with y
try:
    food[1] = "y" # this will not work
except TypeError:
    print("Strings are immutable, we cannot change them")

# instead I could have used replace method
print(food.replace("u", "y")) # so we get ayzy pytra ar kartypeli
# again original food is not changed
# so i would need to assign it to a new variable
new_food = food.replace("u", "y")
print(new_food)
# if I only want to replace first two occurrences
print(food.replace("u", "y", 2)) # so we get ayzy putra ar kartupeli

# we could have replaced a word as well
# lets change putra to tume
print(food.replace("putra", "tume")) # so we get auzu tume ar kartupeli
# again use variable assignment if you want to keep the change

# I can use slicing with new text
# so let's make Baltā putra
print(food.replace("auzu", "Baltā"))
print(food.replace("auzu", "Baltā")[:11]) # so we get Baltā putra
# i could have use slicing and concatenation
print("Baltā" + food[4:]) # so we get Baltā putra ar kartupeli

# in real life off by one errors are very common
# easy to fix as well adjust offset by 1

# so let's look at some more string methods
dogs = "Džulis, Reksis, Šariks, Džeks, mazais Džekijs arī"
# let's make a string all lowercase
print(dogs.lower()) # so we get džulis, reksis, šariks
# let's make a string all uppercase - YELLING!
print(dogs.upper()) # so we get DŽULIS, REKSIS, ŠARIKS, DŽEKS
# again if we want to save it we need to assign it to a variable
yelling_dogs = dogs.upper()
print(yelling_dogs)
# Capitalize will make first letter uppercase
print(dogs.capitalize()) # so we get Džulis, reksis, šariks, džeks, mazais džekijs
# so only first letter is capitalized
# we also have title method which will capitalize all words
print(dogs.title()) # so we get Džulis, Reksis, Šariks, Džeks, Mazais Džekijs
# we have a swapcase method which will swap cases
print(dogs.swapcase()) # so we get dŽULIS, rEKŠIS, šARIKS, dŽEKS, MAZAIS dŽEKIJS ARĪ

# we can use startswith method to check if a string starts with a substring
print(dogs.startswith("Džulis")) # so we get True
# we can use endswith method to check if a string ends with a substring
print(dogs.endswith("arī")) # so we get True

# we can combine these with if statements
# for example I want to check if a string starts with dž and ignore case
if dogs.lower().startswith("dž"): # so I made a copy of dogs and made it lowercase and checked if it starts with dž
    print("We have a dž dog")
else:
    print("We do not have a dž dog")

# we can also use some cleanup methods
dirty_city = "  Rīga\t \n  "
print(dirty_city)
# we can clean it using strip method
clean_city = dirty_city.strip()
print(clean_city)
# we can only clean left side with lstrip
print(dirty_city.lstrip())
# or right side with rstrip
print(dirty_city.rstrip())

# i could apply these string methods to string literal





