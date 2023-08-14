MAX_BAD_GUESSES = 4

word = input("Ievadiet vārdu: ")
# i could normalize the word to lowercase here
hidden_word = ""
for char in word:
    if char == " ":
        hidden_word += " "
    else:
        hidden_word += "*"

print(hidden_word)

while hidden_word != word:
    guess = input("Ievadiet burtu: ")
    # # TODO add code to store the guess in a list ( could use a string as well)
    # and check if it is not a duplicate!
    new_hidden_word = ""
    # for i in range(len(word)):
    #     if guess == word[i]:
    #         new_hidden_word += guess
    #     else:
    #         new_hidden_word += hidden_word[i]
    # we could have used zip to go through two lists at the same time
    # zip lets us loop through two iterables/sequences/strings/lists at the same time
    for hidden_char, word_char in zip(hidden_word, word):
        if guess == word_char:
            new_hidden_word += guess
        else:
            new_hidden_word += hidden_char

    if new_hidden_word == hidden_word:
        print(f"Nepareizs minējums {guess}")
        MAX_BAD_GUESSES -= 1
        
        # TODO add code to draw the person - ASCII art
        # FIXME we use for broken code
        # te ieliktu kodu cilvēka zīmēšanai
        if MAX_BAD_GUESSES == 0:
            print("Spēle beigusies")
            print(f"Pareizais vārds bija {word}")
            break
    hidden_word = new_hidden_word
    print(hidden_word)
    print(f"You have {MAX_BAD_GUESSES} guesses left")