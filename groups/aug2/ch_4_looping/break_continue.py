# we can break out of loops with break

# i = 100
i = 10_000
while True:
    print(f"i is now {i}") # this will always run at least once
    # idea is to break out of loop if something is true
    if i >= 140:
        print("Time to break free i is", i)
        break # immediately jumps to next line after while loop
    i += 10
# we go here after break
print("outside loop and i is", i)

# in effect using break we have made so called do while loop
# Python does not have do while, but it is easy to make one using break

# less used is continue which jumpt to START of while loop immediately
i = 0
threshold = 10
small_step = 1
big_step = 4

while i < 20:
    print("i is", i)
    if i == threshold:
        print("Making a big jump", i, big_step)
        i += big_step # crucial to increment i before continue
        continue # jumps immediately to start of while loop
    # we could have used else instead of continue
    i += small_step
    
    

