# 4 uzdevums

from uzd2_cubes import get_input # very easy in Python to import functions from other files
# as long as the file is in the same folder

def vai_ir_pirmskaitlis(skaitlis):
    if skaitlis < 2:
        return False
    for i in range(2, int(skaitlis**0.5) + 1):
        if skaitlis % i == 0:
            return False
    # default if nothing divides the number
    return True
 
# pirmskaitlu_saraksts = [2]
# skaitlis = 3
PRIME_LIST_LENGTH = get_input("Ievadiet pirmskaitļu saraksta garumu: ", int)
 
# while len(pirmskaitlu_saraksts) < PRIME_LIST_LENGTH:
#     if vai_ir_pirmskaitlis(skaitlis):
#         pirmskaitlu_saraksts.append(skaitlis)
#     skaitlis += 2

# let's create a function to get the prime list
def get_prime_list(how_many):
    """Returns a list of prime numbers
    :param how_many: how many prime numbers to return
    :return: list of prime numbers
    """
    prime_list = [2]
    number = 3
    while len(prime_list) < how_many:
        if vai_ir_pirmskaitlis(number):
            prime_list.append(number)
        number += 2
    return prime_list
 
pirmskaitlu_saraksts = get_prime_list(PRIME_LIST_LENGTH)
print(pirmskaitlu_saraksts)