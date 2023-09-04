# print("Mainigo apstrade, Uzdevums 1") # uzdevuma nosaukums
#  
# name = input("What is your name?")  # prasam cilveka vardu un ierakstam to name
# age = int(input(f"{name}, how old are you?")) # prasam vecumu un ierakstam to age
# if age > 100: #rakstam ja age lielaks par 100
#     print("Too old, dude!")
# else: #izpildam kodu ja jaunaks par 100
#     age_100 = 100 - age #skaitam pec cik laika cilvekam bus 100 gadi
#     import datetime # importejam tagadejo laiku
#     current_year = datetime.datetime.now().year # pieskiram mainigam curent_year tagadejo laiku
#     next_year = current_year + age_100 #skaitam kada gada cilvekam bus 100 un ierakstam mainiga next_year
#     print(f"{name}, after {age_100} years in {next_year} you will be 100 years old!") # rakstam visu ko saskaitijam

#****************
#***********02_01
#****************
import datetime
 
serious_age = 100
name = input("Lūdzu, ievadiet savu vārdu:")
user_age = int(input(f"{name}, kāds ir jūsu vecums?"))
serious_difference = serious_age - user_age
 
if serious_difference%10 == 1 and serious_difference != 11:
    postfix = "a"
else:
    postfix = "iem"
 
print(f"Jums paliks {serious_age} gadu pēc {serious_difference} gad{postfix},")
 
#bonuss
current_year = datetime.datetime.now().year
print(f"un tad būs {current_year + serious_difference}. gads!")