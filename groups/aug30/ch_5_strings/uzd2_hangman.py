# ----- HANGMAN GAME ----
# PLAYER ONE
secret_word = input("\n\nFIRST PLAYER, enter the secret word: ").lower() # Lowercase for case-insensitive matching
# masked_word = '*' * len(secret_word) # good for single word

masked_word = '' # buffer approach suitable for multiple words
for c in secret_word:
    if c == ' ':
        masked_word += ' '
    else:
        masked_word += '*'

print(f"\n\nSECOND PLAYER, you have {len(secret_word)} tries to guess the word: {masked_word}")

penalty = 0 # Penalty counter
MAX_GUESSES = 5 #possible this setting is read from some config file, or passed as argument
 
# THE GAME
while '*' in masked_word and penalty < MAX_GUESSES:
    print("\nGuess the word:", masked_word)
    
    # PLAYER TWO
    guess = input("SECOND PLAYER, guess the letter: ").lower()
    
    # Check if the guessed letter is in the secret word
    correct_guess = False
    # index based approach
    # for i in range(len(secret_word)):
    #     if secret_word[i] == guess:
    #         masked_word = masked_word[:i] + guess + masked_word[i+1:]
    #         correct_guess = True #so as long as we have at least one correct guess we do not get penalty

    # another approach building a new string
    buffer = ''
    # i will loop through both hidden and secret word at the same time
    for c, hidden_c in zip(secret_word, masked_word): # i can loop two(or more) iterables at once with zip
        if c == guess:
            buffer += c
            correct_guess = True
        else:
            buffer += hidden_c
    masked_word = buffer
            
    if correct_guess:
        print("Correct!")
    else: # means we did not find any matching letters
        penalty += 1
        print(f"Incorrect. You get a penalty point now at {penalty}")
       
# END OF GAME
if penalty >= 5:
    print(f"\nGAME OVER! Secret word: {secret_word}")
else:
    print(f"\nCongratulations! You guessed the word: {secret_word}")