##############
## 09.01 a
##############
def get_min_avg_max(seq):
    return min(seq), sum(seq) / len(seq), max(seq)
 
print(get_min_avg_max([0,10,1,9]))
print(get_min_avg_max((0,10,1,9)))
print(get_min_avg_max(range(20)))

##############
## 09.01 b
##############
def get_avg(val1, val2):
    # custom average function
    if type(val1) is str:
        return "".join([val1,val2])
    else:
        return (val1 + val2) / 2
 
def get_med(something):
    if type(something) is tuple:
        return get_avg(something[0], something[1])
    else:
        return something
 
def get_min_med_max(seq):
    med_seq = int(len(seq)/2)
    # med_seq = len(seq)//2   # same as above
 
    if len(seq) % 2:
        med = get_med(seq[med_seq])
    else:
        med = get_med((seq[med_seq-1],seq[med_seq]))
 
    return min(seq), med, max(seq)
 
print(get_min_med_max([2,2,9,9,4,3]))
print(get_min_med_max("baac"))
print(get_min_med_max("bazcxac"))