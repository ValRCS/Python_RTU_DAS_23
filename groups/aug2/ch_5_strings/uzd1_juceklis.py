user_name = input("Lūdzu ievadiet savu vārdu! ")
reverse_user_name = user_name[::-1]
print(reverse_user_name.capitalize() + ", pamatīgs juceklis, vai ne " + user_name[0].upper() + "?")
# same with f-string
print(f"{reverse_user_name.capitalize()}, pamatīgs juceklis, vai ne {user_name[0].upper()}?")