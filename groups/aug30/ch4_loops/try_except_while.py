# we can combine try except which we use for errors
# with while loop to control errors especially for input

# Python has try except construction for handling errors
# n = 0
# try:
#     n = int(input("Please enter an integer"))
#     # if we get an error next lines will not print..
#     print(f"Cool you entered {n}")
#     print(n+10_000)
# except ValueError as e: # good practie to specify the type of error
#     print("Sorry you did not enter an integer")
#     # e actually is optional will print actual error
#     print(f"ERROR: {e}")
#     
# print(f"Normal code, n is {n}")
# 
# so if we want to make sure we get input that is valid int (or float etc)
# we can put try except inside while loop

while True:
    try:
        # int conversion has potential to throw ValueError
        number = int(input("Please enter an integer"))
        # again if we get an error next line will not run
        print(f"Good stuff your is an integer {number}")
        print("We are ready to proceed with rest of program")
        break # here we know for sure that number is integer
    except ValueError:
        print("Sorry yours was not an integer")
        print("Please try again")
        # could use continue but it is required
        
# we will go here after break
print(f"So now we can do work with my number {number}")
print("SQUARE", number**2) # do anything that integers do