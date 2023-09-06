# let's start talking about strings a little bit

# string is basically a collection/sequence of letters(characters)
#n in Python there is no character type , so one letter is still a string

name = "Valdis"

# so we can loop through our string
for c in name:
    print("Letter", c)
    
# strings have length property
print("name variable is holding string of length:", len(name))

# so we can get individual letters from our string using index
# index is inside square brackets
# index starts with 0!
print(name[0]) # first letter from name
print("Valdis"[0]) # would work for fixed strings as well
print(f"First letter of {name} is {name[0]}")

# last letter would be
print(name[5]) # 5 because length is 6 and we start counting with 0
# Python lets us use negative index as well
print(name[-1]) # last letter guaranteed (as long as we have letters)
# more on that later

# now I want to loop through my string letter at a time and show index

# one tempting way would be as follows
for i in range(len(name)): # so we know we start at 0 and we go until length-1
    # very similar to
    # classing for(int i = 0;i<name.length;i++) in many languages
    print("Letter No.", i, "is", name[i])
    
# turns out above approach is NOT considered Pythonic!!
# if we need index, what we really need is enumeration
# Python provides enumerate function to give numbers

# recommended approach below
# i get two variables inside each loop cycle!
for n, c in enumerate(name): # n will be number, and here c will be single letter
    print("Letter No.", n, "is", c, name[n]) # so name[n] is not needed