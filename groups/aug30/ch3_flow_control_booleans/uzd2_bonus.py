print()  #tuksa rinda ar newline pēc noklusējuma
print(end="🍺🍺\n🎄\n")
print("if/else", end=" ") # no newline!!!
print("Uzdevums 2") # uzdevuma nosaukums
MIN_BONUS_YEARS = 2 # could use lowercase if flexible
BONUS_RATE = 0.15
salary = float(input("How much money do you make?"))
experience = float(input("How many years is yours experience?"))
bonus_years_eligible = int(experience - MIN_BONUS_YEARS)
if bonus_years_eligible > 0:
    bonus = salary*bonus_years_eligible*BONUS_RATE
    print(f"Bonus is: {bonus:.2f} EUR")
else: # so not eligible 0 or less
    print("You are not eligible for a Christmas bonus.")
