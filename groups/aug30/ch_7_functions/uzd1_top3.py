number_list = []
while True:
    number = (input("Insert float: "))
    if number == "q":   
        print("Exit")
        break
    else:
        try:
            number_list.append(float(number)) # we could potentially get an error here
            suma = sum(number_list)
            average = suma / len(number_list)
            print(f"You entered {number_list}")
            print(f"Average value: {average:.2f}") # to show only 2 digits after comma
            sorted_list=sorted(number_list)
            print(f"Sortedl list: {sorted_list}")
            print(f"BOTOM3: {sorted_list[:3]}")
            print(f"TOP3: {sorted_list[-3:][::-1]}")
        except ValueError as e:
            print("You did not enter a number")
            print(e)
            # continue # not necessary since we are at the end of the loop

# at the end
# stats
print(f"You entered {number_list}")
print(f"Average value: {average}")
sorted_list=sorted(number_list)
print(f"Sortedl list: {sorted_list}")
print(f"BOTOM3: {sorted_list[:3]}")
print(f"TOP3: {sorted_list[-3:][::-1]}")
