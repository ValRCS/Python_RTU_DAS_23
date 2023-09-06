# how to repeat your auctions
# let's say we want to print "hello" 3 times

print("Hello")
print("Hello")
print("Hello")

# golden rule if we are doing something similar or exactly the same 3 or more times
# then we should seriously consider a loop construction

# basic While Loop
# runs while condition remains true
# below it always is True - constant.. infinite loop
# while True:
#     print("Water runs")
#     print("Still running...")
    # inside loop
# outside loop

i = 0 # i is just a variable name, could be it, n, x, count, etc
while i < 5:
    print("How are you doing?", i)
    i += 1 # Python has no ++ or --
    # i += 1 is same as i = i + 1
    # still inside loop could do more here
# outside loop always run
print("We are outside loop and i is", i)

floor = 12 # initial condition
special_floor = 7
# speed = 2
speed = 5
ground_floor = 0
ABSOLUTE_GROUND_FLOOR = -1
while floor > ground_floor:
    print(f"We are currently on floor {floor}")
    # we could check something inside loop
    if floor == special_floor:
        print(f"You are currently on special floor {floor}")
#     else: # optional, what we do if we are on normal floor
    # floor -= 1
    # floor -= speed # typically we change the iterator at the end
    # if we are afraid that we will go down too deep
#     if floor < ABSOLUTE_GROUND_FLOOR:
#         floor = ABSOLUTE_GROUND_FLOOR
    # alternative to above if is max function
    # there is also min function which is what we do not need here
    floor = max(floor-speed, ABSOLUTE_GROUND_FLOOR)
    
print("Outside again")

# to generalize a while loop
start = 200
stop = 240
step = 5

i = start # set initial condition
while i < stop: # if we use < stop will not be processed
    print(f"Do something with {i}")
    i += step
    
print(f"Outside loop i is {i}")
    