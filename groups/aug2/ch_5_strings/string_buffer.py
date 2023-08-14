# we can use buffer to build strings
# for example
# if we did not know about lists
buffer = ""
sentence = "This is a sentence with number 1414 151015 and some other stuff"
# instead of replace we could use a buffer to perform more complex operations
for char in sentence:
    if char == " ":
        buffer += "_" # so in effect replacing space with underscore
    elif char.isdigit(): # isdigit is a string method for single characters
        buffer += "X"
    else:
        buffer += char # otherwise keep original character
print(buffer)
# in this example we could have used replace method
# buffer method is for more complex operations