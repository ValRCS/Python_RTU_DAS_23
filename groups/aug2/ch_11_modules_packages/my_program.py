# let's talk how we can separate our program into multiple files

# I might have functions that I would like to reuse in other programs
# Maybe I have classes that I would like to reuse in other programs

# maybe I have code from someone else that I would like to use in my program

# first let's look at the order of where python looks for modules

import sys # this is from standard library - it's built into python
# print path
print(sys.path)

# so current directory is first, then python looks in standard library
# thus your own files should not have the same name as standard library modules

# so let's look at what standart library modules are available
# docs: https://docs.python.org/3/library/

# so now I can import my_functions from my_functions.py
# import my_functions
# # I gain ability to use any function from my_functions.py
# print(my_functions.add(1, 2))
# print(my_functions.subtract(1, 20))
# # print PI which is just a variable
# print(my_functions.PI)
# so we gain namespace my_functions and we can use any function or variable from it

# i can also rename my_functions to something else
import my_functions as mf # typical to use two or three letters
# most frequently used is np for numpy, pd for pandas, plt for matplotlib for example

# # now i can use this shorter name
print(mf.add(1, 2))
print(mf.subtract(1, 20))
# print PI which is just a variable
print(mf.PI)

# we can also import specific functions from my_functions
# from my_functions import add, PI # so now I can use add and subtract directly
# # careful with this approach - if you have two functions with the same name
# print(add(1, 2))
# try:
#     print(subtract(1, 20))
# except NameError as e:
#     print(e) # name 'subtract' is not defined - we did not import it!!
# # print PI which is just a variable
# print(PI)

# finally we can import specific things and rename them
# from my_functions import add as my_adder, PI as my_pi
# print(my_adder(10, 20))
# print(my_pi)

# there is also a way to import everything from my_functions
# DO NOT USE THIS APPROACH
# from my_functions import * - we lose control of what we import

# advantages of modules:
# 1. we can reuse code
# 2. we can separate our code into multiple files
# 3. we can import code from other people
# 4. we can import code from standard library
# 5. we gain namespace
# 6. we can rename things

# so now let's import my_package

# import my_package # this will not work

# import my_package.my_cool_module # this will work

# # so now I can use my_cool_module
# print(my_package.my_cool_module.multiply(10, 20))

# instead I could use a shorter name
# very common approach
import my_package.my_cool_module as mcm
print(mcm.multiply(10, 20))
print(mcm.divide(10, 20))

# similarly I can import my_mod_1
import my_package.my_mod_1 as mm1
mm1.pretty_print("Hello Python at RTU!")

# so packages are just folders with modules inside
# packages used to require __init__.py file

# now let's import our robot class
import robot 
# so now I can create robots
r1 = robot.Robot("R2D2")
r1.say_hi()
r1.say_bye()
# anoher robot instance - new object
r2 = robot.Robot("C3PO")
r2.say_hi()

# i could have imported Robot class directly
from robot import Robot
r3 = Robot("BB8")
r3.say_hi()

# how about import Cyborg class
from robot import Cyborg 
# so now I can create cyborgs
c1 = Cyborg("T-800", "T-800a")
c1.say_hi()
c1.say_model()

