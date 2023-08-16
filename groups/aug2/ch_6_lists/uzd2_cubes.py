# 2 uzdevums
 
def kubu_tabula(sakums, beigas):
    kubi = []
 
    for skaitlis in range(sakums, beigas + 1):
        kubs = skaitlis ** 3
        kubi.append(kubs)
        print(f"{skaitlis} kubā: {kubs}")
 
    print(f"Visi kubi: {kubi}")
    return kubi # good idea to return the list so we can use it later
 
# while True:
#     try: 
#         sakums = int(input("Ievadi sākuma skaitli: "))
#         beigas = int(input("Ievadi beigu skaitli: "))
#         break
#     except ValueError:
#         print("Nepareiza ievade. Lūdzu, ievadiet veselus skaitļus.")
 
# let's make a function that will return certain data type from input
# we will use this function to get the start and end numbers
def get_input(message, data_type):
    while True:
        try:
            user_input = data_type(input(message))
            return user_input
        except ValueError:
            print(f"Nepareiza ievade. Lūdzu, ievadiet {data_type.__name__} skaitli.")

# we need a main guard so we can import this file without running the code
# this if checks if the file is run directly or imported
if __name__ == "__main__":
    # so we can pass functions to other functions as arguments
    # in Python functions are first class citizens
    sakums = get_input("Ievadi sākuma skaitli: ", int)
    # so I pass in as arguments the message and the data type conversion function - here int
    beigas = get_input("Ievadi beigu skaitli: ", int)
    # so I could ask for float, str, etc. and the function would still work

    kubu_tabula(sakums, beigas)