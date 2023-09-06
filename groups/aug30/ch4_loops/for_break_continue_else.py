# for loops also have break and continue

for n in range(10):
    print("n is", n)
    if n == 7: #instead of n it could be some input or something
        print("I want to quit")
        break # so we will not reach 8 and 9
    
print("After loop is finished n is", n)

for n in range(10):
    print("n is again", n)
    user_input = input("Do you want to continue (y/n)?")
    if user_input == "n": # we might want to be more liberal with our checking here
        # there are string methods to check for any case letters and starting with more later
        print("Sorry to see you go")
        break
    elif user_input == "y":
        print("Continuing without extra work")
        continue # goes to start with next number
    # else: optional
    print("Doing something with current n", n, n**2, n**3)
    # could do more work here
else: # this is rare feature for for (and also while loops)
    print("Loop finished normally WITHOUT breaking out early")
    # it lets us skip some flag type variable sometimes
# outside loop

print("always runs outside loop", n)