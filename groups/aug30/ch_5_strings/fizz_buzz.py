# simple way to use Copilot to generate some code
# write a simple fizz buzz program
# print numbers 1 to 100
# if number is divisible by 3 print Fizz
# if number is divisible by 5 print Buzz

# if number is divisible by 3 and 5 print FizzBuzz

# otherwise just print the number

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

