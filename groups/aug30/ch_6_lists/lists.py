# let's talk about lists in Python
# we use lists to store multiple values in a single variable
# most other languages call this an array - masīvs Latviešu valodā

# first why do we need lists
# consider we need to store 10 numbers
# we could store them in 10 different variables
a1 = 1
a2 = 2
a3 = 3
# ....
a10 = 10
# ...
# but what if we need to store 100 numbers ?
# one million numbers ?

# as soon as we have two or more variables with the same name and same type and purpose
# we should consider using a list

# philosophically lists would preferably contain values of the same type
# many languages enforce this - for example C, C++, Java, C#
# Python does not enforce this - we can store values of different types in the same list
# we can store numbers, strings, booleans, even other lists inside lists
# ideally we should not overuse this feature

# let's create a list
# we use square brackets to create a list
my_list = [] # empty list
print("MY LIST:", my_list)
# alternative would be to use the list() function
also_empty_list = list()

# typically we use empty list before we start collecting some values

# how long is our list?
print(f"my_list has {len(my_list)} elements")

# we can use append() method to add elements to the end of the list
my_list.append(10) # add number 10 to the end of the list
# NOTE: we did not use = sign here,  my_list was MUTATED - changed IN PLACE
print("MY LIST:", my_list)
print(f"my_list has {len(my_list)} elements")

# alternative to IN PLACE is OUT OF PLACE - we create a new list
# this could mean also overwriting the old list
my_list = my_list + [20] # in effect we create a new list with 20 inside and assign it to my_list
# we could also use += operator
my_list += [30]

print("MY LIST:", my_list)
print(f"my_list has {len(my_list)} elements")

# let's create another list
another_list = [40, 50, 60]

# so what happens if we use append?
my_list.append(another_list)
print("MY LIST:", my_list)
print(f"my_list has {len(my_list)} elements")

# now let's talk about accessing elements in the list
# weuse same square brackets to access elements in the list and use same indexing as in strings
# first element has index 0
print("first element:", my_list[0])
# last element has index -1 or here it would be 3
print("last element:", my_list[-1])
# how about getting 50 from another_list?
print("50:", another_list[1])
# thus we can use same approach in MY LIST
print("50:", my_list[-1][1])
print("50:", my_list[-1][-2]) # so 2nd from the end

# same Index Error if we go out of bounds
try:
    print("50:", my_list[500]) 
except IndexError as e:
    print(f"Index Error {e}")

# let's create a new list of beers
beers = ["Aldaris", "Valmiermuižas", "Tērvetes", "Bauskas", "Užavas"]
print(f"beers: {beers}") 

# first two beers
print(f"first two beers: {beers[0:2]}") # so 0 and 1
# 0 is not required
print(f"first two beers: {beers[:2]}") # so 0 and 1
# last two beers
print(f"last two beers: {beers[-2:]}") # so -2 and -1
# we can use step
print(f"every second beer: {beers[::2]}") # so 0 and 2
# of course also we can reverse the list - without modifying the original list
print(f"reversed beers: {beers[::-1]}") # so -1 and -2 and -3 and -4 and -5

foreign_beers = ["Guinness", "Heineken", "Corona"]
# again if we use append
beers.append(foreign_beers)
print(f"beers: {beers}")
# we can delete the last element with pop() - it returns the deleted element
deleted_beers = beers.pop() # i could skip assignment if we don't need the deleted element
print(f"beers: {beers}")
print(f"deleted beers: {deleted_beers}")

# so we can use extend() to add all elements from another list
beers.extend(foreign_beers) # again IN PLACE - modifies beers
print(f"beers: {beers}")

# we could have used OUT OF PLACE approach - create a new list (or overwrite the old one)
beers = beers + foreign_beers
# now I will have some duplicates
print(f"beers: {beers}")

# now how about deleting last 3 elements?
# i could pop 3 times but not very elegant
# let's just create a new list from slice
print("Everyhing but last 3 beers:", beers[:-3])
beers = beers[:-3] # overwrite the old list
print(f"beers: {beers}")

# let''s insert a beer in the middle say "Cēsu" at index 2 - so after Aldaris and Valmiermuižas
beers.insert(2, "Cēsu") # again IN PLACE - modifies beers, and shifts all elements to the right
print(f"beers: {beers}")

# alternative would have been similar to what we did with strings
# create a new list from slices
beers = beers[:4] + ["Cēsu","Mežpils"] + beers[4:] # so keep all original beers and add new one in the middle
# note I can add multiple elements flatly at once with this approach
print(f"beers: {beers}")

# now let's count Cēsu beers
print(f"Cēsu beer count: {beers.count('Cēsu')}") # should be 2

