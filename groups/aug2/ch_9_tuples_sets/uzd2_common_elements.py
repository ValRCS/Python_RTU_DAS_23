######## uzdevums nr 2
def get_common_elements(seq1, seq2, seq3):
    set1 = set(seq1)
    set2 = set(seq2)
    set3 = set(seq3)
    # intersection
    common_elements = set1 & set2 & set3
    common_tuple = tuple(common_elements)
 
    return common_tuple
 
result = get_common_elements("abc", ['a', 'b'], ('b', 'c'))
print(result)  # Izdrukās ('b',)

# lets make a function to get common elements from unlimited number of sequences

def get_common_elements_all(*sequences, sort_it = False) -> tuple:
    # we can use set intersection on all sequences
    # we need to convert all sequences to sets
    # we can use * to unpack our sequences
    # we can use map to apply set to all sequences
    # we ca
    # check length first
    if len(sequences) == 0:
        return () # return empty tuple - keeping same data type
    # we know we have at least one sequence
    result = set(sequences[0]) # we start with first sequence
    # careful not to start with empty set! then nothing will be common
    for seq in sequences[1:]: # we loop through all other sequences
        result = result & set(seq) # we intersect our current result with next sequence

    # TODO could add sorting here if needed
    if sort_it:
        result = sorted(result)
    return tuple(result)

result = get_common_elements_all("abc", ['a', 'b'], ('b', 'c'), "brauca ar velosipēdu")
print(result)  # Izdrukās ('b',)
# should work with nothing
print(get_common_elements_all()) # ()
# should work with one sequence
print(get_common_elements_all("abc")) # ('a', 'c', 'b')
# should work with two
print(get_common_elements_all("abc", ['a', 'b'])) # ('a', 'b')
print(get_common_elements_all("abc", ['a', 'b'], sort_it = True)) # ('a', 'b')