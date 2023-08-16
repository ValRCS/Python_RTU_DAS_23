result_list = [] # this is global variable
# we should strive to keep as few global variables as possible

# enter some user values
def get_user_values(internal_result_list): # we could use result_list here but it is better to pass it as a parameter
    while True:
        user_input = input("Enter a number or 'done' to finish: ")
        if user_input == "done":
            break
        internal_result_list.append(float(user_input)) # will modify the list we passed
    return internal_result_list # returns same list with new values

def get_average(my_list: list) -> float: # could use any name, x, y, z, etc.
    """Returns average of a list of numbers"""	
    return sum(my_list) / len(my_list)

while True:
    result_list = get_user_values(result_list) # so this list will keep growing
    print(f"Average is {get_average(result_list):.2f}")
    # len(result_list) is the number of values
    print(f"Number of values is {len(result_list)}")
    user_input = input("Do you want to continue? (y/n): ")
    if user_input.lower() != "y":
        break