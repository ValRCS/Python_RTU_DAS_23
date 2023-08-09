# for loops have same constructs as while loops
# break, continue and also else

for n in range(5): # so we go through 0,1,2,3,4 
    
    print(n)
    if n == 3:
        print("Break time!", n)
        break

# here we go after break
print("After break n is", n)

# continue is less used since we can simulate it easily with else
for n in range(10):
    if n % 2 == 0:
        print("Even", n)
        continue # go to start
    # again we could have used else here
    print("Odd", n, n**2)
    
# finally we have less used else attached to for loop

total = 0
for n in range(100):
    total += n**2 # we are adding squares
    print("On number", n)
    print("Total is", total)
    user_input = input("Do you want to quit (y/n)?")
    if user_input == "y":
        print("Quitting time when n is", n)
        break
    # else: # not really needed
    print("Still on n", n)
else: # attached to for loop, runs when loop finishes normally
    print("Whew we finished loop normally")
    # so above will not run if we break
    
print("outside for loop")
    
