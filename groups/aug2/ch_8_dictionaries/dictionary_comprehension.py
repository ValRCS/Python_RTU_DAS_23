# like lists have list comprehension dictionaries have dictionary comprehension

# dictionary comprehension lets us create dictionaries in a compact way

# we can use loops and if statements in dictionary comprehension

# let's get a dictionary from my name to letters and their unicode values

name = "Valdis"
unicode_dict = {letter: ord(letter) for letter in name}
print(unicode_dict)
# compare with list comprehension
unicode_list = [[letter, ord(letter) ] for letter in name]
print(unicode_list)
# with list I would need to loop to get value for say "a"
# with dictionary I can just use key
print(f"Unicode for a is {unicode_dict['a']}")

# i can use dictionary comprehension to reverse a dictionary
unicode_to_letter = {value: key for key, value in unicode_dict.items()}
print(unicode_to_letter)

# a side note on numbers as keys in dictionaries
# lets say we want to get 97 from our unicode_dict
print(unicode_to_letter[97]) # this works - a
# print(unicode_to_letter[98]) # this will fail
# if our numbers are small and close together we can use lists
# so numbers as keys would be good for dictionary if they are large and far apart

# dictionary comprehension with if statements
# we can use to filter out some values
# so only letters with unicode value over 100
unicode_over_100 = {key: value for key, value in unicode_dict.items() if value > 100}
print(unicode_over_100)

# again if we do not like dictionary comprehension we can use loops
# also loops are good if logic is more complex
unicode_over_100_also  = {}
for key, value in unicode_dict.items():
    if value > 100:
        unicode_over_100_also[key] = value
        # note that we are adding key-value pairs to our new dictionary NOT old
print(unicode_over_100_also)