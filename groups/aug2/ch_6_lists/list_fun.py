# let's say we have a sentence
sentence = "Raibi Runči  \t Rīgā    rūca   77 rīšus"
# this sentence is a string
print(sentence)
# we have a split method for strings
# we can use it to split a string into a list of strings
# using ANY whitespace as a separator
words = sentence.split()
# what is whitespace in Python?
# whitespace is any space, tab, newline, carriage return
# docs: https://docs.python.org/3   /library/stdtypes.html#str.split
print(words)
# so words is a list of strings
# print type of words
print(type(words))

# why do we need lists at all
# starting out we used variables to store similar items
a1 = "Valdis"
a2 = "Voldemars"
a3 = "Voldemārs"
a4 = "Voldemar"
# this is not very convenient - bad practice
# we can use a list to store similar items
# Python does not check if things we are storing are similar

number_list = list(range(10)) # range is a not a list, it is a generator
# so i made a list from some other sequence
print(number_list)
letter_list = list("Valdis")
print(letter_list)

# so we can use list() to make a list from any sequence

# how do we access individual items in a list?
# we use index starting from 0
# first word
print(words[0])
# last number
print(number_list[-1])
# third letter
print(letter_list[2]) # note 2 is the third index
# last 3 letters would
print(letter_list[-3:]) # so we get a slice of the last 3 letters

# lists are different from strings in that we can change them!
# we can change individual items
# let's change the last letter to S
letter_list[-1] = "S" # no error
print(letter_list)
# question how do we get a string from letter list?
# we can use join method - this is for lists
# we can use join method on any string
# so new name
new_name = "".join(letter_list) # so we join nothing between letters
print(new_name)
# i could join anything between letters
# say space
new_name = " ".join(letter_list) # so we join space between letters
print(new_name)
# i could join anything between letters say smiley
new_name = "😀😀".join(letter_list) # so we join smiley between letters
print(new_name)
# so i could change words for example
new_sentence = " ".join(words)
print(new_sentence)
# i could have changed some word in words
words[0] = "Rudie"
print(words)
new_sentence = " ".join(words)
print(new_sentence)

# we can also split by anything
# let's say i have a string with commas
csv = "Valdis,Voldemars,Voldemārs,Voldemar"
# i can split by comma
names = csv.split(",") # so instead of whitespace i use comma
print(names)
# splitting by multiple characters
# let's say i have a string with commas and semicolons
csv = "Valdis,Voldemars;Voldemārs;Voldemar,Rūdolfs Rūdis Rūsiņš"
# i can split by comma
names = csv.split(",;") # will not work the way we want
print(names) # will give us single element list
# if we need to split by multiple characters we need to use regular expressions
import re # uses regular expressions standard library
names = re.split("[,; ]", csv) # so we split by comma or semicolon or single space
print(names)
# regular expression are very powerful but also very complex - more on that later

# so first 3 names
print(names[:3])
# last 3 names
print(names[-3:])
# so join last 3 names with comma
joined_names = ",".join(names[-3:]) # we get a string
print(joined_names)

# unlike strings we can change size of lists
# let's add a new name to our list of names
# this is so called IN PLACE method, it modifies the original list! here names will be changed
names.append("Aivars") # so we add a new name to the end of the list

print(names)
# i can change contents of any element
# lets change 4th word to Bruno
names[3] = "Bruno" # so 4th element is at index 3
print(names)

# we can sort them alphabetically
sorted_names = sorted(names) # so we get a new sorted list
# i could have used original names to overwrite
print(sorted_names) # if we had strings to sort we get them sorted alphabetically

# so let's join last 3 names with semi-colon
# but for extra fun let's sort them first
# joined_names = ";".join(names[-3:]) # we get a string
# print(joined_names)

# back to numbers
number_list[5] = 9000
print(number_list)
# now sort
sorted_numbers = sorted(number_list)
print(sorted_numbers)

