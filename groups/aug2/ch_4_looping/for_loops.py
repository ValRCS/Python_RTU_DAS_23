# for loops in Python
# idea is to go through some collection of items using for loop

# philosophically
# while loops are for indefinite (we do not know when to finish)
# for loops are for definite iteration over some collection
# collection could be many things - for now we only know of one type - strings

# string could be thought as collection of individual characters (Unicode)
# technically Python does not have character types
# we still have one character strings in Python

name = "Valdis"
for letter in name: # letter is just a name for the item we are going through
    # could be n, could i, could be c any normal variable name
    print("Letter is", letter)
    
# normal for loops ends when we have exhausted whatever collection we used
# above we use name which held "Valdis"

# how about some numbers?
# we can use range which is gives us numbers on demand
# think of range as number factory
for number in range(5): # by default range starts at 0 and ends 1 less than 5 here
    print("Number is", number)
    
# we can set specific start(inclusive) and stop(exclusive, not included)
for n in range(100, 104): # i could have reused number
    print("n is now", n)
    
# thus if i want numbers 1 to 5 included
total = 0
for n in range(1,6):
    total += n
print("1 to 5 summed is", total)
# incidentally many collections of numbers have sum available to them
print(sum(range(1,6)))

# in general range can also have step
# range(start,stop, step) # those are just variable names

start = 200
stop = 240
step = 8
for n in range(start,stop+1,step): # +1 to include stop
    print("n is now", n)
    
# if we want current index for what we are going through
# in Python the recommended way is to use enumerate
for i, letter in enumerate(name): # i could be any variable name, index, ndx etc
    print(f"Letter No. {i} - {letter} - Unicode value - {ord(letter)}")
    
# i could use enumerate with range as well
# we can adjust start of enumerate using start=start_value
for i, n in enumerate(range(10,20,2), start=1_001):
    print(f"Number No. {i} is {n}")
    
# sometimes we do not care about the number
# we just want something done n times
# good style would be to replace n here with _
# _ signifies we do not care about this variable
for _ in range(5):
    print("Alice talked")
    print("Bob walked")
    
for n in range(10):
    print(n, end= " ") # instead of newline we use space
    
# for fizzbuzz, hint
for n in range(1,11):
    if n % 2 == 0:
        print("Even", n)
    else:
        print("Odd", n)
