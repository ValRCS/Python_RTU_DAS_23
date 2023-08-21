# 1. Min, Avg, Max
# Uzrakstiet funkciju get_min_avg_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, aritmētisko vidējo un lielāko vērtību no virknes.
# get_min_avg_max([0,10,1,9]) -> (0,5,10)
# ienākošā sequence var būt tuple vai list ar skaitliskām vērtībām. 
 
def find_min_max_ave(input_list): # atkal funkcija ar vienu definētu parametru
    #if not input_list:
        #return None
 
    min_value = min(input_list) # iebūvēta f-ja mazākās vērtības atrašanai
    max_value = max(input_list) # lielākās vētrības atrašana
    total_sum = sum(input_list) # summa lai aprēķinātu vidējo
    average = total_sum / len(input_list) # len skaita atsevišķos intus
 
    return min_value, average, max_value # unkcija atgriež trīs skaitļus
 
my_list = [5, 8, 9, 3, 45, 21,17, 30] # arguments
result = find_min_max_ave(my_list) # it kā atgriež tuple
print(result)
result_type = type(result) # šis lai pārliecinātos, ka tik tiešām tuple
print(result_type)
# this function would work on tuples as well
my_tuple = 5, 8, 9, 3, 45, 21,17, 30
result = find_min_max_ave(my_tuple)
print(result)

# lets try with range
result = find_min_max_ave(range(10))
print(result)

# should not work with string because sum() does not work with strings
try:
    result = find_min_max_ave("Valdis")
    print(result)
except TypeError as e:
    print(e)


# 1.b - Min Med Max
# Median - vidējā vērtība, kas ir pa vidu, ja pāra skaitu tad vidējā starp diviem vidējiem
def get_min_med_max(sequence):
    sorted_seq = sorted(sequence)
    min_val = sorted_seq[0]
    max_val = sorted_seq[-1]
 
    if len(sorted_seq) % 2 == 0: # so even number of elements
        # find index of middle left and middle right
        # // is division without remainder
        middle_left = sorted_seq[len(sorted_seq) // 2 - 1]
        middle_right = sorted_seq[len(sorted_seq) // 2]
        if isinstance(middle_left, (int, float)) and isinstance(middle_right, (int, float)):
            median = (middle_left + middle_right) / 2
            # also there is statistics module with median function
        else:
            median = (middle_left + middle_right)  # Force float division
    else:
        median = sorted_seq[len(sorted_seq) // 2]
 
    return min_val, median, max_val

result_1b_1 = get_min_med_max([1, 5, 8, 4, 3])
print(result_1b_1)  # Izdrukās (1, 4, 8)
 
result_1b_2 = get_min_med_max([2, 2, 9, 9, 4, 3])
print(result_1b_2)  # Izdrukās (2, 3.5, 9)
 
result_1b_3 = get_min_med_max("baaac")
print(result_1b_3)  # Izdrukās ('a', 'a', 'c')
 
result_1b_4 = get_min_med_max("faaacb")
print(result_1b_4)  # Izdrukās ('a', 'ab', 'f')