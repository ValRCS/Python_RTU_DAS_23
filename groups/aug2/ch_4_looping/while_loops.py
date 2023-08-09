# while loops
# idea do something while some condition remains True

# while True: # again : will mean indentation block starts
#     # inside while loop
#     print("kaķis murrāja")
#     print("sunis rēja")
#     # still inside
    
# we are outside loop   
print("Outside loop")

# we can use some variable(s) that we check in our while condition
i = 0
while i < 5:
    print("How are you doing No.", i)
    i += 1 # same as i = i + 1 in effect adding 1 to i
    
# again outside loop block
print("Again outside block")

# let's go down the other way
floor = 9
ground = 0
speed = 3
while floor >= ground:
    print(f"Currently on floor {floor}")
    # we can put if elif else inside while loops
    if floor == ground:
        print("Oh we are on ground floor, let's go slowly")
        floor -= 1 # slowly
    else:
        floor -= speed
    # still inside loop
print("Whew outside lift")

# so we can generalize a while loop
start = 200
stop = 250
step = 10
i = start
while i <= stop: # use < or <= depending if you want to stop on or before stop
    print(f"Do something with {i}")
    i += step
    
print("Again outside")


