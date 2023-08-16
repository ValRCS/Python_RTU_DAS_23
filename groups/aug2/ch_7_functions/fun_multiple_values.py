# we can write a function that returns multiple values

def multiply_and_divide(a, b):
    return a * b, a / b # returns a tuple - basically a fixed size list

result = multiply_and_divide(10, 20)
print(result)
# i can also unpack the result
my_multiply_result, my_divide_result = multiply_and_divide(10, 20)
print(my_multiply_result)
print(my_divide_result)

# how about min, max, sum, average

def min_max_sum_average(numbers):
    return min(numbers), max(numbers), sum(numbers), sum(numbers) / len(numbers)

result = min_max_sum_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)

# alternative would be to put the return values in a list but that is less readable