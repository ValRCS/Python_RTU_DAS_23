def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    '''
    Returns True if mytext is a pangram, False otherwise.
    pangram is defined as a sentence using every letter of the alphabet at least once.
    a is the alphabet, by default it is the English alphabet.
    '''
    mytext_set = set(mytext.lower()) # for this we assume case is not important
    alphabet_set = set(a)
    return alphabet_set <= mytext_set # so if all letters of alphabet are in mytext_set then it is a pangram

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("The quick brown fox jumps over the lazy cat")) # should be False

latvian_alphabet = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
# assert length is 33
assert len(latvian_alphabet) == 33
latvian_text = "Ātri brauca āboliņš, āboliņš ātri brauca"
print(is_pangram(latvian_text, latvian_alphabet)) # False
hippies = "Muļķa hipiji mēģina brīvi nogaršot celofāna žņaudzējčūsku."
print(is_pangram(hippies, latvian_alphabet)) # True
gnomes = "Glāžšķūņa rūķīši dzērumā čiepj Baha koncertflīģeļu vākus."
print(is_pangram(gnomes, latvian_alphabet)) # True
fakirs = "Četri psihi faķīri vēlu vakarā zāģēja guļbūvei durvis, fonā šņācot mežam."
print(is_pangram(fakirs, latvian_alphabet)) # True
# TODO find the shortest Latvian pangram
# 33 is possible
# maybe you can make a better one?
# https://jurjans.lv/lvpp/
# TODO check if it is perfect pangram
