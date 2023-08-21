# 3 uzdevums
 
 
def get_city_year(p0, perc, delta, p, debug=False, precision=4):
    """Returns the number of years it takes for a population to reach a certain size.
    Args:
        p0 (int): starting population
        perc (float): percentage of growth per year
        delta (int): how many people leave or join the population per year
        p (int): population to surpass
        debug (bool): if True, prints debug messages
        precision (int): how many decimal places to use for rounding
    Returns:
        int: number of years it takes for the population to reach size p
        -1 if the population never reaches size p
    """	
    years = 0
 
    while p0 < p:
        yearly_change = p0 * perc / 100 + delta
        if round(yearly_change, precision) <= 0: # without round it will take a long time to approach 0
            print("Looks like we are in an infinite loop")
            print(f"So population is stuck at {p0}")
            print(f"It took {years} years to get there")
            return -1
        p0 += yearly_change
        if debug:
            print(f"p0={p0}")
        years += 1
  
    return years
 
print(get_city_year(1500, 5, 100, 5000))

# print(get_city_year(1000,-2, 30, 2000, debug=True))
print(get_city_year(1000,-2, 30, 2000))
