import datetime  # for current year
print("Task 1\n")
name = input("What is your name? ")
age = int(input(f"what is your age {name}? "))
target_age = 100

years_to_target = target_age - age
print(f"You will reach {target_age} years after",
      years_to_target,
      "years.")
 
# current_year = int(input(f"BONUS question. Please enter current year..."))
current_year = datetime.datetime.now().year
print(f"It is now year {current_year}")
target_year = current_year + years_to_target
print(f"You will be {target_age} in year {target_year} year.")