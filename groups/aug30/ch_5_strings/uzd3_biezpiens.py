###########
# 05.03
###########
 
replacable_start = "nav"
replacable_end = "slikt"
 
replacement = "ir lab"
 
sentence = input("Ievadiet teikumu:")
 
while True:
    start_position = sentence.find(replacable_start)
    if start_position >= 0:
        end_position = sentence.find(replacable_end, start_position)
        # so find has extra parameter start looking from this index position
        # if we did not know about it
        # then we would have to check if start_position index is less than end_position
        if end_position > 0:
            sentence = sentence[0:start_position] + replacement + sentence[end_position+len(replacable_end):]
        else: # no suitable end found
            break
    else: # so no start found -1
        break
 
print(sentence)