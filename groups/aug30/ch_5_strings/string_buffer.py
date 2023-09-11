# let's say I have a string that I want to remove some characters from

dirty_string = "Raibi rauj, bet raibāk rauj Rūdolfs"

# i want to remove all vowels
# we have a few ways to do this

vowels = "aeiouāēīū"

# buffer approach
# start with nothing and build a new string
buffer = ""
for c in dirty_string:
    if c not in vowels:
        buffer += c # not efficient for very long strings
consonants = buffer
print("Consonants", consonants)

# another approach would be with replace
temp_string = dirty_string
for v in vowels:
    temp_string = temp_string.replace(v, "")
# same result
print("Consonants", temp_string)

# there is also translate method but for that we need a translation table
# we do not know how to make those yet