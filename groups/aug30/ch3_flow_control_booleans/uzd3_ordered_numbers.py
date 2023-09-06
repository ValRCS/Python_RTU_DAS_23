# 3. Noprasiet lietotājam ievadīt 3 skaitļus, izvadiet tos sakārtotā secībā.
# 
# Piezīme: pagaidām šo uzdevumu risinam tikai ar if, elif, else darbībām
# 
# Pastāv arī risinājums izmantojot kārtošanu un list struktūru, kuru vēl neesam skatījuši.
 
 
print("\n3. uzdevums\n")
 
n1 = int(input("Enter 1st number: >> "))
n2 = int(input("Enter 2nd number: >> "))
n3 = int(input("Enter 3rd number: >> "))
 
# checking and asigning in ascending order s - smallest; m - mid; l - largest
if n1 <= n2 <= n3:  # same as n1 <= n2 and n2 <= n3
    s = n1; m = n2; l = n3
elif n1 <= n3 <= n2:
    s = n1; m = n3; l = n2
elif n2 <= n1 <= n3:
    s = n2; m = n1; l = n3
elif n2 <= n3 <= n1:
    s = n2; m = n3; l = n1
elif n3 <= n1 <= n2:
    s = n3; m = n1; l = n2
else: # n3 <= n2 <= n1
    s = n3; m = n2; l = n1
    
print(f"Numbers: {s=}; {m=}; {l=}")