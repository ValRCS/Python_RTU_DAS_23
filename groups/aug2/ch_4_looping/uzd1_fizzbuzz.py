#1_uzdevums
 
# for number in range (1, 101):
#     if number % 5 == 0:
#         if number % 7 == 0:
#             print("FizzBuzz,", end= " ")
#         else: 
#             print("Fizz,", end= " ")
#     elif number % 7 == 0:
#         print("Buzz,", end= " ")
#     else:
#         print(number, end= ", ")

# 1 uzdevums
start = 1
stop = 100
fizz = 5
buzz = 7

# instead of printing we could collect data in a buffer
# here buffer will be a string
buffer = ""
 
for i in range(start, stop+1):
    end = "," # by default we use , as end symbol for print
    if i == stop:
        end = "" # so we do not print the , at the end
        
    if i % fizz == 0 and i % buzz == 0:
        print("FizzBuzz", end=end)
        buffer += "FizzBuzz" + end # f"FizzBuzz{end}" also would work
    elif i % fizz == 0:
        print("Fizz", end=end)
        buffer += "Fizz" + end
    elif i % buzz == 0:
        print("Buzz", end=end)
        buffer += "Buzz" + end
    else:
        print(i, end=end)
        buffer += f"{i}{end}" # could have use str(i)+end
        
# let's print 40 *
print()
print("*"*40)
# let's see what we have in our buffer
print(buffer)