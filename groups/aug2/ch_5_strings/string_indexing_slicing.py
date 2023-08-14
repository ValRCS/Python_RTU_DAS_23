# let's talk about indexing and slicing strings in Python

food = "kartupelis"
print(food)

# how about length of our string?
print(f"Length of food is {len(food)}")

# how to get the first symbol?
print(food[0]) # so we use 0 based indexing
# so 2nd letter will have index 1
print(food[1])
# so index 10 will be out of bounds!
try:
    print(food[10]) # this would want 11th symbol
except IndexError:
    print("Index 10 is out of bounds!")

# so last letter would be at index len(food) - 1
print(food[len(food) - 1]) # not Pythonic
last_index = len(food) - 1
print(food[last_index])
# Python offers us negative indexing
# so -1 will be the last symbol
print(food[-1])
# see Google Python dev course
# https://developers.google.com/edu/python/strings#string-slices

# so 2nd to last letter would be at index len(food) - 2
# even better would be to use negative indexing -2
print(food[-2])

# and also we remember how we could loop over strings
for letter in food:
    print(letter)

# so you could do this, but no need
for i in range(len(food)): # Not Pythonic
    print(food[i])

# if we need index we can use enumerate
for i, letter in enumerate(food):
    print(f"Index {i} is {letter}")

# we can also slice strings
# we use slicing to get substrings
# we use the syntax [start:stop:step]

# so let's get the first 3 letters
print(food[0:3]) # so we get 0, 1, 2 letters but not 3
# in fact we have a shortcut for this
print(food[:3]) # so we get 0, 1, 2 letters but not 3
# compare with just 3
print(food[3]) # so we get 4th letter with index 3

# let's make an alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz"
# print is it 26 letters?
print(len(alphabet))
# we can use assert to check if something is true
assert len(alphabet) == 26 # so this will not do anything
# assert len(alphabet) == 25 # so this will fail with AssertionError and stop the program
# we could have used import string
# and then string.ascii_lowercase
import string # built into Python
print(string.ascii_lowercase)

# so first 10 letters
print(alphabet[:10])

# so last 4 letters with positive indexing
print(alphabet[22:26])
# easier would be to use negative indexing
print(alphabet[-4:]) # :] means to the end
# so how about middle two characters
print(alphabet[12:14]) # 14 is not included because that is 15th letter
mid = len(alphabet) // 2
print(mid)
print(alphabet[mid-1:mid + 1]) # so we get 13th and 14th letters

# slicing lets us go out of bounds
print(alphabet[22:100]) # so we get 22nd to 99th letters
# no error here
# same for negative indexing
print(alphabet[-400_000:100]) # so we get -400_000 to 99th letters

# again strings are immutable so if we want to save a slice we need to assign it to a variable
# for example
first_10 = alphabet[:10]
print(first_10)
# last 5
last_5 = alphabet[-5:]
print(last_5)

# we have an option to use step
# for example
print(alphabet[::2]) # so we get every other letter
# every 3rd letter
print(alphabet[::3])
# i can start on 2nd letter and get every 5th letter
print(alphabet[1::5])

# finally we have an easy way to reverse a string
print(alphabet[::-1]) # so we get every letter in reverse order
reverse_alphabet = alphabet[::-1]
print(reverse_alphabet)

# so now if we need to change a letter in a string we can use slicing and concatenation
# for example let's change 5th letter to X
print(alphabet[:4] + "X" + alphabet[5:])
# again i'd need to save it to a variable
alphabet_X = alphabet[:4] + "X" + alphabet[5:]
print(alphabet_X)
# alternatively could have used f-string
print(f"{alphabet[:4]}X{alphabet[5:]}")
alphabet_X_too = f"{alphabet[:4]}X😀{alphabet[5:]}"
print(alphabet_X_too)
