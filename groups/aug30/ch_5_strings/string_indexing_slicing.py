# more on string indexing

# Python has two index types
# positive index starts at 0
# negative index starts at -1 from the end of the string
# pic https://developers.google.com/static/edu/python/images/hello.png

# we can use index to get individual letters from our string

food = "kartupelis"

print("First letter", food[0])
# last letter would be
print("Last letter", food[-1]) # last letter guaranteed (as long as we have letters)

# second to last letter
print("Second to last letter", food[-2])

# second from start
print("Second letter", food[1]) # note index is 1 not 2!!

# fifth from start
print("Fifth letter", food[4]) # note index is 4 not 5!!
# how about 6th from end?
print("Sixth from end", food[-6]) # should also be u

# 10th letter?
print("Tenth letter", food[9]) # should be s

# how about out of bounds index?
try:
    print("Out of bounds", food[10]) # this will fail
    # we only have 10 letters so index 10 is out of bounds (0-9)
except IndexError as ie: # ie is just a variable name
    print(f"Index Error {ie}")

# again we could have used len(food) to get the length of our string
print("Length of food", len(food))

# similarly negative index can also be out of bounds
try:
    print("Out of bounds", food[-11]) # this will fail
    # we only have 10 letters so index -11 is out of bounds (-10 to -1)
except IndexError as ie:
    print(f"Index Error {ie}")

# again we can loop through our string
for c in food: # c is just a variable name
    print(c, end="|") # end is a keyword argument, by default it is \n
print() # just to get a new line

# we can check if something is in our string
# we get Boolean True or False
print("There is a in food?", "a" in food) # True
# b
print("There is b in food?", "b" in food) # False
# we could check longer substrings
print("There is kart in food?", "kart" in food) # True
# art ?
print("There is art in food?", "art" in food) # True
# there is fly in food?
print("There is fly in food?", "fly" in food) # False

magic_word = "Abracadabra"
# lets count how many a's we have in our magic word
a_count = 0 # we start with 0
for c in magic_word:
    if c == "a":
        a_count += 1 # same as a_count = a_count + 1
print(f"We have {a_count} a's in {magic_word}")

# we could have used count method that is built in
print(f"We have {magic_word.count('a')} a's in {magic_word}")

# we can count any substring ra for example
print(f"We have {magic_word.count('ra')} ra's in {magic_word}")

# to use count our variable should be of string type
print("Valdis Saulespurens".count("a")) # 2

# count is case sensitive
# count also is strict, it will not count overlapping substrings
band = "ABBBBA"
print(f"We have {band.count('BB')} BB's in {band}") # only 2 not 3

# we have many string methods
print("Rīga un runči".capitalize()) # valdis saulespurens"")
# more on those later

# first let's talk about slicing

# slicing is a way to get a substring from our string
# we use square brackets and colon :
# [start:end] start is inclusive, end is exclusive - exclusive means not included

# so let's get first 3 letters from our food
print("First 3 letters", food[0:3]) # note we get 0,1,2 but not 3
# in fact we can leave out 0 - it is assumed default
print("First 3 letters", food[:3]) # note we get 0,1,2 but not 3
# we can get last 3 letters
print("Last 3 letters", food[-3:]) # we start 3 letters from the end and go to the end
# note that using -1 would give 3rd and 2nd to last letters
print("Last 3 letters", food[-3:-1]) # we start 3 letters from the end and go to the end
# of course i could use positive index as well
print("Last 3 letters", food[7:10]) # we start 3 letters from the end and go to the end
# could have skipped 10
print("Last 3 letters", food[7:]) # we start from 8th letter and go to the end

# slicing does not have out of bounds error
print("Last 3 letters", food[7:100_000]) # we start from 8th letter and go to 100_000th letter


# i can go out of bounds both ways
print("All letters", food[-2_000:7_000]) 
# so we started 2000 letters from the end and went to 7000th letter

# full syntax for slicing is [start:end:step] step is optional and defaults to 1

alphabet = "abcdefghijklmnopqrstuvwxyz"
# check length
print("Length of alphabet", len(alphabet))
# can throw assert error if not 26
assert len(alphabet) == 26, "English alphabet should have 26 letters"
# assert lets us test our assumptions

# let's get every second letter
print("Every second letter", alphabet[::2]) # so we start at 0 and go to the end with step 2
# we could start at 2nd letter
print("Every second letter starting with b", alphabet[1::2]) # so we start at 1 and go to the end with step 2
# how about first ten letters skipping every second letter
print("First ten letters skipping every second letter", alphabet[:10:2]) # so we start at 0 and go to the end with step 2

# so we can use -1 step to reverse our string
print("Reversed alphabet", alphabet[::-1]) 

# how about reversing every second letter
print("Reversed every second letter", alphabet[::-2])

# first ten letters then reversed
print("First ten letters then reversed", alphabet[:10][::-1])

print(food[-7000 : 10000 : -1]) # nothing will be printed
print(food[ : : -1]) # reverse string

# try printing your own name backwards
# also try printing first 5 letters 
# then try printing first 5 letters backwards

