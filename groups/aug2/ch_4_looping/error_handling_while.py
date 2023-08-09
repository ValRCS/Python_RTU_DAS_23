# we can handle errors with while loops and try except inside

# idea is to break when we have a good input
# let's say I want an integer

while True:
    try:
        user_input = input("Please enter an integer") # guaranteed string
        my_int = int(user_input) # potential for ValueError
        # here I am guaranteed to have an integer
        print("Cool my int is", my_int)
        break # we are good to go
    except ValueError:
        print(f"You entered {user_input} which is not a valid integer")
        print("Sorry, you did not enter an integer (for example -5, 0,9_000)")
    # so we ask again by going back to start of while True
    
# outside after break we know we have an int
print(f"{my_int} squared is {my_int**2}")