# height = int(input(f"Lūdzu ievadiet eglītes augstumu! "))
 
# for n in range(height):
#     print((height-n-1)*" "+ "*"*n+"*"*(n-1))
#     height -= 1

#### Otrais uzdevums
while True:
    try:
        tree_height = int(input("Ievadiet eglītes augstumu: "))
        break
    except ValueError:
        print("Please enter an integer!")
 
for i in range(1, tree_height + 1):
    spaces = " " * (tree_height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)