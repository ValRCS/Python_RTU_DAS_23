# conditional Execution means we do something
# when some condition is True
# if True: # in Python : is almost always followed by indentation
if False: # this will not run because it is False
    print("We are inside if block")
    # still inside if block
print("We are outside if block, this will always Run")

# of course usually we will have some comparision with some variables
a = 5
b = 10
if a < b:
    print(f"So {a} is less than {b}?, {a<b}")
    print("Do more stuff when a is less than b")
    # do whatever you want when a is less than b
    # in most Python editors we can use tab that automatically converts to 2 or 4 or 8 whitespaces - user defined in settings
    # standard convention is 4 (but 2 or 8 is used as well)
# gain we are back in global block
print("Always runs")

current_year = 2023
print(f"Hmm it is now year {current_year}")
future_year = 2050
current_year += 100 #
print(f"Hmm it is now year {current_year}")
# idea run only one path from next comparison
if current_year < future_year:
    print(f"Future is still not here", current_year, future_year)
else: # so runs when connected if is False
    print("Future is here!!!")
    print("Current year", current_year)
    print("Future year", future_year)
    
print("Back to common path")

# how about more than two paths?
# we use if elif (elif elif elif...) else statements

secret = 42
guess = int(input("Guess a number(integer only)"))

# so from next path only ONE path will run
if guess > secret:
    print("You guess too high")
    print("Your guess was", guess)
elif guess < secret: # 2nd check, check is performed only when first check is False
    print("You guess too low")
    print("Your guess was", guess)
else: # we only have guess == secret left so
    print("You guessed my secret!!!")
    print("Guess is equal to secret", guess == secret)
    
# we can also use nested if else statements
# WARNING: avoid too much nesting!!

if a < b:
    print("a < b", a, b)
    if secret > b:
        print("Secret is larger than b", secret, b)
    else: # this if is attached to secret > b
        print("Secret is less or equal to b", secret, b)
else: # this else is attached to if a < b:
    print("a >= b", a, b)
    if guess > b:
        print("Guess is larger than b", guess, b)
    else: # this if is attached to guess > b
        print("Guess is less or equal to b", guess, b)
        
# we could have rewritten the above code to flatter single if elif elif        
if a < b and secret > b:
    print("a < b and secret > b")
elif a < b and secret <= b:
    print("a < b and secret <= b")
elif a >=b and guess > b:
    print("a >=b and guess > b")
elif a >=b and guess <= b:
    print("a >=b and guess <= b")
    


# Python 3.10 added match case for multiple if elif elif elif else
# similar to switch case in other languages but more powerful matching

