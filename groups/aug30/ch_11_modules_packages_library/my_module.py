# my module is just a name
# my_module.py is the file name
# my_module is the module name

my_list = [1, 2, 3]
my_string  = "Hello RTU!"

def my_add(a,b):  
    return a + b

class MyPersonClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# in general we want to avoid code being run when we import a module
# print("I am being run!")

# we can use main guard to avoid code being run when we import a module
if __name__ == "__main__":
    print("I am being run as main program!")
    # you could run a normal program here or run tests
    print(my_list)
    print(my_string)
    print(my_add(1,2))
    # a test example
    assert my_add(1,2) == 3
    assert my_add(0,0) == 0
    assert my_add(-1,1) == 0
else: # means I was imported - rarely used - standard is to do nothing
    print("I am being imported!")