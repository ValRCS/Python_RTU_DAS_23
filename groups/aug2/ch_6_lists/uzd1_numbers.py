#### lessons 1 - 1c
 
numbers = []
total = 0 # do not use sum as a variable name, it is a built-in function
 
while True:
    user_input = input("Ievadiet skaitli vai 'q' lai izietu: ")
 
    if user_input.lower().startswith('q'): # so Quit , quit, qUit, etc. will work
        break
 
    try:
        number = float(user_input)
        # so here we are guaranteed that number is a float
        numbers.append(number)
        total += number
        average = total / len(numbers)
        sorted_numbers = sorted(numbers) # default is ascending order
        top3 = sorted_numbers[-3:][::-1] # thus we need to use negative indexes
        # I use [::-1] to reverse the list so I get top 3 from the biggest
        bottom3 = sorted_numbers[:3]
 
        print(f"Vidējā vērtība: {average:.2f}")
        print(f"TOP 3 skaitļi: {top3}")
        print(f"BOTTOM 3 skaitļi: {bottom3}")
        # number length so far
        print(f"Skaitļu skaits: {len(numbers)}")
    except ValueError:
        print("Nepareiza ievade. Lūdzu, ievadiet skaitli vai 'q'.")