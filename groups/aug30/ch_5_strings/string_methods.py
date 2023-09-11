# let's talk about Python string methods
# all methods should be called with ()
# we see methods in Visual Studio Code with . after variable name

cats = "Muris, Pukis, Ķicis, Ķuksiņš, Bubulis un mazais Pelēkais"

# again strings are immutable so we cannot change them
# we can only create new strings using methods , also slicing

# we can YELL by using upper method
print(cats.upper()) # note we do not change cats variable

# we can whisper by using lower method
print(cats.lower())
# again if we need to save the result we need to assign it to a variable
whisper_cats = cats.lower()
print(whisper_cats)
# we can combine slicing with string methods
first_quiet_cat = cats.lower()[:5] # so we get first 5 letters and then lower them
also_first_quiet_cat = cats[:5].lower() # same thing, should be tiny bit faster
# because we do not need to create a new string for whole cats

# other methods
# we can capitalize first letter of our string
print(cats.capitalize()) # note other letters are lowercased

# we can capitalize all words in our string
print(cats.title()) # note other letters are lowercased

# less useful but we can swap case
print(cats.swapcase()) # note other letters are lowercased

# we can check if our string is all lowercase
print(cats.islower()) # False because we have commas and spaces, and capital letters
print("valdis".islower()) # True

# we can check if it is a number
print("123".isnumeric()) # True
print("123.5".isnumeric()) # False
# cats are not numbers
print(cats.isnumeric()) # False

# is all alphabet
print("abc".isalpha()) # True
print("abc123".isalpha()) # False

food = "Auzu putra ar zemenēm"
# i can use replace method to replace one substring with another
print(food.replace("zemenēm", "mellenēm")) # note we do not change food variable
# i would need to save it to a variable
food_with_mellenes = food.replace("zemenēm", "mellenēm")
print(food_with_mellenes)
# food is still the same
print(food)

# I can replace single letters
# so u to y
print(food.replace("u", "y"))
# i can say replace only first 2 u's
print(food.replace("u", "y", 2))

# so how about checking if our string starts with something
print(food.startswith("Auzu")) # True
# how about ends with
print(food.endswith("zemenēm")) # True
# compare with in
print("zemenēm" in food) # True
# so in is less specific than startswith or endswith

# so how about finding something if we do not care about case?
# so auzu but we do not know if it is upper or lower case
print(food.lower().find("auzu")) # 0 - which is start of our string
# how about zemenēm
print(food.lower().find("zemenēm")) # 14 - which is start of our string
# lets gets slice from 14 on
print(food[14:]) # zemenēm

# alternative to find is index for strings
# find will return -1 if substring is not found
# index will throw an error if substring is not found
print(food.find("mušmirēm")) # -1
try:
    print(food.index("mušmirēm")) # ValueError: substring not found
except ValueError as ve:
    print(f"Value Error {ve}")

# okay let's make a dirty string and then cleanup a bit
dirty_city = "   Rīga  mana Rīga\t\n \t "
print(dirty_city)
# reminder we have escape characters \t \n
# most popular escape character is \n for new line
# \t is for tab
# \r is for carriage return
# \b is for backspace - rare
# \a is for bell - rare
# more on these on ASCII table
# see https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html

# reminder if we do not want to escape we can use raw strings
print(r"Valdis Saulespurēns \b\r\n") # note r before string so no escaping
# for multiline strings we can use triple quotes
print("""Valdis Saulespurēns
   Rīga, Latvija
      Riga Business School at Rigas Tehniska Universitate
""")
multi_line_string = """Valdis Saulespurēns

    Rīga, Latvija
    and likes potatoes

    Riga Business School at Rigas Tehniska Universitate
"""
print(multi_line_string)

# i can insert f before string to use f-strings even for multiline strings
drink = "kefīrs"

print(f"""Valdis Saulespurēns
      likes potatoes
      and {food.lower()}.
      His favorite drink is {drink}
""")

# we still have dirty city to clean up
# we can use strip method to remove whitespace from start and end
clean_city = dirty_city.strip() # by default it will remove spaces and tabs from start and end
print("Cleaned up city", clean_city) # so spaces between words are not removed
# if i wanted to remove ALL spaces i would need to replace them
# no spaces example
print(clean_city.replace(" ", "")) # so replace space with nothing
# would work with any text
# again if I want these modifications to stick I need to save them to a variable
clean_city = clean_city.replace(" ", "")

# we still want to replace the 3rd instance of u in our string
# first print our food
print("Food", food)

u_index = 6
print("u_index", u_index, food[u_index]) # so we get u
new_string = food[:u_index] + "y" + food[u_index+1:]
print("New string", new_string)
# could have use f-string
also_new = f"{food[:u_index]}y{food[u_index+1:]}"

# so now how would we go about finding 3rd instance of some substring?
needle = "u"
haystack = "Auzu putra ar zemenēm un sviestu"
# how many needles do we have in our haystack?
print(f"We have {haystack.count(needle)} occurences of {needle} in {haystack}") # 5
# so we need to find 3rd occurence
# this will work for single letter needles
find_count = 3
found_so_far = 0
for i, c in enumerate(haystack):
    # so we are looping through all letters in our haystack
    # and we also have index for each letter
    if c == needle:
        found_so_far += 1
        print(f"Found {needle} at index {i}")
        if found_so_far == find_count:
            print(f"Found {needle} at index {i} which is what we want")
            break # we can stop our loop early

# so now i will hold my index in a variable
print(f"Found {needle} at index {i} which is what we want and we can use it")

# alternative approach to changing 3rd u to y would be to use 
# list and join


