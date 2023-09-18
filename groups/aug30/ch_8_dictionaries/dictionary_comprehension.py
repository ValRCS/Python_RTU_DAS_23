# dictionary comprehension is a short way to create a dictionary

phone_book = {
    "Valdis": 12345678,
    "Līga": 87654321,
    "Maija": 12344321,
    "Rūta": 11111111, # last comma is optional
    "Līga K": 88888888,	
    "Līga P": 77777777,
}

# let's remember how to filter by partial key
liga_book = {}
for key in phone_book:
    if "Līga" in key:
        liga_book[key] = phone_book[key]

print(liga_book)

# let's do the same with dictionary comprehension
liga_book_also = {key:phone_book[key] for key in phone_book if "Līga" in key}
print(liga_book_also)
# iterable does not have to be a dictionary
# i could crate a mapping of letters to their ASCII codes

letter_to_ascii = {letter:ord(letter) for letter in "Valdis"}
print(letter_to_ascii)
# i could have gone reverse
ascii_to_letter = {ord(letter):letter for letter in "Valdis"}
print(ascii_to_letter)

# there is a difference between copy and alias
letter_to_ascii_alias = letter_to_ascii # not a copy just a shortcut
print(letter_to_ascii_alias)
# now copy
letter_to_ascii_copy = letter_to_ascii.copy() # this is a copy values are copied

# let's change the original
letter_to_ascii["XX"] = 999999
print(letter_to_ascii)
print(letter_to_ascii_alias) # changed because it was a shortcut
print(letter_to_ascii_copy) # not CHANGED

# so we use dictionaries to store key-value pairs where we want to be able to quickly find the value by key