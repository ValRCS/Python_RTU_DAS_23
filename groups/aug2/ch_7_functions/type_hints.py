# In Python since 3.5 we can use type hints
# idea is to provide hints to the programmer and IDE on what data types are expected
def add(a: int, b: int) -> int:
    """Adds two numbers and returns the result
    :param a: first integer number
    :param b: second integer number
    :return: sum of a and b
    """	
    return a + b

result = add(10, 20)
print(result)
# pylance will complain if I pass a string, BUT Python will not
string_result = add("hello", "world")
print(string_result)
# i can even pass lists
list_result = add([1, 2, 3], [4, 5, 6])
print(list_result)
float_result = add(10.5, 20.5)
print(float_result)

# so again Type hints are great for documentation and IDEs, but they do not enforce anything