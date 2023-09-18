def is_palindrome(text: str) -> bool:
    # first get rid of whitespaces and commas
    # text_replace = text.replace(' ', '').replace(',', '')
    # # normalize to lowercase
    # text_replace = text_replace.lower()
    # text_reverse = text_replace[::-1]
    # return text_replace == text_reverse
    # one liner - not recommended for readability
    return text.replace(' ', '').replace(',', '').lower() == text.replace(' ', '').replace(',', '').lower()[::-1]

print(is_palindrome("Valdis"))
print(is_palindrome("Alus ,,ari ira      ,   sula"))
print(is_palindrome("TENET"))