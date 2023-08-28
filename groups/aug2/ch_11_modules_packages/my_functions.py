# I will be importing these function from other files
PI = 3.1415926

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# ideally we do not want to do anything in our module except define functions
# print("Hello Python at RTU!")

# solution use name guard

if __name__ == "__main__": # this has to be exactly like this
    print("I will be executed only if this file is run directly")
    # i could run some program here
    # i could put tests here
    # asserts will throw an error if the condition is not met
    assert add(1, 2) == 3
    assert add(2,2) == 4
    assert subtract(1, 2) == -1
    print("All tests passed!")