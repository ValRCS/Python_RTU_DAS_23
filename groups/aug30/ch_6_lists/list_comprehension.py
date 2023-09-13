# list comprehensions in Python let us create new lists based on existing lists
# or any other iterable

# lets create some number list
numbers = [1, 2, 3, 4, 5] # or list(range(1, 6))
print(f"numbers: {numbers}")

# how would we create a list of squares of these numbers?
# we could use a for loop
square_numbers = []
for number in numbers:
    square_numbers.append(number ** 2)
print(f"square_numbers: {square_numbers}")

# list comprehensions let us do this in one line
also_square_numbers = [number ** 2 for number in numbers] # number is just a variable name
print(f"also_square_numbers: {also_square_numbers}")

# we have option if for filtering
odd_numbers = [number for number in numbers if number % 2 == 1]
print(f"odd_numbers: {odd_numbers}")

# we can also get odd numbers squared
odd_squares = [number ** 2 for number in numbers if number % 2 == 1]
print(f"odd_squares: {odd_squares}")

# again we could have used a for loop for odd_squares
odd_squares_also = []
for number in numbers:
    if number % 2 == 1:
        odd_squares_also.append(number ** 2)

print(f"odd_squares_also: {odd_squares_also}")

# when to use list comprehensions? and when to use for loops?

# list comprehensions are more compact and more readable
# use it for simple transformations of lists

# for more complex transformations use for loops

# how would we create a list of 10 zeroes?
zeroes = [0 for _ in range(10)] # _ is a valid variable name, means I don't care about the value
print(f"zeroes: {zeroes}")
# alternative
zeroes_also = [0] * 10 # this is a bit faster
print(f"zeroes_also: {zeroes_also}")

# again the values inside list are mutable!

# let's change 4th value to 9000
zeroes[3] = 9000
print(f"zeroes: {zeroes}")