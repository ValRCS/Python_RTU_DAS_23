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

