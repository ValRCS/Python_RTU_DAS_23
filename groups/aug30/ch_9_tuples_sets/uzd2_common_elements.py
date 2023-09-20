def get_common_elements(seq1,seq2,seq3):
    # seq4 = []
    # for i in seq1:
    #     for j in seq2:
    #         for e in seq3:
    #             if i == j == e:
    #                 seq4.append(i)
    set1 = set(seq1)
    set2 = set(seq2)
    set3 = set(seq3)
    common_elements = set1 & set2 & set3
    return tuple(common_elements)
# print(get_common_elements(seq1,seq2,seq3))
print(get_common_elements("abc",['a','b'],('b','c')))  
print(get_common_elements(range(1000), range(10,1050), range(970,2500)))

def get_common_elements_unlimited(*sequences):
    if len(sequences) == 0:
        return () # base case when nothing is given then we return an empty tuple
    common_elements = set(sequences[0])
    for seq in sequences[1:]: # so we start from 2nd element, meaning if we only have 1 element then we don't do anything
        common_elements &= set(seq) # so intersection is the same as & operator
        # same as common_elements = common_elements & set(seq)
    return tuple(common_elements)

print(get_common_elements_unlimited([999,972,105,997],range(1000), range(10,1050), range(970,2500)))