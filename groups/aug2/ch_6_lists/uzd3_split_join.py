#### lesson 3  
sentence = input("Ievadiet teikumu: ")
 
words = sentence.split() # by whitespace by default
# now we create a list of reversed words
# using list comprehension
# reversed_words = [word[::-1] for word in words]
# if i did not know list comprehension, i could have done this:
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
# and join them back into a sentence
reversed_sentence = ' '.join(reversed_words)
 
print(reversed_sentence)