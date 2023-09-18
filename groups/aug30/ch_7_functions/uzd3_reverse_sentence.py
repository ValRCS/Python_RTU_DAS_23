##############################
## 06.03 ātrs, slinks variants
##############################
user_sentence = input("Ievadiet teikumu:")

def return_reversed_words_sentence(sentence:str) -> str:
    """Returns a sentence with reversed individual words
    Args:
        sentence (str): sentence to reverse
    Returns:

    """
    return " ".join([w[::-1] for w in sentence.split()]).capitalize()

result = return_reversed_words_sentence(user_sentence)
print(result)

sentence_words = user_sentence.split()
reversed_words = [w[::-1] for w in sentence_words]
scrambled_sentence_also = " ".join(reversed_words)
capitalized_scrambled_sentence = scrambled_sentence_also.capitalize()
# could do the above in one line
scrambled_sentence = " ".join([w[::-1] for w in user_sentence.split()]).capitalize()
print(capitalized_scrambled_sentence ) # individual words are reversed
print(scrambled_sentence) # individual words are reversed
# compare with just sentence reversal (this was not asked for in the task)
# print(user_sentence[::-1].capitalize())