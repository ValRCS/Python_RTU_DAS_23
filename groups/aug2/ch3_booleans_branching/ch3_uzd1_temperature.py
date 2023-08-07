# 4. uzdevums
 
temperature = float(input("Please enter your temperature: "))
 
if temperature < 35:
        print("Vai nav par aukstu?")
elif temperature <= 37: # since we already checked less than 35 this covers 35 and up
    print("Viss kārtībā!")
else:
    print("Iespējams, drudzis.")