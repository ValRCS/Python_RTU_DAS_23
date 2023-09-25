# import my_module # runs everything in my_module.py

# print("Hello package world!")

# # i have acces to my_module data
# print(my_module.my_list)
# print(my_module.my_string)
# print(my_module.my_add(1,2))

# me = my_module.MyPersonClass("Valdis", 30)

# print(me.name)

# so module is basically a file with python code

# so why do we need modules?

# we gain modularity

# 1. to organize code by use case
# 2. to reuse code
# 3. to avoid name collisions - in example above my_list is in my_module namespace
# 4. to hide implementation details 

# some advice on naming modules
# 1. use short names
# 2. use lowercase names
# 3. don't use built-in names - avoid names like math.py, random.py, etc.

# we might want to rename our module when we import it

# import my_module as mm  #typical to use 2 or 3 letter abbreviation

# print(mm.my_list)
# print(mm.my_string)
# print(mm.my_add(1,2))
# me = mm.MyPersonClass("Valdis", 30)
# print(me.name)

# we can import only some parts of the module
# lets import just the class
# from my_module import MyPersonClass, my_add
# # typically done with huge modules

# me = MyPersonClass("Valdis", 30)
# print(me.name)
# print(my_add(1,2))
# # above approach loses namespace so we can't use my_module.my_add

# we can rename the parts we import
# from my_module import MyPersonClass as MPC, my_add as add
# me = MPC("Valdis", 30)
# print(me.name)
# print(add(1,2))

# again we have to be careful because we can have name collisions

# finally one approach that is not recommended
# from my_module import * # this will import everything in global namespace
# AVOID THIS