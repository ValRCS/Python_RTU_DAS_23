# so list stores a sequence of items
# we can access individual items by index

# let's make a list of Latvian beers
beers = ["Tervētes", "Bauskas", "Piebalgas"]
print(beers)
# we know how many beers we have
print(f"I have {len(beers)} beers")
# we can get first one
print(f"First beer is {beers[0]}")
# last one
print(f"Last beer is {beers[-1]} {beers[2]}") # so we can use index -1 to get last item
# slice of first two beers
print(f"First two beers are {beers[:2]}")
# slice of last two beers
print(f"Last two beers are {beers[-2:]}")

# we can check for existance of items in a list
print("Is there Tērvetes in my list", "Tervētes" in beers)
# for large lists this will take linear time, need to check every item

# we can loop/iterate over lists
for beer in beers: # typical naming convention is to use plural for lists, singular for items
    print("My beer is", beer)

# using . syntax we can access many methods that lists have
beers.append("Valmiermuižas") # Crucial point: IN PLACE, means modifies the list
print(beers)
# as an alternative we could have used + operator to add two lists
beers = beers + ["Cēsu", "Aldaris"] # this is OUT OF PLACE, means creates a new list
print(beers)
# if we want to add multiple items we can use extend method
beers.extend(["Līvu", "Brālis", "Bauskas"]) # this is IN PLACE, modifies the list
print(beers)
# compare with append
beers.append(["Līvu", "Brālis_atkal", "Bauskas"]) # this is IN PLACE, modifies the list
print(beers)
# so by appending a list to a list we get a nested list
# we can see that last element is a list
print(beers[-1])
# and second element of last element is Brālis
print(beers[-1][1]) # so last element is a list, and we get second element of that list
# lets remove that last element using pop method
last_element = beers.pop() # so pop removes last element and returns it, so IN PLACE operation
# also it returns the removed element
# so if i just wanted to remove last element i could have used pop without assignment
# beers.pop() # deletes last element
print(f"Popped element is {last_element}")
print(beers)
# let's find index of a beer Cēsu
cesu_index = beers.index("Cēsu")
print(f"Cēsu index is {cesu_index}")
# if we try to find something that is not in the list we get an error
try:
    index = beers.index("Carlsberg")
    print(f"Carlsberg index is {index}")
except ValueError as ve:#ve is just a name for our error
    print("Carlsberg is not in the list", ve)

# unlike strings we do not have a find method

# now that we know index we can remove it
beers.pop(cesu_index) # so we remove element at index 4, IN PLACE again, by modifying the list
print(beers)
# let's count how many Bauskas we have
print(f"We have {beers.count('Bauskas')} Bauskas") # count is exact match, not substring
# how about finding all beers that start with B - so substring
b_counter = 0
for beer in beers:
    if beer.startswith("B"): # any logic that returns True or False can be used
        b_counter += 1
print(f"We have {b_counter} beers that start with B")
# we can also use list comprehension - later on

# so we can remove first occurence of Bauskas
beers.remove("Bauskas") # IN PLACE, modifies the list
print(beers)

# we can sort the list - requires all elements to be comparable (will not work on say strings and numbers)
sorted_beers = sorted(beers) # OUT OF PLACE, creates a new list
print(sorted_beers)
print(beers) # original list is not modified
beers.sort() # IN PLACE, modifies the list, original will be gone
print(beers)

# we can compare the contents of our lists
print(f"Are beers and sorted beers the same CONTENTS? {beers == sorted_beers}")
# if we use is we can check if they are the same object - list here
print(f"Are beers and sorted beers the same OBJECT? {beers is sorted_beers}")

# if we create an alias
beer_alias = beers # this is NOT a copy, just an alias, shortcut to the same object
print(f"Are beers and beer_alias the same OBJECT? {beers is beer_alias}")

# now if I change some value in beers
beers[0] = "Tērvetes" # IN PLACE, modifies the list
print(beers)
# beer_alias will also change
print(beer_alias)
# however sorted_beers will not change
print("Sorted beers stays unchanged", sorted_beers)

# we can create a copy of a list
beers_copy = beers.copy() # OUT OF PLACE, creates a new list in memory (so called shallow copy)
print(f"Are beers and beers_copy the same OBJECT? {beers is beers_copy}")
# contents are the same
print(f"Are beers and beers_copy the same CONTENTS? {beers == beers_copy}")
# now if we change beer_alias
beer_alias.append("Cēsu") # IN PLACE, modifies the list, will also modify beers since it is SAME OBJECT
print(beers)
print(beers_copy) # beers_copy is a copy, so it will not change

# this can be important if we iterate over a list and modify it
# we can not change size of a list while iterating over it!
# we can change contents of a list while iterating over it
for beer in beers.copy():
    if beer.startswith("B"):
        beers.remove(beer) # IN PLACE, modifies the list

print(beers) # so we removed all beers that start with B
# we also have a nice list comprehension syntax

# we can use insert to insert an element at a specific index
# let's insert a beer at index 2
beers.insert(2, "Bauskas") # IN PLACE, modifies the list by inserting an element at index 2, rest go to the right
print(beers)

# we could have used + operator to insert element somewhere
new_beer_list = beers[:2] + ["Cēsu"] + beers[2:] # OUT OF PLACE, creates a new list
print(new_beer_list)
# original is unaffected
print(beers)
# finally we can clear the list
# beers.clear() # IN PLACE, modifies the list, leaves an empty list
# print(beers)
# # alias is also cleared
# print(beer_alias)

# instead if I overwrote the beers list with [] empty list then alias would still point to the old list
beers = [] # OUT OF PLACE, creates a new list
print(beers)
print(beer_alias) # beer_alias still points to the old list