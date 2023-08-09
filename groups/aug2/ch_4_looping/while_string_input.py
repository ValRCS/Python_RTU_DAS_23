# we can use some string methods to make user input more flexible

name = "Valdis"
# some string methods
print(name.upper())
print(name.lower())
print(name.startswith("Val"))
print(name.endswith("dis"))
# first letter
print(name[0]) # indexing

total = 0
count = 0
while True:
    try:
        number = float(input("Please enter a number"))
        # we have a number here
        total += number
        count += 1 # makes sense to place count close to our operation
        print(f"total so far after {count} inputs is {total}")
    except ValueError:
        print("Please enter a valid number (-5,0,1,3.1415926 etc)")
        continue # we use continue since we have bad input

    user_input = input("Continue (Y/N)?")
    if user_input.lower().startswith("n"):
        # so we let user quit with anything that starts
        # with n or N
        print("Okay quitting you entered", user_input)
        break
    
print(f"All done total after {count} inputs is {total}")
print(f"Average is {round(total/count, 2)}")
