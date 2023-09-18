##############################
## 06.04
##############################
prime_count = int(input("Cik pirmos pirskaitļus meklēt?:"))
 
def is_prime_number(number:int)->bool:
    if 2 <= number <= 3:
        return True # 2 and 3 are prime numbers
    i = 2
    while i ** 2 <= number:
        if number%i == 0:
            break
        i += 1
    else: # means that the loop did not break and thus we have a prime number
        return True
    return False
 
prime_numbers = [2] # list with one element, here 2 is special case
each_number = 1
while len(prime_numbers) < prime_count:
    each_number += 2
    if is_prime_number(each_number):
        prime_numbers.append(each_number)
 
print(prime_numbers)