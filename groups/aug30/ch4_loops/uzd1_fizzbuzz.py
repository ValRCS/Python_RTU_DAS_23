#1. uzdevums
#  
# i = 1
# while i <= 100:
#     if i % 5 == 0 and i % 7 == 0:
#         print("FizzBuzz,", end="")
#     elif i % 5 == 0:
#         print("Fizz,", end="")
#     elif i % 7 == 0:
#         print("Buzz,", end="")
#     else:
#         print(f"{i},", end="")
#     i += 1


#########
# 04-01 #
#########
start = 1
num_count = 100
fizz = 3
buzz = 5
# for n in range(1, num_count+1):
#     if not n%fizz and not n%buzz: # 0 is considered a falsy value
#         print("FizzBuzz", end="")
#     elif not n%fizz:
#         print("Fizz", end="")
#     elif not n%buzz:
#         print("Buzz", end="")
#     else:
#         print(n, end="")
#     if n<num_count:
#         print(",", end="")

buffer = "" # for now all we have is a string buffer
for n in range(start, num_count+1):
    end = ","
    if n == num_count:
        end = "" # could use \n
    if n % fizz == 0 and n % buzz == 0: # 0 is considered a falsy value
        print("FizzBuzz", end=end) # right side is just a variable
        buffer += "FizzBuzz" + end # could use f"FizzBuzz{end}"
    elif n % fizz == 0:
        print("Fizz", end=end)
        buffer += f"Fizz{end}" # alernative to +
    elif n % buzz == 0:
        print("Buzz", end=end)
        buffer += f"Buzz{end}"
    else:
        print(n, end=end)
        buffer += f"{n}{end}"
print()   
print("*"*40)
print(buffer)