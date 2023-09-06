# philosophicaly speaking
# while loops are for indeterminate looping
# when we do not exactly know how much/long to loop

# we have for loops to loop through
# some iterable/collection/something countable

# which collection of items do we already know?
# we know a string - which is basically a collection of characters
# in Python there is no character data type - character is a string with a single item

name = "Valdis"
# i can iterate/loop through name letter at a time
for c in name: # c is just a variable - here it is made automatically
    print("Letter", c)
    # could do more with c

# outside loop
# c is still alive
print("c value is", c)

# if we want to loop through some whole numbers we have a range function
# range gives us well range - which is sort of half baked numbers
# I call it a number factory
# made on demand

# let's say first 5 numbers
for n in range(5): # n is just a variable name, could be x, a, number etc
    print("My number is", n)
    
# i do not have to use n if I am not using it inside
# let's say I need to do some tasks 3 times
for _ in range(3): # _ indicates that we do not care about the variable
    print("Working")
    print("WOrking with number n", n) # i could use other variables inside
    
# we can reuse n, _, c or any variable in another loop of course
print("outside loop n is still", n)

# by default range(n) will give numbers from 0 to n(excluded) on demand
# we can use range with specified start and stop

for n in range(200, 205): # so start(200) is included, but stop(205) is excluded
    print(f"n is {n}")
    
# we can go the other way if we specify step - here - 1
for floor in range(10, 0, -1):
    print("On floor", floor)
# here we stoppe on floor 1 not 0! because stop is excluded  
print(f"We stopped on floor {floor}")

# so to generalize range(start, stop_exclusive, step)

# again these are just variable names
start = 100
stop = 120
step = 4
# if we want to include stop we just add +1
for n in range(start, stop+1, step):
    print("n is ", n)