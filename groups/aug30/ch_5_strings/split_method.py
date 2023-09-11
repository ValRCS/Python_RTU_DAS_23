# for strings we have a very nice split method
# split returns a list of strings
#list is similar to array in other languages

sentence = "A quick brown fox jumps over the lazy dog"
print(sentence) # by default split uses space as separator
words = sentence.split() # by default split uses space as separator
print(words)
print(type(words)) # so we get a list of strings

# I can use list to get individual letters
food = "kartupelis"
food_list = list(food)
print(food_list)
print(type(food_list)) # so we get a list of strings
# list is mutable so we can change it
# unlike strings which are not changeable
food_list[3] = "X" # so we can change individual letters
print(food_list)

# then I could join my list back into a string
my_new_food = "".join(food_list)
print(my_new_food)