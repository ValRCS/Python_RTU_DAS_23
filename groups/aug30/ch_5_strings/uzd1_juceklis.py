# Uzdevums 1
word = input("Your word: ") # enter your word and save as variable
print(word[::-1]+f", pamatigs juceklis vai ne {word[0]}") # print backwards, than "", than first letter

first_letter = word[0]
# reversed_word =''.join(reversed(word)) # lets us create string from any collection of strings that are iterable
# same as 
reversed_word = word[::-1].capitalize() # lets us create string from any collection of strings that are iterable
print(f"{reversed_word} --> pamatīgs juceklis ar", first_letter)