# This is a comment meant for humans, computers ignore this line
# So Python uses # for comments
print("Hello Python on August 30th!")  # I could comment after some instruction
# ideal comments describe WHY not WHAT
# when learning it is fine to use comments for WHAT as well

# now let's try to break things
print("Hello") # so Thonny used Ctrl-3 (Cmd-3 on Mac), why? Hint look at keyboard
# most code editors and IDEs use Ctrl-/ , because they are C centric

# let's break things again
# plint("Hmmmm...") # will throw an NameError because plint function does not exist

# print has full Unicode support
print("It is sure hot 🥵 and humid 💦 today")
print("I could sure go for a beer 🍺 now")
# i could use Latvian or any language
print("Raibi runči Rīgā rūca")
# Python offers full Unicode support since moving form Python 2 to Python 3 some 10+ years ago
# In Unicode we have support for over 1 million different characters
# So all languages, emojis etc
# problem is that single byte is not enough to encode so much

# now let's see what Python can do as a calculator
print(2+2) # note lack of quotes
print(10-7)
print(5*6) # note * for multiplication
print(20/5) # regular division, note . after result, returns float
print(20//5) # returns whole number without reminder
print(20/6) # will be a little surprising
# in Python as in any other language supporting IEEE-754 standard
# floats behave a bit strangely after some 15-16 digits
# how about whole numbers
print(20//6) # prints 3 because that is the whole part
# we can also get the reminder
print(20%6) # 2 because 20 divided by 6 gives reminder 2
print(10%7) # 3 because result is 1 and we have 3 as a reminder
# useful we can determine odd or even
print(10%2, 11%2, 12%2, 13%2)
# note how I used print for multiple values here
# by default print will put single whitespace between values
print("Valdis","Saulespurēns") # will put single white space again
# compare string concatenation with +
print("Valdis" + "Saule  spurēns") # no whitespace, but whitespace between my last name parts
# do you think you can add number and string?
# print("Year" + 2023) # will not work different types
print("Year "+str(2023)) # one way, there are other ones too

# how about multiplying string with number?
print("beer"*5) # Python offers us a way to multiply some string
# useful for say
print("*"*80)
print("😉"*40)

# let's get back to math
# we can use ** to raise powers
print(2**8) # so this is how many different numbers can be stored in one byte - 8 bits
# how about highest memory address in 16 bit microcontroller (without tricks)
print(2**16)
# maximum colors in 24 bit color monitor
print(2**24) # 16 million
# some monitors advertise 10 bit depth but it is for each color(RGB)
# thus
print(2**10)
print((2**10)**3) # we have 3 colors
# btw we can use _ for writing large numbers, Python will ignore _
print("Here is a big number", 1_000_000_000)
# so 32 bit OS and CPUs memory limit was
print(2**32)
# so how much memory can we address with 64-bit CPU and OS?
print(2**64)
# so good news twice
# first we know that we have plenty memory addressing with 64bits for next few hundred years barring some extra discovery
# second news: Python has built in large number support
print(10**87) # number of atoms in Universe...
print(1000**40) # big number

# we saw that we can use parenthesis to control operations
print((3+7)*(15+5))
print("Almost done")