name = "Valdis"
print((name+"\n")*5)
print("*"*40)
name_with_newline = name + "\n"
print(name_with_newline * 5)
print("Valdis\n"*5)
# notice \n that stands for newline
print("Valdis"*7)
 
# 1 minute 60 seconds
print("60 secundes in 1 minute", 60**1)
# 60 minutes in 1 h.
print("in 1 hour", 60*60)
# 24 hour in 1 day
print("in 1 day", 60*60*24)
# in 365 days
print("in 1 day", 60*60*24*365)
# 10^100..
print("One Googol 10^100=", 10**100)
# 
# notice \n that stands for newline
print ("Ba"+"na"*5)

# print uses newline by default
# if we do not want it
print("Va", end="") # we can use anything for end
print("ldis")