# let's find the index of Cēsu beer
print(f"Cēsu beer index: {beers.index('Cēsu')}") # should be 2
# how about next Cēsu beer?
print(f"Cēsu beer index: {beers.index('Cēsu', 3)}") # should be 4 since we start searching from index 3

# so how to remove Cēsu beer?
beers.remove("Cēsu") # again IN PLACE - modifies beers
print(f"beers: {beers}")
# let's put it back
beers.insert(2, "Cēsu") # again IN PLACE - modifies beers, and shifts all elements to the right
print(f"beers: {beers}")

# now let's talk about assignment vs copy
beers_copy = beers.copy() # creates a new list, completely independent from beers
beers_alias = beers # creates an alias - both variables point to the same list
# we can see this by using id() function
print(f"beers id: {id(beers)}")
print(f"beers_copy id: {id(beers_copy)}")
print(f"beers_alias id: {id(beers_alias)}")
# so beers and beers_alias point to the same list

# let's add a new beer to beers
beers.append("Piebalgas")
print(f"beers: {beers}")
print(f"beers_copy: {beers_copy}") # NOT AFFECTED
print(f"beers_alias: {beers_alias}")

# so now let's remove all instances of "Cēsu" from beers
# we can use remove() method
while "Cēsu" in beers: # not efficent for very large lists
    # because needs to check every time if "Cēsu" is in beers
    beers.remove("Cēsu") # IN PLACE
print(f"beers: {beers}")
print(f"beers_copy: {beers_copy}") # NOT AFFECTED
print(f"beers_alias: {beers_alias}") # AFFECTED

# now let's restore from our copy
beers = beers_copy.copy() # completely independent from beers_copy
# NOTE in this place beers_alias is still pointing to the old list!!
print(f"beers: {beers}")

# another approach is to start with a blank list and add only what we need
# so called BOTTOM UP approach
clean_beers = []
for beer in beers:
    if beer != "Cēsu":
        clean_beers.append(beer)
        # do not modify beers inside the for loop - it will cause problems
print(f"clean_beers: {clean_beers}")
print(f"beers: {beers}") # NOT AFFECTED

# there is list comprehension - a more elegant way to do this in one line later on this

# careful when looping with for loop through a list and modifying it
# we do not want to modify the list we are looping through
# solution: use a copy of the list

# there are a few more methods for lists
# we can always use . to see all methods
reversed_list = beers[::-1] # creates a new list
# alternative would be reversed_list = list(reversed(beers))
print(f"reversed_list: {reversed_list}")
print(f"original beers: {beers}") # NOT AFFECTED
# again we have an option to use IN PLACE approach
beers.reverse() # IN PLACE modifies beers
print(f"beers: {beers}")

# similarly we can sort a list
sorted_list = sorted(beers) # creates a new list
# to use sorted our values need to be comparable by default
# here everything inside is a string so it is comparable
print(f"sorted_list: {sorted_list}")
print(f"original beers: {beers}") # NOT AFFECTED

# again we have an option to use IN PLACE approach
beers.sort() # IN PLACE modifies beers! we lose our original order
print(f"beers: {beers}")

# of course we can clear the list
beers.clear() # IN PLACE deletes all elements from beers
print(f"beers: {beers}")

# i can can create numbers from range
numbers = list(range(10)) # creates a new list
# i can add a float to this list that is ok
numbers.append(3.14)
print(f"numbers: {numbers}")

# if all elements are numeric (int or float) we can use min() and max() and sum()
print(f"min: {min(numbers)}") # 0
print(f"max: {max(numbers)}") # 9
print(f"sum: {sum(numbers)}") # 45

# i can use min and max on strings - lexically
# sum will not work on string list
print(f"min: {min(beers_copy)}") # Aldaris
print(f"max: {max(beers_copy)}") # Valmiermuižas
try:
    print(f"sum: {sum(beers_copy)}") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
except TypeError as e:
    print(f"TypeError: {e}")
# so sum works only on numbers

# list is a very generic data structure
# we can store anything inside

anything_goes_list = [1, 2, 3, 
                      "Aldaris", "Valmiermuižas", "Tērvetes", 
                      "Bauskas", "Užavas", 
                      True, False, None, 
                      [1,2,3]] # there are other lists inside this list
# we can even store functions inside later on this

# so we can convert a string to a list
food = "potatoes, tomatoes, cucumbers, carrots, onions"
default_items = food.split() # creates a new list using whitespace as separator
print(f"default_items: {default_items}")
items = food.split(", ") # creates a new list using custom separator
print(f"items: {items}")


# again to go back to string from list of strings we use join()
big_food = "XXX".join(items) # creates a new string using XXX as separator
print(f"big_food: {big_food}")  


