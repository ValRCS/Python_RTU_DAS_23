# error handling
# we can put things inside try except block in Python
try: # notice : again for indentation
    my_integer = int(input("Enter an integer please"))
    # if int conversion fails the code transfers immediately to except block
    
    print(f"Cool you entered an integer! {my_integer}")
    # we are guaranteed here that my_integer is in fact an integer
    
except ValueError: # it is recommended you catch specific Errors
    print("You did not enter an integer")
    # i could set default here
    my_integer = 9_000 # _ is just cosmetic for large numbers
    
# outside try except
print("So either user integer or 9000", my_integer)