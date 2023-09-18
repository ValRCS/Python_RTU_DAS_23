def return_integer(prompt="Enter an integer: "):
    while True:
        try:
            integer = int(input(prompt))
            break
        except ValueError:
            print("Please enter integers only!")
    return integer

start = return_integer("Enter start integer (inclusive): ")
end = return_integer("Enter end integer (inclusive): ")

# while True:
#     try:
#         # we could get an error here in two places
#         # at either of the int conversions
#         start = int(input("Enter start integer (inclusive): "))
#         end = int(input("Enter end integer (inclusive): "))
#         break
#     except ValueError:
#         print("Please enter integers only!")
# start = int(input("Enter start integer (inclusive): "))
# end = int(input("Enter end integer (inclusive): "))


list_cubes = [i**3 for i in range(start,end+1)]
# could create a list of lists with numbers and cubes
list_numbers_cube = [[i, i**3] for i in range(start,end+1)]
print(list_cubes)
print(list_numbers_cube)
# last number used
last_number = list_numbers_cube[-1][0]
print(last_number)