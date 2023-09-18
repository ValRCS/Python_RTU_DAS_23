# Uzdevums 3
 
# while True:
#     try:
#         p0 = int(input("Citizen count: "))
#         perc = float(input("Percentage: "))
#         delta = int(input("Delta: "))
#         p = int(input("Needed citizens ammount: "))
#         break
#     except ValueError as i:
#         print(f"Erorr: {i}")
 
def get_city_year(p0, perc, delta, p, debug=False):
    year = 0
    while True:
        increase = round(p0*perc*0.01) + delta
        if increase <= 0: # if increase is negative or zero we will never reach our goal
            year = -1
            break
        p0 += increase
        year += 1 # one year has passed
        if p0 >= p: # we have reached our goal
            break
        if debug:
            print(f"Year: {year}, count: {p0}")
    return year

print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000) )
print(get_city_year(1500000, 2.5, 10000, 2000000))
print(get_city_year(1000,-2, 30, 2000))
# print(get_city_year(1000,-2, 30, 2000, debug=True))