# for loops have same constructs as while loops
# break, continue and also else

for n in range(5):
    print(n)
    if n == 3:
        print("Break time!", n)
        break

# here we go after break
print("After break n is", n)
