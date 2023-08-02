# inspecting line number
# https://stackoverflow.com/questions/3056048/filename-and-line-number-of-python-script
import sys # standard library for system calls
print(sys._getframe().f_lineno)
# so more code
my_variable = 10
result = my_variable + 25
print("Line:", sys._getframe().f_lineno, "my result", result)