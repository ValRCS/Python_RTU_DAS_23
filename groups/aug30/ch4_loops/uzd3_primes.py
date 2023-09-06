# ---- PRIME NUMBER ----
# Ask the user for input
num = int(input("\n\nEnter a positive integer: "))
 

 
# Check if the number has any divisors up to
# AND including the square root
# worst case we need to check if square root is the divisor
# meaning both sides the same say 25 will have 5 and 5
# 26 will have divisor 2 un 13
# we do not need to check 13
# 21 will have divisors 3 un 7
# we do not need to go to 7
# is_prime = True
# for i in range(2, int(num**0.5) + 1): # 2 is the smallest prime number (1 has only one factor)
#     if num % i == 0:
#         print(f"{num} has {i} as divisor")
#         is_prime = False
#         break # no need to check anymore
#  
# # Print the result
# if is_prime:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

for i in range(2, int(num**0.5) + 1): # 2 is the smallest prime number (1 has only one factor)
    if num % i == 0:
        print(f"{num} has {i} as divisor")
        break # no need to check anymore
else:
    print(f"{num} is a prime!") 