# more on variables and data types and inputs

# let's see we want to make a food price calculator

# let's ask for user's name
# input will always give us a string
name = input("Hello, what is your name friend? ")
# name will be whatever user inputs untile newline (Enter ) is pressed
print(f"Oh, {name} is a nice name, I like it!")
# i can use f-strings inside input as well
food = input(f"What is your favorite food {name}? ") 
print(f"Oh {name} I like {food} too!")

price = input(f"So {name} how much is/are {food} in your local market?")
# print data type
print(f"Turns out {price} is of type {type(price)}")
# we can change the data type!
price = float(price) # so assuming this string is valid floating point number
print(f"Turns out {price} is of type {type(price)}")
double_price = price*2
print(f"So double {price} would be {double_price} would it not?")

# we can cast immediately
# here we will cast to int
quantity = int(input(f"How many kg of {food} do you want to buy {name}?"))
# we do need quantity to be float or int not string!
total = price * quantity

print(f"Wow so {quantity} kg of {food} would cost {total} Euros at your market!")
print(f"Price to cents would be {total:.2f}") # will not affect total real value
# we could also round it
# i could also overwrite original total here
rounded_total = round(total, 2) # so 2 digits after comma
print(f"Rounded price to cents would be {rounded_total}")

# again we can cast anything to str - no errors
number_as_str = str(price)

