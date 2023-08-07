# so where do we use our booleans?
# we use them for conditional work - do something on some condition
# idea if something is True we do something
# if True: # in Python after : we generally have indentation
#     # if block starts here
#     print("This runs only when if condition is True")
#     print("Still inside")
#     # still inside could do more
# outside if
print("Outside if")
# generally we will want to have at variable for if
a = 20
b = 4
if a < b:
    # inside if
    print("a < b for sure", a, b)
    # still inside
    print(f"So naturally {a} < {b} ? {a<b}")
    # still inside

# outside if
print("Regular code outside if")

# often we want to take exclusive paths depending on some condition
# meaning only one path will run
# b = 30
b = 40
if a * 2 > b:
    # inside if
    print("a * 2 > b for sure", a, b)
    print("could do something when a is more than b")
else: # means a < b or possible a == b so a <= b
    print("a * 2 <= b for sure", a, b)
    print("could do something when a is less or equal to b")
    
# back to normal program flow
print("normal command happens no matter what if else")

# if we need say 3 exclusive branching
# meaning only one of the three will run
# we use if elif else construction

number = int(input("Enter an integer please "))
secret = 42

if number < secret:
    print("Your guess is too low try higher")
elif number > secret:
    print("Your guess is too high")
else: # only number == secret remains # else is optional here
    print("Super!")
    print("You guessed right!", number, secret)
    
# if we need more exclusive paths
# we just add more elif statements before final else
    
# program is outside if elif else block
print("We continue normally")

# compare multiple ifs
if number < secret:
    print("Your guess is too low try higher")
# next if is not related
if number <= secret:
    print("your guess is again too low")
    
# it is also possible to nest ifs inside another if
# just avoid going more than 3-4 levels deep
if number < secret:
    if number < 50:
        print("Oh number is less than 50 and less than secret", number)
    else: # this else is connected to if number < 50
        print("Oh number is at least 50!", number)
else: # so number is at least equal to secret
    print("WE know number is equal or more than secret")
    if number > 100:
        print("Number is over 100")
    else:
        print("Number is 100 or less", number)