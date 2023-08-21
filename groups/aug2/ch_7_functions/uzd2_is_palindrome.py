#2.uzdevums
 
def is_palindrome(text):
    text = text.replace(" ", "")
    text = text.lower()
    return text == text[::-1]
print(is_palindrome("Alus ari ira   sula"))

