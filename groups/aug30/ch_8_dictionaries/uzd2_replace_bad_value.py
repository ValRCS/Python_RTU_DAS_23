# n7_u2
 
def replace_dict_value(d, bad_val, good_val):
    """
        Replace all values in dictionary d that are equal to bad_val with good_val
        OUT OF PLACE approach
        We create a new dictionary and return it
    """
    # new_dict = {key: (int(good_val) if value == int(bad_val) else value) for key, value in d.items()}
    # new_dict = {key: (good_val if value == bad_val else value) for key, value in d.items()}
    # same without dict comprehension
    new_dict = {}
    for key, value in d.items():
        if value == bad_val:
            new_dict[key] = good_val
        else:
            new_dict[key] = value # we keep the old value
    return new_dict
 
my_dict = {'a': 1, 'b': 7, 'c': 3, 'd': 6, 'e': 4}

print(replace_dict_value(my_dict, 7, 0))