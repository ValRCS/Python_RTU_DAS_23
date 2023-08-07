# DRY principle - Do Not Repeat yourself
# data should have a single place
# name = "Līga"
# we can get a string from user input
name = input("What is your name friend?") # when we press Enter
# the text/string results will be stored in name

print(name)
print("Hello " + name)
print(f"Hello there {name}, what a nice name!") # note the f string syntax

food = input(f"What is your favorite food {name}?")
print(f"Awesome, I like {food} too!")

price = input(f"So {name} how much is/are {food} in your market?")
price = float(price) # we convert string to float, errors are possible
double_price = price * 2
print(f"So double price for {food} would be {double_price}?")
# it is possible to immediately convert input string to int (or float )
quantity = int(input(f"So how many kg of {food} would you like to buy?"))
# we will want to convert to integer (or possibly float) depending on problem
# quantity = int(quantity) # if user enters 3.27 it will throw error
# if you want to accept floats then use float(quantity)

total = price * quantity
# f -strings lets us format output without rounding
#  {my_var:.5f} inside f-string would give you 5 digits after comma
print(f"Wow so {quantity} kg of {food} costs {total:.2f} at your market, inflation eh?")
# we could also round things
# https://en.wikipedia.org/wiki/Vancouver_Stock_Exchange careful with rounding
total_rounded = round(total, 2) # 2 refers to precision 2 digits after comma
print(f"Rounded price for {food} would be {total_rounded}")
integer_price = int(total) # will work on floats
price("Just euro price", integer_price)