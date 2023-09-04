# 1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.
# 
# Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
# Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
# Ja ir pāri 37, tad izvadiet "iespējams drudzis"
 
 
print("1. uzdevums"+"\n")
 
temp = float(input("Please enter desired temp >> "))
if temp < 35:
    print(f"{temp} - something wrong!?! it is too coold!")
elif temp <= 37: # optional would be elif 35 <= temp <= 37:
    print(f"{temp} - is good one!")
else:
    print(f"{temp} - is TOO HIGH!!!")