# uzd 7_1
 
def add_mult(a, b, c):
    
    input_list = [a, b, c]
    sort_list = sorted(input_list)
    result = (sum(sort_list[:2] ) * sort_list[-1])
    # same as
    # result = (sort_list[0]+sort_list[1])*sort_list[2]
    return result
 
result = add_mult(2, 5, 4)
print(result)  