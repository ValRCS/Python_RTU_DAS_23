# we can nest our loops within each other

for a in range(10):
    print("a is", a)
    for b in range(5):
        print("b is ", b)
        print(f"{a}*{b} == {a*b}")

# so above example would perform 10*5 loops

# we can have even more nesting as much as we need
# we can also nest while loops