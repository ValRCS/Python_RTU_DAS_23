# surprisingly while loops have their own else
# this is a bit controversial
# possibly it will be removed from future Python

# idea is that this else runs only when while loop did not encounter break
# so if while loop finishes normally we can run the code inside else

i = 0
while i < 5:
    print("i is", i)
    response = input("Do you wanto to quit(y/n)?")
    if response == "y":
        print("Quitting early when i is", i)
        break # will cause else not to run
    i += 1
else: # runs when no break happened, again this else is attached to while not if!
    print("While loop finished normally")
    
print("Outside while loop")

# if I wanted to track break I could have used
# some boolean is_normal_exit or something like that