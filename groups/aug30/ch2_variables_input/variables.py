# let's talk about variables in Python
# we might want to store data for usage later in program
# in Python variables are declared and available use by assigning something to them
# names should start with lowercase
# include _ when separating multiple words
# you can use numbers after first alphabet letter
# ideally no more than 2-3 words for variable
really_long_silly_variable_name = "Monthy"
# in Python we do not use camelCase unless it is an existing project
# which started this way...
# we use ClassNameStyle for classes
# Python has a style guide
# PEP 008
# https://peps.python.org/pep-0008/#function-and-variable-names
# use normal latin alphabet in your variables


name = "Valdis" # so name points to fixed string "Valdis"
food = "potatoes"
age = 49
speed = 110
# nothing happens so far since I only stored some
# notice I did not need to specify data type it is inferred automatically
# and it can be changed later
# so called duck typing - if it quacks like a a duck, walks like a duck it is a duck
print("My name is " + name) # show name using concatenation
# the whitespace between + is of not importance
# python offers a nice way of formatting strings
print(f"My name is {name}") # so i put f before quotes
# and I get f-strings - so called string interpolation
# idea - I can put variables and expressions inside { }

print(f"I am {name} and I like {food}")
print(f"I am {age} years old and I drive {speed} km/h fast")
last_name = "Saulespurēns"
print(f"My full name without spaces {name}{last_name}")
print(f"My full name with 3 spaces {name}   {last_name}")
# i can use any normal expression inside { }
print("2+2={2+2}") # not f-strings
print(f"2+2={2+2}") # f-strings
drink = "beer"
print(f"My name is {name} and I want {drink*3}") # so drink*3 is legal expression
# for complicated expressions better save result in a variable first
big_drink = drink * 7
print(f"My name is {name} and I want {big_drink}")
# i can change my mind and change values for some variables
drink = "kefir"
# i can add space and then multiply
medium_drink = (drink + " ") * 3
print(f"My name is {name} and I want {medium_drink}")
print("Whew all done")
# Python does not have true constance
# however we often use ALL_CAPS for constant values
PI = 3.1415926 # constant by convention
print(f"My pi is {PI}")
radius = 6
area = PI*radius**2 
print(f"Area of circle with radius {radius} is {area}")
# we can format output precision  with :.precisionf
# next example I only want 2 digits after comma
print(f"Area of circle with radius {radius} is {area:.2f}")

# if I wanted to change value i could have used round function
rounded_area = round(area, 2) # 2 is for 2 digits after comma
print(f"Rounded area is {rounded_area}")
# i can overwrite original
area = round(area, 3) # original is changed here
print(f"Area of circle with radius {radius} is {area}")
