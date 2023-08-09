import random
 
attempt = 0
max_attempts = 10
floor = 1
ceil = 100
 
secret_number = random.randint(floor,ceil)
 
print(f"Esat sveicināts spēlē - Uzminu skaitli. Jums ir {max_attempts} iespējas, lai atminētu skaitli, kuru ir izvēlējies dators.")
 
while attempt < max_attempts:
    guess = int(input("Ievadiet savu minējumu (1 līdz 100): "))
    
    if guess == secret_number:
        print(f"Apsveicam! Jūs uzminējāt skaitli ar { attempt } reizi")
        break
    
    elif guess > secret_number:
        print("Jūsu ievadītais skaitls ir lielāks nekā datora izvēlētais.")
    else:
        print("Jūsu skaitlis ir mazāks nekā datora izvēlētais")
    
    attempt += 1
    
    if attempt == max_attempts:
        print("Diemžēl ir beigušies atļautie minējuma reizes.")