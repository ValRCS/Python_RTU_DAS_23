######## uzdevums nr 3
def is_pangram(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    mytext = mytext.lower().replace(" ", "")  # Konvertējam uz mazajiem burtiem un noņemam atstarpes
    return all(char in mytext for char in a)
 
print(is_pangram("abcd foo"))  # Izdrukās False
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Izdrukās True
print(is_pangram("The five boxing wizards jump quickly"))  # Izdrukās True

# let's solve the same problem with sets

def is_pangram_set(mytext, a='abcdefghijklmnopqrstuvwxyz'):
    mytext = mytext.lower() # Konvertējam uz mazajiem burtiem un noņemam atstarpes
    # now we check if mytext is super set of a
    return set(mytext) >= set(a)

# test it
print(is_pangram_set("abcd foo"))  # Izdrukās False
print(is_pangram_set("The quick brown fox jumps over the lazy dog"))  # Izdrukās True
print(is_pangram_set("The five boxing wizards jump quickly"))  # Izdrukās True

# should work with Latvian as well
latvian_a = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
assert len(latvian_a) == 33

print(is_pangram_set("Ārā kalnos bija biezpiens, bet mājās biezpiena nebija")) # False - English alphabet
print(is_pangram_set("Ārā kalnos bija biezpiens, bet mājās biezpiena nebija", latvian_a)) # False

# latvian pangram
# https://clagnut.com/blog/2380#Latvian

hippies = "Muļķa hipiji mēģina brīvi nogaršot celofāna žņaudzējčūsku."
print(is_pangram_set(hippies, latvian_a)) # True
gnomes = "Glāžšķūņa rūķīši dzērumā čiepj Baha koncertflīģeļu vākus."
print(is_pangram_set(gnomes, latvian_a)) # True
fakirs = "Četri psihi faķīri vēlu vakarā zāģēja guļbūvei durvis, fonā šņācot mežam."
print(is_pangram_set(fakirs, latvian_a)) # True

# there are even shorter Latvian pangrams, find them!