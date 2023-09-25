# packages in Python

# packages are a way to organize modules
# typically we will have a folder with __init__.py file
# not required in Python 3.3 and above

# so package is basically a folder with .py files

# so lets import our package

# import my_package # this will run __init__.py file

# instead we can import just the module
import my_package.another_mod as another_mod # we shorten the name space
print(another_mod.mult(2,3))

# without renaming I would have to use full namespace
import my_package.my_mod_1
print(my_package.my_mod_1.add(2,3))

# it is possible to have sub packages and sub sub packages and so on
# just keep making subfolders with __init__.py files and .py files

# again we can import specifc parts of the module within the package
from my_package.my_mod_1 import add, sub
# we do lose the namespace then
print(add(2,3))