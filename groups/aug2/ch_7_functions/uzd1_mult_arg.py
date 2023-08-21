# 1 Uzdevums
 
def add_mult(a, b, c):
    arguments = [a, b, c] # list , lives inside our function
    arguments.sort() # IN PLACE SORTING
    smallest_sum = arguments[0] + arguments[1]
    largest_value = arguments[2]
    result = smallest_sum * largest_value
    return result

print(add_mult(2, 5, 4))

