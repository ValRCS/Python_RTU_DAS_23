# Python has a very rich standard library. 
# You can find the full list of modules here: https://docs.python.org/3/library/index.html

# to use standart library we just import it

import math
print(math.pi)

# what is the order of imports?
# 1. built-in modules
# 2. modules in sys.path
# 3. PYTHONPATH environment variable
# 4. .pth files in site-packages

# to see paths where python looks for modules
import sys
print("Python paths where it will look for modules")
print(sys.path)

# thus Python first looks in the current folder!

# print Python version
print(f"Python version is {sys.version}")

# how much memory I have free now?
import os
print(f"CPU count is {os.cpu_count()}") # shows thread count