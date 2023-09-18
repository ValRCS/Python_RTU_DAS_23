#Uzd 8.1.a Simbolu biežums
def get_char_count(text):
    my_dict = {}
    # for i in text:
    #     my_dict[i] = my_dict.get(i, 0)+1 
    # same as
    for c in text:
        if c in my_dict:
            my_dict[c] += 1
        else:
            my_dict[c] = 1
    return my_dict
    
print(get_char_count('hubba bubba'))