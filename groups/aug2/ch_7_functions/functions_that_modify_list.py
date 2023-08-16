# let's talk about how functions can modify lists
# let's make a function that will multiply all numbers in a list by a given number

def multiply_list_by_number(number_list, number):
    """Multiplies all numbers in a list by a given number
    IN PLACE
    :param number_list: list of numbers
    :param number: number to multiply by
    """
    for index in range(len(number_list)):
        number_list[index] *= number

original_list = [1, 2, 3, 4, 5]
print(original_list)
multiply_list_by_number(original_list, 10)
print(original_list)

# i could create a similar function that returns a new list
def multiply_list_by_number_new(number_list, m_number):
    """Multiplies all numbers in a list by a given number
    original list is not modified!
    :param number_list: list of numbers
    :param number: number to multiply by
    :return: new list with multiplied numbers
    """
    new_list = []
    for n in number_list:
        new_list.append(n * m_number)
    # if i do not return new_list, then the function will return None
    # and new_list will be lost!
    return new_list
    # I could have used list comprehension
    # return [n * m_number for n in number_list]

original_list = [1, 2, 3, 4, 5]
print(original_list)
new_list = multiply_list_by_number_new(original_list, 10)
print(original_list)
print(new_list)