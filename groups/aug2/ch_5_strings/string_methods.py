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

