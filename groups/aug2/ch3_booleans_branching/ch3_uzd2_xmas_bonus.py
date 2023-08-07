# 2.papilduzdevums
# Firma apsolījusi Ziemassvētku bonusu 15%
# apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.
# Uzdevums. Noprasiet lietotājam mēneša algas apjomu
# un nostrādāto gadu skaitu.
# # Izvadiet bonusu.
# 
# Piemērs 5 gadu stāžs, 1000 Eiro alga,
# bonuss būs 450 Eiro.
salary = int(input("Kāda jums ir mēneša alga?"))
period = int(input("Cik gadus strādājat?"))
# CAPITAL variables are meant to be constants but not enforced in Python
MIN_PERIOD = 2
BONUS_RATE = 0.15
# could have used lower case

bonus_period = period - MIN_PERIOD
bonus_salary = salary * BONUS_RATE
bonus_total = bonus_period * bonus_salary
# let's be nice and just round
bonus_total = int(round(bonus_total, 0 ) )
if period <= MIN_PERIOD:
    print(f"Prēmija nebūs, jāstrāda vairāk par {min_period} gadiem")
else:
    print(f"Tu esi nopelnījis {bonus_total} EUR lielu prēmiju")