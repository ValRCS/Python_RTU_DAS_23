# uzd. 2. Eglīte
while True:
    try:
        h = int(input("Please enter Christmas tree's desirable height: "))
        break
    except ValueError:
        print("Please Enter an integer")
 
print("Look in to your Christmas tree")
for i in range(h):
    print(" " * (h - i - 1) + "*" * (2*i + 1))

rows = h
a = 1 # First row — one star
 
while a <= rows:
    spaces = " " * (rows - a) # Align the asterisks in each row of the pyramid, centred.
    stars = "*" * (2 * a - 1) # If -a- is 1 — one star, if a is 2 — three stars.
    print(spaces + stars)
    a += 1