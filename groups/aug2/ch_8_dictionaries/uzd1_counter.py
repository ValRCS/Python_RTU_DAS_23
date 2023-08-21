def count_letters(input_string): # funkcija ar vienu parametru
    input_string = input_string.lower() # pārvēršam Vārds par vārds
    letter_count = {}  # startējam tukšu dictionary, vieta atmiņā, kur varēs ierakstīt key:value pāri
 
    for letter in input_string: # cikls iet cauri ievadītajam stringam un skaita katru unikālo burtu
        if letter in letter_count:  # in atgriež True, ja burts atrasts
            letter_count[letter] += 1 # šis skaita tos True gadījumus
        else:
            letter_count[letter] = 1 # ja burts ir viens, tad viens arī paliek
 
    return letter_count # funkcija atgriež dictionary

input_string = "JanisJurisAinarsIlzeIlga" # input strings arguments tiks padots uz funkciju
result = count_letters(input_string) # mainīgajā result tiks ierakstīts funkcijā saskatītie burti
print(result)

print(count_letters("Valdis is testing this"))

# counting is so common that there is a built in Counter class
from collections import Counter # standard library
my_counter = Counter("Valdis is testing this")
print(my_counter) # so we get a dictionary like object with counts
# i call it dictionary with benefits
pure_dict = dict(my_counter) # we can convert it to a pure dictionary
print(pure_dict)
# i can get most common letters
print(my_counter.most_common(3)) # most common 3 letters
# so most_common is this benefit of Counter class
# most_common returns a list of tuples
# again we can convert list of tuples to a dictionary
top_3_dict = dict(my_counter.most_common(3))
print(top_3_dict)

# I can count say a list of food items
food_items = ['banana', 'apple', 'banana', 'orange', 'apple', 'banana', 'banana']
food_counter = Counter(food_items)
print(food_counter)
# top 2
print(food_counter.most_common(2))