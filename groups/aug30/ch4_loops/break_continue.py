# let's look at some extra ways to control our loops
# we might want to quit our loop early
i = 0
# in effect we have created a do while loop
# in a do while loop we do something at least once and check condition later
i = 10
i = 9_000_000 # so no matter the starting number we will run
# start of loop at least once
while True:
    print(f"So {i=}") # little syntax trick from Python 3.8
    print("This and above line will always run at least once")
    if i > 10: # here we could check input to finish work
        print("I want to break free.....")
        break # so we immediately break out of the loop
    # we still need to change our i value
    i += 2
    
# outside
print(f"Outside loop an i is {i}")
    
# we also have a continue  which immediately goes back to start of loop

speed = 60
turbo_limit = 70
turbo_jump = 5

while speed < 80:
    print(f"speed is {speed}")
    if speed == turbo_limit:
        print("Turbo just hit", speed)
        speed += turbo_jump
        continue # we go back to the start of the loop
    print("Normal operation")
    speed += 2
    
# continue is less often used because often we can use else
while speed < 80:
    print(f"speed is {speed}")
    if speed == turbo_limit:
        print("Turbo just hit", speed)
        speed += turbo_jump
    else: # so here we have few instructions so no need for continue
        print("Normal operation")
        speed += 2


    