# list comprehensions provide a concise way to create lists

# for example I want squares from 0 to 19
squares = [] # typical way
for x in range(20):
    squares.append(x**2)
print(squares)

# alternative way using list comprehension
squares_also = [x**2 for x in range(20)] # x could be n, or any other name
print(squares_also)

# we can also use if statements in list comprehensions
# for example I want squares from 0 to 19 but only even ones
squares_even = [x**2 for x in range(20) if x % 2 == 0]
print(squares_even)

# if we did not know about list comprehensions we could do this
squares_even_also = []
for x in range(20):
    if x % 2 == 0:
        squares_even_also.append(x**2)
print(squares_even_also)

# general advice use list comprehensions when the logic is simple
# use loops when logic is more complex

# theoretically we could have nested loops in list comprehensions
# say multiplication table for 0 to 10 inclusive

multiplication_table = [f"{x}x{y}={x*y}" for x in range(11) for y in range(11)]
print(multiplication_table)

# I could have made two dimension table
multiplication_table_2d = [[f"{x}x{y}={x*y}" for x in range(11)] for y in range(11)]
# print 5x6
print(multiplication_table_2d[5][6])

# instead we could have used two loops
multiplication_table_2d_also = []
for y in range(11):
    row = [] # create new row
    for x in range(11):
        row.append(f"{y}x{x}={x*y}")
    multiplication_table_2d_also.append(row)    
# print 5x6
print(multiplication_table_2d_also[5][6])

# I could use list comprehensions to create a list of lists
# with even number and its square
even_squares = [[x, x**2] for x in range(20) if x % 2 == 0]
print(even_squares)
# last entry is a list
print(even_squares[-1])
# so let's get last value
print(even_squares[-1][-1])


# I could use a list comprehension on say a string
name = "Valdis"
name_list = [letter for letter in name] # not much point since list(name) would do the same
print(name_list)
vowel_list = "aeiou"
# not consonants - vowels
consonants = [letter for letter in name if letter not in vowel_list]
# note: instead of vowel_list a set would be better for larger lists
print(consonants)
# i could convert back to string with
new_name = "".join(consonants)
print(new_name)

# i could have used list comprehension to create a list of lists with string and ordinal value
name_ord_list = [[letter, ord(letter)] for letter in name]
# a dictionary would be better for this, but list suffices for now
print(name_ord_list)