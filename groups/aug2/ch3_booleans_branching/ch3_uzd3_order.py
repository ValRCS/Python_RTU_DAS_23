skaitlis1 = input("Ievadiet pirmo skaitli ")
skaitlis1 = float(skaitlis1)
skaitlis2 = input("Ievadiet otro skaitli ")
skaitlis2 = float(skaitlis2)
skaitlis3 = input("Ievadiet trešo skaitli ")
skaitlis3 = float(skaitlis3)
 
 
if skaitlis1>=skaitlis2>=skaitlis3:
    print(f"{skaitlis1}, {skaitlis2}, {skaitlis3}")
elif skaitlis1>=skaitlis3>=skaitlis2:
    print(f"{skaitlis1}, {skaitlis3}, {skaitlis2}")
elif skaitlis2>=skaitlis3>=skaitlis1:
    print(f"{skaitlis2}, {skaitlis3}, {skaitlis1}")
elif skaitlis2>=skaitlis1>=skaitlis3:
    print(f"{skaitlis2}, {skaitlis1}, {skaitlis3}")
elif skaitlis3>=skaitlis1>=skaitlis2:
    print(f"{skaitlis3}, {skaitlis1}, {skaitlis2}")
elif skaitlis3>=skaitlis2>=skaitlis1:
    print(f"{skaitlis3}, {skaitlis2}, {skaitlis1}")
else:
    print("Kaut kas nesagāja")